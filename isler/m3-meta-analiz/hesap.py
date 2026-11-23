"""m3 · Eğitim amaçlı KURGU veri: Hedges' g, ters varyans ağırlıkları,
DerSimonian-Laird rastgele etkiler, Q, tau^2, I^2, tahmin aralığı; funnel verisi ve Egger testi.
Yalnız Python standart kütüphanesi (scipy gerekmez). Çalıştır: python3 hesap.py"""
import math

# t dağılımı kritik değeri (iki yönlü %95), sayısal ters fonksiyon
def t_cdf(t, df):
    # düzenli tamamlanmamış beta ile
    x = df / (df + t * t)
    def betacf(a, b, x):
        MAXIT, EPS, FPMIN = 200, 3e-14, 1e-300
        qab, qap, qam = a + b, a + 1, a - 1
        c, d = 1.0, 1 - qab * x / qap
        d = 1 / (d if abs(d) > FPMIN else FPMIN); h = d
        for m in range(1, MAXIT):
            m2 = 2 * m
            aa = m * (b - m) * x / ((qam + m2) * (a + m2))
            d = 1 + aa * d; d = 1 / (d if abs(d) > FPMIN else FPMIN)
            c = 1 + aa / c; c = c if abs(c) > FPMIN else FPMIN; h *= d * c
            aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
            d = 1 + aa * d; d = 1 / (d if abs(d) > FPMIN else FPMIN)
            c = 1 + aa / c; c = c if abs(c) > FPMIN else FPMIN
            de = d * c; h *= de
            if abs(de - 1) < EPS: break
        return h
    a, b = df / 2, 0.5
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    ib = bt * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - bt * betacf(b, a, 1 - x) / b
    return 1 - 0.5 * ib if t > 0 else 0.5 * ib

def t_crit(df, p=0.975):
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_cdf(mid, df) < p else (lo, mid)
    return (lo + hi) / 2

def chi2_sf(q, df):  # üst kuyruk, düzenli tamamlanmamış gamma
    a, x = df / 2, q / 2
    if x < a + 1:
        s, term, n = 1 / a, 1 / a, a
        for _ in range(500):
            n += 1; term *= x / n; s += term
        return 1 - s * math.exp(-x + a * math.log(x) - math.lgamma(a))
    b, c, d = x + 1 - a, 1e300, 1 / (x + 1 - a); h = d
    for i in range(1, 500):
        an = -i * (i - a); b += 2
        d = an * d + b; d = 1 / d if d else 1e300
        c = b + an / c; h *= d * c
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h

Z = 1.959964

def hedges(d, n1, n2):
    df = n1 + n2 - 2
    J = 1 - 3 / (4 * df - 1)
    vd = (n1 + n2) / (n1 * n2) + d * d / (2 * (n1 + n2))
    return J * d, J * J * vd, J

def meta(ys, vs):
    k = len(ys)
    w = [1 / v for v in vs]
    fe = sum(wi * y for wi, y in zip(w, ys)) / sum(w)
    se_fe = math.sqrt(1 / sum(w))
    Q = sum(wi * (y - fe) ** 2 for wi, y in zip(w, ys))
    C = sum(w) - sum(wi * wi for wi in w) / sum(w)
    tau2 = max(0.0, (Q - (k - 1)) / C)
    I2 = max(0.0, (Q - (k - 1)) / Q) * 100 if Q > 0 else 0.0
    ws = [1 / (v + tau2) for v in vs]
    re = sum(wi * y for wi, y in zip(ws, ys)) / sum(ws)
    se_re = math.sqrt(1 / sum(ws))
    tc = t_crit(k - 2)
    pi = (re - tc * math.sqrt(tau2 + se_re ** 2), re + tc * math.sqrt(tau2 + se_re ** 2))
    zre = re / se_re
    p_re = math.erfc(abs(zre) / math.sqrt(2))
    return dict(k=k, w=w, ws=ws, fe=fe, se_fe=se_fe, Q=Q, pQ=chi2_sf(Q, k - 1), tau2=tau2, tau=math.sqrt(tau2),
                I2=I2, re=re, se_re=se_re, z=zre, p=p_re, pi=pi, tc=tc)

def forest():
    # KURGU: pliometrik antrenmanın dikey sıçrama yüksekliğine etkisi (deney/kontrol, son test)
    data = [("Çalışma A", 10, 10, 1.10), ("Çalışma B", 12, 12, -0.20), ("Çalışma C", 30, 30, 0.35),
            ("Çalışma D", 16, 16, 0.95), ("Çalışma E", 20, 20, -0.10), ("Çalışma F", 40, 40, 0.50)]
    ys, vs, rows = [], [], []
    for name, n1, n2, d in data:
        g, v, J = hedges(d, n1, n2)
        ys.append(g); vs.append(v); rows.append((name, n1 + n2, d, J, g, v))
    m = meta(ys, vs)
    print("FOREST (KURGU) · Hedges g · DerSimonian-Laird")
    print("| Çalışma | n (deney+kontrol) | Cohen d | J | Hedges g | SE | %95 GA | Ağırlık SE (%) | Ağırlık RE (%) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for (name, n, d, J, g, v), wf, wr in zip(rows, m['w'], m['ws']):
        se = math.sqrt(v)
        print(f"| {name} | {n} | {d:.2f} | {J:.3f} | {g:.2f} | {se:.3f} | {g - Z*se:.2f} ile {g + Z*se:.2f} | "
              f"{100*wf/sum(m['w']):.1f} | {100*wr/sum(m['ws']):.1f} |")
    print(f"Sabit etki özeti: g = {m['fe']:.2f}, %95 GA {m['fe']-Z*m['se_fe']:.2f} ile {m['fe']+Z*m['se_fe']:.2f}")
    print(f"Rastgele etkiler (DL) özeti: g = {m['re']:.2f}, SE = {m['se_re']:.3f}, %95 GA {m['re']-Z*m['se_re']:.2f} ile "
          f"{m['re']+Z*m['se_re']:.2f}, z = {m['z']:.2f}, p = {m['p']:.4f}")
    print(f"Q = {m['Q']:.2f} (sd = {m['k']-1}), p = {m['pQ']:.3f}; tau^2 = {m['tau2']:.4f}; tau = {m['tau']:.3f}; I^2 = {m['I2']:.1f}%")
    print(f"%95 tahmin aralığı (t, sd = k-2 = {m['k']-2}, t = {m['tc']:.3f}): {m['pi'][0]:.2f} ile {m['pi'][1]:.2f}")
    print()

def funnel():
    # KURGU: 14 çalışma, hafif asimetri (küçük ve etkisiz çalışmalar köşesi seyrek)
    pts = [(0.42, 0.08), (0.36, 0.10), (0.47, 0.12), (0.30, 0.14), (0.52, 0.16), (0.38, 0.18),
           (0.58, 0.21), (0.24, 0.23), (0.66, 0.26), (0.50, 0.28), (0.74, 0.31), (0.20, 0.33),
           (0.86, 0.36), (0.70, 0.39)]
    ys = [g for g, s in pts]; vs = [s * s for g, s in pts]
    m = meta(ys, vs)
    # Egger: standart normal sapma (g/SE) ~ kesinlik (1/SE); kesişim = asimetri ölçüsü
    X = [1 / s for g, s in pts]; Y = [g / s for g, s in pts]; k = len(pts)
    mx, my = sum(X) / k, sum(Y) / k
    sxx = sum((x - mx) ** 2 for x in X); sxy = sum((x - mx) * (y - my) for x, y in zip(X, Y))
    b1 = sxy / sxx; b0 = my - b1 * mx
    res = [y - (b0 + b1 * x) for x, y in zip(X, Y)]
    s2 = sum(r * r for r in res) / (k - 2)
    se_b0 = math.sqrt(s2 * (1 / k + mx * mx / sxx))
    t0 = b0 / se_b0
    p0 = 2 * (1 - t_cdf(abs(t0), k - 2))
    print("FUNNEL (KURGU) · 14 çalışma")
    print("| No | Hedges g | SE |"); print("|---|---|---|")
    for i, (g, s) in enumerate(pts, 1): print(f"| {i} | {g:.2f} | {s:.2f} |")
    print(f"Sabit etki özeti (huni ekseninin ortası): g = {m['fe']:.2f}; RE (DL) g = {m['re']:.2f}; "
          f"Q = {m['Q']:.2f}, I^2 = {m['I2']:.1f}%, tau^2 = {m['tau2']:.4f}")
    print(f"Egger regresyonu: kesişim = {b0:.2f} (SE {se_b0:.2f}), t = {t0:.2f}, sd = {k-2}, p = {p0:.3f}; eğim = {b1:.2f}")

if __name__ == "__main__":
    forest(); funnel()
