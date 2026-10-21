#!/usr/bin/env python3
"""odev.md denetimi: metin içi atıf <-> kaynakça eşleşmesi, alfabetik sıra, em dash, kaynak sayıları."""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
odev = (ROOT / "odev.md").read_text(encoding="utf-8")
hata = 0

# Em dash ve en dash denetimi (bütün çıktı dosyaları)
for f in ["odev.md", "okuma-listesi.md", "SONUC.md", "word_uret.py", "denetle.py"]:
    p = ROOT / f
    if p.exists():
        n = p.read_text(encoding="utf-8").count(chr(0x2014))
        print(f"em dash {f}: {n}")
        if n:
            hata += 1

govde = odev.split("## Kaynakça")[0]
kaynakca = odev.split("## Kaynakça")[1].split("## Ek")[0]
refs = [l.strip() for l in kaynakca.strip().splitlines() if l.strip()]

YIL = r"(?:\d{4}(?:/\d{4})?[a-z]?|t\.y\.(?:-[a-z])?)"

def ref_key(r):
    m = re.match(r"^(.*?)\.? \((" + YIL + r")(?:, [^)]*)?\)\.", r)
    if not m:
        m = re.match(r"^(.*?) \(Ed\.\)\. \((" + YIL + r")\)\.", r)
    if not m:
        return None
    yazar, yil = m.group(1) + ".", m.group(2)
    yazar = re.sub(r"\.? \(Ed\.\)\.?$", ".", yazar)
    kis = re.search(r"\[([^\]]+)\]$", yazar)
    yazar = yazar.rstrip(".") if not re.search(r", (?:[A-ZÇĞİÖŞÜ]\.[ -]?)+$", yazar) else yazar
    kis = re.search(r"\[([^\]]+)\]$", yazar)
    if kis:
        return kis.group(1), yil
    soyadlar = re.findall(r"([A-ZÇĞİÖŞÜa-zçğıöşüßäöü\-]+), (?:[A-ZÇĞİÖŞÜ]\.[ -]?)+", yazar)
    if soyadlar:
        if len(soyadlar) == 1:
            return soyadlar[0], yil
        if len(soyadlar) == 2:
            return f"{soyadlar[0]} ve {soyadlar[1]}", yil
        return f"{soyadlar[0]} vd.", yil
    return yazar, yil

anahtarlar = {}
for r in refs:
    k = ref_key(r)
    if k is None:
        print("COZULEMEDI:", r[:80]); hata += 1; continue
    if k in anahtarlar:
        print("CIFT ANAHTAR:", k); hata += 1
    anahtarlar[k] = r

# Metin içi atıflar
atiflar = set()
def ekle(yazar, yillar):
    yazar = yazar.strip()
    kis = re.search(r"\[([^\]]+)\]$", yazar)
    if kis:
        yazar = kis.group(1)
    for y in re.findall(YIL, yillar):
        atiflar.add((yazar, y))

for par in re.findall(r"\(([^()]*?\d{4}[^()]*?|[^()]*?t\.y\.[^()]*?)\)", govde):
    for parca in par.split(";"):
        m = re.match(r"^\s*(.+?), ((?:" + YIL + r")(?:, " + YIL + r")*)\s*$", parca)
        if m and not re.match(r"^\d", m.group(1)):
            ekle(m.group(1), m.group(2))
# Anlatı biçimli atıflar: Yazar (yıl). Çok kelimeli yazarlar için kaynakça anahtarlarıyla eşleştir.
for m in re.finditer(r"([A-ZÇĞİÖŞÜ][\wçğıöşüÇĞİÖŞÜäöüß\-/]+(?: ve [A-ZÇĞİÖŞÜ][\wçğıöşüäöüß\-]+| vd\.)?)(?:'[a-zıüöç]+)? \(((?:" + YIL + r")(?:, " + YIL + r")*)\)", govde):
    ad, yillar = m.group(1), m.group(2)
    onceki = govde[max(0, m.start()-80):m.end()]
    for y in re.findall(YIL, yillar):
        tam = [k for k in anahtarlar if k[1] == y and (k[0] == ad or (k[0].endswith(" " + ad) or k[0].endswith("/" + ad)) and k[0] + " (" in onceki)]
        if tam:
            atiflar.add(tam[0])
        else:
            atiflar.add((ad, y))
ref_set = set(anahtarlar)
eksik_ref = sorted(a for a in atiflar if a not in ref_set)
kullanilmayan = sorted(a for a in ref_set if a not in atiflar)
# Tablo kaynak satırları "Kaynak: X (yıl)" anlatı regex'iyle yakalanır; kalanlar raporlanır
print("Metinde olup kaynakçada olmayan:", eksik_ref)
print("Kaynakçada olup metinde olmayan:", kullanilmayan)
hata += len(eksik_ref) + len(kullanilmayan)

# Alfabetik sıra (Türkçe harf sırası)
ALF = "aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPqQrRsSşŞtTuUüÜvVwWxXyYzZ"
def sirala(s):
    s = s.rstrip(".").replace("ä", "a").replace("ß", "ss")
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = re.sub(r"\bve\b", " ", s)
    s = re.sub(r"[^\w ]", "", s)
    s = re.sub(r" +", " ", s)
    return [-1 if not ch.isalnum() else (ALF.lower().find(ch) if ch in ALF.lower() else 200 + ord(ch)) for ch in s]
def tr_lower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()
sira_hata = 0
for a, b in zip(refs, refs[1:]):
    ka = tr_lower(re.split(r" \(", a)[0]); kb = tr_lower(re.split(r" \(", b)[0])
    if ka != kb and sirala(ka) > sirala(kb):
        print("SIRA:", a[:50], "|", b[:50]); sira_hata += 1
hata += sira_hata

tr_harf = re.compile(r"[çğışöüÇĞİŞÖÜ]")
turkce = [r for r in refs if tr_harf.search(r.split("http")[0]) and not re.search(r"\b(und|der|die|für|Ländern|über)\b", r)]
print(f"Kaynak sayısı: {len(refs)}  Türkçe (yaklaşık): {len(turkce)}")
print(f"Metin içi farklı atıf: {len(atiflar)}")
govde_kelime = len(" ".join(l for l in govde.splitlines() if not l.startswith("|")).split())
print(f"Kelime (gövde, tablolar hariç): {govde_kelime}  tablolar dahil: {len(govde.split())}")
print("SONUC:", "TEMIZ" if hata == 0 else f"{hata} SORUN")
sys.exit(1 if hata else 0)
