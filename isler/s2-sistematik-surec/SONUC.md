# SONUC · s2 · Sistematik derlemenin adımları

## 1. Hedef durumu

- **Doğrulanmış bilimsel kaynak sayısı: 20** (hedef en az 10), ayrıca 1 kurumsal web sayfası (Cochrane Community, Covidence). **Hedef tuttu.**
- 2018-2026 arası: 9 kaynak (Ardern ve ark., 2022; Cashin ve McAuley, 2020; Gusenbauer ve Haddaway, 2020; Higgins ve Thomas, 2019; Lefebvre ve ark., 2019; Page ve ark., 2018; Page ve ark., 2021; Pieper ve Rombey, 2022; Sterne ve ark., 2019). Hedef (en az 4) tuttu.
- Türkçe hakemli kaynak: 1 (Karaçam, 2013, TR Dizin kaydı bulundu). Hedef tuttu.
- Önemli sınır: birçok kaynakta yalnız ilk yazar ve künye doğrulanabildi; tam yazar listesi aramada görünmedi. Bu kaynaklar kaynakçada "ve ark. (tam liste DOI sayfasından tamamlanmalı)" diye işaretli. Bkz. bölüm 7.

## 2. Veri tabanı erişimi

| Taban | Durum | Not |
|---|---|---|
| PubMed / PMC | Doğrudan erişilemedi (curl ve WebFetch DNS hatası) | Kayıtlar WebSearch sonuçlarında PubMed/PMC sayfası olarak göründü; PMID/PMC numaraları tabloda |
| SPORTDiscus (EBSCO) | Erişilemedi | Abonelik ve ağ; curl yanıt vermedi |
| Web of Science | Erişilemedi | Abonelik ve ağ |
| Google Akademik | Doğrudan erişilemedi | Yalnız WebSearch üzerinden dolaylı |
| YÖK Ulusal Tez Merkezi | Erişilemedi | curl yanıt vermedi; tez taraması yapılamadı |
| TR Dizin | Doğrudan erişilemedi (WebFetch DNS hatası) | Kayıt WebSearch sonucunda göründü (Karaçam, 2013) |
| Asıl kanal | WebSearch | Tüm künyeler bu oturumda WebSearch ile eşleştirildi |

## 3. İçerik

### 3.1 Araştırma sorusu: PICO, PICOS, SPIDER

- Sistematik derleme, belirli bir soruya yönelik olarak benzer yöntemlerle yapılmış çok sayıda araştırmanın yapılandırılmış ve kapsamlı sentezidir; ilk adım işin (sorunun) tanımlanmasıdır (Karaçam, 2013).
- Nicel müdahale soruları için PICO kullanılır: **P** (popülasyon/katılımcı), **I** (müdahale), **C** (karşılaştırma), **O** (sonuç/çıktı). PICOS, buna **S** (çalışma deseni) ekler. PICO nicel sorulara göre kurulduğu için nitel ve karma yöntem sorularında zayıf kalır; bunun için SPIDER önerilmiştir: **S**ample (örneklem), **PI** phenomenon of interest (ilgilenilen olgu), **D**esign (desen), **E**valuation (değerlendirme), **R**esearch type (araştırma türü) (Cooke ve ark., 2012). Yazarlar SPIDER'ın PICO'nun yerini tam alabilmesi için daha fazla sınanması gerektiğini belirtir (Cooke ve ark., 2012).
- **Örnek soru (ÖRNEK KURGU, gerçek bir çalışma değildir):** "Genç futbolcularda (P: 13-18 yaş, lisanslı futbolcular) nöromüsküler ısınma programı (I), olağan ısınmaya göre (C), alt ekstremite sakatlık sıklığını (O) azaltır mı? (S: randomize kontrollü ve küme randomize çalışmalar)"
- **Nitel örnek (ÖRNEK KURGU):** S: elit kadın sporcular · PI: sakatlık sonrası spora dönüş deneyimi · D: yarı yapılandırılmış görüşme · E: algılar, engeller · R: nitel çalışmalar.

Slayta öneri: Dört renkli PICO(S) tablosu, her harfin yanında futbol örneğinin karşılığı; altında tek satırda "nitel sorular için SPIDER".

### 3.2 Protokol ve kayıt: PRISMA-P, PROSPERO, OSF

- Protokol, derleme başlamadan yöntemin yazıya dökülmesidir. PRISMA-P 2015, bir sistematik derleme protokolünü hazırlamak ve raporlamak için **17 maddelik** bir kontrol listesi sunar (Moher ve ark., 2015).
- **PROSPERO**, York Üniversitesi Centre for Reviews and Dissemination tarafından Şubat 2011'de kurulan, sağlıkla ilgili sonuçları olan sistematik derlemeler için uluslararası ileriye dönük kayıt sistemidir; amaçları planlanmamış tekrarları (aynı derlemenin birden çok yapılmasını) azaltmak ve şeffaflığı artırmaktır (Booth ve ark., 2012). Kayıt ideal olarak tarama başlamadan yapılır; veri çıkarımı tamamlanmadıysa derleme hâlâ kayıt için uygundur (Booth ve ark., 2012). Kayıt formları kapsam ve açıklık açısından kontrol edilir (Booth ve ark., 2012).
- Büyüme: 10 Ekim 2017 itibarıyla PROSPERO'da 26.535 kayıtlı derleme vardı; aylık kayıt 2012'deki 63'ten 2017'de 800'e çıktı (Page ve ark., 2018).
- **Alternatifler:** Pieper ve Rombey (2022) beş seçenek belirlemiştir: derlemeye özgü PROSPERO, Research Registry (Registry of Systematic Reviews/Meta-Analyses) ve INPLASY ile her çalışma türünü kabul eden genel kayıtlar OSF Registries ve protocols.io. PROSPERO en yaygın olanıdır, ancak yoğunluk işlem süresini uzatabilir (Pieper ve Rombey, 2022). PROSPERO yalnız sağlıkla ilgili sonuçları olan derlemeleri kabul ettiği için (Booth ve ark., 2012), sağlık dışı spor bilimi soruları (ör. performans, pedagoji) OSF gibi genel kayıtlara yönelebilir.
- **Neden önceden kayıt:** tekrarı önlemek ve yöntemi sonuçları görmeden sabitleyerek şeffaflık sağlamak (Booth ve ark., 2012). AMSTAR 2'de önceden belirlenmiş protokol kritik maddelerden biridir (Shea ve ark., 2017).

Slayta öneri: Soldan sağa üç kutu: "Protokolü yaz (PRISMA-P, 17 madde) → Kaydet (PROSPERO / OSF) → Sonra ara"; altında tek cümle: "Kayıt, kale direklerini maçtan önce dikmektir."

### 3.3 Arama stratejisi

- **Veri tabanları:** Tek veri tabanı yetmez. Bramer ve ark. (2017), 58 yayımlanmış sistematik derlemede ilgili referansların %16'sının (291 makale) yalnız tek bir veri tabanında bulunduğunu gösterdi. En iyi kombinasyon Embase, MEDLINE, Web of Science Core Collection ve Google Scholar idi ve toplam %98,3 duyarlılığa (recall) ulaştı (Bramer ve ark., 2017). Spor alanında bunlara SPORTDiscus eklenmesi yaygındır; bu cümle için bu oturumda ayrı bir kaynak doğrulanmadı (bkz. bölüm 7).
- **Google Akademik'in rolü ve sınırları:** Gusenbauer ve Haddaway (2020), Google Scholar, PubMed ve Web of Science dahil 28 akademik arama sistemini Boolean aramalarda duyarlılık, kesinlik ve tekrarlanabilirlik açısından sınadı; yalnız 14'ü ana arama sistemi olarak uygun bulundu ve Google Scholar'ın **ana arama sistemi olarak uygun olmadığı** sonucuna varıldı. Bramer ve ark. (2017) ise Google Scholar'ı tek başına değil, diğer tabanlara **ek** olarak yararlı buldu. Mesaj: Google Akademik tamamlayıcıdır, tek başına yeterli değildir.
- **Boolean operatörler ve kontrollü sözcükler:** Eş anlamlılar OR ile birleştirilir (geniş kümeler), PICO öğeleri AND ile kesiştirilir (daraltma), NOT dikkatle ve az kullanılır çünkü ilgili kayıtları da atabilir. MEDLINE/PubMed'de MeSH (kontrollü konu başlıkları) serbest metin sözcükleriyle birlikte kullanılır. Arama stratejisi tasarımı Cochrane El Kitabı'nın 4. bölümünde ve teknik ekinde ayrıntılı anlatılır (Lefebvre ve ark., 2019; Higgins ve Thomas, 2019).
  - Örnek dizgi (ÖRNEK KURGU): `(soccer OR football) AND (adolescent* OR youth) AND ("warm-up" OR "neuromuscular training" OR "FIFA 11+") AND (injur*)`
- **Gri literatür ve el ile tarama:** Cochrane El Kitabı'nın 4. bölüm teknik eki; klinik deney kayıtlarını (ClinicalTrials.gov, WHO ICTRP), kongre özetlerini ve bildirileri, diğer derlemeleri, kılavuzları ve kaynakça listelerini, genel web aramasını (Google Scholar dahil) ek kaynak olarak ele alır (Lefebvre ve ark., 2019). PRISMA 2020 akış şeması da "diğer yöntemlerle tanımlanan çalışmalar" için ayrı bir sütun içerir (Page ve ark., 2021).
- **Türkiye bağlamı:** YÖK Ulusal Tez Merkezi (YÖKTEZ) yayımlanmamış lisansüstü tezler için temel gri literatür kaynağıdır; TR Dizin, TÜBİTAK ULAKBİM tarafından yürütülen ulusal dergi atıf dizinidir. Türkçe yayımlanmış birçok sistematik derleme ve meta-analiz YÖKTEZ ve TR Dizin'i Türkçe ve İngilizce anahtar sözcüklerle taramıştır. Bu paragraf için hakemli bir yöntem kaynağı bu oturumda doğrulanamadı; yalnız örnek derlemeler ve dizin tanıtım sayfaları görüldü (bkz. bölüm 7). Sunumda "uygulamada" ifadesiyle verilmesi önerilir.

Slayta öneri: Solda veri tabanı listesi (PubMed/MEDLINE, SPORTDiscus, Web of Science, Scopus, + YÖKTEZ, TR Dizin), sağda "Google Akademik: ek kaynak, ana kaynak değil" uyarı kutusu ve Bramer'in "%16 tek tabanda" verisi.

### 3.4 Tarama ve seçim

- Seçim, önceden belirlenen dahil etme ve dışlama ölçütlerine göre iki aşamada yapılır: önce başlık-özet, sonra tam metin (Karaçam, 2013; Lefebvre ve ark., 2019).
- **İki bağımsız araştırmacı:** Her kaydı iki kişi birbirinden habersiz değerlendirir; uyuşmazlıklar tartışmayla ya da üçüncü bir araştırmacıyla çözülür. Bu ilke Cochrane yöntemlerinin parçasıdır (Higgins ve Thomas, 2019). Benzer bir çift değerlendirici ve üçüncü hakem düzeni PEDro güvenirlik çalışmasında da kullanılmıştır (Maher ve ark., 2003).
- **Ölçüt örneği (ÖRNEK KURGU):** Dahil: 13-18 yaş futbolcu, yapılandırılmış nöromüsküler ısınma, kontrol grubu, sakatlık sonucu, RKÇ. Dışla: yetişkin, laboratuvar sonuçları (ör. sıçrama yüksekliği) ama sakatlık yok, vaka raporu.
- **Araçlar:** Rayyan, başlık ve özet taramasını yarı otomasyonla hızlandıran ücretsiz web ve mobil uygulamadır; kullanıcı anketinde ortalama %40 zaman tasarrufu bildirilmiştir (Ouzzani ve ark., 2016). Covidence, Cochrane tarafından standart müdahale derlemeleri için birincil tarama ve veri çıkarım aracı olarak tanınır (Cochrane Community sayfası; hakemli kaynak değil, bkz. bölüm 7).

Slayta öneri: Huni görseli: "Başlık-özet → Tam metin → Dahil", yanında iki insan simgesi ve "uyuşmazlıkta 3. kişi"; altta Rayyan ve Covidence logosuz isim olarak.

### 3.5 PRISMA 2020: kontrol listesi ve akış şeması

- PRISMA 2020, 2009 bildirgesinin yerini alan güncel raporlama kılavuzudur; **27 maddelik kontrol listesi**, genişletilmiş kontrol listesi, özet kontrol listesi ve yeni ve güncellenen derlemeler için akış şemaları içerir (Page ve ark., 2021). Türkçe kontrol listesi PRISMA sitesinde yayımlanmıştır (aramada görüldü).
- **Akış şeması (yeni derleme, veri tabanları ve kayıtlar sütunu), kutular sırasıyla** (Page ve ark., 2021; şablon kopyaları aramada doğrulandı):

  **TANIMLAMA (Identification)**
  1. Tanımlanan kayıtlar: veri tabanları (n = ), kayıtlar/registers (n = ) · mümkünse her veri tabanı ayrı yazılır.
  2. (Yan kutu) Taramadan önce çıkarılan kayıtlar: yinelenen kayıtlar (n = ), otomasyon araçlarıyla uygun değil işaretlenenler (n = ), diğer nedenlerle çıkarılanlar (n = ).

  **TARAMA (Screening)**
  3. Taranan kayıtlar (n = ) → (yan kutu) Dışlanan kayıtlar (n = ).
  4. Erişilmeye çalışılan raporlar (n = ) → (yan kutu) Erişilemeyen raporlar (n = ).
  5. Uygunluk açısından değerlendirilen raporlar (n = ) → (yan kutu) Dışlanan raporlar, nedenleriyle (Neden 1 n = , Neden 2 n = ...).

  **DAHİL ETME (Included)**
  6. Derlemeye dahil edilen çalışmalar (n = ) ve dahil edilen çalışmaların raporları (n = ).

  İsteğe bağlı ikinci sütun: **diğer yöntemlerle tanımlama** (web siteleri, kuruluşlar, atıf taraması vb.) kendi "erişilmeye çalışılan / erişilemeyen / değerlendirilen / dışlanan raporlar" kutularıyla aynı dahil etme kutusuna bağlanır. Güncellenen derlemeler için "önceki sürüme dahil edilen çalışmalar" kutusu eklenir.
- **Çalışma mı, rapor mu?** Bir çalışma birden çok yayında raporlanabilir; bu yüzden PRISMA 2020 "dahil edilen çalışmalar" ile "dahil edilen çalışmaların raporları"nı ayırır (Page ve ark., 2021).
- **Spor bilimine uyarlama, PERSiST:** Ardern ve ark. (2022), PRISMA 2020'nin 27 maddesinin spor ve egzersiz hekimliği, kas-iskelet rehabilitasyonu ve spor bilimlerinde nasıl uygulanacağını gösteren uygulama kılavuzunu (PERSiST) *British Journal of Sports Medicine*'de yayımladı. 19 içerik uzmanı ve 3 yöntem uzmanı, her madde için alandan en az bir örnek "mükemmel raporlama" seçti (Ardern ve ark., 2022). Çevrimiçi ilk yayın 2021, sayı tarihi 2022'dir.

Slayta öneri: Akış şemasını üç yatay bant (Tanımlama, Tarama, Dahil etme) ve sağda dışlama yan kutularıyla çiz; ayrı bir küçük slaytta "PERSiST: PRISMA'nın sporcu forması" mesajı.

### 3.6 Veri çıkarımı ve yanlılık riski

- **Veri çıkarımı:** Dahil edilen her çalışmadan önceden hazırlanmış bir formla katılımcı, müdahale, karşılaştırma, sonuç ve desen bilgileri çıkarılır (Karaçam, 2013; Higgins ve Thomas, 2019). Covidence'ın Cochrane çıkarım şablonu RevMan'e aktarılabilir (Cochrane Community sayfası).
- **RoB 2 (randomize çalışmalar):** 2008'deki ilk Cochrane yanlılık aracının yerini alır; beş alan: randomizasyon süreci, amaçlanan müdahaleden sapmalar, eksik sonuç verisi, sonucun ölçümü ve raporlanan sonucun seçimi. Her alanda yönlendirici (signalling) sorular ve alan düzeyinde yargıya götüren bir algoritma vardır (Sterne ve ark., 2019).
- **ROBINS-I (randomize olmayan müdahale çalışmaları):** Kohort, vaka-kontrol, kontrollü önce-sonra gibi desenler için; yedi alan: karıştırıcılık, katılımcı seçimi, müdahalelerin sınıflandırılması, amaçlanan müdahaleden sapmalar, eksik veri, sonuç ölçümü, raporlanan sonucun seçimi (Sterne ve ark., 2016; alan listesi ikincil özetten, bkz. bölüm 7).
- **PEDro ölçeği (fizyoterapi ve spor alanında yaygın):** 11 madde; madde 1 dış geçerlilik, 2-9 iç geçerlilik, 10-11 istatistiksel raporlama; madde 1 puana katılmaz, toplam puan 10 üzerindendir (Cashin ve McAuley, 2020). Güvenirlik: madde düzeyinde kappa .36 ile .80 arası (tek değerlendirici), toplam puan ICC .56 (tek değerlendirici) ve .68 (uzlaşı); yazarlar toplam puan güvenirliğini "orta ile iyi" (fair to good) olarak niteler (Maher ve ark., 2003). Not: PEDro bir "metodolojik kalite" ölçeğidir; RoB 2 ise doğrudan yanlılık riskine odaklanır.

Slayta öneri: Üç sütunlu tablo: Araç · Hangi çalışma türü · Ne değerlendirir (RoB 2: RKÇ, 5 alan · ROBINS-I: randomize olmayan, 7 alan · PEDro: RKÇ, 11 madde / 10 puan).

### 3.7 Kanıtın kesinliği ve derlemenin kalitesi: GRADE, AMSTAR 2

- **GRADE:** Kanıt kalitesini ve öneri gücünü tutarlı biçimde derecelendirmek için geliştirilmiş, dünyada giderek yaygınlaşan sistemdir (Guyatt ve ark., 2008). Dört düzey: **yüksek, orta, düşük, çok düşük**; tek tek çalışmalara değil, bir sonuç için kanıt bütününe uygulanır (Balshem ve ark., 2011).
  - Başlangıç: RKÇ'ler "yüksek", gözlemsel çalışmalar "düşük" başlar (Balshem ve ark., 2011).
  - Düşürme nedenleri: yanlılık riski, kesinsizlik (imprecision), tutarsızlık, dolaylılık, yayın yanlılığı (Balshem ve ark., 2011).
  - Yükseltme: bazı etkenler güveni artırabilir (ör. büyük etki) (Balshem ve ark., 2011).
  - Sistematik derleme bağlamında kesinlik, "etki tahmininin doğru olduğuna duyulan güven" demektir (Balshem ve ark., 2011).
- **AMSTAR 2:** Randomize ve/veya randomize olmayan çalışmaları içeren sistematik derlemelerin kalitesini eleştirel değerlendirme aracıdır (Shea ve ark., 2017). 16 madde, 7'si kritik (madde 2, 4, 7, 9, 11, 13, 15: protokol, arama yeterliliği, dışlanan çalışmaların gerekçeli listesi, tek tek çalışmalarda yanlılık riski, meta-analiz yöntemleri, sonuç yorumunda yanlılık riski, yayın yanlılığı). Genel güven düzeyi: **yüksek** (hiç ya da bir kritik olmayan zayıflık), **orta** (birden fazla kritik olmayan zayıflık, kritik kusur yok), **düşük** (bir kritik kusur), **kritik düzeyde düşük** (birden fazla kritik kusur) (Shea ve ark., 2017; madde ve düzey ayrıntıları ikincil kaynaklardan, bkz. bölüm 7).
- Ayrım: GRADE **kanıtın** kesinliğini, AMSTAR 2 **derlemenin kendisinin** kalitesini değerlendirir.

Slayta öneri: Solda dört basamaklı GRADE merdiveni (yüksek → çok düşük, düşürme/yükseltme okları), sağda AMSTAR 2 "trafik ışığı" (yüksek, orta, düşük, kritik düşük); başlık: "Kanıtı mı değerlendiriyorum, derlemeyi mi?"

## 4. Konuşmacı notu malzemesi

1. **Benzetme:** Protokolü önceden kaydetmek, kale direklerini maç başlamadan dikmek gibidir; sonuç görüldükten sonra direği kaydırmak mümkün olmaz (kayıt mantığı için Booth ve ark., 2012).
2. **Kaynaklı:** "Tek veri tabanında arama yapmak, takımın yalnız bir yarısını sahaya sürmek gibidir": ilgili makalelerin %16'sı yalnız tek bir veri tabanında bulunuyordu (Bramer ve ark., 2017). (Benzetme kısmı benzetmedir, sayı kaynaklıdır.)
3. **Kaynaklı:** 28 arama sisteminden yalnız 14'ü sistematik derlemede ana arama aracı olmaya uygun bulundu ve Google Akademik bunlardan biri değildi (Gusenbauer ve Haddaway, 2020).
4. **Benzetme:** İki bağımsız araştırmacı, maçta iki yardımcı hakem gibidir; birbirini görmeden karar verir, anlaşamazlarsa orta hakem (üçüncü araştırmacı) karar verir.
5. **Kaynaklı:** PRISMA akış şeması, derlemenin "kadro listesi"dir: kaç kayıtla başladık, kimi neden kesip attık, kimle sahaya çıktık, hepsi sayılarıyla görünür (Page ve ark., 2021). ("Kadro listesi" ifadesi benzetmedir.)
6. **Kaynaklı:** GRADE'de RKÇ'ler "yüksek", gözlemsel çalışmalar "düşük" kesinlikle başlar; ama zayıf yöntem RKÇ'yi aşağı çekebilir, büyük etki gözlemsel kanıtı yukarı taşıyabilir (Balshem ve ark., 2011).

## 5. Kaynak tablosu

| # | Yazar (Yıl) | Başlık | Dergi/Yayıncı | Tür | Neyi destekliyor | Taban | DOI/bağlantı |
|---|---|---|---|---|---|---|---|
| 1 | Ardern ve ark. (2022) | Implementing the 27 PRISMA 2020 Statement items for systematic reviews in the sport and exercise medicine, musculoskeletal rehabilitation and sports science fields: the PERSiST (implementing Prisma in Exercise, Rehabilitation, Sport medicine and SporTs science) guidance | British Journal of Sports Medicine, 56(4), 175-195 | Kılavuz | PRISMA'nın spora uyarlanması | PubMed/PMC (PMC8862073) | 10.1136/bjsports-2021-103987 |
| 2 | Balshem ve ark. (2011) | GRADE guidelines: 3. Rating the quality of evidence | Journal of Clinical Epidemiology, 64(4), 401-406 | Yöntem makalesi | GRADE dört düzey, düşürme/yükseltme | Kurumsal depolar (McMaster, Basel) | 10.1016/j.jclinepi.2010.07.015 |
| 3 | Booth ve ark. (2012) | The nuts and bolts of PROSPERO: an international prospective register of systematic reviews | Systematic Reviews, 1, 2 | Yöntem makalesi | PROSPERO, kayıt gerekçesi ve zamanı | PubMed/PMC (PMC3348673), DOAJ | 10.1186/2046-4053-1-2 |
| 4 | Bramer ve ark. (2017) | Optimal database combinations for literature searches in systematic reviews: a prospective exploratory study | Systematic Reviews, 6, 245 | Özgün araştırma | Çoklu veri tabanı, Google Scholar'ın ek rolü | PubMed (29208034)/PMC (PMC5718002) | 10.1186/s13643-017-0644-y |
| 5 | Cashin ve McAuley (2020) | Clinimetrics: Physiotherapy Evidence Database (PEDro) Scale | Journal of Physiotherapy, 66(1), 59 | Yöntem makalesi | PEDro yapısı (11 madde, 10 puan) | ResearchGate kaydı, PEDro sitesi | 10.1016/j.jphys.2019.08.005 |
| 6 | Cooke ve ark. (2012) | Beyond PICO: The SPIDER tool for qualitative evidence synthesis | Qualitative Health Research, 22(10), 1435-1443 | Yöntem makalesi | PICO sınırı, SPIDER | PubMed (22829486) | 10.1177/1049732312452938 |
| 7 | Gusenbauer ve Haddaway (2020) | Which academic search systems are suitable for systematic reviews or meta-analyses? Evaluating retrieval qualities of Google Scholar, PubMed, and 26 other resources | Research Synthesis Methods, 11(2), 181-217 | Özgün araştırma | Google Akademik ana arama aracı değil | Kurumsal depolar (JKU, SEI) | 10.1002/jrsm.1378 |
| 8 | Guyatt ve ark. (2008) | GRADE: an emerging consensus on rating quality of evidence and strength of recommendations | BMJ, 336(7650), 924-926 | Yöntem makalesi | GRADE'in amacı | PubMed (18436948) | 10.1136/bmj.39489.470347.AD |
| 9 | Higgins ve Thomas (Ed.) (2019) | Cochrane Handbook for Systematic Reviews of Interventions (2. baskı) | Wiley-Blackwell | Kitap / kılavuz | Genel yöntem çerçevesi | Cochrane sitesi | ISBN 9781119536628 |
| 10 | Karaçam (2013) | Sistematik derleme metodolojisi: Sistematik derleme hazırlamak için bir rehber | Dokuz Eylül Üniversitesi Hemşirelik Fakültesi Elektronik Dergisi, 6(1), 26-33 | Yöntem makalesi (Türkçe) | Tanım ve aşamalar | TR Dizin (kayıt 229802), DergiPark | https://dergipark.org.tr/tr/pub/deuhfed/issue/46815/587078 |
| 11 | Lefebvre ve ark. (2019) | Searching for and selecting studies (Bölüm 4) | Cochrane Handbook, Wiley | Kitap bölümü | Arama stratejisi, gri literatür, seçim | Cochrane sitesi, Nottingham deposu | 10.1002/9781119536604.ch4 |
| 12 | Maher ve ark. (2003) | Reliability of the PEDro scale for rating quality of randomized controlled trials | Physical Therapy, 83(8), 713-721 | Özgün araştırma | PEDro güvenirliği | ProQuest, McMaster | 10.1093/ptj/83.8.713 |
| 13 | Moher ve ark. (2015) | Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement | Systematic Reviews, 4, 1 | Kılavuz | PRISMA-P 17 madde | Kurumsal depolar, prisma-statement.org | 10.1186/2046-4053-4-1 |
| 14 | Ouzzani ve ark. (2016) | Rayyan: a web and mobile app for systematic reviews | Systematic Reviews, 5, 210 | Yöntem makalesi | Tarama aracı | PubMed (27919275)/PMC (PMC5139140) | 10.1186/s13643-016-0384-4 |
| 15 | Page ve ark. (2018) | Registration of systematic reviews in PROSPERO: 30,000 records and counting | Systematic Reviews, 7 (makale no. doğrulanmadı) | Yöntem makalesi | PROSPERO büyümesi | DOAJ, Ottawa deposu | 10.1186/s13643-018-0699-4 |
| 16 | Page ve ark. (2021) | The PRISMA 2020 statement: an updated guideline for reporting systematic reviews | BMJ, 372, n71 | Kılavuz | 27 madde, akış şeması | PubMed/PMC (PMC8005924) | 10.1136/bmj.n71 |
| 17 | Pieper ve Rombey (2022) | Where to prospectively register a systematic review | Systematic Reviews, 11, 8 | Yöntem makalesi (yorum) | PROSPERO dışı kayıt seçenekleri (OSF vb.) | PMC (PMC8742923) | 10.1186/s13643-021-01877-1 |
| 18 | Shea ve ark. (2017) | AMSTAR 2: a critical appraisal tool for systematic reviews that include randomised or non-randomised studies of healthcare interventions, or both | BMJ, 358, j4008 | Yöntem makalesi | Derleme kalitesi | PMC (PMC5833365) | 10.1136/bmj.j4008 |
| 19 | Sterne ve ark. (2016) | ROBINS-I: a tool for assessing risk of bias in non-randomised studies of interventions | BMJ, 355, i4919 | Yöntem makalesi | Randomize olmayan çalışmalarda yanlılık | White Rose, Liverpool depoları | 10.1136/bmj.i4919 |
| 20 | Sterne ve ark. (2019) | RoB 2: a revised tool for assessing risk of bias in randomised trials | BMJ, 366, l4898 | Yöntem makalesi | RKÇ'de yanlılık, 5 alan | White Rose, York, UCL depoları | 10.1136/bmj.l4898 |
| 21 | Cochrane Community (t.y.) | Covidence | Cochrane | Web sayfası (hakemli değil) | Covidence'ın Cochrane'deki rolü | Cochrane sitesi | https://community.cochrane.org/help/tools-and-software/covidence |

Not: 21. satır bilimsel kaynak sayısına dahil edilmedi; bilimsel doğrulanmış kaynak sayısı 20'dir.

## 6. Kaynakça (APA 7, alfabetik)

Uyarı: "[tam yazar listesi DOI sayfasından tamamlanmalı]" işaretli künyelerde bu oturumda yalnız ilk yazar(lar) doğrulanabildi. APA 7 en fazla 20 yazarın yazılmasını ister; dalga 2'de tamamlanmalı, hafızadan doldurulmamalıdır.

Ardern, C. L., et al. (2022). Implementing the 27 PRISMA 2020 Statement items for systematic reviews in the sport and exercise medicine, musculoskeletal rehabilitation and sports science fields: The PERSiST (implementing Prisma in Exercise, Rehabilitation, Sport medicine and SporTs science) guidance. *British Journal of Sports Medicine, 56*(4), 175-195. https://doi.org/10.1136/bjsports-2021-103987 [tam yazar listesi DOI sayfasından tamamlanmalı]

Balshem, H., et al. (2011). GRADE guidelines: 3. Rating the quality of evidence. *Journal of Clinical Epidemiology, 64*(4), 401-406. https://doi.org/10.1016/j.jclinepi.2010.07.015 [tam yazar listesi DOI sayfasından tamamlanmalı]

Booth, A., et al. (2012). The nuts and bolts of PROSPERO: An international prospective register of systematic reviews. *Systematic Reviews, 1*, 2. https://doi.org/10.1186/2046-4053-1-2 [tam yazar listesi DOI sayfasından tamamlanmalı]

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews, 6*, 245. https://doi.org/10.1186/s13643-017-0644-y

Cashin, A. G., & McAuley, J. H. (2020). Clinimetrics: Physiotherapy Evidence Database (PEDro) Scale. *Journal of Physiotherapy, 66*(1), 59. https://doi.org/10.1016/j.jphys.2019.08.005 [yazar adlarının baş harfleri doğrulanmalı]

Cooke, A., Smith, D., & Booth, A. (2012). Beyond PICO: The SPIDER tool for qualitative evidence synthesis. *Qualitative Health Research, 22*(10), 1435-1443. https://doi.org/10.1177/1049732312452938 [baş harfler doğrulanmalı]

Gusenbauer, M., & Haddaway, N. R. (2020). Which academic search systems are suitable for systematic reviews or meta-analyses? Evaluating retrieval qualities of Google Scholar, PubMed, and 26 other resources. *Research Synthesis Methods, 11*(2), 181-217. https://doi.org/10.1002/jrsm.1378

Guyatt, G. H., Oxman, A. D., Vist, G. E., Kunz, R., Falck-Ytter, Y., Alonso-Coello, P., & Schünemann, H. J. (2008). GRADE: An emerging consensus on rating quality of evidence and strength of recommendations. *BMJ, 336*(7650), 924-926. https://doi.org/10.1136/bmj.39489.470347.AD

Higgins, J. P. T., & Thomas, J. (Eds.). (2019). *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley-Blackwell. [ortak editörler: Chandler, J., Cumpston, M., Li, T., Page, M. J., Welch, V. A.; tam editör listesi kontrol edilmeli]

Karaçam, Z. (2013). Sistematik derleme metodolojisi: Sistematik derleme hazırlamak için bir rehber. *Dokuz Eylül Üniversitesi Hemşirelik Fakültesi Elektronik Dergisi, 6*(1), 26-33. https://dergipark.org.tr/tr/pub/deuhfed/issue/46815/587078

Lefebvre, C., Glanville, J., Briscoe, S., Littlewood, A., Marshall, C., Metzendorf, M.-I., ... Wieland, L. S. (2019). Searching for and selecting studies. In J. P. T. Higgins & J. Thomas (Eds.), *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley-Blackwell. https://doi.org/10.1002/9781119536604.ch4 [ara yazarlar ve sayfa aralığı doğrulanmadı; tamamlanmalı]

Maher, C. G., Sherrington, C., Herbert, R. D., Moseley, A. M., & Elkins, M. (2003). Reliability of the PEDro scale for rating quality of randomized controlled trials. *Physical Therapy, 83*(8), 713-721. https://doi.org/10.1093/ptj/83.8.713

Moher, D., et al. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews, 4*, 1. https://doi.org/10.1186/2046-4053-4-1 [tam yazar listesi DOI sayfasından tamamlanmalı]

Ouzzani, M., Hammady, H., Fedorowicz, Z., & Elmagarmid, A. (2016). Rayyan: A web and mobile app for systematic reviews. *Systematic Reviews, 5*, 210. https://doi.org/10.1186/s13643-016-0384-4

Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71 [tam yazar listesi DOI sayfasından tamamlanmalı]

Page, M. J., Shamseer, L., & Tricco, A. C. (2018). Registration of systematic reviews in PROSPERO: 30,000 records and counting. *Systematic Reviews, 7*. https://doi.org/10.1186/s13643-018-0699-4 [makale numarası doğrulanmalı]

Pieper, D., & Rombey, T. (2022). Where to prospectively register a systematic review. *Systematic Reviews, 11*, 8. https://doi.org/10.1186/s13643-021-01877-1

Shea, B. J., et al. (2017). AMSTAR 2: A critical appraisal tool for systematic reviews that include randomised or non-randomised studies of healthcare interventions, or both. *BMJ, 358*, j4008. https://doi.org/10.1136/bmj.j4008 [tam yazar listesi DOI sayfasından tamamlanmalı]

Sterne, J. A. C., et al. (2016). ROBINS-I: A tool for assessing risk of bias in non-randomised studies of interventions. *BMJ, 355*, i4919. https://doi.org/10.1136/bmj.i4919 [tam yazar listesi DOI sayfasından tamamlanmalı]

Sterne, J. A. C., et al. (2019). RoB 2: A revised tool for assessing risk of bias in randomised trials. *BMJ, 366*, l4898. https://doi.org/10.1136/bmj.l4898 [tam yazar listesi DOI sayfasından tamamlanmalı]

## 7. Doğrulanamayanlar ve sınırlar

- **Tam yazar listeleri:** Ardern 2022, Balshem 2011, Booth 2012, Moher 2015, Page 2021, Shea 2017, Sterne 2016 ve Sterne 2019 için yalnız ilk yazar, başlık, dergi, cilt, sayfa/makale no. ve DOI doğrulandı. Lefebvre 2019'da ara yazarlar ve sayfa aralığı doğrulanmadı, bu yüzden sayfa yazılmadı. Page 2018 makale numarası doğrulanmadı, bu yüzden yazılmadı. Cashin 2020 ve Cooke 2012 için yazar baş harfleri aramada görünmedi.
- **İkincil kaynaktan gelen ayrıntılar:** ROBINS-I'in yedi alanı (NCCMT özeti), AMSTAR 2'nin 16 madde / 7 kritik madde ve dört güven düzeyi tanımları (CASRAI ve BMC tabloları), PEDro'nun 11 madde yapısı (Cashin ve McAuley özetinden). Tam metinler açılamadı (PMC ve yayıncı sayfalarına WebFetch DNS hatası).
- **Kaynaksız bırakılan genel bilgiler:** Boolean operatörlerin ve MeSH'in kullanımı genel yöntem bilgisidir; Lefebvre ve ark. (2019) bölümüne yönlendirildi ama ilgili alt başlık metni görülmedi. "Spor alanında SPORTDiscus eklenmesi yaygındır" ifadesi için ayrı kaynak doğrulanmadı.
- **Türkiye bağlamı:** YÖKTEZ ve TR Dizin'in gri literatür / ulusal kaynak olarak yerine dair hakemli bir yöntem makalesi bulunamadı; yalnız bu tabanları kullanan Türkçe derlemeler ve TR Dizin tanıtım sayfası görüldü. Sunumda kaynaksız, "uygulamada" ifadesiyle verilmeli.
- **Covidence:** Hakemli kaynak bulunmadı; yalnız Cochrane Community sayfası (kurumsal) ve satıcı sayfaları görüldü.
- **PRISMA akış şeması:** Resmi prisma-statement.org sayfası açılamadı; kutu adları birden çok bağımsız şablon kopyasında (Page ve ark., 2021'e atıflı) eşleştirildi.
- **Gusenbauer ve Haddaway yılı:** Çevrimiçi 2019'da, sayı olarak 2020'de (11[2]) yayımlandı; 2020 kullanıldı.
- **Ardern yılı:** Çevrimiçi ilk 2021, sayı 2022; 2022 kullanıldı.
- **Doğrulanamayan ve listeye konmayan:** Shamseer ve ark. (2015) PRISMA-P açıklama belgesi (BMJ, 349, g7647) aramada görüldü ama tam yazar listesi doğrulanmadığı için tabloya alınmadı. Methley ve ark. (2014) PICO/PICOS/SPIDER karşılaştırması yalnız ikincil anılış olarak görüldü, alınmadı.
- **Erişim:** PubMed API, YÖK Tez, EBSCO (SPORTDiscus), Web of Science, Google Scholar curl ile bir kez denendi, hiçbiri yanıt vermedi.

## 8. Zaman

- Başlangıç (UTC): 20:07:22
- Bitiş (UTC): 20:11:37
