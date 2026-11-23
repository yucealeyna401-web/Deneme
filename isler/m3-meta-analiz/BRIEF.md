# BRIEF · m3-meta-analiz · Meta-analiz istatistiği

> Plan: `plan/2026-11-23-plan.md` · Dalga 1 (m1, m2, m3, m4 paralel) · Çıktı: `isler/m3-meta-analiz/SONUC.md` · Bu klasör dışına yazma.

## Görev

Sunumun slayt 7 (meta-analiz: tanım ve SR ile ilişkisi), slayt 8 (temel istatistik) ve slayt 9 (forest ve funnel plot, yayın yanlılığı) için içerik ve doğrulanmış kaynak üret. **Her kavram için iki şey yaz: (a) ne demek, sade Türkçeyle; (b) sonuçların yorumunda neden önemli.** Formül yalnız gerekiyorsa ve kısa.

### Başlıklar
1. Tanım (Cochrane El Kitabı bölüm 10 ve Borenstein ve ark., 2021); Glass (1976) terimin kökeni (doğrula).
2. SR ile ilişkisi: meta-analiz bir SR'nin istatistiksel sentez adımı olabilir; her SR'de gerekmez; SR olmadan yapılan meta-analizin sorunu (tuzak 2). Ne zaman uygun: benzer PICO, karşılaştırılabilir sonuç ölçümü, yeterli veri; ne zaman uygun değil (klinik/yöntemsel heterojenlik, "elma ile armut").
3. Etki büyüklüğü (ES): neden p değeri yetmez; standartlaştırılmış ortalama farkı. Cohen's d, Hedges' g (küçük örneklem düzeltmesi, tuzak 5), Cohen'in 0,2/0,5/0,8 gelenekleri ve sınırı; spor biliminde Hopkins ve ark. (2009) eşikleri (doğrula, isteğe bağlı). Oran türü ölçütler (OR, RR) tek cümle.
4. %95 güven aralığı ve ağırlıklandırma (ters varyans).
5. Sabit etkiler ve rastgele etkiler: varsayım farkı (tek gerçek etki vs etki dağılımı), ağırlıklara etkisi, seçimin teste göre değil varsayıma göre yapılması (tuzak 3). Kaynak: Borenstein ve ark. (2010) "A basic introduction to fixed-effect and random-effects models" (Res Synth Methods), El Kitabı bölüm 10.
6. Heterojenlik: Cochran Q, τ², I² (Higgins ve Thompson, 2002; Higgins ve ark., 2003, BMJ), I²'nin oran olduğu ve çalışma sayısı ile kesinliğe duyarlılığı (Borenstein ve ark., 2017 "Basics of meta-analysis: I² is not an absolute measure of heterogeneity"), El Kitabı'ndaki örtüşen yorum aralıkları (birebir alıntıyla doğrula), tahmin aralığı (IntHout ve ark., 2016). Alt grup analizi ve meta-regresyon bir cümle.
7. Forest plot: satırlar, kare boyutu (ağırlık), yatay çizgi (GA), elmas (özet etki ve GA), dikey sıfır etki çizgisi, tahmin aralığı. **Eğitim amaçlı kurgu veri** üret: 6 çalışma (ad: Çalışma A ile F), her biri için n, Hedges' g, %95 GA, ağırlık (%); rastgele etkiler özetini gerçekten hesapla (Python ile DerSimonian-Laird; kodu ve sonucu SONUC.md'ye koy) ve Q, τ², I² değerlerini yaz. Değerler gerçekçi ve tutarlı olsun (m7 bu veriyle çizecek).
8. Funnel plot: eksenler, simetri beklentisi, asimetrinin nedenleri (yayın yanlılığı, küçük çalışma etkileri, heterojenlik, şans; Sterne ve ark., 2011 BMJ "Recommendations for examining and interpreting funnel plot asymmetry"); Egger testi (Egger ve ark., 1997), trim-and-fill (Duval ve Tweedie, 2000) ve sınırları; test için en az çalışma sayısı önerisini (genellikle 10) **yalnız birebir kaynakla** doğrularsan yaz (tuzak 6). Kurgu funnel plot için 12 ile 15 noktalık hafif asimetrik veri üret (g ve SE), "kurgu" diye işaretle.
9. Güçlü ve sınırlı yönler (kesinlik artışı, tutarlılığı sınama; çöp girer çöp çıkar, yayın yanlılığı, heterojenlik, ekolojik yanılgı).
10. Türkçe kaynak adayları: Üstün ve Eryılmaz (2014) Eğitim ve Bilim; Dinçer'in meta-analiz kitabı ya da makaleleri; DergiPark'ta meta-analiz yöntemini anlatan Türkçe hakemli makaleler.

## Ortak kurallar (bütün çalışanlar)

- **Önce oku:** `sen/kaynak/2026-11-23-sunum-gorevi.md` (görev metni) ve `plan/2026-11-23-plan.md` (özellikle "Bilimsel doğruluk tuzakları" listesi ve Bölüm G).
- **Yalnız kendi klasörüne yaz:** `isler/m3-meta-analiz/`. Başka hiçbir dosyaya yazma, git commit yapma.
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
