# SONUC · m7 · PowerPoint sunum dosyası

> Durum: **bitti.** Girdi yalnız `isler/m6-denetim/slaytlar-son.md` (değiştirilmedi). Yazılan yer yalnız `isler/m7-slaytlar/`. Git commit yapılmadı.

## 1. Üretilenler

| Dosya | Ne |
|---|---|
| `isler/m7-slaytlar/sunum.pptx` | 15 slayt, 16:9 (13,333 × 7,5 inç), Calibri, beyaz zemin, lacivert #1F2A44 ve koyu mavi #2B5797 |
| `isler/m7-slaytlar/uret.py` | Üretici. Slayt metni, tablo hücreleri, kutu metinleri, kaynakça ve notlar girdiden **ayrıştırılarak** alınır (elle kopyalama yok); `python3 uret.py` ile yeniden üretilir |
| `isler/m7-slaytlar/onizleme/sunum.pdf` | LibreOffice ile PDF önizleme |
| `isler/m7-slaytlar/onizleme/slayt-01.png` ... `slayt-15.png` | 80 dpi önizleme PNG'leri |
| `isler/m7-slaytlar/onizleme/grafik/forest.png`, `funnel.png` | Slayt 9 grafikleri, matplotlib, 200 dpi, m3 kurgu verisi (girdideki tablolardan okunur) |

Slayt başına ana görsel: 2 yelpaze (Kutu 3 Kutu 2'nin içinde, kesik çizgili) · 3 derleme türleri tablosu · 4 PICOS tablosu (harf sütunu renkli kutu) · 5 sekiz adımlı süreç şeridi + PRISMA 2020 akış şeması · 6 üç sütun (tabanlar, I/P/O/S etiketli kurgu dize, RoB 2 mini tablo) · 7 iç içe küme (SR dış elips, MA iç daire, SWiM kesik kutu) · 8 kavram tablosu + formül · 9 forest ve funnel plot · 10 on ölçütlü tablo (SR ile MA arasında kesik çizgi ve not) · 11 üç makale kartı · 12 on etiket + üç kutulu etik kurul şeması + ortak şerit · 13 karar akışı + soru-cevap tablosu · 14 üç mesaj ve üç soru kutusu · 15 iki sütunlu kaynakça.

## 2. Denetim tablosu

| Ölçüt | Sonuç |
|---|---|
| Slayt sayısı | 15 |
| Not alanı dolu | 15 / 15; her notta "Konuşma metni", "Kavram notu", "Yöntemsel dikkat", "Hoca sorarsa", "Süre" var (slayt 15 konuşma metni girdide "(yok; ...)") |
| Okuma kuralı uyarısı | Yalnız slayt 1 notunun başında, girdideki "Okuma kuralı" cümlesiyle, bir kez |
| Em dash / en dash | 0 (slayt metinleri, tablo hücreleri ve notlar python-pptx ile tarandı) |
| Slayt metni kapsamı | Her slaytın "Slayt metni" maddeleri betikle karşılaştırıldı; birebir olmayan 4 durum yalnız düzen farkı: s1 başlık iki satıra bölündü (başlık + alt başlık), s5 ilk madde sekiz kutulu şerit olarak, s6 ilk madde "Nerede ararım" sütunundaki taban listesi olarak, s14 soruların "Soru N" etiketi ayrı satırda |
| Kaynakça | 26 kaynak, APA 7, asılı girinti, sol 1 ile 13, sağ 14 ile 26; italikler korunmuş; ikincil atıf notu alt satırda |
| Kurgu veri etiketi | Forest ve funnel plot başlıklarında "Eğitim amaçlı kurgu veri"; s4 "Eğitim amaçlı kurgu örnek", s6 "Eğitim amaçlı kurgu arama dizesi" |
| PRISMA akış şeması | Üç bant (Tanımlama/Identification, Tarama/Screening, Dahil etme/Included), iki sütun (kayıtlar / dışlananlar), Türkçe metin + küçük puntoyla İngilizce özgün terim, sayılar "(n = )" boş; altında "Page ve ark. (2021) akış şemasından uyarlanmıştır" ve girdideki çeviri notu; sağda PRISMA alıntısı |
| Atıf satırı ve slayt no | Her slaytın altında; "yalnız notta" atıflar alt satıra konmadı, notta kaldı |
| Türkçe karakter | ğ, ş, ı, İ, ç, ö, ü önizlemede doğru (Calibri, LibreOffice'te metrik uyumlu Carlito ile çizildi; grafiklerde Carlito) |
| Punto | Başlık 28 (s10: 26), gövde 16 ile 20, tablolar 12 ile 14, kart metinleri 11,5, kaynakça 9, PRISMA kutuları 10,5 (İngilizce terim 8,5) |

## 3. Görsel kontrolde düzeltilenler

1. LibreOffice boş `effectLst`'i yok sayıp tema gölgesi çiziyordu: bütün şekillerde `effectRef` 0 yapıldı.
2. s6 kurgu dizedeki `adolescen*[tiab] OR youth*` yıldızları italik işaretine dönüşüyordu: italik ayrıştırma yalnız makale kartları ve kaynakçada açık bırakıldı; dize birebir.
3. s5 "Dahil etme" bant etiketi kısa kutuya sığmıyordu: satır yüksekliği artırıldı, bant yazısı 10,5 pt.
4. s10 başlık 28 pt'de iki satıra taşıp ayraç çizgisine biniyordu: 72 karakterden uzun başlık 26 pt. Tablo üstü not yanlış tırnağı alıyordu ("Sistematik derleme"), düzeltildi.
5. s11 kart vurgu satırı (ikinci ve üçüncü kart) taşıyordu: kutu yüksekliği ve punto ayarlandı.
6. s15 kaynakça sağ sütunu alt bilgi çizgisine taşıyordu: paragraf aralığı daraltıldı, alan genişletildi; 9 pt'de iki sütun sığdı.
7. s9 funnel dikey eksen etiketleri tekrar ediyordu (0,1 0,1 ...): tikler 0 ile 0,4 arası sabitlendi. s13 tablo başlık satırı ve s3 tablo satırları yüksekliği düzeltildi.

## 4. Metin kısaltmaları

Yok. Hiçbir slayt metni, tablo hücresi, kutu metni ya da not kısaltılmadı veya değiştirilmedi. Yalnız düzen: s5 dışlanan rapor nedenleri tek satırda "·" ile; PRISMA kutularındaki "(n = )" satırları "·" yerine alt alta.

## 5. Bilinen sorunlar ve sapmalar

- **Kaynakça 9 pt:** BRIEF tablo ve kaynakça için en az 10 ile 11 pt diyor; girdi 9 ile 10 pt öneriyor. 26 tam APA kaydı iki sütunda tek slayta 10 pt'de sığmıyor; girdideki 9 pt kullanıldı. 10 pt istenirse kaynakça iki slayta bölünmeli (slayt sayısı 16 olur).
- **s10 başlığı 26 pt** (28 ile 32 aralığının altında); başlık metni 78 karakter ve kısaltılmadı.
- **PRISMA İngilizce terimleri 8,5 pt**: ana oturum notu "küçük puntoyla" istediği için bilinçli.
- **Kapak yer tutucuları** girdideki biçimde: "[Sunucunun adı soyadı] · Yüksek Lisans Öğrencisi", "Bilimsel Araştırma ve Etik · [Hocanın unvanı, adı soyadı]", "[Üniversite] · [Enstitü] · [Anabilim Dalı] · [Sunum tarihi]". BRIEF'teki "[Ad Soyad]" vb. biçim yerine içerik kuralı gereği girdi metni korundu; anlam aynı.
- **İngilizce PRISMA terimleri** girdide yok; ana oturum notu üzerine Page ve ark. (2021) akış şemasının özgün kutu adlarından eklendi (`uret.py` içinde `PRISMA_EN`). Resmi şablonla karşılaştırma yapılamadı (şablon indirilemedi, ana oturum notu).
- Önizleme LibreOffice ile yapıldı; PowerPoint'te Calibri metrik olarak Carlito ile aynı olduğundan satır kırılımlarının aynı kalması beklenir, ama PowerPoint'te açılıp bakılmadı.
- Slayt 15 notunun başında "Konuşma metni: (yok; ...)" var; girdideki gibi.

## 6. Zaman

Yaklaşık 21:46 ile 21:58 arası (BRIEF ek notunun yazılmasından SONUC'a). İskelet önce yazılıp çalıştırıldı, sonra slayt slayt geliştirildi; 7 kez yeniden üretilip önizlendi.
