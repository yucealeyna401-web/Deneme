# BRIEF · Sistematik derlemenin adımları

> Plan: `plan/2026-10-10-plan.md`, dalga 1. Bu iş dalgadaki diğer üç işle aynı anda koşuyor.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi için 20 ile 25 slaytlık sunum: "Meta-analiz, sistematik derleme ve derleme". Dinleyici: beden eğitimi ve spor alanında yüksek lisans öğrencileri ve dersin hocası. Bazı öğrenciler konuyu ilk kez duyuyor. Sunum ~15 dk anlatım + 5 dk tartışma.
> Senin çıktın dalga 2'de slayt metni, konuşmacı notları ve APA 7 kaynakçaya dönüşecek. Bu yüzden anlatım hem doğru hem yeni başlayana anlaşılır olmalı, kaynaklar eksiksiz ve doğrulanmış olmalı.

## İş ne

Sistematik derlemenin uçtan uca nasıl yapıldığı. Kapsam (yalnız bunlar):

1. **Araştırma sorusu:** PICO / PICOS (ve nitel için SPIDER gibi alternatifler kısaca). Spor bilimine uygun bir örnek soru yaz (ör. "Genç futbolcularda (P) nöromüsküler ısınma programı (I), olağan ısınmaya göre (C) alt ekstremite sakatlığını (O) azaltır mı?"). Örnek soru senin kurgun olabilir; bunu "örnek kurgu" diye işaretle.
2. **Protokol ve kayıt:** PRISMA-P, PROSPERO kaydı (ve OSF gibi alternatifler); neden önceden kayıt.
3. **Arama stratejisi:** veri tabanları (PubMed/MEDLINE, SPORTDiscus, Web of Science, Scopus, Google Akademik'in rolü ve sınırları), Boolean operatörler (AND, OR, NOT), MeSH terimleri, gri literatür, el ile tarama. Google Akademik'in sistematik derlemede tek başına yeterli olmadığına dair kanıt (ör. Gusenbauer ve Haddaway, 2020; Bramer ve ark., 2017; doğrula). Türkiye bağlamında YÖK Tez ve TR Dizin'in gri literatür / ulusal kaynak olarak yeri.
4. **Tarama ve seçim:** dahil etme / dışlama ölçütleri, iki bağımsız araştırmacı, başlık-özet ve tam metin taraması, uyuşmazlık çözümü, Rayyan / Covidence gibi araçlar.
5. **PRISMA 2020:** 27 maddelik kontrol listesi ve akış şeması (tanımlama, tarama, dahil etme aşamaları). Akış şemasının kutularını ve sırasını tam yaz; slaytta çizilecek. (Page ve ark., 2021; doğrula.) PRISMA'nın spor bilimine uyarlanmış eki varsa (PERSiST, Ardern ve ark., 2022; doğrula) ekle; bu, sunumun spor alanına bağlanması için değerli.
6. **Veri çıkarımı ve yanlılık riski:** RoB 2 (randomize), ROBINS-I (randomize olmayan), PEDro ölçeği (spor ve fizyoterapide yaygın; doğrula).
7. **Kanıtın kesinliği ve derlemenin kalitesi:** GRADE (yüksek, orta, düşük, çok düşük), AMSTAR 2 (bir sistematik derlemenin kalitesini değerlendirme).

**Sınır:** derleme türlerinin tanımı ve etik iş s1'in; meta-analiz istatistiği iş s3'ün; gerçek spor örnek çalışmaları iş s4'ün (yalnız PERSiST burada).

## Arama için başlangıç anahtar kelimeleri

PRISMA 2020 statement Page, PRISMA-P 2015, PROSPERO registration systematic review, PERSiST sport exercise medicine PRISMA, Cochrane Handbook searching for studies, Google Scholar systematic review suitability Gusenbauer, RoB 2 Sterne 2019, ROBINS-I, PEDro scale reliability, GRADE Guyatt 2008, AMSTAR 2 Shea 2017, Rayyan systematic review

## Kaynak hedefi

En az **10** doğrulanmış bilimsel kaynak (kılavuz bildirgeleri ve yöntem makaleleri bu iş için temel kaynaktır, sayılır). En az 4'ü 2018-2026 arası. En az 1 Türkçe hakemli kaynak (ör. sistematik derleme nasıl yapılır üzerine Türk dergisinde makale) hedefle; bulunamazsa yaz.

## Girdisi

Web ve bilimsel veri tabanları. Repodaki başka dosyalar girdi değil.

## Çıktısı ve nereye yazacak

Tek dosya: `isler/s2-sistematik-surec/SONUC.md`. Bu dosyayı dalga 2'deki sunum içeriği işi okuyacak.

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

- YALNIZ kendi klasörüne yaz: `isler/s2-sistematik-surec/`. Başka hiçbir yere dosya yazma, başka işlerin klasörlerini okuma.
- Tek dosya üret: `isler/s2-sistematik-surec/SONUC.md`. Commit ya da push YAPMA.

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
