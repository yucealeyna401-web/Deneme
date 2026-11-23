# BRIEF · m7 · PowerPoint sunum dosyası

> Plan: `plan/2026-11-23-plan.md` · Dalga 4 (tek) · Çıktı: `isler/m7-slaytlar/sunum.pptx` + `uret.py` + `SONUC.md` (+ önizleme PNG'leri) · Bu klasör dışına yazma, git commit yapma.

## Girdi
- **Yalnız** `isler/m6-denetim/slaytlar-son.md` (denetlenmiş son metin). İçeriği değiştirme, kısaltma ya da yeni bilgi ekleme; yalnız görsel düzen. Metin slayta sığmıyorsa yazı boyutunu makul ölçüde küçült ya da düzeni değiştir; anlam değiştirmeden kısaltma gerekiyorsa SONUC.md'de listele.
- Tasarım şartları: `sen/kaynak/2026-11-23-sunum-gorevi.md` bölüm 7.

## Araçlar (kurulu)
python-pptx 1.0.2, matplotlib, LibreOffice (`soffice --headless --convert-to pdf` ile önizleme; sonra `pdftoppm` ya da LibreOffice ile PNG). Görselleri matplotlib ile PNG (200 dpi) üret ve slayta yerleştir ya da python-pptx şekilleriyle çiz.

## Tasarım
- 16:9 (13,333 × 7,5 inç). Beyaz zemin; lacivert (#1F2A44 civarı) başlık ve vurgu, koyu mavi (#2B5797 civarı) ikincil, açık gri çizgiler. Tek yazı tipi ailesi (Calibri ya da sistemde olan sans-serif; Türkçe karakterler ğ, ş, ı, İ, ç, ö, ü doğru görünmeli, önizlemede kontrol et).
- Başlık 28 ile 32 pt, gövde en az 16 pt (tablo ve kaynakça en az 10 ile 11 pt). Görsel kalabalık yok; slayt başına bir ana görsel.
- Her slaytın altında küçük atıf satırı (metin içi kaynaklar) ve slayt numarası.
- **Sunucu notları:** her slaytın konuşma metni + kavram notu + yöntemsel dikkat + hoca sorarsa + süre, PowerPoint not alanına (`slide.notes_slide.notes_text_frame`).
- Gerekli görseller: kanıt sentezi yelpazesi (slayt 2), derleme türleri mini tablosu (3), PICOS kutuları (4), PRISMA 2020 akış şeması (5; kutu metinleri slaytlar-son.md'den), arama/Boolean ve seçim şeması (6), SR ile MA ilişkisi (iç içe küme ya da akış, 7), kavram kartları (8), **forest plot ve funnel plot** (9; m3'ün kurgu verisiyle matplotlib, "Eğitim amaçlı kurgu veri" etiketi görünür), 10 ölçütlü karşılaştırma tablosu (10; okunaklı), 3 makale kartı (11), etik ikon/kutu düzeni (12), karar akışı (13), 3 soru (14), iki sütunlu kaynakça (15).
- Kapak: başlık, alt başlık, [Ad Soyad], [Ders: Bilimsel Araştırma ve Etik], [Öğretim Üyesi: Unvan Ad Soyad], [Üniversite / Enstitü / Anabilim Dalı], [Tarih] yer tutucuları.

## Çalışma sırası (kesinti dersi, 2026-10-13)
1. `uret.py`'yi önce iskelet hâliyle yaz ve HEMEN çalıştır (15 slayt, başlıklar, notlar). `sunum.pptx` diske düşsün.
2. Sonra slayt slayt görselleri ekle, her birkaç slaytta bir yeniden çalıştır.
3. PDF ve PNG önizleme üret (`onizleme/`), her slaytı göz ile kontrol et: taşma, üst üste binme, okunaksız yazı, Türkçe karakter. Sorunları düzelt.
4. Denetim: 15 slayt, 15 not alanı dolu, em dash/en dash yok (pptx içindeki metni python-pptx ile tara), kaynakça slaytı tam.

## SONUC.md
Üretilenler, denetim tablosu, görsel kontrolde düzeltilenler, metin kısaltmaları (varsa), bilinen sorunlar, zaman.

## Bitince döndür
Dosya yolu, slayt sayısı, not alanı durumu, görsel kontrol sonucu, bilinen sorunlar.
