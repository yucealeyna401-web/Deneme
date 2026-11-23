# BRIEF · m1-derleme-etik · Derleme türleri ve etik

> Plan: `plan/2026-11-23-plan.md` · Dalga 1 (m1, m2, m3, m4 paralel) · Çıktı: `isler/m1-derleme-etik/SONUC.md` · Bu klasör dışına yazma.

## Görev

Sunumun "Derleme" (slayt 3) ve "Etik boyut" (slayt 12) slaytları ile "Hangi durumda hangi yöntem" (slayt 13) için kavramsal temel ve doğrulanmış kaynak üret.

### A. Anlatı (geleneksel) derlemesi
- Tanım ve bilimsel araştırmadaki amacı; temel özellikleri.
- Nasıl hazırlanır; literatür taraması ve kaynak seçimi nasıl yapılır (yazarın uzmanlığına dayalı, açık olmayan seçim).
- Güçlü yönler (kuram, geniş bakış, yeni alan, yorum) ve zayıf yönler (seçim yanlılığı, tekrarlanamazlık). Tuzak 7'ye uy: "kötü yöntem" diye sunma.
- Kalite değerlendirme aracı: SANRA (Baethge ve ark., 2019) doğrula.
- Sistematik derlemeden temel metodolojik ayrım (tek cümle, kaynaklı).
- Aday kaynaklar (doğrula, uygun değilse bırak): Baumeister ve Leary (1997); Green, Johnson ve Adams (2006); Grant ve Booth (2009) "A typology of reviews"; Ferrari (2015) "Writing narrative style literature reviews"; Sukhera (2022) "Narrative reviews: flexible, rigorous, and practical"; Gregory ve Denniss (2018).

### B. Diğer derleme türleri (kısa ayrım tablosu)
- Scoping review: amaç kanıtı haritalamak; JBI yöntemi (Peters ve ark.), PRISMA-ScR (Tricco ve ark., 2018); Munn ve ark. (2018) "systematic review or scoping review?".
- Integrative review: Whittemore ve Knafl (2005).
- Umbrella review: Aromataris ve ark. (2015); JBI Manual bölümü.
- (İsteğe bağlı tek satır) rapid review: Garritty ve ark. (2021) Cochrane Rapid Reviews.
- Tablo sütunları: amaç · soru türü · arama · yanlılık riski değerlendirmesi · sentez · raporlama kılavuzu.

### C. Etik (görevin E bölümü, 10 başlık)
İntihal ve aşırmacılık · kaynak gösterme · seçici raporlama (sonuç raporlama yanlılığı) · yayın yanlılığı · araştırmacı yanlılığı · çıkar çatışması · protokolün önceden oluşturulması (PRISMA-P: Moher ve ark., 2015 / Shamseer ve ark., 2015) · PROSPERO kaydı (kapsamını crd.york.ac.uk'dan doğrula; tuzak 9) · PRISMA'ya uygun raporlama · veri şeffaflığı (veri, kod, analiz paylaşımı; PRISMA 2020 madde 27 gibi).
- **Etik kurul izni (tuzak 10):** yayımlanmış toplulaştırılmış verinin ikincil analizi ile insan katılımcıdan yeni veri toplanması ya da bireysel katılımcı verisi (IPD) kullanımı arasındaki farkı kaynakla açıkla; kurum ve dergi politikalarının belirleyici olduğunu yaz. Kaynak adayları: COPE yönergeleri, ICMJE önerileri, Cochrane El Kitabı ilgili bölüm, Vergnes ve ark. (2010) "Ethics in systematic reviews" (J Med Ethics), Weingarten ve ark. (2004), Türkiye için YÖK Bilimsel Araştırma ve Yayın Etiği Yönergesi (yayın etiği ihlallerinin tanımları; resmi metinden doğrula).
- Türkçe kaynak adayları: Ata ve Urman (2008) ve DergiPark'ta yayın etiği/intihal üzerine hakemli makaleler; anlatı ve sistematik derleme ayrımını anlatan Türkçe makaleler.

### D. Karar desteği
"Hangi araştırma sorusunda hangi yöntem" için kaynaklı kısa karar kuralları (ör. Munn ve ark., 2018'in scoping ve sistematik ayrımı; Grant ve Booth, 2009).

## Ortak kurallar (bütün çalışanlar)

- **Önce oku:** `sen/kaynak/2026-11-23-sunum-gorevi.md` (görev metni) ve `plan/2026-11-23-plan.md` (özellikle "Bilimsel doğruluk tuzakları" listesi ve Bölüm G).
- **Yalnız kendi klasörüne yaz:** `isler/m1-derleme-etik/`. Başka hiçbir dosyaya yazma, git commit yapma.
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
