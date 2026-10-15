# SONUC · p2-sablon

**Durum: BİTTİ**

**Ne üretti:**
- `sablon.html`: 70×90 cm dikey poster şablonu. Lacivert başlık bandı (iki logo yeri, başlık, yazarlar, üst simgeli kurumlar, e-postalar), 3 sütunlu gövde (Giriş, Amaç, Yöntem | Bulgular | Sonuç, Öneriler, Kaynakça), alt bantta TÜBİTAK 2209-A teşekkür satırı ve isteğe bağlı QR yeri. Bütün metin alanları köşeli parantezli yer tutucu, içerik uydurulmadı.
- `uret.js`: HTML'den PDF üreten ve sayfa taşmasını ölçen betik (`node uret.js girdi.html cikti.pdf`). p5-poster aynı betiği son poster için kullanabilir.
- `deneme.pdf`: boş şablonun baskı PDF'i. `onizleme.png`: küçük önizleme.

**Ölçü denetimi:**
- Sayfa: 1 sayfa, 1984 × 2551 pt = **700 × 900 mm**, dikey. İçerik yüksekliği 900 mm, taşma yok.
- Yazı boyutları: başlık 84 pt (yaklaşık 3 cm büyük harf), bölüm başlıkları 48 pt, gövde 30 pt, şekil açıklaması ve teşekkür 22 pt, kaynakça 21 pt. Gövde 2 m'den okunur.
- Kaynakça APA 7 asılı girintili.
- Kelime bütçesi yer tutuculara yazıldı: Giriş 100 ile 130, Bulgular 80 ile 110, Tartışma 80 ile 100 kelime. Toplam gövde yaklaşık 600 ile 800 kelime.

**Takıldığı yer / yapamadığı:**
- TÜBED kongresinin resmi poster şablonu ya da logo şartı bulunamadı (web araması sonuç vermedi). Şablon yalnız kullanıcının verdiği kurallara göre kuruldu. Kongrenin şablonu varsa renk ve başlık bandı ona uyarlanmalı.
- Yazı tipi Inter (OTF); Chromium bunu PDF'e Type 3 olarak gömüyor. Vektör ve baskıda net, ama bazı matbaalar Type 3 yazı tipini istemiyor. Matbaa itiraz ederse PDF Ghostscript ile yazı tipleri dışa çevrilerek ya da TrueType bir yazı tipiyle (Liberation Sans, Carlito) yeniden üretilmeli.
- Yöntem sütunundaki şekil kutusu, kalan boşluğu doldurmak için uzun. Gerçek içerik gelince kutu boyu içeriğe göre ayarlanacak.
