# BRIEF · Meta-analizin temel istatistiği

> Plan: `plan/2026-10-10-plan.md`, dalga 1. Bu iş dalgadaki diğer üç işle aynı anda koşuyor.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi için 20 ile 25 slaytlık sunum: "Meta-analiz, sistematik derleme ve derleme". Dinleyici: beden eğitimi ve spor alanında yüksek lisans öğrencileri ve dersin hocası. Bazı öğrenciler konuyu ilk kez duyuyor. Sunum ~15 dk anlatım + 5 dk tartışma.
> Senin çıktın dalga 2'de slayt metni, konuşmacı notları ve APA 7 kaynakçaya dönüşecek. Bu yüzden anlatım hem doğru hem yeni başlayana anlaşılır olmalı, kaynaklar eksiksiz ve doğrulanmış olmalı.

## İş ne

Meta-analizin mantığı ve temel istatistiği, istatistik geçmişi zayıf bir yüksek lisans öğrencisinin anlayacağı dille. Kapsam (yalnız bunlar):

1. **Mantık:** neden tek çalışma yetmez, çalışmaları ağırlıklandırarak birleştirme (ters varyans ağırlıklandırma), istatistiksel gücün artması.
2. **Etki büyüklüğü:** Cohen d, Hedges g (küçük örneklem düzeltmesi), olasılık oranı (OR), risk oranı (RR), korelasyon r. Cohen'in küçük/orta/büyük eşikleri ve bu eşiklerin bağlama göre yorumlanması gerektiği uyarısı. Spor bilimine özgü yorum önerisi varsa (ör. Hopkins ve ark., 2009; doğrula) ekle.
3. **Modeller:** sabit etkiler ve rastgele etkiler modeli; hangi durumda hangisi; basit bir benzetmeyle.
4. **Heterojenlik:** Cochran Q, I² ve kabaca yorumu (Higgins ve ark., 2003; doğrula), tau², tahmin aralığı (prediction interval; IntHout ve ark., 2016 gibi; doğrula).
5. **Orman grafiği (forest plot) nasıl okunur:** kare, kare büyüklüğü, yatay çizgi (güven aralığı), dikey sıfır/etkisizlik çizgisi, elmas. Slaytta çizilebilmesi için **kurgu bir örnek veri seti** öner (ör. 5 çalışma, her biri için g ve %95 GA ve ağırlık, ve birleşik etki); bunu açıkça "eğitim amaçlı kurgu veri" diye işaretle, gerçek çalışma gibi sunma.
6. **Yayın yanlılığının tespiti:** huni grafiği (funnel plot), Egger testi (Egger ve ark., 1997; doğrula), kırp ve doldur (trim and fill). Bu araçların sınırları.
7. **Ek analizler:** alt grup analizi, meta-regresyon, duyarlılık analizi (bir çalışmayı çıkarma).
8. **Yazılımlar:** RevMan, R (metafor, Viechtbauer, 2010; doğrula), Comprehensive Meta-Analysis, JASP, Jamovi (MAJOR). Ücretsiz olanları belirt.

**Sınır:** derleme türleri ve etik iş s1'in; PRISMA, arama, yanlılık riski araçları iş s2'nin; gerçek spor örnek meta-analizleri iş s4'ün.

## Arama için başlangıç anahtar kelimeleri

Borenstein introduction to meta-analysis fixed random effects, Higgins 2003 measuring inconsistency I2, Egger 1997 bias in meta-analysis funnel, trim and fill Duval Tweedie, prediction intervals meta-analysis IntHout, Hopkins 2009 progressive statistics sports medicine, Hedges g small sample correction, metafor Viechtbauer 2010, how to read a forest plot, Cochrane Handbook analysing data meta-analysis

## Kaynak hedefi

En az **8** doğrulanmış bilimsel kaynak (yöntem makaleleri ve ders kitapları sayılır; kitaplar için yayıncı ve baskı bilgisini doğrula). En az 3'ü 2016-2026 arası. Türkçe hakemli bir meta-analiz yöntem makalesi bulunursa ekle.

## Girdisi

Web ve bilimsel veri tabanları. Repodaki başka dosyalar girdi değil.

## Çıktısı ve nereye yazacak

Tek dosya: `isler/s3-meta-analiz-yontemi/SONUC.md`. Bu dosyayı dalga 2'deki sunum içeriği işi okuyacak.

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

- YALNIZ kendi klasörüne yaz: `isler/s3-meta-analiz-yontemi/`. Başka hiçbir yere dosya yazma, başka işlerin klasörlerini okuma.
- Tek dosya üret: `isler/s3-meta-analiz-yontemi/SONUC.md`. Commit ya da push YAPMA.

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
