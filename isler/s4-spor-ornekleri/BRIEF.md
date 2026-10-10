# BRIEF · Beden eğitimi ve spordan örnek sistematik derleme ve meta-analizler

> Plan: `plan/2026-10-10-plan.md`, dalga 1. Bu iş dalgadaki diğer üç işle aynı anda koşuyor.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi için 20 ile 25 slaytlık sunum: "Meta-analiz, sistematik derleme ve derleme". Dinleyici: beden eğitimi ve spor alanında yüksek lisans öğrencileri ve dersin hocası. Bazı öğrenciler konuyu ilk kez duyuyor. Sunum ~15 dk anlatım + 5 dk tartışma.
> Senin çıktın dalga 2'de slayt metni, konuşmacı notları ve APA 7 kaynakçaya dönüşecek. Bu yüzden anlatım hem doğru hem yeni başlayana anlaşılır olmalı, kaynaklar eksiksiz ve doğrulanmış olmalı.

## İş ne

Sunumu dinleyicinin alanına bağlayacak gerçek örnekler. Her örnek bir kavramı göstermek için kullanılacak.

**Bul ve doğrula:**

1. **En az 3 meta-analiz**, beden eğitimi ve spor alanından, birbirinden farklı alt alanlardan. Aday alanlar (doğrula, uygunsa kullan): sakatlık önleme egzersiz programları (ör. Lauersen ve ark., 2014, BJSM), kafein ve performans, direnç antrenmanı hacmi ve kas hipertrofisi (ör. Schoenfeld ve ark., 2017), HIIT ve aerobik kapasite, beden eğitimi derslerinin akademik başarı ya da fiziksel aktiviteye etkisi, FIFA 11+ programı. Güncel (2020-2026) olanları öncele.
2. **En az 2 sistematik derleme** (meta-analizsiz olanlar dahil), mümkünse biri beden eğitimi / okul sporu, biri antrenman bilimi.
3. **En az 1 Türkiye kaynaklı örnek:** Türk araştırmacıların spor bilimlerinde yaptığı bir sistematik derleme / meta-analiz (Türkçe ya da İngilizce), ya da YÖK Tez'de spor alanında meta-analiz tezi. YÖK Tez doğrudan erişilemeyebilir; web aramasıyla dene.
4. **Mümkünse 1 tane yanlılık ya da çelişki örneği:** spor biliminde meta-analiz kalitesini eleştiren bir çalışma (ör. spor ve egzersiz bilimlerinde meta-analizlerin raporlama kalitesi, ya da aynı soruya farklı sonuç veren iki meta-analiz). Tartışma bölümü için değerli.

**Her örnek için bir kart yaz:** künye · araştırma sorusu (PICO biçiminde) · taranan veri tabanları · dahil edilen çalışma ve katılımcı sayısı · kullanılan yöntem (sabit/rastgele etkiler, yanlılık riski aracı, PRISMA uyumu) · ana bulgu (etki büyüklüğü ve %95 GA ya da RR, yalnız özette ya da tam metinde gördüğün sayılar) · heterojenlik (I² varsa) · sunumda hangi kavramı örnekliyor (ör. "orman grafiği okuma", "yüksek heterojenlik", "PRISMA akış şeması").

**Sınır:** genel yöntem anlatımı (PRISMA, I² tanımı, etik) diğer işlerin; sen yalnız örnek bul ve kartını yaz.

## Arama için başlangıç anahtar kelimeleri

meta-analysis injury prevention exercise programs Lauersen, FIFA 11+ meta-analysis, caffeine exercise performance umbrella review, resistance training volume hypertrophy meta-analysis Schoenfeld, HIIT VO2max meta-analysis, physical education intervention academic achievement meta-analysis, school physical education systematic review, reporting quality meta-analyses sport exercise science, spor bilimleri meta-analiz Türkiye, beden eğitimi sistematik derleme Türkçe, YÖK tez meta-analiz spor

## Kaynak hedefi

En az **6** doğrulanmış örnek çalışma (3 meta-analiz + 2 sistematik derleme + 1 Türkiye kaynaklı), hedef 7 ile 9. En az 4'ü 2018-2026 arası.

## Girdisi

Web ve bilimsel veri tabanları. Repodaki başka dosyalar girdi değil.

## Çıktısı ve nereye yazacak

Tek dosya: `isler/s4-spor-ornekleri/SONUC.md`. Bu dosyayı dalga 2'deki sunum içeriği işi okuyacak.

## Veri tabanları ve doğrulama

Kullanıcının istediği tabanlar: PubMed, SPORTDiscus, Google Akademik, Web of Science, YÖK Ulusal Tez Merkezi.

- **Filo defteri uyarısı:** bu ortamda PubMed API, Crossref, doi.org, Europe PMC, OpenAlex ve YÖK Tez doğrudan erişilemedi (403 / DNS hatası). Bunları en fazla bir kez dene, zaman kaybetme. Asıl kanal **WebSearch** aracıdır (ToolSearch ile `select:WebSearch,WebFetch` yükle). WebFetch bazı yayıncı sayfalarında çalışabilir, dene.
- Her kaynağı bu oturumda bir aramayla doğrula: yazar, yıl, başlık, dergi/yayıncı ve DOI (varsa) arama sonucundaki kayıtla eşleşmeli. Kaynağın hangi tabanda dizinlendiğini (PubMed/PMC, Google Akademik, YÖK Tez vb.) gördüğün kadarıyla yaz.
- SPORTDiscus ve Web of Science abonelik ister; erişemezsen "erişilemedi" yaz.

## Dürüstlük

- Yalnız gerçek ve doğrulanmış kaynak. Hafızandan künye yazma; her künye bu oturumda bir aramayla teyit edilmiş olmalı.
- Doğrulayamadığın kaynağı listeye koyma; "Doğrulanamayanlar" başlığında ayrıca not et.
- Her iddianın yanında (Yazar, Yıl) olsun. Sayısal bilgi (ör. eşik değerler, yüzdeler) yalnız kaynakta gördüysen yazılır.
- Hedef sayı tutmazsa SONUC.md'nin en başına açıkça yaz. Uydurarak tamamlama.

## İzolasyon

- YALNIZ kendi klasörüne yaz: `isler/s4-spor-ornekleri/`. Başka hiçbir yere dosya yazma, başka işlerin klasörlerini okuma.
- Tek dosya üret: `isler/s4-spor-ornekleri/SONUC.md`. Commit ya da push YAPMA.

## SONUC.md yapısı (Türkçe; em dash (uzun tire) HİÇBİR yerde yok; ayraç olarak nokta, virgül, iki nokta ya da orta nokta · kullan)

1. **Hedef durumu:** kaç doğrulanmış kaynak, hedef tuttu mu.
2. **Veri tabanı erişimi:** her taban için erişildi / erişilemedi.
3. **İçerik:** alt başlıklar halinde; yeni başlayana anlaşılır, yüksek lisans düzeyinde doğru. Her iddiada (Yazar, Yıl). Her alt başlığın sonunda "Slayta öneri:" satırı (tek cümle: bu kısım slaytta nasıl gösterilir, ör. tablo, şema, tek cümlelik mesaj).
4. **Konuşmacı notu malzemesi:** sınıfa söylenebilecek 4 ile 6 kısa, akılda kalıcı açıklama ya da benzetme (her biri kaynaklı ya da açıkça "benzetme" diye işaretli).
5. **Kaynak tablosu:** # · Yazar (Yıl) · Başlık · Dergi/Yayıncı · Tür (yöntem makalesi, kılavuz, kitap, özgün araştırma, derleme, tez) · Neyi destekliyor · Taban · DOI/bağlantı.
6. **Kaynakça (APA 7),** alfabetik.
7. **Doğrulanamayanlar ve sınırlar.**
8. **Zaman:** başlarken ve bitirirken `date -u +%H:%M:%S` çalıştır, ikisini de yaz.

## Bitince ne döndür

Tek paragraf: kaç doğrulanmış kaynak, hedef tuttu mu, erişilemeyen tabanlar, başlangıç ve bitiş saati.
