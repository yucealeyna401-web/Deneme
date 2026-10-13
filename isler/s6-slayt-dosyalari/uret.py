# -*- coding: utf-8 -*-
"""s6 slayt dosyalarini ureten betik. Yalniz isler/s6-slayt-dosyalari/project/ altina yazar."""
import json, os, re, html, datetime

KOK = os.path.dirname(os.path.abspath(__file__))
KAYNAK = os.path.join(KOK, '..', 's5-sunum-icerigi', 'slaytlar.md')
PROJE = os.path.join(KOK, 'project')
SLAYT = os.path.join(PROJE, 'slides')
os.makedirs(SLAYT, exist_ok=True)

# ---------------- palet ----------------
D = '#1F2A37'      # koyu
L = '#F7F5F0'      # acik
L2 = '#ECE8DF'     # ikinci acik
CARD = '#FDFCF9'
BRD = '#DDD7CB'
T2 = '#3F4A5A'     # ikincil metin (acik zeminde)
MUT = '#5B6472'    # soluk metin
BLUE = '#2F6F8F'   # vurgu 1
BLUED = '#245A75'  # vurgu 1 koyu (acik zeminde metin)
BLUEL = '#DCE9EF'  # vurgu 1 acik ton
OR = '#D9632B'     # vurgu 2 (sekil)
ORD = '#B04A16'    # vurgu 2 koyu (metin)
ORL = '#FBE3D6'    # vurgu 2 acik ton
DK2 = '#2C3A4B'    # koyu kart
DKB = '#4B5B6E'    # koyu kart kenari
DT2 = '#BFC7D1'    # koyu zeminde ikincil metin
BLUEDK = '#8FC1D8' # koyu zeminde mavi vurgu metni

SANS = "'IBM Plex Sans', Arial, sans-serif"
SERIF = "'Source Serif 4', Georgia, serif"
COND = "'IBM Plex Sans Condensed', Arial, sans-serif"

# ---------------- slaytlar.md ayristirma ----------------
md = open(KAYNAK, encoding='utf-8').read()
govde = md.split('## Tam kaynakça (APA 7, alfabetik)')[0]
bloklar = re.split(r'\n## (\d+)\. ', govde)
notlar = {}
for i in range(1, len(bloklar), 2):
    no = int(bloklar[i])
    blok = bloklar[i + 1]
    m = re.search(r'\*\*Konuşmacı notu:\*\*\n(.*)', blok, re.S)
    metin = m.group(1)
    metin = metin.split('\n---')[0].strip()
    satirlar = []
    for s in metin.split('\n'):
        s = s.strip()
        if not s:
            continue
        if s.startswith('- '):
            s = '• ' + s[2:]
        satirlar.append(s)
    metin = ' '.join(satirlar).replace('**', '')
    notlar[no] = metin

tam = md.split('## Tam kaynakça (APA 7, alfabetik)')[1]
kunyeler = [s.strip() for s in tam.split('\n') if s.strip()]
assert len(kunyeler) == 30, len(kunyeler)


def esc(s):
    return html.escape(s, quote=False)


def kunye_html(k):
    """APA kunyesi: *italik* -> <i>, URL -> tiklanabilir baglanti."""
    parcalar = re.split(r'(\*[^*]+\*)', k)
    out = ''
    for p in parcalar:
        if p.startswith('*') and p.endswith('*'):
            out += '<i>' + esc(p[1:-1]) + '</i>'
        else:
            m = re.search(r'(https://\S+)$', p)
            if m:
                url = m.group(1)
                out += esc(p[:m.start()]) + '<a href="' + html.escape(url) + '">' + esc(url) + '</a>'
            else:
                out += esc(p)
    return out


# ---------------- ortak parcalar ----------------
def eyebrow(t, renk=BLUED):
    return f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:{renk}">{t}</p>'


def baslik(ust, ana, koyu=False):
    ur = BLUEDK if koyu else BLUED
    ar = L if koyu else D
    return ('<div style="display:flex;flex-direction:column;gap:12px">'
            + eyebrow(ust, ur)
            + f'<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.1;color:{ar}">{ana}</h2>'
            + '</div>')


def altbilgi(kaynak, sayfa, koyu=False):
    r = DT2 if koyu else MUT
    if kaynak:
        return ('<div style="position:absolute;left:128px;bottom:64px;width:1664px;display:flex;justify-content:space-between;gap:32px">'
                f'<p style="font-size:24px;white-space:nowrap;color:{r}">{kaynak}</p>'
                f'<p style="font-size:24px;color:{r}">{sayfa}</p></div>')
    return ('<div style="position:absolute;left:128px;bottom:64px;width:1664px;display:flex;justify-content:end">'
            f'<p style="font-size:24px;color:{r}">{sayfa}</p></div>')


SAYFALAR = []   # (id, html)
BOLUMLER = {}   # id -> aciklama


def slayt(sid, no, bg, icerik, kaynak=None, sayfa=True, koyu=False, renk=None, bolum=None,
          stil='padding:128px 128px 160px;display:flex;flex-direction:column;gap:40px'):
    renk = renk or (L if koyu else D)
    ds = ''
    if bolum:
        BOLUMLER[sid] = bolum
        ds = f' data-section="{esc(bolum)}"'
    h = (f'<section id="{sid}"{ds} data-transition="fade" style="background:{bg};color:{renk};'
         f'font-family:{SANS};{stil}">\n')
    h += icerik + '\n'
    if sayfa:
        h += altbilgi(kaynak, no, koyu) + '\n'
    h += '<aside>' + esc(notlar[no]) + '</aside>\n</section>\n'
    SAYFALAR.append((sid, h))


def kart(ic, ek='', bg=CARD, kenar=BRD, ust=None, pad='32px 40px', gap=12):
    ut = f'border-top:8px solid {ust};' if ust else ''
    return (f'<div style="display:flex;flex-direction:column;gap:{gap}px;background:{bg};border:1px solid {kenar};{ut}'
            f'border-radius:16px;padding:{pad};{ek}">{ic}</div>')


def con(x1, y1, x2, y2, renk=MUT, w=2, head='none', ek=''):
    return (f'<x-connector x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" head="{head}" '
            f'style="color:{renk};border-width:{w}px{";" + ek if ek else ""}"></x-connector>')


def pin_p(x, y, w, metin, boy=24, renk=D, hiza='left', ek=''):
    return (f'<p style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:{boy}px;'
            f'line-height:1.4;text-align:{hiza};color:{renk};{ek}">{metin}</p>')


# =====================================================================
# 1 · cover
# =====================================================================
orman_silu = ['<svg aria-label="Soluk bir orman grafiği silüeti" style="position:absolute;left:1152px;top:592px;opacity:0.3" width="640" height="320" viewBox="0 0 640 320">',
              '<line x1="240" y1="12" x2="240" y2="300" stroke="#8FC1D8" stroke-width="3" stroke-dasharray="10 8"/>',
              '<line x1="20" y1="306" x2="620" y2="306" stroke="#8FC1D8" stroke-width="3"/>']
for (cx, a, b, s, y) in [(330, 200, 460, 20, 34), (420, 330, 510, 26, 82), (370, 310, 430, 34, 130), (520, 320, 620, 16, 178), (290, 160, 420, 24, 226)]:
    orman_silu.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="#8FC1D8" stroke-width="4"/>')
    orman_silu.append(f'<rect x="{cx - s // 2}" y="{y - s // 2}" width="{s}" height="{s}" fill="#8FC1D8"/>')
orman_silu.append('<polygon points="300,272 370,256 440,272 370,288" fill="#F08A52"/>')
orman_silu.append('</svg>')

ic = '\n'.join(orman_silu) + f'''
<div style="position:absolute;left:0;top:0;width:24px;height:1080px;background:{BLUE}"></div>
<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:{BLUEDK}">Bilimsel Araştırma Yöntemleri ve Araştırma Etiği</p>
<div style="display:flex;flex-direction:column;gap:36px">
<h1 style="font-family:{SERIF};font-size:112px;font-weight:600;line-height:1.05;color:{L}">Meta-analiz, Sistematik<br>Derleme ve Derleme</h1>
<p style="font-size:48px;line-height:1.3;color:{DT2}">Kanıtı Bir Araya Getirmek</p>
</div>
<div style="display:flex;flex-direction:column;gap:8px">
<p style="font-size:32px;font-weight:600;color:{L}">[Adınız Soyadınız]</p>
<p style="font-size:24px;color:{DT2}">Ders hocası: [Unvan Ad Soyad] · [Üniversite, Enstitü, Anabilim Dalı] · [Tarih]</p>
</div>'''
slayt('cover', 1, D, ic, sayfa=False, koyu=True, bolum='Kapak, spordan tanıdık bir soru ve yol haritası.',
      stil='padding:128px;display:flex;flex-direction:column;justify-content:space-between')

# =====================================================================
# 2 · acilis-soru
# =====================================================================
def xr(v):
    return round(40 + v * 733.33)

aralik = f'''<div style="position:relative;width:960px;height:208px">
{con(40, 160, 920, 160, MUT, 2)}
{con(xr(1), 14, xr(1), 160, ORD, 3, ek='border-style:dashed')}
{con(xr(0.846), 40, xr(1.095), 40, '#8A929C', 5)}
<div style="position:absolute;left:{xr(0.963) - 10}px;top:30px;width:20px;height:20px;background:#6B7480"></div>
{con(xr(0.207), 110, xr(0.480), 110, BLUE, 5)}
<div style="position:absolute;left:{xr(0.315) - 10}px;top:100px;width:20px;height:20px;background:{BLUED}"></div>
{pin_p(400, 22, 240, 'Germe', 24, MUT, 'right')}
{pin_p(412, 92, 260, 'Kuvvet antrenmanı', 24, BLUED)}
{pin_p(0, 172, 80, '0', 24, MUT, 'center')}
{pin_p(xr(0.5) - 40, 172, 80, '0,5', 24, MUT, 'center')}
{pin_p(xr(1) - 90, 172, 180, '1 = fark yok', 24, ORD, 'center')}
</div>'''

ic = baslik('Açılış', 'Tek çalışma mı, yirmi beş çalışma mı?') + f'''
<div style="display:flex;gap:64px">
<div style="width:560px;display:flex;flex-direction:column;gap:20px">
<p style="font-family:{SERIF};font-size:200px;font-weight:600;line-height:1;color:{ORD}">?</p>
<p style="font-family:{SERIF};font-size:36px;line-height:1.3">“Antrenmandan önce germe, sakatlığı önler.” Doğru mu?</p>
<p style="font-size:28px;line-height:1.4;color:{T2}">Tek bir çalışma: belki evet, belki hayır.</p>
<p style="font-size:28px;line-height:1.4"><b>25 randomize kontrollü çalışma (RKÇ), 26.610 sporcu, 3.464 sakatlık.</b></p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;gap:24px">
{kart(f'<p style="font-size:28px;font-weight:600;color:{T2}">Germe</p><p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{MUT}">0,963</p><p style="font-size:24px;line-height:1.4;color:{T2}">RR · %95 GA 0,846-1,095 · etki yok</p>', 'flex:1', pad='28px 32px', gap=8)}
{kart(f'<p style="font-size:28px;font-weight:600;color:{BLUED}">Kuvvet antrenmanı</p><p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{BLUED}">0,315</p><p style="font-size:24px;line-height:1.4;color:{T2}">RR · %95 GA 0,207-0,480</p>', 'flex:1', ust=BLUE, pad='28px 32px', gap=8)}
</div>
<p style="font-size:24px;color:{MUT}">Risk oranı (RR) ve %95 güven aralığı: germe aralığı 1'i kesiyor, kuvvet aralığı kesmiyor.</p>
{aralik}
</div>
</div>'''
slayt('acilis-soru', 2, L, ic, 'Lauersen ve ark., 2014')

# =====================================================================
# 3 · yol-haritasi
# =====================================================================
duraklar = [('1', 'Kavramlar', 'üç tür, kanıt piramidi'),
            ('2', 'Sistematik derleme', 'soru, kayıt, arama, PRISMA, kalite'),
            ('3', 'Meta-analiz', 'etki büyüklüğü, modeller, orman ve huni grafiği'),
            ('4', 'Spordan örnekler ve etik', 'Beden eğitimi ve spordan gerçek örnekler, araştırma etiği')]
parca = []
for i, (n, t, a) in enumerate(duraklar):
    if i:
        parca.append(f'<x-shape kind="arrow-right" style="background:{OR};width:64px;height:32px"></x-shape>')
    parca.append(kart(f'<p style="font-family:{SERIF};font-size:72px;font-weight:600;line-height:1;color:{BLUED}">{n}</p>'
                      f'<h3 style="font-size:32px;font-weight:600;line-height:1.25">{t}</h3>'
                      f'<p style="font-size:24px;line-height:1.4;color:{T2}">{a}</p>', 'flex:1;align-self:stretch', pad='32px'))
ic = baslik('Açılış', 'Yol haritası ve ana mesaj') + f'''
<div style="display:flex;align-items:center;gap:24px">
{''.join(parca)}
</div>
<div style="display:flex;flex-direction:column;gap:12px;background:{BLUED};border-radius:16px;padding:36px 48px">
<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:#D6E7EF">Ana mesaj</p>
<p style="font-family:{SERIF};font-size:48px;font-weight:600;line-height:1.2;color:{L}">“Derleme kanıtın haritasıdır; haritanın kalitesi de sorgulanır.”</p>
</div>'''
slayt('yol-haritasi', 3, L, ic, None)

# =====================================================================
# 4 · uc-tur  (karsilastirma tablosu)
# =====================================================================
satirlar = [('Soru', 'Geniş, esnek', 'Dar, önceden tanımlı', 'Nicel bir etki'),
            ('Arama', 'Çoğu kez açıklanmaz', 'Kapsamlı, belgelenmiş', 'Sistematik aramaya dayanmalı'),
            ('Seçim', 'Yazarın tercihi', 'Önceden belirlenmiş ölçütler', 'Aynı ölçütler'),
            ('Sentez', 'Anlatısal', 'Anlatısal ya da istatistiksel', 'İstatistiksel birleştirme'),
            ('Tekrarlanabilirlik', 'Düşük', 'Yüksek', 'Yüksek (yöntem raporlanırsa)')]
P = 'padding:14px 20px'
tb = (f'<table style="font-family:{SANS};font-size:26px;line-height:1.3;color:{D}">'
      f'<tr style="background:{D}"><th style="width:19%;text-align:left;color:{L};{P}">Boyut</th>'
      f'<th style="width:27%;text-align:left;color:{L};{P}">Anlatı derlemesi (narrative review)</th>'
      f'<th style="width:27%;text-align:left;color:{L};{P}">Sistematik derleme (systematic review)</th>'
      f'<th style="width:27%;text-align:left;color:{L};{P}">Meta-analiz (meta-analysis)</th></tr>')
for j, (a, b, c, d) in enumerate(satirlar):
    bg = CARD if j % 2 == 0 else L2
    tb += (f'<tr style="background:{bg}"><td style="color:{BLUED};{P}">{a}</td><td style="{P}">{b}</td>'
           f'<td style="{P}">{c}</td><td style="{P}">{d}</td></tr>')
tb += '</table>'
ikonlar = (f'<div style="display:flex">'
           f'<div style="width:19%"></div>'
           f'<div style="width:27%;display:flex;gap:12px;align-items:center;padding:0 20px"><x-icon name="Book" style="color:{MUT};width:40px;height:40px"></x-icon><p style="font-size:24px;color:{MUT}">kütüphaneci</p></div>'
           f'<div style="width:27%;display:flex;gap:12px;align-items:center;padding:0 20px"><x-icon name="Search" style="color:{BLUED};width:40px;height:40px"></x-icon><p style="font-size:24px;color:{BLUED}">dedektif</p></div>'
           f'<div style="width:27%;display:flex;gap:12px;align-items:center;padding:0 20px"><x-icon name="Chart" style="color:{ORD};width:40px;height:40px"></x-icon><p style="font-size:24px;color:{ORD}">istatistik</p></div>'
           f'</div>')
ic = baslik('Kavramlar', 'Üç tür, üç farklı iş') + f'''
<div style="display:flex;flex-direction:column;gap:16px">
{ikonlar}
{tb}
</div>
<p style="font-size:28px;line-height:1.4;background:{BLUEL};border-left:8px solid {BLUE};border-radius:8px;padding:20px 32px">Her sistematik derleme meta-analiz içermez; meta-analizin sistematik bir derlemenin içinde yapılması önerilir.</p>'''
slayt('uc-tur', 4, L, ic, 'Grant ve Booth, 2009; Higgins ve ark., 2024; Munn ve ark., 2018; Borenstein ve ark., 2021',
      bolum='Anlatı derlemesi, sistematik derleme ve meta-analiz farkı; diğer türler; kanıt piramidi ve eleştirisi.')

# =====================================================================
# 5 · diger-turler
# =====================================================================
turler = [('Kapsam (scoping) derlemesi', 'Literatürün haritası, bilgi boşlukları; özet etki yok.', 'Alan ne kadar çalışılmış?', BLUE),
          ('Şemsiye (umbrella) derleme', 'Derlemelerin derlemesi; yalnız SD ve MA dahil.', 'Zaten çok meta-analiz var.', BLUE),
          ('Sistematik derleme', 'Dar soru, yanlılık riski değerlendirmesi zorunlu.', 'Belirli bir müdahale işe yarıyor mu?', OR)]
kartlar = ''.join(kart(
    f'<h3 style="font-size:36px;font-weight:600;line-height:1.2">{a}</h3>'
    f'<p style="font-size:28px;line-height:1.4;color:{T2}">{b}</p>'
    f'<div style="flex:1"></div>'
    f'<div style="display:flex;flex-direction:column;gap:6px;border-top:1px solid {BRD};padding:16px 0 0 0">'
    f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;color:{MUT}">Ne zaman seçilir?</p>'
    f'<p style="font-family:{SERIF};font-size:30px;font-style:italic;line-height:1.3">“{c}”</p></div>', 'flex:1', ust=u)
    for a, b, c, u in turler)
ic = baslik('Kavramlar', 'Derleme ailesi geniş: 14 tür') + f'''
<div style="display:flex;gap:32px">{kartlar}</div>
<div style="display:flex;gap:32px;align-items:center">
<p style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1;color:{BLUED}">14</p>
<p style="font-size:32px;line-height:1.35;color:{T2}">Grant ve Booth 14 tür sayar; türlerin sınırları her zaman net değildir.</p>
</div>'''
slayt('diger-turler', 5, L, ic, 'Grant ve Booth, 2009; Munn ve ark., 2018; Aromataris ve ark., 2015')

# =====================================================================
# 6 · kanit-piramidi
# =====================================================================
basamak = [('SD/MA', 220, BLUED, L), ('RKÇ', 320, CARD, D), ('Kohort', 420, CARD, D), ('Vaka-kontrol', 520, CARD, D),
           ('Vaka serileri', 620, CARD, D), ('Uzman görüşü', 720, CARD, D)]
sol_pir = ''.join(f'<p style="width:{w}px;align-self:center;padding:13px 0;text-align:center;font-size:26px;line-height:1.3;'
                  f'background:{bg};color:{c};border:1px solid {BRD}">{t}</p>' for t, w, bg, c in basamak)


def hw(y):
    return 130 + (y - 70) * (220 / 360)


def dalga(y):
    x0, x1 = 380 - hw(y) + 4, 380 + hw(y) - 4
    n = max(4, int((x1 - x0) // 44))
    adim = (x1 - x0) / n
    d = f'M {x0:.0f} {y}'
    for k in range(n):
        a = -8 if k % 2 == 0 else 8
        d += f' Q {x0 + adim * (k + 0.5):.0f} {y + a} {x0 + adim * (k + 1):.0f} {y}'
    return f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="3"/>'


svg = (f'<svg aria-label="Tepesi olmayan, basamakları dalgalı çizgilerle ayrılmış kanıt piramidi" style="position:absolute;left:0;top:0" width="760" height="450" viewBox="0 0 760 450">'
       f'<polygon points="250,70 510,70 730,430 30,430" fill="{BLUEL}" stroke="{BLUE}" stroke-width="2"/>'
       + ''.join(dalga(y) for y in (142, 214, 286, 358)) + '</svg>')
etiket = ''.join(pin_p(250, cy - 18, 260, t, 26, D, 'center') for cy, t in
                 [(106, 'RKÇ'), (178, 'Kohort'), (250, 'Vaka-kontrol'), (322, 'Vaka serileri'), (394, 'Uzman görüşü')])
sag_pir = f'''<div style="position:relative;width:760px;height:450px">
{svg}
{etiket}
<x-shape kind="ellipse" style="position:absolute;left:540px;top:0px;width:200px;height:200px;background:rgba(253,252,249,0.75);border:8px solid {OR}"></x-shape>
{pin_p(560, 64, 160, '<b>Sistematik derleme</b>', 26, ORD, 'center', 'line-height:1.3')}
{con(711, 171, 750, 210, OR, 14)}
</div>'''
ic = baslik('Kavramlar', 'Kanıt piramidi: tepe mi, mercek mi?') + f'''
<div style="display:flex;gap:64px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<h3 style="font-size:32px;font-weight:600;color:{MUT}">Klasik piramit</h3>
<p style="font-size:26px;line-height:1.4;color:{T2}">Tepede sistematik derleme ve meta-analiz. Sorun: kötü derleme, iyi çalışmaları da çarpıtabilir.</p>
<div style="display:flex;flex-direction:column;gap:6px;padding:24px 0 0 0">{sol_pir}</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<h3 style="font-size:32px;font-weight:600;color:{BLUED}">Yeni kanıt piramidi</h3>
<p style="font-size:26px;line-height:1.4;color:{T2}">Öneri 1: basamaklar arası çizgiler dalgalı. Öneri 2: sistematik derleme bir mercek, kanıta bakılan araç.</p>
{sag_pir}
</div>
</div>'''
slayt('kanit-piramidi', 6, L, ic, 'Murad ve ark., 2016')

# =====================================================================
# 7 · pico
# =====================================================================
pico = [('P', 'Popülasyon (population)', '13-18 yaş lisanslı futbolcular', BLUEL),
        ('I', 'Müdahale (intervention)', 'Nöromüsküler ısınma programı', '#E6EFF3'),
        ('C', 'Karşılaştırma (comparison)', 'Olağan ısınma', BLUEL),
        ('O', 'Sonuç (outcome)', 'Alt ekstremite sakatlık sıklığı', '#E6EFF3'),
        ('S', 'Çalışma deseni (study design)', 'RKÇ ve küme randomize çalışmalar', CARD)]
P = 'padding:16px 24px'
tb = (f'<table style="font-family:{SANS};font-size:30px;line-height:1.3;color:{D}">'
      f'<tr style="background:{D}"><th style="width:12%;text-align:center;color:{L};{P}">Harf</th>'
      f'<th style="width:40%;text-align:left;color:{L};{P}">Anlamı</th>'
      f'<th style="width:48%;text-align:left;color:{L};{P}">Futbol örneği (kurgu)</th></tr>')
for h_, a, b, bg in pico:
    rk = MUT if h_ == 'S' else BLUED
    tb += (f'<tr style="background:{bg}"><td style="text-align:center;color:{rk};{P}">{h_}</td>'
           f'<td style="{P}">{a}</td><td style="{P}">{b}</td></tr>')
tb += '</table>'
ic = f'''<p style="position:absolute;left:1312px;top:128px;width:480px;font-size:24px;font-weight:600;text-align:center;color:{L};background:{ORD};border-radius:999px;padding:10px 24px">Örnek soru · eğitim amaçlı kurgu</p>
''' + baslik('Sistematik derleme · Adım 1', 'Her şey iyi bir soruyla başlar: PICO') + f'''
{tb}
<p style="font-size:28px;line-height:1.4;background:{CARD};border:1px solid {BRD};border-left:8px solid {OR};border-radius:8px;padding:20px 32px"><b>Nitel sorular için: SPIDER</b> (Sample, Phenomenon of Interest, Design, Evaluation, Research type)</p>'''
slayt('pico', 7, L2, ic, 'Cooke ve ark., 2012',
      bolum='PICO, protokol ve kayıt, arama, PRISMA 2020 akışı, yanlılık riski ve GRADE.')

# =====================================================================
# 8 · protokol-kayit
# =====================================================================
adimlar = [('1', 'Protokolü yaz', 'yöntem, veriye bakmadan önce'), ('2', 'Kaydet (PROSPERO)', 'herkese açık, tarih damgalı'),
           ('3', 'Sonra ara', 'tarama kayıttan sonra başlar')]
parca = []
for i, (n, t, a) in enumerate(adimlar):
    if i:
        parca.append(f'<x-shape kind="arrow-right" style="background:{OR};width:64px;height:32px"></x-shape>')
    parca.append(kart(f'<div style="display:flex;gap:20px;align-items:baseline"><p style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1;color:{BLUED}">{n}</p>'
                      f'<h3 style="font-size:34px;font-weight:600;line-height:1.2">{t}</h3></div>'
                      f'<p style="font-size:24px;line-height:1.4;color:{T2}">{a}</p>', 'flex:1;align-self:stretch', ust=BLUE, pad='28px 32px'))
maddeler = ['<b>Protokol:</b> yöntem, veriye bakmadan önce yazılır.',
            '<b>PROSPERO:</b> Şubat 2011\'den beri uluslararası, ücretsiz kayıt sistemi.',
            '<b>Amaç:</b> planlanmamış tekrarları azaltmak, şeffaflığı artırmak.',
            '<b>Zamanlama:</b> kayıt ideal olarak tarama başlamadan yapılır.']
kale = f'''<div style="position:relative;width:240px;height:130px">
<div style="position:absolute;left:20px;top:10px;width:200px;height:14px;background:{L}"></div>
<div style="position:absolute;left:20px;top:10px;width:14px;height:110px;background:{L}"></div>
<div style="position:absolute;left:206px;top:10px;width:14px;height:110px;background:{L}"></div>
<div style="position:absolute;left:0px;top:118px;width:240px;height:6px;background:{BLUEDK}"></div>
</div>'''
ic = baslik('Sistematik derleme · Adım 2', 'Protokolü yaz, kaydet, sonra ara') + f'''
<div style="display:flex;align-items:center;gap:24px">{''.join(parca)}</div>
<div style="display:flex;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{''.join(f'<p style="font-size:28px;line-height:1.4">{m}</p>' for m in maddeler)}
</div>
<div style="width:640px;display:flex;flex-direction:column;gap:20px;background:{D};border-radius:16px;padding:32px 40px">
<div style="display:flex;gap:32px;align-items:center">
{kale}
<p style="font-family:{SERIF};font-size:36px;font-style:italic;line-height:1.25;color:{L}">Direkler maçtan önce dikilir.</p>
</div>
<p style="font-size:24px;line-height:1.4;color:{DT2}"><b>Spordan örnek:</b> PROSPERO CRD42024532607 (Boke ve ark., 2025)</p>
</div>
</div>'''
slayt('protokol-kayit', 8, L2, ic, 'Booth ve ark., 2012; Boke ve ark., 2025')

# =====================================================================
# 9 · arama
# =====================================================================
tabanlar = ['PubMed', 'SPORTDiscus', 'Web of Science', 'YÖK Tez', 'Google Akademik']
tlist = ''.join(f'<p style="font-size:30px;font-weight:600;background:{CARD};border:1px solid {BRD};border-left:8px solid {BLUE if t != "Google Akademik" else OR};border-radius:8px;padding:14px 28px">{t}</p>' for t in tabanlar)
ic = baslik('Sistematik derleme · Adım 3', 'Arama: tek taban yetmez') + f'''
<div style="display:flex;gap:56px">
<div style="width:520px;display:flex;flex-direction:column;gap:12px">
<p style="font-size:24px;font-weight:600;letter-spacing:2px;color:{MUT}">Önerilen tabanlar</p>
{tlist}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;gap:32px;align-items:center;background:#FCEFD9;border:2px solid {OR};border-radius:16px;padding:28px 36px">
<x-icon name="Warning" style="color:{ORD};width:64px;height:64px"></x-icon>
<div style="flex:1;display:flex;flex-direction:column;gap:8px">
<p style="font-size:30px;font-weight:600;line-height:1.3">Google Akademik: ek kaynak, ana kaynak değil</p>
<p style="font-size:28px;line-height:1.4;color:{T2}">28 arama sisteminden yalnız 14'ü ana araç olmaya uygun.</p>
</div>
<p style="font-family:{SERIF};font-size:72px;font-weight:600;line-height:1;color:{ORD};white-space:nowrap">14/28</p>
</div>
<p style="font-size:28px;line-height:1.4">Spor meta-analizleri SPORTDiscus'u tarıyor (Lauersen 2014, Thorborg 2017).</p>
<p style="font-size:28px;line-height:1.4">YÖK Tez: yayımlanmamış tezler; ör. Böke (2020) meta-analiz tezi.</p>
<p style="font-size:24px;line-height:1.4;color:{MUT}">Tabanlara erişim üniversite aboneliğine bağlıdır.</p>
</div>
</div>'''
slayt('arama', 9, L2, ic, 'Gusenbauer ve Haddaway, 2020; Lauersen ve ark., 2014; Thorborg ve ark., 2017; Böke, 2020')

# =====================================================================
# 10 · prisma  (akis semasi)
# node listesi (host 1664x518):
#  serit: Tanimlama 0,0,168,114 · Tarama 0,146,168,256 · Dahil 0,434,168,84
#  ana:   M1 200,0,700,114 · M2 200,146,700,54 · M3 200,232,700,54 · M4 200,318,700,84 · M5 200,434,700,84
#  yan:   S1 980,0,684,114 · S2 980,146,684,54 · S3 980,232,684,54 · S4 980,318,684,84
# =====================================================================
def kutu(x, y, w, h, metin, tur='ana'):
    if tur == 'ana':
        st = f'background:{CARD};border:2px solid {BLUE}'
    else:
        st = f'background:#F6EDE6;border:2px dashed {OR}'
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;display:flex;align-items:center;'
            f'{st};border-radius:10px;padding:0 20px"><p style="font-size:24px;line-height:1.25">{metin}</p></div>')


def serit(y, h, t):
    return (f'<div style="position:absolute;left:0px;top:{y}px;width:168px;height:{h}px;display:flex;align-items:center;'
            f'justify-content:center;background:{BLUED};border-radius:10px"><p style="font-size:24px;font-weight:600;color:{L};text-align:center">{t}</p></div>')


pr = [serit(0, 114, 'Tanımlama'), serit(146, 256, 'Tarama'), serit(434, 84, 'Dahil etme'),
      kutu(200, 0, 700, 114, '<b>Tanımlanan kayıtlar:</b><br>veri tabanları (n = ) · kayıtlar (registers) (n = )'),
      kutu(200, 146, 700, 54, 'Taranan kayıtlar (n = )'),
      kutu(200, 232, 700, 54, 'Erişilmeye çalışılan raporlar (n = )'),
      kutu(200, 318, 700, 84, 'Uygunluk açısından değerlendirilen raporlar (n = )'),
      kutu(200, 434, 700, 84, '<b>Derlemeye dahil edilen çalışmalar (n = )</b><br>Dahil edilen çalışmaların raporları (n = )'),
      kutu(980, 0, 684, 114, '<b>Taramadan önce çıkarılanlar:</b> yinelenen kayıtlar (n = ) · otomasyonla uygun değil işaretlenen (n = ) · diğer nedenler (n = )', 'yan'),
      kutu(980, 146, 684, 54, 'Dışlanan kayıtlar (n = )', 'yan'),
      kutu(980, 232, 684, 54, 'Erişilemeyen raporlar (n = )', 'yan'),
      kutu(980, 318, 684, 84, '<b>Dışlanan raporlar, nedenleriyle:</b><br>Neden 1 (n = ) · Neden 2 (n = )', 'yan')]
for (a, b) in [(114, 146), (200, 232), (286, 318), (402, 434)]:
    pr.append(con(550, a, 550, b, BLUED, 3, 'end'))
for y in (57, 173, 259, 360):
    pr.append(con(900, y, 980, y, ORD, 3, 'end'))
olgular = ['27 maddelik raporlama kontrol listesi + akış şeması', '“Çalışma” ile “rapor” ayrı sayılır.', 'Spor bilimine uyarlama: PERSiST kılavuzu (2022)']
ic = baslik('Sistematik derleme · Adım 4', 'PRISMA 2020: derlemenin kadro listesi') + f'''
<div style="display:flex;flex-direction:column;gap:20px">
<div style="position:relative;width:1664px;height:518px">
{chr(10).join(pr)}
</div>
<div style="display:flex;gap:16px">
{''.join(f'<p style="flex:1;font-size:24px;line-height:1.3;background:{L2};border-radius:8px;padding:12px 20px">{o}</p>' for o in olgular)}
</div>
</div>'''
slayt('prisma', 10, L, ic, 'Page ve ark., 2021; Ardern ve ark., 2022')

# =====================================================================
# 11 · yanlilik-grade
# =====================================================================
RK = {'d': BLUE, 'b': '#C9A961', 'y': ORD}
alanlar = [('Randomizasyon', 'd'), ('Müdahaleden sapma', 'b'), ('Eksik veri', 'd'), ('Sonuç ölçümü', 'y'), ('Raporlanan sonucun seçimi', 'b')]


def isik(sec):
    out = ''
    for k in ('d', 'b', 'y'):
        r = RK[k] if k == sec else '#E4DFD4'
        out += f'<x-shape kind="ellipse" style="background:{r};width:30px;height:30px"></x-shape>'
    return out


rob = ''.join(f'<div style="display:flex;gap:10px;align-items:center;background:{CARD};border:1px solid {BRD};border-radius:10px;padding:10px 20px">'
              f'{isik(s)}<p style="font-size:26px;padding:0 0 0 12px">{t}</p></div>' for t, s in alanlar)
lejant = ''.join(f'<div style="display:flex;gap:8px;align-items:center"><x-shape kind="ellipse" style="background:{RK[k]};width:24px;height:24px"></x-shape><p style="font-size:24px;color:{T2}">{t}</p></div>'
                 for k, t in (('d', 'düşük risk'), ('b', 'bazı endişeler'), ('y', 'yüksek risk')))
grade = [('Yüksek · RKÇ buradan başlar', 760, BLUED, L), ('Orta', 680, BLUE, L),
         ('Düşük · gözlemsel çalışma buradan başlar', 620, BLUEL, D), ('Çok düşük', 540, L2, D)]
merdiven = ''.join(f'<p style="width:{w}px;font-size:26px;font-weight:600;background:{bg};color:{c};border-radius:8px;padding:13px 24px">{t}</p>' for t, w, bg, c in grade)
ic = baslik('Sistematik derleme · Adım 5', 'Kanıtı mı değerlendiriyorum, derlemeyi mi?') + f'''
<div style="display:flex;gap:64px">
<div style="width:760px;display:flex;flex-direction:column;gap:12px">
<h3 style="font-size:32px;font-weight:600;line-height:1.2">RoB 2: tek tek RKÇ'ler, 5 alan</h3>
{rob}
<div style="display:flex;gap:28px;padding:8px 0 0 0">{lejant}</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<h3 style="font-size:32px;font-weight:600;line-height:1.2">GRADE: kanıtın kesinliği, 4 düzey</h3>
{merdiven}
<div style="display:flex;gap:20px;align-items:center;padding:14px 0 0 0">
<x-shape kind="arrow-down" style="background:{OR};width:36px;height:72px"></x-shape>
<p style="flex:1;font-size:26px;line-height:1.35"><b style="color:{ORD}">Düşürür:</b> yanlılık riski, kesinsizlik, tutarsızlık, dolaylılık, yayın yanlılığı</p>
</div>
<div style="display:flex;gap:20px;align-items:center">
<x-shape kind="arrow-up" style="background:{BLUE};width:36px;height:72px"></x-shape>
<p style="flex:1;font-size:26px;line-height:1.35"><b style="color:{BLUED}">Yükseltebilir:</b> büyük etki</p>
</div>
</div>
</div>'''
slayt('yanlilik-grade', 11, L, ic, 'Sterne ve ark., 2019; Balshem ve ark., 2011')

# =====================================================================
# 12 · etki-buyuklugu
# =====================================================================
P = 'padding:12px 20px'
tb = (f'<table style="font-family:{SANS};font-size:26px;line-height:1.3;color:{D}">'
      f'<tr style="background:{D}"><th style="width:36%;text-align:left;color:{L};{P}">Veri türü</th>'
      f'<th style="width:42%;text-align:left;color:{L};{P}">Ölçü</th>'
      f'<th style="width:22%;text-align:center;color:{L};{P}">“Fark yok” değeri</th></tr>')
for j, (a, b, c) in enumerate([('Sürekli (sıçrama, VO2maks)', 'Cohen d, Hedges g', '0'),
                                ('İkili (sakatlandı / sakatlanmadı)', 'Risk oranı (RR), olasılık oranı (OR)', '1'),
                                ('İki değişken ilişkisi', 'Korelasyon r', '0')]):
    bg = CARD if j % 2 == 0 else L2
    tb += f'<tr style="background:{bg}"><td style="{P}">{a}</td><td style="{P}">{b}</td><td style="text-align:center;color:{BLUED};{P}">{c}</td></tr>'
tb += '</table>'


def rx(v):
    return round(40 + v * 1000 / 1.4)


cet = [pin_p(0, 0, 900, '<b>Cohen (1988)</b> · genel', 24, D), con(40, 66, 1040, 66, MUT, 3),
       pin_p(0, 150, 900, '<b>Hopkins ve ark. (2009)</b> · spor bilimi', 24, D), con(40, 216, 1040, 216, MUT, 3)]
for v, t in ((0.2, '0,2 küçük'), (0.5, '0,5 orta'), (0.8, '0,8 büyük')):
    cet.append(f'<div style="position:absolute;left:{rx(v) - 4}px;top:50px;width:8px;height:32px;background:{BLUED}"></div>')
    cet.append(pin_p(rx(v) - 90, 86, 180, t, 24, BLUED, 'center'))
for v, t in ((0.2, '0,20 küçük'), (0.6, '0,60 orta'), (1.2, '1,20 büyük')):
    cet.append(f'<div style="position:absolute;left:{rx(v) - 4}px;top:200px;width:8px;height:32px;background:{ORD}"></div>')
    cet.append(pin_p(rx(v) - 90, 236, 180, t, 24, ORD, 'center'))
ic = baslik('Meta-analiz', 'Meta-analiz p değerini değil, etki büyüklüğünü birleştirir') + f'''
{tb}
<div style="display:flex;gap:48px;align-items:center">
<div style="position:relative;width:1080px;height:272px">
{chr(10).join(cet)}
</div>
{kart(f'<div style="display:flex;gap:16px;align-items:center"><x-icon name="Activity" style="color:{BLUED};width:40px;height:40px"></x-icon><p style="font-size:24px;font-weight:600;letter-spacing:2px;color:{BLUED}">Ters varyans ağırlığı</p></div><p style="font-family:{SERIF};font-size:40px;font-weight:600;line-height:1.15">Ağırlık = kesinlik.</p><p style="font-size:26px;line-height:1.4;color:{T2}">Kesin çalışma daha çok söz hakkı alır.</p>', 'flex:1', ust=BLUE, pad='28px 32px')}
</div>'''
slayt('etki-buyuklugu', 12, L, ic, 'Borenstein ve ark., 2021; Borenstein ve ark., 2010; Cohen, 1988; Hopkins ve ark., 2009',
      bolum='Etki büyüklüğü, sabit ve rastgele etkiler, heterojenlik, orman ve huni grafiği.')

# =====================================================================
# 13 · modeller-heterojenlik
# =====================================================================
sabit = [con(340, 8, 340, 162, BLUED, 3)] + [
    f'<x-shape kind="ellipse" style="position:absolute;left:{x - 13}px;top:{y - 13}px;width:26px;height:26px;background:{OR}"></x-shape>'
    for x, y in ((318, 24), (362, 54), (326, 84), (358, 114), (322, 144))]
bell = (f'<svg aria-label="Çan eğrisi: gerçek etkiler bir dağılımdan gelir" style="position:absolute;left:0;top:0" width="680" height="170" viewBox="0 0 680 170">'
        f'<path d="M 60 150 C 220 150 250 20 340 20 C 430 20 460 150 620 150 Z" fill="{BLUEL}" stroke="{BLUE}" stroke-width="3"/>'
        f'<line x1="340" y1="20" x2="340" y2="150" stroke="{BLUED}" stroke-width="3" stroke-dasharray="8 6"/></svg>')
rastgele = [bell] + [
    f'<x-shape kind="ellipse" style="position:absolute;left:{x - 13}px;top:{137}px;width:26px;height:26px;background:{OR}"></x-shape>'
    for x in (190, 280, 360, 430, 505)]
panel = lambda baslik_, aciklama, ogeler, etiket: kart(
    f'<h3 style="font-size:32px;font-weight:600;line-height:1.2">{baslik_}</h3>'
    f'<p style="font-size:26px;line-height:1.4;color:{T2}">{aciklama}</p>'
    f'<div style="position:relative;width:680px;height:170px;align-self:center">{"".join(ogeler)}</div>'
    f'<p style="font-family:{SERIF};font-size:28px;font-style:italic;text-align:center">{etiket}</p>', 'flex:1', pad='28px 36px')
i2x = [0, 416, 832, 1248, 1664]
i2 = [f'<div style="position:absolute;left:0px;top:0px;width:1664px;height:28px;border-radius:14px;background:linear-gradient(to right, {BLUEL}, {BLUE} 50%, {OR})"></div>']
for x, t in zip(i2x, ['%0', '%25 düşük', '%50 orta', '%75 yüksek', '%100']):
    if 0 < x < 1664:
        i2.append(f'<div style="position:absolute;left:{x - 2}px;top:0px;width:4px;height:40px;background:{D}"></div>')
    if x == 0:
        i2.append(pin_p(0, 44, 200, t, 24, T2))
    elif x == 1664:
        i2.append(pin_p(1464, 44, 200, t, 24, T2, 'right'))
    else:
        i2.append(pin_p(x - 100, 44, 200, t, 24, D, 'center', 'font-weight:600'))
ic = baslik('Meta-analiz', 'Sabit mi, rastgele mi? Ve I²') + f'''
<div style="display:flex;gap:32px">
{panel('Sabit etkiler (fixed-effect)', 'Tek bir gerçek etki; farklar örnekleme hatası.', sabit, 'Sabit: tek oda, beş ölçüm')}
{panel('Rastgele etkiler (random-effects)', 'Gerçek etki çalışmadan çalışmaya değişir.', rastgele, 'Rastgele: beş şehir, ortalama sıcaklık')}
</div>
<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:28px;line-height:1.35"><b>I² = %100 × (Q - sd) / Q:</b> değişkenliğin şanstan gelmeyen yüzdesi · <span style="color:{T2}">%25 · %50 · %75: düşük · orta · yüksek (çekinceli etiketler)</span></p>
<div style="position:relative;width:1664px;height:80px">{''.join(i2)}</div>
<p style="font-size:26px;line-height:1.35;color:{ORD}">Q testi az çalışmada zayıf: anlamsız Q, homojenlik kanıtı değil.</p>
</div>'''
slayt('modeller-heterojenlik', 13, L2, ic, 'Borenstein ve ark., 2010; Higgins ve ark., 2003; Borenstein ve ark., 2021')

# =====================================================================
# 14 · orman-grafigi
# =====================================================================
veri = [('Çalışma A', 0.20, -0.30, 0.70, 14.1), ('Çalışma B', 0.55, 0.15, 0.95, 22.1), ('Çalışma C', 0.35, 0.05, 0.65, 39.2),
        ('Çalışma D', 0.80, 0.10, 1.50, 7.2), ('Çalışma E', 0.10, -0.35, 0.55, 17.4)]
YS = [70, 124, 178, 232, 286]
YP = 360


def gx(g):
    return 40 + (g + 0.5) * 400


def tr_(v):
    return f'{v:.2f}'.replace('.', ',')


s = [f'<svg aria-label="Orman grafiği: beş kurgu çalışma, kareler ve güven aralıkları, g = 0 etkisizlik çizgisi ve birleşik etki elması" style="position:absolute;left:0;top:0" width="880" height="444" viewBox="0 0 880 444">',
     f'<line x1="0" y1="326" x2="880" y2="326" stroke="{BRD}" stroke-width="2"/>',
     f'<line x1="{gx(0):.0f}" y1="44" x2="{gx(0):.0f}" y2="400" stroke="{ORD}" stroke-width="3" stroke-dasharray="10 8"/>',
     f'<line x1="40" y1="400" x2="840" y2="400" stroke="{MUT}" stroke-width="2"/>']
for g in (-0.5, 0, 0.5, 1.0, 1.5):
    s.append(f'<line x1="{gx(g):.0f}" y1="400" x2="{gx(g):.0f}" y2="410" stroke="{MUT}" stroke-width="2"/>')
for (n, g, lo, hi, w), y in zip(veri, YS):
    k = 6 * (w ** 0.5)
    s.append(f'<line x1="{gx(lo):.0f}" y1="{y}" x2="{gx(hi):.0f}" y2="{y}" stroke="{D}" stroke-width="3"/>')
    s.append(f'<rect x="{gx(g) - k / 2:.0f}" y="{y - k / 2:.0f}" width="{k:.0f}" height="{k:.0f}" fill="{BLUED}"/>')
s.append(f'<polygon points="{gx(0.17):.0f},{YP} {gx(0.36):.0f},{YP - 18} {gx(0.55):.0f},{YP} {gx(0.36):.0f},{YP + 18}" fill="{OR}"/>')
s.append('</svg>')
tick = ''.join(pin_p(round(gx(g)) - 40, 410, 80, t, 24, MUT, 'center') for g, t in ((-0.5, '-0,5'), (0, '0'), (0.5, '0,5'), (1.0, '1'), (1.5, '1,5')))
isim = pin_p(0, 0, 280, '<b>Çalışma (kurgu)</b>', 24, MUT) + ''.join(pin_p(0, y - 17, 280, n, 24) for (n, *_), y in zip(veri, YS)) \
    + pin_p(0, YP - 17, 280, '<b>Birleşik (elmas)</b>', 24, ORD)
deger = pin_p(0, 0, 330, '<b>g (%95 GA)</b>', 24, MUT) + pin_p(340, 0, 124, '<b>Ağırlık %</b>', 24, MUT, 'right')
for (n, g, lo, hi, w), y in zip(veri, YS):
    deger += pin_p(0, y - 17, 330, f'{tr_(g)} ({tr_(lo)} ile {tr_(hi)})', 24)
    deger += pin_p(340, y - 17, 124, f'{w:.1f}'.replace('.', ','), 24, D, 'right')
deger += pin_p(0, YP - 17, 330, '<b>0,36 (0,17 ile 0,55)</b>', 24, ORD) + pin_p(340, YP - 17, 124, '<b>100</b>', 24, ORD, 'right')
deger += pin_p(0, 396, 464, 'Q = 4,06 (sd = 4) · I² ≈ %2', 24, T2)
glif = {
    'kare': f'<div style="width:24px;height:24px;background:{BLUED}"></div>',
    'cizgi': f'<div style="width:40px;height:4px;background:{D}"></div>',
    'dikey': f'<div style="width:4px;height:32px;background:{ORD}"></div>',
    'elmas': f'<x-shape kind="diamond" style="background:{OR};width:44px;height:26px"></x-shape>'}
lej = ''.join(f'<div style="display:flex;gap:14px;align-items:center"><div style="width:48px;display:flex;justify-content:center">{glif[k]}</div><p style="font-size:24px;color:{T2}">{t}</p></div>'
              for k, t in (('kare', 'Kare: çalışmanın etkisi · büyüklüğü = ağırlık'), ('cizgi', 'Çizgi: %95 güven aralığı'),
                           ('dikey', 'Dikey çizgi: etki yok (g = 0)'), ('elmas', 'Elmas: birleşik etki')))
ic = baslik('Meta-analiz', 'Orman grafiği (forest plot) nasıl okunur?') + f'''
<div style="display:flex;flex-direction:column;gap:20px">
<div style="display:flex;gap:24px;align-items:center;justify-content:space-between">
<p style="font-size:26px;line-height:1.3"><b>Senaryo (kurgu):</b> Pliometrik antrenmanın dikey sıçramaya etkisi, Hedges g</p>
<p style="font-size:24px;font-weight:600;color:{L};background:{ORD};border-radius:999px;padding:8px 24px;white-space:nowrap">EĞİTİM AMAÇLI KURGU VERİ · gerçek çalışmalar değildir</p>
</div>
<div style="display:flex;gap:20px">
<div style="position:relative;width:280px;height:444px">{isim}</div>
<div style="position:relative;width:880px;height:444px">{''.join(s)}{tick}</div>
<div style="position:relative;width:464px;height:444px">{deger}</div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px 32px">{lej}</div>
</div>'''
slayt('orman-grafigi', 14, L, ic, 'Okuma anahtarı: Borenstein ve ark., 2021 · Veri: eğitim amaçlı kurgu')

# =====================================================================
# 15 · huni-grafigi
# =====================================================================
nokta_sim = [(372, 40), (392, 58), (362, 82), (402, 98), (346, 118), (416, 132), (332, 160), (430, 168), (306, 196), (456, 204),
             (286, 232), (476, 238), (252, 262), (508, 264), (222, 280), (540, 280)]
nokta_asim = [(372, 40), (392, 58), (362, 82), (402, 98), (346, 118), (416, 132), (360, 160), (430, 168), (456, 204), (420, 196),
              (476, 238), (500, 226), (508, 264), (540, 280), (470, 276), (566, 270)]


def huni(noktalar, bos=False, etiket=''):
    s = [f'<svg aria-label="{etiket}" style="position:absolute;left:0;top:0" width="760" height="300" viewBox="0 0 760 300">']
    if bos:
        s.append(f'<ellipse cx="250" cy="250" rx="120" ry="40" fill="{ORL}" stroke="{OR}" stroke-width="3" stroke-dasharray="10 8"/>')
    s += [f'<line x1="380" y1="20" x2="80" y2="292" stroke="{MUT}" stroke-width="2" stroke-dasharray="8 6"/>',
          f'<line x1="380" y1="20" x2="680" y2="292" stroke="{MUT}" stroke-width="2" stroke-dasharray="8 6"/>',
          f'<line x1="380" y1="14" x2="380" y2="292" stroke="{BLUED}" stroke-width="3"/>',
          f'<line x1="20" y1="296" x2="740" y2="296" stroke="{MUT}" stroke-width="2"/>',
          f'<line x1="20" y1="296" x2="20" y2="10" stroke="{MUT}" stroke-width="2"/>']
    s += [f'<circle cx="{x}" cy="{y}" r="11" fill="{BLUED}"/>' for x, y in noktalar]
    s.append('</svg>')
    return ''.join(s)


def huni_kart(bas, renk, svg, alt):
    return kart(f'<h3 style="font-size:32px;font-weight:600;line-height:1.2;color:{renk}">{bas}</h3>'
                f'<div style="position:relative;width:760px;height:300px;align-self:center">{svg}</div>'
                f'<p style="font-size:24px;line-height:1.4;color:{T2}">{alt}</p>', 'flex:1', pad='24px 28px')


ic = baslik('Meta-analiz', 'Huni grafiği (funnel plot): kayıp çalışmalar nerede?') + f'''
<div style="display:flex;gap:32px">
{huni_kart('Simetrik huni: yanlılık işareti yok', BLUED, huni(nokta_sim, False, 'Simetrik huni grafiği'), 'Yatay eksen: etki büyüklüğü · dikey eksen: kesinlik (yukarı = daha kesin)')}
{huni_kart('Boş köşe: asimetri', ORD, huni(nokta_asim, True, 'Asimetrik huni grafiği, sol alt köşe boş'), 'Sol alt köşe boş: küçük ve etkisiz çalışmalar yok')}
</div>
<div style="display:flex;gap:40px;align-items:center">
<p style="flex:1;font-size:28px;line-height:1.4"><b>Egger testi:</b> asimetriyi regresyonla ölçer.</p>
<p style="font-family:{SERIF};font-size:40px;font-style:italic;font-weight:600;line-height:1.2;color:{ORD};border-left:8px solid {OR};padding:4px 0 4px 28px">“Asimetri bir alarmdır, kanıt değil.”</p>
</div>'''
slayt('huni-grafigi', 15, L2, ic, 'Egger ve ark., 1997; Sterne ve ark., 2011')

# =====================================================================
# 16 · ornek-fifa
# =====================================================================
def fifa(yazar, sayi, renk, satir, ust):
    return kart(f'<p style="font-size:26px;font-weight:600;color:{T2}">{yazar}</p>'
                f'<div style="display:flex;gap:24px;align-items:baseline"><p style="font-family:{SERIF};font-size:128px;font-weight:600;line-height:1;color:{renk}">{sayi}</p>'
                f'<p style="font-size:28px;color:{T2}">sakatlıkta azalma (FIFA 11+)</p></div>'
                + ''.join(f'<p style="font-size:26px;line-height:1.35;border-top:1px solid {BRD};padding:10px 0 0 0"><b>{a}:</b> {b}</p>' for a, b in satir),
                'flex:1', ust=ust, pad='28px 36px', gap=10)


ic = baslik('Spordan örnek', 'Aynı soru, aynı yıl, iki farklı sayı: FIFA 11+') + f'''
<div style="display:flex;gap:32px">
{fifa('Thorborg ve ark. (2017)', '%39', BLUED, [('Dahil edilen', '6 küme RKÇ'), ('Taranan tabanlar', '6 taban (SPORTDiscus dahil)'), ('Etki ölçüsü', 'IRR'), ('Bulgu', 'IRR 0,61 (0,48-0,77) · %39 azalma')], BLUE)}
{fifa('Sadigursky ve ark. (2017)', '%30', ORD, [('Dahil edilen', '6 RKÇ, 6.344 oyuncu'), ('Taranan tabanlar', '5 taban (LILACS, SciELO dahil)'), ('Etki ölçüsü', 'RR'), ('Bulgu', 'RR 0,70 (0,52-0,93) · %30 azalma')], OR)}
</div>
<div style="display:flex;gap:32px;align-items:center;background:{D};border-radius:16px;padding:24px 36px">
<p style="flex:1;font-family:{SERIF};font-size:34px;font-weight:600;line-height:1.25;color:{L}">Yön aynı, büyüklük farklı. Sonuç, arama ve dahil etme kararlarına bağlıdır.</p>
<p style="font-size:24px;line-height:1.5;color:{DT2}">Farklar: tabanlar ·<br>dahil etme ölçütleri ·<br>etki ölçüsü</p>
</div>'''
slayt('ornek-fifa', 16, L, ic, 'Thorborg ve ark., 2017; Sadigursky ve ark., 2017',
      bolum='FIFA 11+ için iki meta-analiz ve Türkiye\'den üç örnek.')

# =====================================================================
# 17 · ornek-turkiye
# =====================================================================
W = (220, 440, 360)
bas = (f'<div style="display:flex;gap:32px;padding:0 32px">'
       f'<p style="width:{W[0]}px;font-size:24px;font-weight:600;color:{MUT}">Anahtar kavram</p>'
       f'<p style="width:{W[1]}px;font-size:24px;font-weight:600;color:{MUT}">Çalışma</p>'
       f'<p style="width:{W[2]}px;font-size:24px;font-weight:600;color:{MUT}">Ne öğretir</p>'
       f'<p style="flex:1;font-size:24px;font-weight:600;color:{MUT}">Bulgu</p></div>')
tur = [('Tez', BLUED, 'Böke (2020), doktora tezi, İnönü Üniv.', 'Yerli bir meta-analiz tezi', '51 çalışma, 144 etki büyüklüğü · bilişsel d = 1,179 · duyuşsal d = 0,279'),
       ('I² = 83,83', ORD, 'Aygun ve ark. (2024), Children', 'Yüksek heterojenlik, rastgele etkiler', 'g = 0,337 (0,199-0,476) · I² = 83,83'),
       ('PROSPERO', BLUED, 'Boke ve ark. (2025), Frontiers in Psychology', 'Protokol kaydı, çok dilli arama', 'PROSPERO kayıtlı · 40 çalışma, 3.985 katılımcı · ES = 0,459 (0,324-0,592)')]
sat = ''.join(f'<div style="display:flex;gap:32px;align-items:center;background:{CARD};border:1px solid {BRD};border-radius:16px;padding:24px 32px">'
              f'<div style="width:{W[0]}px"><p style="font-size:26px;font-weight:600;color:{L};background:{r};border-radius:999px;padding:8px 20px;text-align:center">{k}</p></div>'
              f'<p style="width:{W[1]}px;font-size:26px;line-height:1.35;font-weight:600">{a}</p>'
              f'<p style="width:{W[2]}px;font-size:26px;line-height:1.35;color:{T2}">{b}</p>'
              f'<p style="flex:1;font-size:26px;line-height:1.35">{c}</p></div>' for k, r, a, b, c in tur)
ic = baslik('Spordan örnek · Türkiye', 'Türkiye\'den üç örnek: bu sizin tez konunuz olabilir') + f'''
<div style="display:flex;flex-direction:column;gap:16px">
{bas}
{sat}
</div>
<p style="font-family:{SERIF};font-size:40px;font-style:italic;font-weight:600;line-height:1.2;color:{BLUED};border-left:8px solid {BLUE};padding:4px 0 4px 28px">Bu yöntem sizin tez konunuz olabilir.</p>'''
slayt('ornek-turkiye', 17, L2, ic, 'Böke, 2020; Aygun ve ark., 2024; Boke ve ark., 2025')

# =====================================================================
# 18 · etik
# =====================================================================
riskler = [('Yayın yanlılığı', 'Suistimal', 'Yayımlamamak: raporlamamak bilimsel suistimaldir.'),
           ('Tekrar yayın', '9,5 → 3,9', 'Aynı hastalar iki kez sayılınca NNT 9,5\'ten 3,9\'a düştü.'),
           ('Geri çekilmiş çalışmalar', '%8,4', 'Çıkarılınca meta-analizlerin %8,4\'ünde etkinin yönü değişti.'),
           ('Çıkar çatışması', 'Seri üretim', 'Derlemelerin önemli kısmı gereksiz, yanıltıcı, çıkar çatışmalı.')]
rk = ''.join(kart(f'<div style="display:flex;gap:12px;align-items:center"><x-icon name="Warning" style="color:{ORD};width:36px;height:36px"></x-icon>'
                  f'<p style="font-size:24px;font-weight:600;line-height:1.3;color:{ORD}">{a}</p></div>'
                  f'<p style="font-family:{SERIF};font-size:52px;font-weight:600;line-height:1.1;white-space:nowrap">{b}</p>'
                  f'<p style="font-size:26px;line-height:1.4;color:{T2}">{c}</p>', 'flex:1', ust=OR, pad='28px 28px', gap=14)
             for a, b, c in riskler)
ic = baslik('Araştırma etiği', 'Etik kurul gerekmez, etik sorumluluk gerekir') + f'''
<div style="display:flex;gap:24px">{rk}</div>
<div style="display:flex;gap:24px;align-items:center;background:{BLUEL};border-left:8px solid {BLUE};border-radius:12px;padding:24px 36px">
<x-icon name="CheckCircle" style="color:{BLUED};width:48px;height:48px"></x-icon>
<p style="flex:1;font-size:30px;line-height:1.35"><b>Çözüm başlangıcı:</b> protokolü önceden kaydet.</p>
<p style="font-family:{SERIF};font-size:36px;font-weight:600;color:{BLUED};white-space:nowrap">Önceden kayıt = şeffaflık</p>
</div>'''
slayt('etik', 18, L, ic, 'Chalmers, 1990; Tramèr ve ark., 1997; Xu ve ark., 2025; Ioannidis, 2016; Booth ve ark., 2012',
      bolum='Derlemeye sızan etik riskler; güçlü ve zayıf yönler.')

# =====================================================================
# 19 · elestirel
# =====================================================================
def liste(bas, renk, isaret, ogeler):
    return kart(f'<h3 style="font-size:34px;font-weight:600;color:{renk}">{bas}</h3>'
                + ''.join(f'<div style="display:flex;gap:16px;align-items:baseline"><p style="font-size:30px;font-weight:600;color:{renk}">{isaret}</p><p style="font-size:28px;line-height:1.35">{o}</p></div>' for o in ogeler),
                'flex:1', ust=renk, pad='28px 36px')


ic = baslik('Eleştirel bakış', 'Güçlü ama kusursuz değil') + f'''
<div style="display:flex;gap:32px">
{liste('Artılar', BLUED, '+', ['daha kesin tahmin', 'farklılığın kendisi incelenir', 'yöntem açık ve tekrarlanabilir'])}
{liste('Eksiler', ORD, '-', ['sonuç, arama kararlarına bağlı', 'asimetri ve yayın yanlılığı', 'seri üretim'])}
</div>
<div style="display:flex;gap:48px;align-items:end">
<div style="display:flex;flex-direction:column;gap:6px">
<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{BLUED}">266.782</p>
<p style="font-size:24px;line-height:1.4;color:{T2}">PubMed'de “sistematik derleme” · 58.611 “meta-analiz” (1986-2015)</p>
</div>
<div style="display:flex;flex-direction:column;gap:6px">
<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{ORD}">%70,38</p>
<p style="font-size:24px;line-height:1.4;color:{T2}">Spor sakatlığı meta-analizlerinin<br>PRISMA 2020'ye ortalama uyumu</p>
</div>
<p style="flex:1;font-family:{SERIF};font-size:32px;font-style:italic;line-height:1.3;text-align:right">Okuduğunuz meta-analiz kendi kurallarının yüzde kaçına uyuyor?</p>
</div>'''
slayt('elestirel', 19, L2, ic, 'Borenstein ve ark., 2021; Grant ve Booth, 2009; Ioannidis, 2016; Plakias ve ark., 2025; Thorborg ve ark., 2017; Sadigursky ve ark., 2017')

# =====================================================================
# 20 · ozet (koyu)
# =====================================================================
ozet = [('1', '<x-icon name="Settings" style="color:#F08A52;width:48px;height:48px"></x-icon>', 'Sistematik derleme bir süreç, meta-analiz bir istatistik tekniği.'),
        ('2', '<x-icon name="Lock" style="color:#F08A52;width:48px;height:48px"></x-icon>', 'Soru (PICO) ve kayıt (PROSPERO) aramadan önce gelir.'),
        ('3', '<x-shape kind="diamond" style="background:#F08A52;width:56px;height:40px"></x-shape>', 'Orman grafiğinde önce elmasa, sonra dikey çizgiye bakın.'),
        ('4', '<x-icon name="Search" style="color:#F7F5F0;width:48px;height:48px"></x-icon>', 'Derleme kanıtın haritasıdır; haritanın kalitesi de sorgulanır.')]
ok = ''
for n, ik, t in ozet:
    son = n == '4'
    bg, kn = (BLUED, BLUEDK) if son else (DK2, DKB)
    nr = L if son else '#F08A52'
    ok += (f'<div style="flex:1;display:flex;flex-direction:column;gap:20px;background:{bg};border:2px solid {kn};border-radius:16px;padding:32px 32px">'
           f'<div style="display:flex;justify-content:space-between;align-items:center"><p style="font-family:{SERIF};font-size:64px;font-weight:600;line-height:1;color:{nr}">{n}</p>{ik}</div>'
           f'<p style="font-size:32px;line-height:1.35;color:{L}">{t}</p></div>')
ic = baslik('Kapanış', 'Akılda kalacak dört şey', koyu=True) + f'''
<div style="display:flex;gap:24px">{ok}</div>'''
slayt('ozet', 20, D, ic, 'Higgins ve ark., 2024; Booth ve ark., 2012; Borenstein ve ark., 2021; Murad ve ark., 2016', koyu=True,
      bolum='Özet, ana mesaja dönüş ve teşekkür.')

# =====================================================================
# 21 · tesekkur (kapakla ayni zemin)
# =====================================================================
ic = f'''<div style="position:absolute;left:0;top:0;width:24px;height:1080px;background:{BLUE}"></div>
<p style="font-size:24px;font-weight:600;letter-spacing:3px;color:{BLUEDK}">Kapanış</p>
<div style="display:flex;flex-direction:column;gap:32px">
<h1 style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1.05;color:{L}">Teşekkürler</h1>
<p style="font-size:40px;line-height:1.4;color:{DT2}">Teşekkür ederim. Sorular ve tartışma</p>
</div>
<div style="display:flex;flex-direction:column;gap:8px">
<p style="font-size:32px;font-weight:600;color:{L}">[Adınız Soyadınız]</p>
<p style="font-size:24px;color:{DT2}">[e-posta adresiniz]</p>
</div>'''
slayt('tesekkur', 21, D, ic, sayfa=False, koyu=True,
      stil='padding:128px;display:flex;flex-direction:column;justify-content:space-between')

# =====================================================================
# 22 · tartisma (vurgu / statement slayti)
# =====================================================================
sorular = ['Aynı soruya iki meta-analiz farklı sayı verirse, uygulamada hangisine nasıl karar verirsiniz?',
           'Kendi tez konunuzda sistematik derleme mi, kapsam derlemesi mi daha dürüst bir seçim olurdu? Neden?',
           'Etik kurul gerekmiyorsa, bir derleme yazarının etik sorumlulukları nelerdir?',
           'Beden eğitiminde I² yüksek çıkıyorsa, bu bir zayıflık mı, yoksa bir bulgu mu?',
           'Antrenöre “germe sakatlığı önlemez” demeden önce hangi sorulara bakardınız?']
sq = ''.join(f'<div style="display:flex;gap:28px;align-items:center">'
             f'<p style="width:56px;font-family:{SERIF};font-size:44px;font-weight:600;line-height:1;text-align:center;color:{BLUED};background:{L};border-radius:999px;padding:6px 0">{i + 1}</p>'
             f'<p style="flex:1;font-size:32px;line-height:1.3;color:{L}">{q}</p></div>' for i, q in enumerate(sorular))
ic = f'''<div style="position:absolute;left:1552px;top:128px;width:240px;display:flex;gap:12px;align-items:center;justify-content:center;border:2px solid #D6E7EF;border-radius:999px;padding:10px 20px">
<x-icon name="Clock" style="color:{L};width:36px;height:36px"></x-icon><p style="font-size:28px;font-weight:600;color:{L}">5 dakika</p></div>
''' + f'''<div style="display:flex;flex-direction:column;gap:12px">
{eyebrow('Tartışma · 5 dakika', '#D6E7EF')}
<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.1;color:{L}">Tartışalım</h2>
</div>
<div style="display:flex;flex-direction:column;gap:28px">{sq}</div>'''
slayt('tartisma', 22, BLUED, ic, 'Thorborg ve ark., 2017; Sadigursky ve ark., 2017; Munn ve ark., 2018; Aygun ve ark., 2024; Lauersen ve ark., 2014',
      koyu=True, renk=L, bolum='5 dakikalık açık uçlu soru turu.')

# =====================================================================
# 23-25 · kaynakca
# =====================================================================
bolme = [(0, 11), (11, 22), (22, 30)]
for k, (a, b) in enumerate(bolme):
    no = 23 + k
    kl = ''.join(f'<p style="font-family:{COND};font-size:24px;line-height:1.2;color:{D}">{kunye_html(x)}</p>' for x in kunyeler[a:b])
    ic = f'''<div style="display:flex;justify-content:space-between;align-items:baseline;gap:32px">
<h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.1">Kaynakça ({k + 1}/3)</h2>
{eyebrow('Kaynakça · APA 7')}
</div>
<div style="display:flex;flex-direction:column;gap:8px">{kl}</div>'''
    slayt(f'kaynakca-{k + 1}', no, L2, ic, 'APA 7, alfabetik',
          bolum='30 kaynağın tam APA 7 künyesi.' if k == 0 else None,
          stil='padding:128px 128px 160px;display:flex;flex-direction:column;gap:24px')

# ---------------- yaz ----------------
for f in os.listdir(SLAYT):
    if f.endswith('.html'):
        os.remove(os.path.join(SLAYT, f))
for sid, h in SAYFALAR:
    with open(os.path.join(SLAYT, sid + '.html'), 'w', encoding='utf-8') as fh:
        fh.write(h)

order = [sid for sid, _ in SAYFALAR]
sections = {}
for i, sid in enumerate([s for s in order if s in BOLUMLER]):
    sections[f's{i + 1}'] = {'description': BOLUMLER[sid], 'start': sid}
deck = {
    'v': 4,
    'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},
    'lists': 'css',
    'title': 'Meta-analiz, Sistematik Derleme ve Derleme',
    'order': order,
    'sections': sections,
    'faces': {
        'source-serif-4': {'family': 'Source Serif 4', 'href': 'https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap'},
        'ibm-plex-sans': {'family': 'IBM Plex Sans', 'href': 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap'},
        'ibm-plex-sans-condensed': {'family': 'IBM Plex Sans Condensed', 'href': 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@400;600&display=swap'},
    },
    'designSystems': [],
}
with open(os.path.join(PROJE, 'deck.json'), 'w', encoding='utf-8') as fh:
    json.dump(deck, fh, ensure_ascii=False)
print(len(order), 'slayt yazildi')
