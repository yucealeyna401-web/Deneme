# SONUC · k4 · Sentez: ödev metni ve Word dosyası

**Durum:** tamamlandı. Tek sapma sayfa sayısında (bkz. "Eksikler", madde 1).

## Ne üretildi

| Dosya | İçerik |
|---|---|
| `odev.md` | Ödevin tam metni: 1 Giriş, 2 Yöntem, 3 Almanya, 4 Türkiye, 5 Karşılaştırma (9 ölçütlü tablo ve ölçüt ölçüt tartışma), 6 Tartışma ve Sonuç (7 öneri), Kaynakça (APA 7), Ek: Okuma Listesi |
| `odev.docx` | Word sürümü: başlık sayfası (öğrenci adı, numarası, ders, sorumlu ve tarih için boş alanlar), içindekiler alanı, ana metinde 1'den başlayan sayfa numarası, Times New Roman 12, 1,5 satır aralığı, iki yana yaslı metin, gri başlık satırlı biçimli tablolar (5 tablo, başlık satırı her sayfada tekrar eder), kaynakçada 1,27 cm asılı girinti, 141 tıklanabilir bağlantı |
| `okuma-listesi.md` | Ekteki okuma listesinin ayrı kopyası: 6 grup (A-F), 24 kaynak; her biri künye, bağlantı, özet ve "neden okunmalı" içeriyor |
| `word_uret.py` | odev.md'den odev.docx üreten python-docx betiği (`python3 word_uret.py`) |
| `denetle.py` | Denetim betiği: metin içi atıf ile kaynakça eşleşmesi, alfabetik sıra, em dash sayımı, kelime sayımı (`python3 denetle.py`) |

**İçindekiler notu:** İçindekiler bir Word alanı olarak eklendi. Word dosyayı açarken alanları güncellemeyi sorar; "Evet" denirse içindekiler dolar. Sorulmazsa: içindekiler alanına sağ tıklayın, "Alanı Güncelleştir"i seçin.

## Kelime ve sayfa sayısı

- Ana metin (Giriş'ten Sonuç'a kadar, başlıklar dahil): **5.811 kelime düzyazı; tablolarla 6.534 kelime.** Hedef 5.000-6.500 aralığındaydı.
- Bölüm payları: Giriş 499 (%7,6) · Yöntem 439 (%6,7) · **Almanya 2.664 (%40,8, en uzun bölüm)** · Türkiye 1.427 (%21,8) · Karşılaştırma 930 (%14,2) · Tartışma ve Sonuç 558 (%8,5).
- Word dosyası (LibreOffice ile PDF'e dönüştürülerek sayıldı, Liberation Serif = Times New Roman ölçüleri): toplam 43 sayfa. Başlık sayfası 1 · içindekiler 1 · **ana metin 21 sayfa** · kaynakça 13 sayfa · ek (okuma listesi) 7 sayfa.

## Kaynak sayısı

- Kaynakçada **114 künye** var. **34'ü Türkçe**, 80'i yabancı dilde (Almanca ve İngilizce). Bunlara ek olarak 4 kaynak Türk yazarların İngilizce yayınıdır (Akşit ve Ağbuğa, 2024; Karakaya vd., 2016; Korkmaz vd., 2021; Türkeli ve Namlı, 2024).
- `denetle.py` sonucu TEMİZ: metindeki her atıf kaynakçada var, kaynakçadaki her künye metinde atıflanmış (114/114). Kaynakça Türkçe harf sırasına göre alfabetik. Bütün çıktı dosyalarında em dash sayısı 0.
- Okuma listesi kaynakçadan ayrı bir ektir. Oradaki bazı kaynaklar (ör. Eurydice 2013) ana metinde atıflanmadığı için kaynakçada yok.

## Çelişkiler ve nasıl çözüldü

1. **Namlı ve Temel (2019).** k2 "Namlı, A. K." ve kısa başlıkla "doğrulandı" diyordu. k3 başlığı "...ve program önerisi" diye veriyor, ilk yazarın adını tutarsız bulup "doğrulanamadı" demişti. WebSearch'e göre AVESİS (Akdeniz) kaydı şöyle: Namlı, A. K. ve Temel, C. (2019). *Beden eğitimi ve spor öğretmenliği lisans programının değerlendirilmesi ve program önerisi*. Milli Eğitim, 48(1), 321-351. Yazar baş harfleri A. K.'dır ve tam başlık k3'ün verdiği uzun başlıktır. Kısa başlıklı Açıkbilim (YÖK) kaydı büyük olasılıkla Namlı'nın 2018 tarihli lisansüstü tezidir (danışmanı Cenk Temel, karma yöntem). Bu, başlıktaki ve addaki karışıklığı açıklıyor. **Çözüm:** makale künyesi kullanıldı ve ana metinde kaynak olarak yer aldı.
2. **KMK branş profili belgesinin sürüm tarihi.** k1a "2008/2016" verdi, k3 ise "2008/2019"u yer tutucu olarak yazmıştı. WebSearch: belgenin 12.06.2014 ve 06.10.2016 tarihli güncel hâlleri teyit edildi (Aşağı Saksonya formları "i. d. F. vom 06.10.2016" diye atıf yapıyor). 2019 ya da 2024 sürümü bulunamadı. **Çözüm:** KMK (2008/2016).
3. **Hazırlık hizmetinin süresi.** k3 (Deutscher Bildungsserver) "18 ay ile 2 yıl" diyor. k1b'de Eurydice (2021) "12-24 ay" diyor ve Brandenburg'u 12 ay olarak veriyor. **Çözüm:** resmî karşılaştırmalı rapor esas alındı, metinde "12-24 ay, çoğu eyalette 18 ay" yazıldı. Bu madde için yeni web araması yapılmadı, girdilerdeki resmî kaynaklar yeterli görüldü.
4. **Yıldırım ve Şimşek (2021) baskı numarası** (11. mi, 12. mi). WebSearch: Haziran 2021 tarihli baskı satış kaydında 12. baskı olarak geçiyor (ISBN 9789750269820). Yayınevi sayfasından teyit edilemedi. **Çözüm:** "12. baskı" yazıldı, teslimden önce kontrol edilmeli.
5. **Türkeli ve Namlı (2024) dergi adı** (TOJRAS mı, OJRS mi). WebSearch: AVESİS künyesi *The Online Journal of Recreation and Sports, 13*(1), 95-102. e-ijer.com'daki TOJRAS sayfası aynı başlığı taşıyor (yayın tarihi 25.01.2024). **Çözüm:** AVESİS künyesi kullanıldı.
6. **YÖK'ün 2020 yetki devri kararının tarihi.** k2 bunu "10 Ağustos" tarihiyle, yılı belirsiz bir Anka Haber kaynağına (doğrulanamadı) dayandırmıştı. WebSearch: YÖK basın arşivinin 2020 klasöründe "Eğitim fakülteleri ile ilgili karar" belgesi var. Ders, içerik ve kredi yetkisi, alan eğitimi, meslek bilgisi ve genel kültür gruplamasının korunması koşuluyla devredilmiş. Yıl 2020 olarak teyit edildi, "10 Ağustos" günü teyit edilemedi. **Çözüm:** Anka Haber yerine YÖK (2020b) basın belgesi kullanıldı ve gün yazılmadı.
7. **Gazi'nin kuruluşu 1926 mı, 1932 mi.** k2'nin açıklaması izlendi: 1926 kurumun kuruluşu, 1932 beden eğitimi şubesinin açılışıdır. Metinde ikisi de bu anlamlarıyla verildi.
8. **Hildebrandt-Stramann (2003 mı, 2008 mi).** PDF'teki sayı tarihi 2003, OJS sayfasındaki yayın tarihi 2008. k3'ün kararı izlendi, sayı tarihi olan 2003 kullanıldı.
9. **Praxissemester'in kredisi (25 mi, 33 AKTS mi).** Bu gerçek bir çelişki değil. 25 AKTS, 2009 yönetmeliğindeki asgari değer. Köln'deki 33 AKTS ise hazırlık ve değerlendirmeyi de kapsayan üniversite uygulaması. Metinde ikisi de kaynağıyla birlikte verildi.
10. **1997 YÖK düzenlemesinin tarihi** (k2'de 04.11.1997 ve 19.09.1997 tarihleri var). Kesin gün metne alınmadı. Metinde yalnız "1997'de başlayan yeniden yapılanma" ve 1998-1999 uygulama yılı var.

## Doğrulanamayan kaynaklar (ana metinde kullanılmadı)

Girdilerde "doğrulanamadı" işaretli olan şu kaynaklar ödeve **alınmadı**:

- k1a: Laufen in Köln (2010) ve sporteignungstest-koeln.de, yani DSHS sınavının sayısal ölçütleri (3000 m 13:00 vb.) · mygermanuniversity.com (%62 NC'siz) · Wikipedia ve zeitgeschichte-online (1947 ve 1973 bilgileri) · Hofmann (2021) · Reuker (2012) · Winter (2008) · Reinhart ve Krüger (2025) · den Ouden · wbv (2026) · studieren.de · Budrich Journals.
- k1b: dvs dizisinin 226. cildi (Referendariat im Fach Sport) · Theo-Web (2025) · ZfsL Solingen · Bayerischer Landtag (2016) ve onunla gelen 3.979 kişilik bekleme listesi rakamı (Drucksache eşleşmesi kesin değildi).
- k2: Günay (2013), yerine Gazi tarihçesi kullanıldı · Anka Haber (2020), yerine YÖK (2020b) kullanıldı · Cumhuriyet (2022) ve 2022 için 288 kontenjan rakamı · Balıkesir Üniversitesi (2025) · YÖK portalındaki 2025 tarihli "Beden Eğitimi Öğretmenliği Lisans Programı" belgesi · k2 ders tablosundaki [Ç] hücreleri: Tablo 4'e yalnız en az bir kaynakta görülmüş dersler alındı · engelli adayların öğretmenlik programına başvuramadığı iddiası · ÖZYES katsayıları · ilk AGS tarihi · 2024 ÖABT aday sayısı (22.949) · 2023'te atanan 990 kişi · 500 bin ve 140 bin rakamları.
- k3: Çekya (2022), Finlandiya (Bartın), Avusturya (Sakarya) ve İnönü (2018) çalışmaları ana metinde kullanılmadı. Okuma listesinde "F. Teyit edilmesi gerekenler" alt başlığında yer alıyorlar, yalnız başlık ve bağlantıyla. Yazar ve yıl uydurulmadı.

## Kullanıcının teslimden önce kontrol etmesi gerekenler

Bu kaynaklar ödevde kullanıldı ama girdi çalışanları yalnız arama özetlerini görebildi, tam metinler açılamadı. Teslimden önce özgün belgeden kontrol edilmeli:

1. **Eksik künye öğeleri (APA için tamamlanmalı):** Fischer, Gissel ve Pfitzner (2018) ve Neuber (2018) kitap bölümlerinin sayfa aralıkları · Braksiek ve Wolters (2022) için editör adlarının baş harfleri · Kastrup ve Kleindienst-Cachay (2021) kitabının alt başlığının tam ifadesi · Schaarschmidt ve Kieschke (2007), künye ikincil atıflardan · Baumgartner (2018) için cilt ve sayfa, yazarın yayın listesinden · Aykaç vd. (2014) için cilt, sayı ve sayfa, tek arama sonucundan · Hardman ve Marshall (2009) için yayın yeri · Bayerischer Landtag (2024), yıl tahmini · hessenschau, GEW, KMK (t.y.) ve diğer "t.y." kayıtlarının tarihleri · Hürriyet (2018) ve Anadolu Ajansı (2026) için gün ve ay · Yıldırım ve Şimşek baskı numarası · Eurydice (2025a, 2025b) sayfaları yalnız arama özetiyle görüldü.
2. **Sayısal veriler:** DSHS ve BaySpET sınav ayrıntıları (Bavyera'da 3000/2000 m, 10:30/8:30, 100 m serbest) · NRW kredi dağılımı (2009 LZV; güncel § 4 doğrulanmadı) · TUM 105/92/10 AKTS · NRW devlet sınavı ağırlıkları (%25/15/5/10; 2023 metnine ait, 2026 OVP bunları değiştirdi mi bilinmiyor) · Bavyera LPO II ağırlıkları · Eurydice'teki %75 memur / %25 sözleşmeli oranı · KMK projeksiyonu (417.000 / 367.000; news4teachers'tan aktarıldı, KMK Dokümantasyon 244 ile kontrol edilmeli) · %11,9 yan giriş, Brandenburg %48 · SPRINT %49, Berlin %27,8 · Bavyera'da 4 yılda 12 gün · Türkiye'de 800.000'inci başarı sırası · 240 AKTS · YÖK oranları (%30-35 / %15-20 / %45-50) · beden eğitimi kontenjanları 320 (2024, Habertürk), 190 (2025), 160 ve 16 (2026) · taban puan 85,69 (Timeturk) · Akademi değerlendirme oranları (%40 / %60) · uygulama öğretim elemanı başına 12 öğrenci.
3. **Tablolar:** Tablo 2 ve Tablo 3'teki modüller modül kitaplarından **seçilmiştir**, tam liste değildir. Tablo 4'teki (Türkiye ders planı) yarıyıl yerleşimleri farklı üniversitelerin planlarından derlendi. Sınıf Yönetimi ve Topluma Hizmet Uygulamaları başka bir 2018 programındaki yarıyıla göre yerleştirildi. Tablonun altına "yarıyıl yerleşimleri üniversiteden üniversiteye farklılık gösterebilmektedir" notu eklendi. YÖK 2018 program PDF'iyle satır satır karşılaştırılması önerilir.
4. **Kaynak eşleşmesi:** 4.1'de BESYO'ların spor bilimleri fakültelerine dönüşümü Marmara SBF sayfasına dayandırıldı. k2 bu bilgiyi birkaç üniversite tarihçe sayfasından ve Marmara haber sayfasından derlemişti. Gerekirse Resmî Gazete kararlarıyla desteklenmeli.
5. **Tam metinler:** Resmî Gazete (7528), YÖK 2018 programı ve ÖSYM 2026 ÖZYES kılavuzu elle açılıp kontrol edilmeli. Hiçbir girdi çalışanı bunları açamadı.

## Eksikler ve sapmalar

1. **Sayfa sayısı brieften fazla.** Brief 12-18 sayfa ile 5.000-6.500 kelimeyi eş tutuyor. Oysa Times New Roman 12 punto, 1,5 satır aralığı ve 2,5 cm kenar boşluğunda bir sayfa yaklaşık 280 kelime alıyor: 5.800 kelime ana metin 21 sayfa tutuyor. Kelime aralığına uyuldu, sayfa aralığı aşıldı. 18 sayfaya inmek için ana metin yaklaşık 4.900 kelimeye düşürülmeli ya da kenar boşlukları veya paragraf aralığı küçültülmeli. Bu, kullanıcının kararı.
2. **Başlık sayfası alanları boş:** öğrenci adı, numara, ders, sorumlu ve tarih.
3. **İçindekiler** Word açılışta güncellenir. LibreOffice ile açılırsa elle güncellenmesi gerekir (Araçlar > Güncelle).
4. **Dalga 1 sınırı sürüyor:** WebFetch kapalı olduğu için yeni çelişki denetimleri de yalnız WebSearch özetleriyle yapıldı (4 arama: Namlı ve Temel, KMK sürümü, Yıldırım ve Şimşek, Türkeli ve Namlı; ayrıca YÖK yetki devri). Hiçbir tam metin okunmadı.
5. Filo defterine (`sen/01-isler.md`) yazılmadı, çünkü izolasyon kuralı gereği bu klasör dışına yazılmadı. Orkestratör için önerilen satır: "k4: girdi 21 bin kelime, çıktı 5,8 bin; brief'teki 12-18 sayfa ile 5-6,5 bin kelime hedefi 1,5 satır aralığında birbiriyle çelişiyor (5,8 bin kelime = 21 sayfa)."
