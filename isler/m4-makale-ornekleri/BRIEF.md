# BRIEF · m4-makale-ornekleri · Gerçek makale örnekleri

> Plan: `plan/2026-11-23-plan.md` · Dalga 1 (m1, m2, m3, m4 paralel) · Çıktı: `isler/m4-makale-ornekleri/SONUC.md` · Bu klasör dışına yazma.

## Görev

Sunumun slayt 11 (gerçek makale örnekleri) ve gerektiğinde slayt 3, 5, 9 için beden eğitimi ve spor bilimlerinden **gerçek** örnek makaleler bul, **yöntem bölümünü okuyarak** sınıflandır.

### Hedef
- Her yöntem için 2 aday: **anlatı derlemesi ×2, meta-analizsiz sistematik derleme ×2, meta-analiz (sistematik derleme içinde) ×2**. Toplam 6.
- **Tercih: aynı konuda üçlü** (bir anlatı derlemesi, bir sistematik derleme, bir meta-analiz), ör. fiziksel aktivite/beden eğitimi ve akademik başarı ya da bilişsel işlev; sakatlık önleme egzersiz programları; çocuk ve ergenlerde kuvvet/pliometrik antrenman. Üçlü bulursan ayrıca belirt; dinleyiciye "aynı soru, üç yöntem" farkını göstermek için ideal.
- **Türkçe ya da Türkiye kaynaklı en az 1 örnek** (Bölüm G): DergiPark/TR Dizin'de yayımlanmış bir sistematik derleme ya da meta-analiz, ya da Türkiye'den yazarların uluslararası dergideki çalışması. Yöntem bölümünü aynı titizlikle kontrol et.
- Öncelik açık erişim (PMC, BMC, Frontiers, MDPI, Sports Medicine Open, DergiPark) çünkü yöntem bölümü okunabilmeli. Tam metni Europe PMC fullTextXML ya da PMC sayfasından oku.

### Başlangıç listesi (önceki koşu, yeniden doğrula)
`isler/s4-spor-ornekleri/SONUC.md` (Lauersen ve ark. 2014; Thorborg ve ark. 2017; Sadigursky ve ark. 2017; Álvarez-Bueno ve ark. 2017; Aygun ve ark. 2024; Böke 2020; Plakias 2025 vb.). Akademik başarı üçlüsü için aday fikirler (yalnız fikir, hepsini doğrula ya da ele): Hillman, Erickson ve Kramer (2008) Nature Reviews Neuroscience (anlatı derlemesi?), Donnelly ve ark. (2016) Medicine and Science in Sports and Exercise (sistematik derleme, meta-analiz yok?), Álvarez-Bueno ve ark. (2017) Pediatrics (meta-analiz?). Sınıflandırmayı yöntem metnine göre yap; tahminim yanlışsa düzelt.

### Sınıflandırma ölçütü (yöntem metninde ara)
- **Sistematik derleme:** önceden tanımlı soru/kriterler, birden çok tabanda raporlanmış arama (taban adları, tarih, arama dizesi), açık seçim süreci (çoğunlukla PRISMA akışı), genellikle yanlılık riski/kalite değerlendirmesi. Meta-analiz yoksa "meta-analizsiz SR" ve sentez türünü yaz.
- **Meta-analiz:** yukarıdakine ek olarak etki büyüklüklerinin istatistiksel birleştirilmesi (model, yazılım, heterojenlik istatistiği).
- **Anlatı derlemesi:** arama ve seçim yöntemi raporlanmamış ya da yalnız genel ifade. Başlıkta "systematic" geçip yöntemi sistematik olmayanları ve "review" deyip aslında SR olanları ayrıca işaretle.

### Her makale kartı
Tam başlık · bütün yazarlar (APA 7 için) · yıl · dergi · cilt(sayı) · sayfa/makale no · DOI (Crossref ile eşleştir) · açık erişim mi · amaç (1 cümle) · yöntem (taban adları, tarih aralığı, dahil edilen çalışma sayısı, RoB aracı, sentez/model; hepsi yöntem metninden) · **neden bu sınıfta** (yöntem metninden 1 ile 2 kısa İngilizce alıntı) · ana bulgu (1 cümle, yalnız okunan metinden) · kanıt düzeyi · konu üçlüsüne ait mi.

### Sonda
"Önerilen sunum seçimi": slayt 11'e girecek 3 makale (her yönteme 1, mümkünse aynı konu) + gerekirse forest plot slaytında gönderme yapılabilecek 1 meta-analiz; gerekçesiyle.

## Ortak kurallar (bütün çalışanlar)

- **Önce oku:** `sen/kaynak/2026-11-23-sunum-gorevi.md` (görev metni) ve `plan/2026-11-23-plan.md` (özellikle "Bilimsel doğruluk tuzakları" listesi ve Bölüm G).
- **Yalnız kendi klasörüne yaz:** `isler/m4-makale-ornekleri/`. Başka hiçbir dosyaya yazma, git commit yapma.
- **Erişim (açık):** kabuktan `curl` ile şu adresler çalışıyor: `api.crossref.org` (künye/DOI: `https://api.crossref.org/works/<DOI>`), Europe PMC (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&resultType=core` ve açık erişim tam metin `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`), PubMed E-utilities (`eutils.ncbi.nlm.nih.gov`), `pmc.ncbi.nlm.nih.gov`, `doi.org`, `dergipark.org.tr`, `search.trdizin.gov.tr`, `training.cochrane.org`, `jbi-global-wiki.refined.site`, `www.prisma-statement.org`, `www.crd.york.ac.uk` (PROSPERO), `api.openalex.org`. Ayrıca web araması (WebSearch aracı; ToolSearch ile `select:WebSearch` yükle) ve web-fetch kullanılabilir. Başka alan adları engelli olabilir; engellenirse not et, uydurma.
- **Uydurma yasak:** yazar, başlık, dergi, yıl, cilt, sayfa, DOI ya da bulgu uydurulmaz. Her künye Crossref (ya da PubMed/DergiPark kaydı) ile eşleştirilir. Her kaynak için **kanıt düzeyi** yaz: `tam metin okundu` / `özet okundu` / `yalnız künye doğrulandı`. Yöntem ve bulgu iddiası yalnız okunan metne dayanır.
- **Her iddia kaynaklı:** SONUC.md'deki her önemli iddianın yanında (Yazar, yıl) ve mümkünse bölüm/sayfa. Doğrudan alıntı yapılan yerde kaynak cümlesini İngilizce olarak tırnak içinde ver (denetim için).
- **Türkçe kaynak:** Bölüm G gereği yöntemle ilgili en az 2 Türkçe hakemli kaynak (TR Dizin/DergiPark) bul ve doğrula (m4 için: Türkçe ya da Türkiye kaynaklı örnek çalışma ara).
- **Kesinti dersi:** her bölümü bitirince SONUC.md'ye hemen yaz (dosyayı parça parça büyüt); iş kesilirse yapılan kaybolmasın.
- **Em dash (uzun tire) ve en dash hiçbir yerde yok.** Ayraç: nokta, virgül, iki nokta, orta nokta (·).
- **Temel kaynakların tercih edilen biçimi (çelişki olmasın):** PRISMA 2020 = Page ve ark. (2021), BMJ, 372, n71, https://doi.org/10.1136/bmj.n71 · Cochrane El Kitabı = güncel çevrimiçi sürüm (sürüm numarası ve yılı training.cochrane.org'dan doğrula; bölüm yazarlarıyla bölüm olarak atıf tercih edilir) · JBI Manual for Evidence Synthesis = güncel sürüm (editör listesi, yıl ve DOI'yi JBI sitesinden doğrula) · Borenstein ve ark. (2021) Introduction to Meta-Analysis, 2. baskı, Wiley.

## SONUC.md yapısı

1. Hedef durumu (kaç kaynak, kaçı Türkçe, kanıt düzeylerinin dağılımı)
2. Erişim notu (hangi tabanlar çalıştı, hangileri engellendi)
3. İçerik (aşağıdaki başlıklar; her madde kısa, kaynaklı; her kavram için "ne demek" ve "yorumda/araştırmada neden önemli")
4. Sunuma önerilen çekirdek (slayt metnine girecek 5 ile 8 kısa ifade + sunucu notu malzemesi)
5. Kaynak tablosu: Kısa ad · tam APA 7 künye · DOI · doğrulama yolu (Crossref/PubMed/DergiPark/yayıncı) · kanıt düzeyi · Türkçe mi
6. Doğrulanamayanlar ve sınırlar (neyi doğrulayamadın, nereye bakılmalı)
7. Zaman (başlangıç ve bitiş saati)

## Bitince döndür

Kısa özet: kaç doğrulanmış kaynak (kaçı Türkçe), kanıt düzeyi dağılımı, doğrulanamayanlar, sunum için en kritik 3 bulgu.
