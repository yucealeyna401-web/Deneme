# -*- coding: utf-8 -*-
"""m7 · sunum.pptx üretici.

Girdi: isler/m6-denetim/slaytlar-son.md (değiştirilmez, yalnız okunur).
Çıktı: isler/m7-slaytlar/sunum.pptx ve isler/m7-slaytlar/onizleme/ altındaki grafik PNG'leri.
Bütün slayt metinleri, tablo hücreleri, kutu metinleri ve notlar girdi dosyasından ayrıştırılır.
"""
import os
import re

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn
from lxml import etree

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.abspath(os.path.join(BURASI, "..", ".."))
GIRDI = os.path.join(KOK, "isler", "m6-denetim", "slaytlar-son.md")
CIKTI = os.path.join(BURASI, "sunum.pptx")
GORSEL = os.path.join(BURASI, "onizleme", "grafik")

LACI = RGBColor(0x1F, 0x2A, 0x44)
MAVI = RGBColor(0x2B, 0x57, 0x97)
ACIKMAVI = RGBColor(0xE8, 0xEE, 0xF7)
GRI = RGBColor(0xBF, 0xC5, 0xCE)
ACIKGRI = RGBColor(0xF3, 0xF4, 0xF6)
KOYUGRI = RGBColor(0x5A, 0x60, 0x6B)
METIN = RGBColor(0x22, 0x26, 0x2E)
BEYAZ = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

TOPLAM = 15


# --------------------------------------------------------------------------- ayrıştırma
def oku():
    with open(GIRDI, encoding="utf-8") as f:
        return f.read()


def slayt_bolumleri(md):
    parcalar = re.split(r"^## Slayt (\d+) · .*$", md, flags=re.M)
    bolum = {}
    for i in range(1, len(parcalar), 2):
        no = int(parcalar[i])
        govde = parcalar[i + 1]
        govde = re.split(r"^---\s*$", govde, flags=re.M)[0]
        bolum[no] = govde
    return bolum


def alan(govde, ad):
    m = re.search(r"^\*\*" + re.escape(ad) + r":\*\*\s*(.*)$", govde, flags=re.M)
    return m.group(1).strip() if m else ""


def blok(govde, bas, son_desen=r"^\*\*[^*]+(\*\*|:\*\*)"):
    """bas etiketinden sonraki satırları bir sonraki ** etiketine kadar döndürür."""
    m = re.search(r"^\*\*" + re.escape(bas) + r"[^\n]*$", govde, flags=re.M)
    if not m:
        return ""
    kalan = govde[m.end():]
    s = re.search(son_desen, kalan, flags=re.M)
    son = m.end() + s.start() if s else len(govde)
    return govde[m.start():son]  # başlık satırının kalanı dahil


def maddeler(metin):
    return [l[2:].strip() for l in metin.splitlines() if l.startswith("- ")]


def tablolar(metin):
    sonuc, cur = [], []
    for l in metin.splitlines():
        if l.startswith("|"):
            cur.append(l)
        else:
            if cur:
                sonuc.append(cur)
                cur = []
    if cur:
        sonuc.append(cur)
    out = []
    for t in sonuc:
        satirlar = []
        for l in t:
            hucre = [h.strip() for h in l.strip().strip("|").split("|")]
            if all(re.fullmatch(r"-+", h) for h in hucre if h):
                continue
            satirlar.append(hucre)
        out.append(satirlar)
    return out


def tirnaklar(metin):
    return re.findall(r"\"([^\"]+)\"", metin)


def notlar(govde):
    i = govde.find("**Sunucu notu**")
    metin = govde[i + len("**Sunucu notu**"):].strip()
    satirlar = []
    for l in metin.splitlines():
        l = l.rstrip()
        l = re.sub(r"^\*([^*]+?):\*\s*", lambda m: m.group(1) + ": ", l)
        l = re.sub(r"^\*\*([^*]+?):\*\*\s*", lambda m: m.group(1) + ": ", l)
        l = l.replace("`", "").rstrip()
        satirlar.append(l)
    metin = "\n".join(satirlar)
    metin = re.sub(r"\n{3,}", "\n\n", metin).strip()
    return metin


def kaynak_satiri(govde):
    k = alan(govde, "Metin içi kaynaklar")
    # yalnız slaytta görünen atıflar alt satıra; "yalnız notta" vb. kısım notta kalır
    k = re.split(r"\s·\s(?:yalnız notta|ikincil atıf|cevaplarda|notta)", k)[0].strip()
    if k.startswith("yok"):
        return ""
    if k.startswith("Alt bilgi satırı:"):
        return tirnaklar(k)[0]
    return "Kaynaklar: " + k


# --------------------------------------------------------------------------- çizim yardımcıları
def runlar(p, metin, boyut, renk=METIN, kalin=False, italik_izin=False):
    """*italik* işaretini koruyarak paragrafa run ekler."""
    parca = re.split(r"(\*[^*]+\*)", metin) if italik_izin else [metin]
    for s in parca:
        if not s:
            continue
        it = italik_izin and s.startswith("*") and s.endswith("*") and len(s) > 2
        r = p.add_run()
        r.text = s[1:-1] if it else s
        f = r.font
        f.name = FONT
        f.size = Pt(boyut)
        f.bold = kalin
        f.italic = it
        f.color.rgb = renk
    return p


def metin_kutusu(sl, x, y, w, h, paragraflar, boyut=18, renk=METIN, kalin=False,
                 hiza=PP_ALIGN.LEFT, dikey=MSO_ANCHOR.TOP, bosluk=0, ic=0.05, italik=False):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = dikey
    for kenar in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, kenar, Inches(ic))
    if isinstance(paragraflar, str):
        paragraflar = [paragraflar]
    for i, par in enumerate(paragraflar):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = hiza
        if bosluk:
            p.space_after = Pt(bosluk)
        if isinstance(par, tuple):
            m, ozel = par
            runlar(p, m, ozel.get("boyut", boyut), ozel.get("renk", renk), ozel.get("kalin", kalin),
                   italik)
        else:
            runlar(p, par, boyut, renk, kalin, italik)
    return tb


def madde_isareti(p, girinti=0.28, isaret="•", renk="2B5797"):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Inches(girinti)))
    pPr.set("indent", str(-Inches(girinti)))
    for eski in pPr.findall(qn("a:buChar")):
        pPr.remove(eski)
    buClr = etree.SubElement(pPr, qn("a:buClr"))
    srgb = etree.SubElement(buClr, qn("a:srgbClr"))
    srgb.set("val", renk)
    buFont = etree.SubElement(pPr, qn("a:buFont"))
    buFont.set("typeface", "Arial")
    bu = etree.SubElement(pPr, qn("a:buChar"))
    bu.set("char", isaret)


def asili_girinti(p, girinti=0.3):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(Inches(girinti)))
    pPr.set("indent", str(-Inches(girinti)))


def madde_kutusu(sl, x, y, w, h, liste, boyut=18, renk=METIN, bosluk=8):
    tb = metin_kutusu(sl, x, y, w, h, liste, boyut=boyut, renk=renk, bosluk=bosluk)
    for p in tb.text_frame.paragraphs:
        madde_isareti(p)
    return tb


def kutu(sl, x, y, w, h, paragraflar, boyut=14, dolgu=ACIKMAVI, cizgi=MAVI, renk=METIN,
         kalin=False, sekil=MSO_SHAPE.RECTANGLE, kesik=False, hiza=PP_ALIGN.CENTER,
         dikey=MSO_ANCHOR.MIDDLE, kalinlik=1.0, ic=0.06):
    s = sl.shapes.add_shape(sekil, Inches(x), Inches(y), Inches(w), Inches(h))
    if sekil == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.12
    if dolgu is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = dolgu
    if cizgi is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = cizgi
        s.line.width = Pt(kalinlik)
        if kesik:
            ln = s.line._get_or_add_ln()
            d = etree.SubElement(ln, qn("a:prstDash"))
            d.set("val", "dash")
    s.shadow.inherit = False
    tf = s.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = dikey
    for kenar in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, kenar, Inches(ic))
    if isinstance(paragraflar, str):
        paragraflar = [paragraflar]
    for i, par in enumerate(paragraflar):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = hiza
        if isinstance(par, tuple):
            m, ozel = par
            runlar(p, m, ozel.get("boyut", boyut), ozel.get("renk", renk), ozel.get("kalin", kalin))
        else:
            runlar(p, par, boyut, renk, kalin)
    return s


def cizgi(sl, x1, y1, x2, y2, renk=GRI, kalinlik=1.0, ok=False, kesik=False):
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = renk
    c.line.width = Pt(kalinlik)
    ln = c.line._get_or_add_ln()
    if kesik:
        d = etree.SubElement(ln, qn("a:prstDash"))
        d.set("val", "dash")
    if ok:
        t = etree.SubElement(ln, qn("a:tailEnd"))
        t.set("type", "triangle")
        t.set("w", "med")
        t.set("len", "med")
    return c


def tablo(sl, x, y, w, h, satirlar, gen, boyut=12, bas_boyut=None, ilk_sutun_kalin=True,
          bas_dolgu=LACI, satir_yuk=None, italik=False):
    r, c = len(satirlar), len(satirlar[0])
    gs = sl.shapes.add_table(r, c, Inches(x), Inches(y), Inches(w), Inches(h))
    t = gs.table
    tblPr = t._tbl.tblPr
    # temanın hazır stilini kapat (düz görünüm)
    for a in ("bandRow", "firstRow"):
        tblPr.set(a, "0")
    for j, g in enumerate(gen):
        t.columns[j].width = Inches(g)
    for i in range(r):
        if satir_yuk:
            t.rows[i].height = Inches(satir_yuk[i] if isinstance(satir_yuk, list) else satir_yuk)
        for j in range(c):
            hc = t.cell(i, j)
            hc.margin_left = hc.margin_right = Inches(0.06)
            hc.margin_top = hc.margin_bottom = Inches(0.03)
            hc.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = hc.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            metin = satirlar[i][j]
            if i == 0:
                runlar(p, metin, bas_boyut or boyut, BEYAZ, True)
                hc.fill.solid()
                hc.fill.fore_color.rgb = bas_dolgu
            else:
                runlar(p, metin, boyut, LACI if (j == 0 and ilk_sutun_kalin) else METIN,
                       j == 0 and ilk_sutun_kalin, italik)
                hc.fill.solid()
                hc.fill.fore_color.rgb = BEYAZ if i % 2 else ACIKGRI
            kenarlik(hc)
    return gs


def kenarlik(hc, renk="BFC5CE"):
    tcPr = hc._tc.get_or_add_tcPr()
    for ad in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        ln = etree.SubElement(tcPr, qn(ad))
        ln.set("w", str(Pt(0.75)))
        sf = etree.SubElement(ln, qn("a:solidFill"))
        cl = etree.SubElement(sf, qn("a:srgbClr"))
        cl.set("val", renk)
    # sıra: OOXML ln* elemanları solidFill'den önce gelmeli
    fill = tcPr.find(qn("a:solidFill"))
    if fill is not None:
        tcPr.remove(fill)
        tcPr.append(fill)


# --------------------------------------------------------------------------- slayt çerçevesi
def cerceve(prs, no, baslik, kaynak, notu):
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    bant = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    bant.fill.solid(); bant.fill.fore_color.rgb = LACI; bant.line.fill.background()
    bant.shadow.inherit = False
    if baslik:
        metin_kutusu(sl, 0.5, 0.28, 12.33, 0.8, baslik, boyut=28 if len(baslik) <= 72 else 26, renk=LACI, kalin=True,
                     dikey=MSO_ANCHOR.MIDDLE)
        cizgi(sl, 0.5, 1.13, 12.83, 1.13, renk=GRI, kalinlik=1.0)
    cizgi(sl, 0.5, 6.98, 12.83, 6.98, renk=GRI, kalinlik=0.75)
    if kaynak:
        metin_kutusu(sl, 0.5, 7.0, 11.6, 0.4, kaynak, boyut=10, renk=KOYUGRI,
                     dikey=MSO_ANCHOR.MIDDLE)
    metin_kutusu(sl, 12.13, 7.0, 0.7, 0.4, f"{no} / {TOPLAM}", boyut=10, renk=KOYUGRI,
                 hiza=PP_ALIGN.RIGHT, dikey=MSO_ANCHOR.MIDDLE)
    sl.notes_slide.notes_text_frame.text = notu
    return sl


# --------------------------------------------------------------------------- slaytlar
def iskelet(sl, govde):
    liste = maddeler(blok(govde, "Slayt metni"))
    if liste:
        madde_kutusu(sl, 0.6, 1.35, 12.1, 5.4, liste, boyut=18)


def gorsel_blok(govde):
    return blok(govde, "Görsel/tablo önerisi")


def satir_bul(metin, bas):
    for l in metin.splitlines():
        if l.strip().startswith(bas):
            return l.strip()
    return ""


def dikey_metin(shape):
    shape.text_frame._txBody.bodyPr.set("vert", "vert270")


# ---- Slayt 1 · Kapak
def s1(sl, g):
    baslik = alan(g, "Başlık")
    ana, alt = baslik.split(": ", 1)
    liste = maddeler(blok(g, "Slayt metni"))
    metin_kutusu(sl, 0.9, 1.75, 11.5, 0.9, ana, boyut=32, renk=LACI, kalin=True,
                 dikey=MSO_ANCHOR.BOTTOM)
    metin_kutusu(sl, 0.9, 2.65, 11.5, 0.7, alt, boyut=26, renk=MAVI, dikey=MSO_ANCHOR.TOP)
    cizgi(sl, 0.95, 3.55, 4.2, 3.55, renk=MAVI, kalinlik=2.5)
    metin_kutusu(sl, 0.9, 3.85, 11.5, 2.0, liste[1:], boyut=18, renk=KOYUGRI, bosluk=10)


# ---- Slayt 2 · Amaç ve yelpaze
def s2(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    madde_kutusu(sl, 0.6, 1.35, 12.1, 1.45, liste[:3], boyut=18, bosluk=4)
    metin_kutusu(sl, 0.6, 2.85, 12.1, 0.45, liste[3], boyut=16, renk=MAVI, kalin=True)
    q = tirnaklar(gorsel_blok(g))
    k1, k2, k3, okm = q[0].split(" · "), q[1].split(" · "), q[2].split(" · "), q[3]

    def par(parca, b=16):
        return [(parca[0], {"kalin": True, "renk": LACI, "boyut": b + 2})] + parca[1:]

    kutu(sl, 0.6, 3.45, 3.7, 2.45, par(k1), boyut=16, dolgu=ACIKMAVI, cizgi=MAVI,
         sekil=MSO_SHAPE.ROUNDED_RECTANGLE, kalinlik=1.25)
    kutu(sl, 4.6, 3.45, 8.23, 2.45, "", dolgu=BEYAZ, cizgi=LACI,
         sekil=MSO_SHAPE.ROUNDED_RECTANGLE, kalinlik=1.75)
    metin_kutusu(sl, 4.8, 3.6, 4.2, 2.15, par(k2), boyut=16, dikey=MSO_ANCHOR.MIDDLE)
    kutu(sl, 9.2, 3.75, 3.4, 1.85, par(k3, 15), boyut=15, dolgu=ACIKMAVI, cizgi=MAVI,
         sekil=MSO_SHAPE.ROUNDED_RECTANGLE, kesik=True, kalinlik=1.5)
    cizgi(sl, 0.6, 6.2, 12.8, 6.2, renk=LACI, kalinlik=2.25, ok=True)
    metin_kutusu(sl, 0.6, 6.27, 12.2, 0.4, okm, boyut=14, renk=MAVI, hiza=PP_ALIGN.CENTER)


# ---- Slayt 3 · Anlatı derlemesi
def s3(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    madde_kutusu(sl, 0.6, 1.4, 5.6, 5.4, liste, boyut=20, bosluk=10)
    t = tablolar(gorsel_blok(g))[0]
    tablo(sl, 6.45, 1.5, 6.38, 3.9, t, [1.8, 2.25, 2.33], boyut=13.5, bas_boyut=14,
          satir_yuk=[0.5, 1.1, 1.2, 1.1])


# ---- Slayt 4 · Sistematik derleme ve PICOS
def s4(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    madde_kutusu(sl, 0.6, 1.4, 5.3, 5.4, liste, boyut=20, bosluk=10)
    gb = gorsel_blok(g)
    etiket = tirnaklar(satir_bul(gb, "**Görsel") or gb)[0]
    kutu(sl, 6.2, 1.45, 3.1, 0.38, etiket, boyut=12, dolgu=ACIKMAVI, cizgi=MAVI, renk=MAVI,
         kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
    t = tablolar(gb)[0]
    gs = tablo(sl, 6.2, 1.95, 6.63, 4.3, t, [0.65, 2.0, 3.98], boyut=13, bas_boyut=13,
               satir_yuk=[0.45] + [0.75] * 5)
    tb = gs.table
    for i in range(1, len(t)):
        hc = tb.cell(i, 0)
        hc.fill.solid(); hc.fill.fore_color.rgb = MAVI
        p = hc.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = Pt(22); r.font.color.rgb = BEYAZ; r.font.bold = True


# ---- Slayt 5 · Süreç ve PRISMA 2020 akış şeması
PRISMA_EN = {
    "Başlık": ("Identification of studies via databases and registers", ""),
    1: ("Records identified from: Databases · Registers", "Records removed before screening"),
    2: ("Records screened", "Records excluded"),
    3: ("Reports sought for retrieval", "Reports not retrieved"),
    4: ("Reports assessed for eligibility", "Reports excluded"),
    5: ("Studies included in review · Reports of included studies", ""),
}


def prisma_satirlari(metin):
    parca = metin.split(" · ")
    if ":" in parca[0]:
        bas, ilk = parca[0].split(": ", 1)
        return [bas + ":"] + [ilk] + parca[1:]
    return parca


def prisma_kutu(sl, x, y, w, h, metin, en):
    paragraf = [(s, {"boyut": 10.5, "kalin": i == 0 and s.endswith(":"), "renk": METIN})
                for i, s in enumerate(prisma_satirlari(metin))]
    # neden satırlarını tek satıra topla (yer kazanmak için, metin aynı)
    if metin.startswith("Dışlanan raporlar:"):
        bas, kalan = metin.split(": ", 1)
        paragraf = [(bas + ":", {"boyut": 10.5, "kalin": True}), (kalan, {"boyut": 10.5})]
    if en:
        paragraf.append((en, {"boyut": 8.5, "renk": KOYUGRI}))
    return kutu(sl, x, y, w, h, paragraf, dolgu=BEYAZ, cizgi=MAVI, kalinlik=1.0, ic=0.05)


def s5(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    gb = gorsel_blok(g)
    q = tirnaklar(gb)
    adim = q[:8]
    w = (12.33 - 7 * 0.17) / 8
    for i, a in enumerate(adim):
        x = 0.5 + i * (w + 0.17)
        kutu(sl, x, 1.27, w, 0.52, a, boyut=12, dolgu=LACI if i == 7 else ACIKMAVI,
             cizgi=MAVI, renk=BEYAZ if i == 7 else LACI, kalin=True,
             sekil=MSO_SHAPE.ROUNDED_RECTANGLE, ic=0.03)
        if i < 7:
            cizgi(sl, x + w + 0.01, 1.53, x + w + 0.16, 1.53, renk=MAVI, kalinlik=1.5, ok=True)

    t = tablolar(gb)[0][1:]
    bas = t[0][1]
    satirlar = t[1:]
    X_BANT, W_BANT, X_ANA, W_ANA, X_YAN, W_YAN = 0.5, 0.42, 1.02, 3.5, 5.0, 3.62
    y = 1.98
    kutu(sl, X_ANA, y, X_YAN + W_YAN - X_ANA, 0.36,
         [(bas, {"boyut": 11.5, "kalin": True, "renk": BEYAZ}),
          (PRISMA_EN["Başlık"][0], {"boyut": 8.5, "renk": RGBColor(0xDD, 0xE4, 0xF0)})],
         dolgu=LACI, cizgi=None, ic=0.02)
    y += 0.36 + 0.13
    yuk = [0.92, 0.5, 0.5, 0.64, 0.74]
    konum = []
    for i, (bant, ana, yan) in enumerate(satirlar):
        h = yuk[i]
        en_ana, en_yan = PRISMA_EN[i + 1]
        prisma_kutu(sl, X_ANA, y, W_ANA, h, ana, en_ana)
        if yan:
            prisma_kutu(sl, X_YAN, y, W_YAN, h, yan, en_yan)
            cizgi(sl, X_ANA + W_ANA, y + h / 2, X_YAN, y + h / 2, renk=MAVI, kalinlik=1.25, ok=True)
        konum.append((bant, y, h))
        y += h + 0.13
    for i in range(len(konum) - 1):
        _, y0, h0 = konum[i]
        cizgi(sl, X_ANA + W_ANA / 2, y0 + h0, X_ANA + W_ANA / 2, konum[i + 1][1],
              renk=MAVI, kalinlik=1.25, ok=True)
    # bantlar
    bant_en = {"Tanımlama": "Identification", "Tarama": "Screening", "Dahil etme": "Included"}
    gruplar = []
    for bant, y0, h0 in konum:
        if gruplar and gruplar[-1][0] == bant:
            gruplar[-1][2] = y0 + h0
        else:
            gruplar.append([bant, y0, y0 + h0])
    for bant, y0, y1 in gruplar:
        s = kutu(sl, X_BANT, y0, W_BANT, y1 - y0,
                 [(bant, {"boyut": 10.5, "kalin": True, "renk": BEYAZ}),
                  (bant_en[bant], {"boyut": 8.5, "renk": RGBColor(0xDD, 0xE4, 0xF0)})],
                 dolgu=MAVI, cizgi=None, ic=0.01)
        dikey_metin(s)
    alt_not = satir_bul(gb, "Şemanın altında küçük not:")
    alt_not = tirnaklar(alt_not)[0]
    metin_kutusu(sl, 0.5, y - 0.05, 8.2, 0.5,
                 ["Page ve ark. (2021) akış şemasından uyarlanmıştır · " + alt_not],
                 boyut=10, renk=KOYUGRI)
    # sağ panel
    madde_kutusu(sl, 9.0, 2.0, 3.83, 2.6, liste[1:], boyut=17, bosluk=8)
    alinti = tirnaklar(satir_bul(gb, "Şemanın altında küçük not:"))[1]
    kutu(sl, 9.0, 4.75, 3.83, 1.6,
         [("“" + alinti + "”", {"boyut": 12, "renk": LACI}),
          ("(Page ve ark., 2021)", {"boyut": 11, "renk": KOYUGRI})],
         dolgu=ACIKGRI, cizgi=None, hiza=PP_ALIGN.LEFT, ic=0.12)


# ---- Slayt 6 · Arama, seçim, yanlılık riski
def s6(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    gb = gorsel_blok(g)
    sut = [satir_bul(gb, "- Sütun %d" % i) for i in (1, 2, 3)]
    basliklar = [tirnaklar(s)[0] for s in sut]
    xs = [(0.5, 3.45), (4.15, 5.05), (9.42, 3.41)]
    for (x, w), b in zip(xs, basliklar):
        kutu(sl, x, 1.3, w, 0.42, b, boyut=16, dolgu=LACI, cizgi=None, renk=BEYAZ, kalin=True)
    # sütun 1: tabanlar
    s1m = sut[0].split("etiketi:", 1)[1].split(". Altında")[0]
    tabanlar = re.findall(r"([A-Za-z][A-Za-z ]*?) \"([^\"]+)\"", s1m)
    par = []
    for ad, et in tabanlar:
        par.append((ad, {"boyut": 16, "kalin": True, "renk": LACI}))
        par.append((et, {"boyut": 13, "renk": KOYUGRI}))
    gri = tirnaklar(satir_bul(gb, "Altında"))[0] if satir_bul(gb, "Altında") else \
        re.search(r"Altında \"([^\"]+)\"", sut[0]).group(1)
    par.append((gri, {"boyut": 14, "renk": MAVI, "kalin": True}))
    metin_kutusu(sl, 0.55, 1.85, 3.4, 4.3, par, boyut=14)
    # sütun 2: dize
    metin_kutusu(sl, 4.15, 1.8, 5.05, 0.7, liste[1], boyut=16)
    etiket = tirnaklar(sut[1])[1]
    kutu(sl, 4.15, 2.55, 3.2, 0.34, etiket, boyut=11.5, dolgu=ACIKMAVI, cizgi=MAVI, renk=MAVI,
         kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE, ic=0.02)
    kod = re.search(r"```text\n(.*?)```", gb, flags=re.S).group(1).strip().splitlines()
    etk = re.search(r"küçük etiketler: (.*)\.", gb).group(1).split(" · ")
    kutu(sl, 4.15, 2.98, 5.05, 2.62, "", dolgu=ACIKGRI, cizgi=GRI)
    yy = 3.06
    for satir, e in zip(kod, etk):
        kutu(sl, 4.22, yy + 0.08, 0.4, 0.4, e.split(" ")[0], boyut=14, dolgu=MAVI, cizgi=None,
             renk=BEYAZ, kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE, ic=0.0)
        metin_kutusu(sl, 4.68, yy, 4.48, 0.62, satir, boyut=12, renk=LACI,
                     dikey=MSO_ANCHOR.MIDDLE, ic=0.02)
        yy += 0.63
    metin_kutusu(sl, 4.15, 5.62, 5.05, 0.35, "  ·  ".join(etk), boyut=12, renk=KOYUGRI,
                 hiza=PP_ALIGN.CENTER)
    # sütun 3
    metin_kutusu(sl, 9.42, 1.8, 3.41, 0.5, liste[4], boyut=16)
    t = tablolar(gb)[0]
    tablo(sl, 9.42, 2.4, 3.41, 2.4, t, [1.6, 1.81], boyut=12, bas_boyut=12.5)
    # alt şerit
    kutu(sl, 0.5, 6.15, 12.33, 0.58, "     ·     ".join(liste[2:4]), boyut=16,
         dolgu=ACIKMAVI, cizgi=None, renk=LACI, kalin=True)


# ---- Slayt 7 · Meta-analiz ve SR ilişkisi
def s7(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    madde_kutusu(sl, 0.6, 1.4, 5.0, 5.3, liste, boyut=18, bosluk=10)
    q = tirnaklar(gorsel_blok(g))
    dis, ic_, swim, karar = q[0], q[1], q[2], q[3]
    kutu(sl, 5.95, 1.32, 6.88, 4.45, "", dolgu=ACIKMAVI, cizgi=LACI, sekil=MSO_SHAPE.OVAL,
         kalinlik=1.75)
    d1, d2 = dis.split(" (", 1)
    metin_kutusu(sl, 7.0, 1.55, 4.8, 1.0,
                 [(d1, {"boyut": 18, "kalin": True, "renk": LACI}),
                  ("(" + d2, {"boyut": 13, "renk": KOYUGRI})], hiza=PP_ALIGN.CENTER)
    i1, i2 = ic_.split(" (", 1)
    kutu(sl, 6.85, 2.75, 2.65, 2.65,
         [(i1, {"boyut": 18, "kalin": True, "renk": BEYAZ}), ("(" + i2, {"boyut": 13, "renk": BEYAZ})],
         dolgu=MAVI, cizgi=None, sekil=MSO_SHAPE.OVAL)
    kutu(sl, 9.75, 3.45, 2.35, 1.25, swim, boyut=15, dolgu=BEYAZ, cizgi=MAVI, renk=LACI,
         kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE, kesik=True, kalinlik=1.5)
    kutu(sl, 5.95, 5.95, 6.88, 0.8, karar, boyut=13, dolgu=ACIKGRI, cizgi=None, renk=LACI)


# ---- Slayt 8 · İstatistiksel kavramlar
def s8(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    madde_kutusu(sl, 0.6, 1.4, 4.25, 5.4, liste, boyut=17, bosluk=9)
    gb = gorsel_blok(g)
    t = tablolar(gb)[0]
    tablo(sl, 5.05, 1.38, 7.78, 4.85, t, [2.25, 3.05, 2.48], boyut=12, bas_boyut=13)
    formul = re.search(r"formül satırı: (.*?)\.\s*$", gb, flags=re.M).group(1)
    kutu(sl, 5.05, 6.33, 7.78, 0.5, formul, boyut=16, dolgu=ACIKMAVI, cizgi=None, renk=LACI,
         kalin=True)


# ---- Slayt 9 · Forest ve funnel plot (matplotlib)
def sayi(s):
    return float(s.replace(",", ".").replace("−", "-"))


def virgul(x, _=None):
    s = ("%.1f" % x).replace(".", ",")
    return "0" if s in ("0,0", "-0,0") else s


def grafikler(g):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from matplotlib.ticker import FuncFormatter
    from matplotlib.patches import Polygon
    aile = "Carlito" if any("Carlito" in f.name for f in font_manager.fontManager.ttflist) else "DejaVu Sans"
    plt.rcParams.update({"font.family": aile, "font.size": 11, "axes.edgecolor": "#5A606B",
                         "axes.linewidth": 0.8})
    L, M, GR = "#1F2A44", "#2B5797", "#5A606B"
    gb = gorsel_blok(g)
    tb = tablolar(gb)
    forest, funnel = tb[0], tb[1]
    etiket = "Eğitim amaçlı kurgu veri"
    alt_f = re.search(r"Alt bilgi satırı: (.*?)\. Dikey çizgi", gb).group(1)
    alt_u = re.search(r"Alt bilgi: (.*?)\.\s*$", gb, flags=re.M).group(1)

    # --- forest
    cal = [r for r in forest[1:] if r[0].startswith("Çalışma")]
    ozet = [r for r in forest[1:] if r[0].startswith("Özet")][0]
    ta = [r for r in forest[1:] if "tahmin aralığı" in r[0]][0]
    fig = plt.figure(figsize=(6.3, 4.45), dpi=200)
    ax = fig.add_axes([0.30, 0.25, 0.40, 0.58])
    n = len(cal)
    ys = list(range(n + 2, 2, -1))
    for y, r in zip(ys, cal):
        gv = sayi(r[2]); lo, hi = [sayi(v) for v in r[3].split(" ile ")]; w = sayi(r[4])
        ax.plot([lo, hi], [y, y], color=L, lw=1.2)
        ax.scatter([gv], [y], marker="s", s=w * 9, color=M, zorder=3)
        tr = ax.get_yaxis_transform()
        ax.text(-0.72, y, r[0], transform=tr, va="center",
                ha="left", fontsize=10.5, color=L)
        ax.text(-0.12, y, r[1], transform=tr, va="center", ha="right", fontsize=10.5, color=GR)
        ax.text(1.04, y, "%s [%s; %s]" % (r[2], *r[3].split(" ile ")),
                transform=tr, va="center", ha="left", fontsize=10.5, color=L)
        ax.text(1.70, y, r[4], transform=tr, va="center", ha="right", fontsize=10.5, color=GR)
    gv = sayi(ozet[2]); lo, hi = [sayi(v) for v in ozet[3].split(" ile ")]
    yo = 1.6
    ax.add_patch(Polygon([[lo, yo], [gv, yo + 0.38], [hi, yo], [gv, yo - 0.38]], closed=True,
                         color=L, zorder=3))
    plo, phi = [sayi(v) for v in ta[3].split(" ile ")]
    yp = 0.75
    ax.plot([plo, phi], [yp, yp], color=M, lw=3.2, solid_capstyle="butt")
    tr = ax.get_yaxis_transform()
    ax.text(-0.72, yo, "Özet (RE, DL)", transform=tr, va="center", ha="left", fontsize=10.5,
            color=L, weight="bold")
    ax.text(-0.12, yo, ozet[1], transform=tr, va="center", ha="right", fontsize=10.5, color=GR)
    ax.text(1.04, yo, "%s [%s; %s]" % (ozet[2], *ozet[3].split(" ile ")), transform=tr,
            va="center", ha="left", fontsize=10.5, color=L, weight="bold")
    ax.text(1.70, yo, ozet[4], transform=tr, va="center", ha="right", fontsize=10.5, color=GR)
    ax.text(-0.72, yp, "%95 tahmin aralığı", transform=tr, va="center", ha="left",
            fontsize=10.5, color=M)
    ax.text(1.04, yp, "[%s; %s]" % tuple(ta[3].split(" ile ")), transform=tr, va="center",
            ha="left", fontsize=10.5, color=M)
    top = n + 3.2
    for xx, s, ha in ((-0.72, "Çalışma", "left"), (-0.12, "n", "right"),
                      (1.04, "g [%95 GA]", "left"), (1.70, "Ağırlık %", "right")):
        ax.text(xx, top, s, transform=tr, va="center", ha=ha, fontsize=10.5, color=L,
                weight="bold")
    ax.axvline(0, color=GR, lw=0.9)
    ax.axvline(gv, color=M, lw=0.8, ls=(0, (3, 3)))
    ax.set_ylim(0.2, n + 3.7)
    ax.set_xlim(-1.2, 2.0)
    ax.set_yticks([])
    for k in ("left", "right", "top"):
        ax.spines[k].set_visible(False)
    ax.xaxis.set_major_formatter(FuncFormatter(virgul))
    ax.set_xticks([-1, -0.5, 0, 0.5, 1, 1.5, 2])
    ax.tick_params(labelsize=9.5, colors=GR)
    ax.set_xlabel("Hedges' g", fontsize=10.5, color=L, labelpad=2)
    fig.text(0.30, 0.118, "← Kontrol lehine", ha="left", fontsize=10, color=GR)
    fig.text(0.70, 0.118, "Deney lehine →", ha="right", fontsize=10, color=GR)
    fig.text(0.02, 0.955, "Forest plot", ha="left", va="center", fontsize=14, color=L, weight="bold")
    fig.text(0.98, 0.955, etiket, ha="right", va="center", fontsize=11.5, color="white",
             weight="bold", bbox=dict(boxstyle="round,pad=0.3", fc="#B4472E", ec="none"))
    parca = alt_f.split(" · ")
    fig.text(0.02, 0.055, " · ".join(parca[:3]), ha="left", fontsize=8.8, color=GR)
    fig.text(0.02, 0.012, " · ".join(parca[3:]), ha="left", fontsize=8.8, color=GR)
    yol_f = os.path.join(GORSEL, "forest.png")
    fig.savefig(yol_f, dpi=200, facecolor="white")
    plt.close(fig)

    # --- funnel
    gl = [sayi(v) for v in funnel[1][1:]]
    se = [sayi(v) for v in funnel[2][1:]]
    oz = sayi(re.search(r"özet g = ([\d,]+)", gb).group(1))
    fig = plt.figure(figsize=(6.0, 4.45), dpi=200)
    ax = fig.add_axes([0.13, 0.2, 0.83, 0.65])
    import numpy as np
    s_ = np.linspace(0, 0.45, 50)
    ax.fill_betweenx(s_, oz - 1.96 * s_, oz + 1.96 * s_, color="#E8EEF7", zorder=0)
    ax.plot(oz - 1.96 * s_, s_, color=GR, lw=0.9, ls=(0, (4, 3)))
    ax.plot(oz + 1.96 * s_, s_, color=GR, lw=0.9, ls=(0, (4, 3)))
    ax.axvline(oz, color=L, lw=1.1)
    ax.scatter(gl, se, s=34, color=M, edgecolor="white", linewidth=0.6, zorder=3)
    ax.set_xlim(-0.4, 1.4)
    ax.set_ylim(0.45, 0)
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
    ax.xaxis.set_major_formatter(FuncFormatter(virgul))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: ("%.1f" % v).replace(".", ",")))
    ax.set_xlabel("Hedges' g", fontsize=10.5, color=L)
    ax.set_ylabel("SE", fontsize=10.5, color=L)
    ax.tick_params(labelsize=9.5, colors=GR)
    for k in ("right", "top"):
        ax.spines[k].set_visible(False)
    ax.text(oz + 0.02, 0.43, "özet g = %s" % ("%.2f" % oz).replace(".", ","), fontsize=9.5,
            color=L, va="bottom")
    fig.text(0.02, 0.955, "Funnel plot", ha="left", va="center", fontsize=14, color=L, weight="bold")
    fig.text(0.98, 0.955, etiket, ha="right", va="center", fontsize=11.5, color="white",
             weight="bold", bbox=dict(boxstyle="round,pad=0.3", fc="#B4472E", ec="none"))
    fig.text(0.02, 0.03, alt_u, ha="left", fontsize=8.8, color=GR)
    yol_u = os.path.join(GORSEL, "funnel.png")
    fig.savefig(yol_u, dpi=200, facecolor="white")
    plt.close(fig)
    return yol_f, yol_u


def s9(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    yf, yu = grafikler(g)
    sl.shapes.add_picture(yf, Inches(0.4), Inches(1.25), Inches(6.3), Inches(4.45))
    sl.shapes.add_picture(yu, Inches(6.85), Inches(1.25), Inches(6.0), Inches(4.45))
    madde_kutusu(sl, 0.6, 5.8, 5.9, 1.15, liste[:3], boyut=16, bosluk=1)
    madde_kutusu(sl, 6.95, 5.8, 5.9, 1.15, liste[3:], boyut=16, bosluk=1)


# ---- Slayt 10 · Karşılaştırma tablosu
def s10(sl, g):
    t = tablolar(blok(g, "Slayt metni"))[0]
    gen = [1.85, 3.3, 3.5, 3.68]
    tablo(sl, 0.5, 1.55, 12.33, 5.3, t, gen, boyut=12, bas_boyut=14)
    not_ = [q for q in tirnaklar(satir_bul(gorsel_blok(g), "**Görsel")) if "içinde" in q][0]
    xk = 0.5 + sum(gen[:3])
    metin_kutusu(sl, xk - 2.6, 1.17, 5.2, 0.36, not_, boyut=12, renk=MAVI, kalin=True,
                 hiza=PP_ALIGN.CENTER, dikey=MSO_ANCHOR.MIDDLE)
    cizgi(sl, xk, 1.5, xk, 6.88, renk=MAVI, kalinlik=2.0, kesik=True)


# ---- Slayt 11 · Üç makale kartı
def s11(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    gb = gorsel_blok(g)
    t = tablolar(gb)[0]
    w, x0, ara = 4.0, 0.5, (12.33 - 3 * 4.0) / 2
    for k in range(3):
        x = x0 + k * (w + ara)
        kutu(sl, x, 1.3, w, 4.75, "", dolgu=BEYAZ, cizgi=GRI, kalinlik=1.0)
        kutu(sl, x, 1.3, w, 0.42, t[0][k + 1], boyut=14, dolgu=LACI, cizgi=None, renk=BEYAZ,
             kalin=True)
        kutu(sl, x, 1.72, w, 0.66, liste[k], boyut=14, dolgu=ACIKMAVI, cizgi=None, renk=MAVI,
             kalin=True, ic=0.04)
        par = []
        for r in t[1:]:
            par.append((r[0], {"boyut": 11.5, "kalin": True, "renk": LACI}))
            par.append((r[k + 1], {"boyut": 11.5}))
        tb = metin_kutusu(sl, x + 0.06, 2.45, w - 0.12, 3.58, par, boyut=11.5, italik=True)
        for i, p in enumerate(tb.text_frame.paragraphs):
            if i % 2 == 1:
                p.space_after = Pt(4)
    kutu(sl, 0.5, 6.13, 12.33, 0.4, liste[3], boyut=16, dolgu=MAVI, cizgi=None, renk=BEYAZ,
         kalin=True)
    tr = tirnaklar(satir_bul(gb, "Kartların altında"))[0]
    metin_kutusu(sl, 0.5, 6.55, 12.33, 0.38, tr, boyut=13, renk=LACI, hiza=PP_ALIGN.CENTER,
                 dikey=MSO_ANCHOR.MIDDLE)


# ---- Slayt 12 · Etik
def s12(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    gb = gorsel_blok(g)
    etiketler = tirnaklar(satir_bul(gb, "Üst bölüm:"))
    w = (12.33 - 4 * 0.15) / 5
    for i, e in enumerate(etiketler):
        x = 0.5 + (i % 5) * (w + 0.15)
        y = 1.32 + (i // 5) * 0.55
        kutu(sl, x, y, w, 0.45, e, boyut=14, dolgu=ACIKMAVI, cizgi=None, renk=LACI, kalin=True,
             sekil=MSO_SHAPE.ROUNDED_RECTANGLE, ic=0.03)
    madde_kutusu(sl, 0.6, 2.65, 5.5, 4.2, liste, boyut=17, bosluk=7)
    kutular = [tirnaklar(satir_bul(gb, "- Kutu %d" % i))[0] for i in (1, 2, 3)]
    y = 2.65
    for k in kutular:
        sol, sag = k.split(" → ", 1)
        s = kutu(sl, 6.4, y, 6.43, 0.92,
                 [(sol + " →", {"boyut": 15, "kalin": True, "renk": LACI}),
                  (sag, {"boyut": 15})], dolgu=BEYAZ, cizgi=MAVI, kalinlik=1.25,
                 hiza=PP_ALIGN.LEFT, ic=0.12, sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
        y += 1.04
    serit = tirnaklar(satir_bul(gb, "Üç kutunun altında"))[0]
    kutu(sl, 6.4, y + 0.05, 6.43, 0.62, serit, boyut=16, dolgu=LACI, cizgi=None, renk=BEYAZ,
         kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE)


# ---- Slayt 13 · Karar şeması ve soru-cevap tablosu
def s13(sl, g):
    q = tirnaklar(gorsel_blok(g))
    bas, b1, r1, soru, evet, hayir, b2, r2, b3, r3 = q[:10]
    kutu(sl, 2.2, 1.35, 3.0, 0.52, bas, boyut=16, dolgu=LACI, cizgi=None, renk=BEYAZ, kalin=True,
         sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
    xs = [0.5, 2.68, 4.86]
    for x, b, r in zip(xs, (b1, b2, b3), (r1, r2, r3)):
        kutu(sl, x, 2.25, 2.0, 0.9, b, boyut=13, dolgu=ACIKMAVI, cizgi=MAVI,
             sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
        kutu(sl, x, 3.5, 2.0, 0.66, r, boyut=13.5, dolgu=MAVI, cizgi=None, renk=BEYAZ, kalin=True,
             sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
        cizgi(sl, 3.7, 1.87, x + 1.0, 2.25, renk=MAVI, kalinlik=1.25, ok=True)
        cizgi(sl, x + 1.0, 3.15, x + 1.0, 3.5, renk=MAVI, kalinlik=1.25, ok=True)
    kutu(sl, 0.5, 4.55, 3.6, 0.95, soru, boyut=13, dolgu=BEYAZ, cizgi=MAVI, kesik=True,
         kalinlik=1.25, sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
    cizgi(sl, 1.5, 4.16, 1.5, 4.55, renk=MAVI, kalinlik=1.25, ok=True)
    for x, m in ((0.5, evet), (2.35, hayir)):
        kutu(sl, x, 5.85, 1.75, 0.85, m, boyut=13, dolgu=ACIKMAVI, cizgi=MAVI, renk=LACI,
             kalin=True, sekil=MSO_SHAPE.ROUNDED_RECTANGLE)
        cizgi(sl, x + 0.875, 5.5, x + 0.875, 5.85, renk=MAVI, kalinlik=1.25, ok=True)
    t = tablolar(blok(g, "Slayt metni"))[0]
    tablo(sl, 7.2, 1.35, 5.63, 5.0, t, [2.2, 3.43], boyut=14, bas_boyut=15,
          satir_yuk=[0.5, 1.15, 1.05, 1.05, 1.25])


# ---- Slayt 14 · Üç mesaj, üç soru
def s14(sl, g):
    liste = maddeler(blok(g, "Slayt metni"))
    mesaj, soru = liste[:3], liste[3:]
    for i, m in enumerate(mesaj):
        y = 1.6 + i * 1.5
        kutu(sl, 0.6, y, 0.8, 0.8, str(i + 1), boyut=28, dolgu=LACI, cizgi=None, renk=BEYAZ,
             kalin=True, sekil=MSO_SHAPE.OVAL)
        metin_kutusu(sl, 1.6, y - 0.1, 4.8, 1.0, m, boyut=24, renk=LACI, kalin=True,
                     dikey=MSO_ANCHOR.MIDDLE)
    for i, s in enumerate(soru):
        y = 1.5 + i * 1.5
        bas, govde = s.split(": ", 1)
        kutu(sl, 6.9, y, 5.93, 1.1, [(bas, {"boyut": 15, "renk": RGBColor(0xDD, 0xE4, 0xF0),
                                            "kalin": True}),
                                     (govde, {"boyut": 20, "renk": BEYAZ, "kalin": True})],
             dolgu=MAVI, cizgi=None, sekil=MSO_SHAPE.ROUNDED_RECTANGLE, hiza=PP_ALIGN.LEFT,
             ic=0.18)


# ---- Slayt 15 · Kaynakça
def s15(sl, g):
    k = g.split("**Kaynakça (slayt metni, tam liste):**", 1)[1]
    refs = re.findall(r"^\d+\. (.*)$", k.split("**Sunucu notu**")[0], flags=re.M)
    assert len(refs) == 26, len(refs)
    yarim = 13
    for c, parca in enumerate((refs[:yarim], refs[yarim:])):
        tb = metin_kutusu(sl, 0.4 + c * 6.33, 1.17, 6.23, 5.78, parca, boyut=KAYNAK_PT,
                          bosluk=0.6, italik=True, ic=0.0)
        for p in tb.text_frame.paragraphs:
            asili_girinti(p, 0.25)
    gb = gorsel_blok(g)
    not_ = tirnaklar(satir_bul(gb, "**Görsel"))[0]
    metin_kutusu(sl, 0.5, 7.0, 11.6, 0.4, not_, boyut=10, renk=KOYUGRI, dikey=MSO_ANCHOR.MIDDLE)


KAYNAK_PT = 9

CIZICI = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7, 8: s8, 9: s9, 10: s10, 11: s11,
          12: s12, 13: s13, 14: s14, 15: s15}


def uret():
    md = oku()
    bol = slayt_bolumleri(md)
    assert sorted(bol) == list(range(1, 16)), sorted(bol)
    okuma_kurali = re.search(r"^Okuma kuralı:[^\n]*?görünür\.", md, flags=re.M).group(0)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    os.makedirs(GORSEL, exist_ok=True)

    for no in range(1, 16):
        g = bol[no]
        notu = notlar(g)
        if no == 1:
            notu = okuma_kurali + "\n\n" + notu
        baslik = "" if no == 1 else alan(g, "Başlık")
        sl = cerceve(prs, no, baslik, kaynak_satiri(g), notu)
        CIZICI.get(no, iskelet)(sl, g)

    # LibreOffice boş effectLst'i yok sayıp tema gölgesini çiziyor: gölge referansını kapat
    for sl in prs.slides:
        for sh in sl.shapes:
            for e in sh._element.iter(qn("a:effectRef")):
                e.set("idx", "0")
    prs.save(CIKTI)
    print("kaydedildi:", CIKTI, "slayt:", len(prs.slides))


if __name__ == "__main__":
    uret()
