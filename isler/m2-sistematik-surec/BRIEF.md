# BRIEF · m2-sistematik-surec · Sistematik derleme süreci

> Plan: `plan/2026-11-23-plan.md` · Dalga 1 (m1, m2, m3, m4 paralel) · Çıktı: `isler/m2-sistematik-surec/SONUC.md` · Bu klasör dışına yazma.

## Görev

Sunumun slayt 4 (tanım ve özellikler), slayt 5 (süreç ve PRISMA 2020) ve slayt 6 (arama, seçim, yanlılık riski) için içerik ve doğrulanmış kaynak üret.

### Başlıklar
1. Tanım (Cochrane El Kitabı bölüm 1 tanımını birebir alıntıyla), amaçlar, anlatı derlemesinden farkı.
2. Araştırma sorusu: PICO ve PICOS (S = study design); kısaca SPIDER ya da PEO alternatifleri. Spor bilimine uygun **kurgu** bir PICOS örneği yaz ve "kurgu örnek" diye işaretle.
3. Protokolün önceden yazılması (PRISMA-P) ve kayıt (PROSPERO; ayrıntıyı m1 etik tarafında da yapıyor, burada süreç adımı olarak bir cümle yeter).
4. Literatür taraması: PubMed (MEDLINE, MeSH, ücretsiz), Scopus ve Web of Science (abonelikli, atıf dizinleri), SPORTDiscus (EBSCO, spor bilimleri, abonelikli), ERIC (eğitim, ücretsiz). Her birinin kapsamı ve neden spor/beden eğitimi derlemesinde birlikte kullanıldığı; gri literatür; tek tabanın yetmediği (kaynak: Cochrane El Kitabı arama bölümü, Lefebvre ve ark.; Bramer ve ark., 2017 "Optimal database combinations" gibi). Tabanların kapsamını resmi sayfalarından doğrula, sayı veriyorsan tarihini yaz.
5. Boolean operatörleri (AND, OR, NOT), kesme işareti (*), tırnak, alan etiketleri, MeSH; **kurgu** bir spor arama dizesi (ör. "plyometric training" AND adolescents) yaz ve "kurgu" diye işaretle. PRISMA-S (Rethlefsen ve ark., 2021) arama raporlama uzantısı.
6. Dahil etme ve dışlama kriterleri (PICOS'a bağlı, önceden tanımlı); iki bağımsız değerlendiricinin başlık/özet ve tam metin elemesi, anlaşmazlık çözümü (El Kitabı bölümleri).
7. **PRISMA 2020** (Page ve ark., 2021): 27 maddelik kontrol listesi, özet kontrol listesi, akış şeması (tanımlama, eleme, dahil etme). **Bir raporlama kılavuzu olduğunu, yöntem ya da kalite aracı olmadığını** makaleden birebir alıntıyla doğrula (tuzak 1). Akış şemasının kutu metinlerini (İngilizce ve Türkçe karşılığı) ver ki m7 çizebilsin. Page ve ark. (2021) açıklama makalesi (BMJ n160) da varsa doğrula.
8. Veri çıkarma (önceden pilotlanmış form, iki kişi), sentez: meta-analiz mümkün değilse yapılandırılmış anlatısal sentez ve SWiM (Campbell ve ark., 2020).
9. Yanlılık riski ve metodolojik kalite: RoB 2 (Sterne ve ark., 2019), ROBINS-I (Sterne ve ark., 2016), gerekirse PEDro ölçeği (spor ve fizyoterapide yaygın; doğrula); "kalite" ile "yanlılık riski" ayrımı; kanıt kesinliği için GRADE (Guyatt ve ark., 2008 ya da El Kitabı bölüm 14). Derlemenin kendi kalitesi için AMSTAR 2 (Shea ve ark., 2017) bir cümle.
10. Güçlü ve sınırlı yönler (kaynaklı).
11. Türkçe kaynak adayları: Karaçam (2013) sistematik derleme metodolojisi; DergiPark'ta sistematik derleme/PRISMA anlatan Türkçe makaleler (ör. PRISMA 2020'nin Türkçe çevirisi yayımlanmışsa doğrula).

## Ortak kurallar (bütün çalışanlar)

- **Önce oku:** `sen/kaynak/2026-11-23-sunum-gorevi.md` (görev metni) ve `plan/2026-11-23-plan.md` (özellikle "Bilimsel doğruluk tuzakları" listesi ve Bölüm G).
- **Yalnız kendi klasörüne yaz:** `isler/m2-sistematik-surec/`. Başka hiçbir dosyaya yazma, git commit yapma.
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
