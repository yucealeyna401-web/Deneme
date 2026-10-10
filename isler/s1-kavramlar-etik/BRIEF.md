# BRIEF · Derleme türleri, kanıt hiyerarşisi ve etik

> Plan: `plan/2026-10-10-plan.md`, dalga 1. Bu iş dalgadaki diğer üç işle aynı anda koşuyor.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi için 20 ile 25 slaytlık sunum: "Meta-analiz, sistematik derleme ve derleme". Dinleyici: beden eğitimi ve spor alanında yüksek lisans öğrencileri ve dersin hocası. Bazı öğrenciler konuyu ilk kez duyuyor. Sunum ~15 dk anlatım + 5 dk tartışma.
> Senin çıktın dalga 2'de slayt metni, konuşmacı notları ve APA 7 kaynakçaya dönüşecek. Bu yüzden anlatım hem doğru hem yeni başlayana anlaşılır olmalı, kaynaklar eksiksiz ve doğrulanmış olmalı.

## İş ne

Sunumun kavramsal temeli. Kapsam (yalnız bunlar):

1. **Tanımlar:** geleneksel (anlatı / narrative) derleme, sistematik derleme, meta-analiz. Üçünün farkı: soru, arama, seçim, değerlendirme, sentez, tekrarlanabilirlik. Sistematik derleme meta-analiz içermek zorunda değil; meta-analiz sistematik derleme olmadan da yapılabilir ama önerilmez. Bunu kaynakla göster.
2. **Diğer derleme türleri kısaca:** kapsam (scoping) derlemesi, şemsiye derleme, hızlı (rapid) derleme vb. (Grant ve Booth, 2009 türlemesi; Munn ve ark., 2018 scoping ve sistematik ayrımı gibi; doğrula).
3. **Kanıt hiyerarşisi / kanıt piramidi:** sistematik derleme ve meta-analizin yeri, piramide yönelik eleştiriler ve güncel yaklaşımlar (ör. Murad ve ark., 2016 "new evidence pyramid"; doğrula).
4. **Güçlü ve zayıf yönler:** "çöp girerse çöp çıkar", elma ile armut karşılaştırması, araştırmalar arası farklılık. Meta-analizlerin seri ve gereksiz üretimi eleştirisi (Ioannidis, 2016; doğrula).
5. **Araştırma etiği boyutu (ders etik dersi olduğu için önemli):** yayın yanlılığı ve seçici raporlamanın etik yönü, intihal ve aynı verinin çoklu yayını (duplicate publication) meta-analizi nasıl bozar, geri çekilmiş (retracted) çalışmaların derlemelere girmesi, yağmacı (predatory) dergiler, çıkar çatışması ve finansman, protokol kaydının şeffaflık işlevi. Derlemeler için etik kurul gerekmez ama etik sorumluluk vardır: bunu kaynakla anlat. Türkçe kaynak (ör. Türk dergilerinde araştırma etiği ya da derleme yöntemi makalesi, YÖK Tez) bulunursa ekle.

**Sınır:** PRISMA adımları, PICO, yanlılık riski araçları (RoB 2 vb.) iş s2'nin; etki büyüklüğü, heterojenlik, huni grafiği iş s3'ün; spor örnekleri iş s4'ün. Bunlara yalnız bir cümleyle değin, ayrıntıya girme.

## Arama için başlangıç anahtar kelimeleri

typology of reviews Grant Booth, systematic review vs narrative review, scoping review vs systematic review Munn, new evidence pyramid Murad, mass production of redundant meta-analyses Ioannidis, retracted studies in systematic reviews, duplicate publication meta-analysis bias, predatory journals systematic reviews, sistematik derleme meta-analiz nedir Türkçe

## Kaynak hedefi

En az **8** doğrulanmış bilimsel kaynak; en az 3'ü 2018-2026 arası. Yöntem makaleleri, kılavuzlar ve hakemli makaleler öncelikli; web sayfası ve blog kaynak sayılmaz (Cochrane Handbook gibi resmi kılavuzlar sayılır). En az 1 Türkçe hakemli kaynak hedefle; bulunamazsa yaz.

## Girdisi

Web ve bilimsel veri tabanları. Repodaki başka dosyalar girdi değil.

## Çıktısı ve nereye yazacak

Tek dosya: `isler/s1-kavramlar-etik/SONUC.md`. Bu dosyayı dalga 2'deki sunum içeriği işi okuyacak.

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

- YALNIZ kendi klasörüne yaz: `isler/s1-kavramlar-etik/`. Başka hiçbir yere dosya yazma, başka işlerin klasörlerini okuma.
- Tek dosya üret: `isler/s1-kavramlar-etik/SONUC.md`. Commit ya da push YAPMA.

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
