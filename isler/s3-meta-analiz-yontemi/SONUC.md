# SONUC · s3 · Meta-analizin temel istatistiği

## 1. Hedef durumu

- **Doğrulanmış bilimsel kaynak: 15** (hedef en az 8). **Hedef tuttu.**
- **2016-2026 arası: 4** (IntHout ve ark., 2016; Higgins ve ark., 2019; Borenstein ve ark., 2021; Deeks ve ark., 2024). Hedef (en az 3) tuttu.
- **Türkçe hakemli yöntem makalesi: 1** bulundu ve doğrulandı (Üstün ve Eryılmaz, 2014, Eğitim ve Bilim).
- Ek olarak yazılımlar için 3 resmi web sayfası (Cochrane RevMan fiyat sayfası, jamovi duyurusu, Biostat CMA fiyat sayfası) kullanıldı; bunlar bilimsel kaynak sayısına katılmadı.
- Doğrulama yöntemi: her künye bu oturumda WebSearch ile arandı; yazar, yıl, başlık, dergi/yayıncı ve (varsa) DOI arama sonucundaki kayıtla eşleştirildi. Tam metin açılamadı (WebFetch tüm alan adlarında DNS hatası verdi); bu yüzden içerik iddiaları arama sonuçlarındaki özet, başlık sayfası ve ikincil alıntılara dayanıyor. Bunun sınırları 7. bölümde.

## 2. Veri tabanı erişimi

| Taban | Durum | Not |
|---|---|---|
| PubMed / PMC | Doğrudan API erişilemedi | eutils isteği yanıt vermedi. PMC kayıtları (ör. PMC192859, PMC4947751) WebSearch sonuçlarında göründü, dizinlenme oradan not edildi. |
| SPORTDiscus | Erişilemedi | Abonelik gerektiriyor, denenmedi. Hopkins ve ark. (2009) için BISp-SURF (Alman spor bilimi tabanı) kaydı arama sonucunda göründü. |
| Google Akademik | Erişilemedi | scholar.google.com proxy tarafından reddedildi (connect_rejected). |
| Web of Science | Erişilemedi | Abonelik gerektiriyor. |
| YÖK Ulusal Tez Merkezi | Erişilemedi | tez.yok.gov.tr proxy tarafından reddedildi. YÖK Açık Bilim kayıtları arama sonucunda göründü ama tez kaynak olarak eklenmedi. |
| TR Dizin | Sayfa açılamadı (DNS) | Üstün ve Eryılmaz (2014) kaydı TR Dizin arama sonucunda göründü. |
| Asıl kanal | WebSearch | Tüm doğrulamalar bununla yapıldı. |

## 3. İçerik

### 3.1 Mantık: neden tek çalışma yetmez?

- Tek bir çalışma çoğu zaman küçük örneklemlidir; sonucu şans dalgalanmasına açıktır ve güven aralığı geniştir. Meta-analiz, aynı soruyu soran çalışmaların sonuçlarını istatistiksel olarak birleştirerek tek, daha kesin bir özet etki tahmini üretir (Borenstein ve ark., 2021; Üstün ve Eryılmaz, 2014).
- Birleştirme basit ortalama değildir: her çalışma **ters varyans** ile ağırlıklandırılır. Varyansı küçük (yani kesin, genellikle büyük örneklemli) çalışma daha çok ağırlık alır (Borenstein ve ark., 2010; Deeks ve ark., 2024). Hedges (1981), en kesin ağırlıklı etki tahminini veren ağırlıkların ifadesini türetmiştir.
- Çalışmalar birleşince toplam bilgi artar, özet tahminin güven aralığı daralır ve tek tek çalışmaların yakalayamadığı etkiyi saptama gücü yükselir (Borenstein ve ark., 2021). Ancak heterojenlik arttıkça meta-analizin gücü düşer (Türkiye Klinikleri Biyoistatistik Dergisi'ndeki bir güç çalışması bunu gösteriyor; künyesi tam doğrulanamadığı için kaynak listesine alınmadı, bkz. bölüm 7).

Slayta öneri: Solda beş küçük, geniş güven aralıklı çalışma, sağda onların ağırlıklı birleşimi olan tek dar aralık; tek mesaj: "Birleştirmek = daha kesin tahmin".

### 3.2 Etki büyüklüğü

Meta-analiz p değerlerini değil, **etki büyüklüklerini** birleştirir. Hangi ölçünün seçileceği verinin türüne bağlıdır (Borenstein ve ark., 2021; Deeks ve ark., 2024):

| Veri türü | Ölçü | Ne anlatır |
|---|---|---|
| Sürekli (ör. sıçrama yüksekliği, VO2maks) | Cohen d | İki grup ortalaması farkının standart sapmaya bölümü (standartlaştırılmış ortalama farkı). |
| Sürekli, küçük örneklem | Hedges g | d'nin küçük örneklem yanlılığı düzeltilmiş hâli. Hedges (1981), Glass'ın etki büyüklüğü kestiricisinin küçük örneklemde yanlı olduğunu gösterip yansız kestiriciyi türetmiştir. |
| İkili (ör. sakatlandı / sakatlanmadı) | Olasılık oranı (OR), risk oranı (RR) | 1 = fark yok. RR riskleri, OR odds'ları oranlar. |
| İki sürekli değişkenin ilişkisi | Korelasyon r | -1 ile +1 arası. |

**Cohen'in eşikleri:** d için 0.2 küçük, 0.5 orta, 0.8 büyük (Cohen, 1988). Cohen bunları daha iyi bir dayanak yokken kullanılacak kaba ölçütler olarak sundu; anlam her zaman bağlama göre yorumlanmalı (Cohen, 1988; bu uyarının sayfa düzeyindeki ifadesi ikincil kaynaklardan görüldü, bkz. bölüm 7).

**Spor bilimine özgü öneri:** Hopkins ve ark. (2009), standartlaştırılmış ortalama farkı için 0.20, 0.60, 1.20, 2.0 ve 4.0 eşiklerini küçük, orta, büyük, çok büyük ve son derece büyük sınırları olarak önerdi (paydada denekler arası standart sapma). Korelasyon için eşikler 0.1, 0.3, 0.5, 0.7 ve 0.9'dur. Bu ölçekte "küçük" sınırı Cohen ile aynı (0.20), ama "orta" ve "büyük" sınırları daha yüksektir (Hopkins ve ark., 2009). Makale ayrıca çıkarımda sıfır hipotezi testi yerine tahminin kesinliğine (güven aralığına) dayanmayı savunur (Hopkins ve ark., 2009).

Slayta öneri: Üç sütunlu tablo (veri türü · ölçü · "fark yok" değeri: d/g için 0, OR/RR için 1, r için 0) ve altında Cohen ile Hopkins eşiklerini yan yana gösteren tek satırlık cetvel.

### 3.3 Modeller: sabit etkiler ve rastgele etkiler

- **Sabit etkiler (fixed-effect) modeli:** Tüm çalışmaların altında **tek bir gerçek etki** olduğunu varsayar; gözlenen farkların tamamı örnekleme hatasıdır (Borenstein ve ark., 2010; Riley ve ark., 2011).
- **Rastgele etkiler (random-effects) modeli:** Gerçek etkinin çalışmadan çalışmaya **değişebileceğine** izin verir (farklı yaş grupları, branşlar, antrenman protokolleri). Özet tahmin, bu gerçek etkiler dağılımının **ortalamasıdır** (Borenstein ve ark., 2010; Riley ve ark., 2011).
- İki model benzer formüller kullanır ve bazen benzer sayılar verir, ama verilere ilişkin temelden farklı varsayımlara dayanır; birbirinin yerine kullanılabilir değildir (Borenstein ve ark., 2010).
- Rastgele etkiler modelinde küçük çalışmalar, sabit etkiler modeline göre görece daha çok ağırlık alır (Borenstein ve ark., 2010).
- **Ne zaman hangisi:** Çalışmalar aynı popülasyonda, aynı müdahaleyle, neredeyse birbirinin kopyası gibi yapıldıysa sabit etkiler savunulabilir. Spor bilimindeki gibi farklı örneklem ve protokollerden genelleme yapılacaksa rastgele etkiler daha gerçekçidir (Borenstein ve ark., 2010; Borenstein ve ark., 2021).

**Benzetme (açıkça benzetme):** Sabit etkiler, aynı termometreyle aynı odanın sıcaklığını beş kez ölçmek gibidir: tek bir gerçek değer var, farklar ölçüm hatası. Rastgele etkiler, beş farklı şehrin sıcaklığını ölçüp "ortalama sıcaklık" sormak gibidir: her şehrin gerçek değeri zaten farklı.

Slayta öneri: İki panelli şema: solda tüm çalışmaların tek bir dikey "gerçek etki" çizgisine dizildiği resim, sağda gerçek etkilerin bir çan eğrisinden geldiği resim; altında termometre benzetmesi.

### 3.4 Heterojenlik

Heterojenlik, çalışma sonuçlarının yalnız şansla açıklanamayacak kadar farklı olmasıdır.

- **Cochran Q:** Her çalışmanın özet tahminden sapmasının karesinin ağırlıklı toplamı. Klasik heterojenlik testi budur (Higgins ve ark., 2003). Sınırı: çalışma sayısı azken gücü düşüktür; anlamsız bir Q, homojenliğin kanıtı sayılmamalıdır (Higgins ve ark., 2003).
- **I²:** Çalışmalar arası toplam değişkenliğin şanstan değil, gerçek heterojenlikten kaynaklanan yüzdesi. Formül: I² = 100% × (Q - sd) / Q; negatif çıkarsa 0 alınır (Higgins ve ark., 2003). Yazarlar %25, %50 ve %75 değerlerine çekinceli olarak düşük, orta ve yüksek etiketlerini önermiştir (Higgins ve ark., 2003; ifade ikincil alıntılardan doğrulandı).
- **Cochrane'in kaba rehberi (örtüşen aralıklar):** %0-40 önemli olmayabilir, %30-60 orta, %50-90 önemli (substantial), %75-100 çok yüksek (considerable). Bu bantlar Cochrane El Kitabı'nın 5.0.1 sürümüne atfedilerek ikincil kaynaklarda doğrulandı; El Kitabı eşiklerin yanıltıcı olabileceğini, yorumun etkinin büyüklüğüne, yönüne ve heterojenlik kanıtının gücüne bağlı olduğunu vurgular (Deeks ve ark., 2024; güncel sürüm metni açılamadı, bkz. bölüm 7).
- **tau² (τ²):** Gerçek etkilerin çalışmalar arası varyansı; rastgele etkiler modelinin heterojenlik parametresi. I²'den farkı, çalışmaların kesinliğine bağlı olmamasıdır (Borenstein ve ark., 2021; IntHout ve ark., 2016).
- **Tahmin aralığı (prediction interval):** "Benzer yeni bir çalışmada gerçek etki büyük olasılıkla nerede olur?" sorusunu yanıtlar. τ² ve I²'yi uygulamada yorumlamak zordur; tahmin aralığı ise orijinal etki büyüklüğü biriminde, beklenen gerçek etkiler aralığını gösterir. Heterojenlik varsa güven aralığından geniştir ve farklı bir sonuca götürebilir. Yazarlar meta-analizlerde rutin olarak raporlanmasını önerir (IntHout ve ark., 2016; Riley ve ark., 2011).

Slayta öneri: Aynı özet etki için iki çubuk: dar olan "%95 güven aralığı: ortalama nerede?", geniş olan "%95 tahmin aralığı: yeni bir çalışmada etki nerede?"; yanında I² için renkli, örtüşen bant cetveli.

### 3.5 Orman grafiği (forest plot) nasıl okunur

Okuma anahtarı (Borenstein ve ark., 2021; Deeks ve ark., 2024):

1. **Her satır bir çalışma.** Solda çalışma adı, sağda sayısal etki ve güven aralığı.
2. **Kare:** O çalışmanın etki tahmini (nokta tahmini).
3. **Kare büyüklüğü:** Çalışmanın meta-analizdeki ağırlığı. Büyük kare = kesin çalışma = çok ağırlık.
4. **Yatay çizgi:** Çalışmanın %95 güven aralığı. Kısa çizgi = kesin tahmin.
5. **Dikey çizgi (etkisizlik çizgisi):** d/g için 0, OR/RR için 1. Bir çizgi bunu kesiyorsa o çalışma tek başına istatistiksel olarak anlamlı değildir.
6. **Elmas:** Birleşik (özet) etki. Ortası tahmin, sol ve sağ uçları güven aralığı. Elmas dikey çizgiye değmiyorsa özet etki anlamlıdır.
7. Altta heterojenlik istatistikleri (Q, I², τ²) ve varsa tahmin aralığı yazılır.

**EĞİTİM AMAÇLI KURGU VERİ. Gerçek çalışmalar değildir, gerçekmiş gibi sunulmamalıdır.**
Senaryo: "Pliometrik antrenmanın dikey sıçramaya etkisi" (kurgu). Etki ölçüsü Hedges g.

| Çalışma (kurgu) | g | %95 GA | Ağırlık (%) |
|---|---|---|---|
| Çalışma A | 0.20 | -0.30 ile 0.70 | 14.1 |
| Çalışma B | 0.55 | 0.15 ile 0.95 | 22.1 |
| Çalışma C | 0.35 | 0.05 ile 0.65 | 39.2 |
| Çalışma D | 0.80 | 0.10 ile 1.50 | 7.2 |
| Çalışma E | 0.10 | -0.35 ile 0.55 | 17.4 |
| **Birleşik (elmas)** | **0.36** | **0.17 ile 0.55** | 100 |

Hesap notu: Standart hatalar GA genişliği / 3.92 ile türetildi, ağırlıklar ters varyans (sabit etkiler). Q = 4.06 (sd = 4), I² ≈ %2, τ² ≈ 0; yani bu kurgu veride heterojenlik neredeyse yok ve rastgele etkiler sonucu sabit etkilerle hemen hemen aynı çıkar. Öğretici noktalar: A ve E tek başına anlamsız (çizgileri 0'ı kesiyor), ama birleşik elmas 0'ı kesmiyor; D'nin etkisi en büyük ama çizgisi en uzun, bu yüzden karesi en küçük; C en dar aralıklı, bu yüzden en büyük kare.

Slayta öneri: Bu tabloyu çizilmiş bir orman grafiğine dönüştür, köşeye "Kurgu veri · eğitim amaçlı" etiketi koy ve kare, çizgi, dikey çizgi, elmas üzerine dört ok ile açıklama yaz.

### 3.6 Yayın yanlılığının tespiti

- **Sorun:** Anlamlı, "olumlu" sonuçlu çalışmaların yayımlanma olasılığı daha yüksektir; yalnız yayımlananlar birleştirilirse özet etki şişebilir (Egger ve ark., 1997; Duval ve Tweedie, 2000).
- **Huni grafiği (funnel plot):** Yatay eksende etki büyüklüğü, dikey eksende kesinlik (ör. standart hata). Yanlılık yoksa küçük çalışmalar altta geniş, büyükler üstte dar dağılır ve simetrik bir ters huni oluşur. Bir köşe (genellikle küçük ve etkisiz çalışmalar köşesi) boşsa asimetri vardır (Egger ve ark., 1997; Sterne ve ark., 2011).
- **Egger testi:** Huni asimetrisini regresyonla ölçer: standart normal sapmalar kesinliğe karşı regrese edilir, kesişim (intercept) asimetrinin ölçüsüdür (Egger ve ark., 1997). Yazarların incelediği sekiz meta-analiz ile büyük deneme çiftinden dördü uyuşmazdı; uyuşmazların hepsinde meta-analiz daha büyük etki bildiriyordu (Egger ve ark., 1997).
- **Kırp ve doldur (trim and fill):** Huni grafiğindeki asimetriye bakarak "eksik" çalışma sayısını sıra tabanlı bir yöntemle kestirir, simetriyi bozan çalışmaları kırpar, eksik tarafı ayna görüntüleriyle doldurur ve düzeltilmiş özet etkiyi verir (Duval ve Tweedie, 2000).
- **Sınırlar (önemli):** Huni asimetrisi yayın yanlılığıyla eş anlamlı değildir; gerçek heterojenlik, küçük çalışmalarda düşük yöntem kalitesi, şans gibi başka nedenleri olabilir (Sterne ve ark., 2011). Bu testler az çalışma varken güvenilir değildir; Sterne ve ark. (2011) asimetri testlerinin uygun kullanımına dair öneriler verir (sık alıntılanan "en az 10 çalışma" önerisi bu makaleye atfedilir, ancak tam metin bu oturumda açılamadı; slayta koymadan önce bkz. bölüm 7). Kırp ve doldur yöntemi bir düzeltme "tahmini"dir, kesin gerçeği vermez (Duval ve Tweedie, 2000).

Slayta öneri: Yan yana iki huni grafiği şeması (simetrik ve sağ alt köşesi boş asimetrik), altında tek cümle: "Asimetri bir alarmdır, kanıt değil."

### 3.7 Ek analizler

- **Alt grup analizi:** Çalışmaları bir özelliğe göre (ör. erkek/kadın sporcular, elit/amatör) gruplara ayırıp etkileri karşılaştırır. Heterojenliğin kaynağını aramak için kullanılır (Deeks ve ark., 2024; Borenstein ve ark., 2021). Gözlemsel bir karşılaştırma olduğu için nedensellik kanıtı sayılmaz (Borenstein ve ark., 2021).
- **Meta-regresyon:** Alt grup analizinin sürekli değişkenlere genelleştirilmiş hâli; etki büyüklüğü bir çalışma özelliğine (ör. antrenman süresi, hafta) karşı regrese edilir (Viechtbauer, 2010; Deeks ve ark., 2024). Cochrane El Kitabı'nın 5.1 arşiv sürümü, on çalışmadan azsa meta-regresyonun genellikle düşünülmemesi gerektiğini yazar; güncel bölüm ise modellenen her özellik için en az on çalışma ister (ikincil alıntı ile doğrulandı, bkz. bölüm 7).
- **Duyarlılık analizi:** Sonucun sağlamlığını sınar; ör. çalışmaları birer birer çıkarıp ("bir çalışmayı dışarıda bırak") özet etkinin değişip değişmediğine bakmak, ya da yüksek yanlılık riskli çalışmaları çıkarmak (Deeks ve ark., 2024; Borenstein ve ark., 2021).

Slayta öneri: Üç kutulu yatay şema: "Kimlerde farklı? (alt grup) · Neye bağlı değişiyor? (meta-regresyon) · Sonuç tek çalışmaya mı yaslanıyor? (duyarlılık)".

### 3.8 Yazılımlar

| Yazılım | Ücret | Not |
|---|---|---|
| R · metafor paketi | **Ücretsiz**, açık kaynak | Sabit ve rastgele etkiler, meta-regresyon, huni grafiği ve yayın yanlılığı araçları (Viechtbauer, 2010). |
| JASP · Meta-Analysis modülü | **Ücretsiz**, açık kaynak | Menülü arayüz; klasik analizler metafor üzerine kurulu, Bayesçi seçenekler de var (bkz. bölüm 7: JASP kaynağı ön baskı). |
| jamovi · MAJOR modülü | **Ücretsiz** | Kyle Hamilton'ın geliştirdiği, metafor'a dayalı arayüz (jamovi duyurusu, 2017). Forum kayıtlarında eski metafor sürümü kullandığı ve bakımının belirsiz olduğu belirtiliyor. |
| RevMan (RevMan Web) | Cochrane derlemeleri için ücretsiz; Cochrane dışı işler için yıllık abonelik | Research4Life ülkelerine ücretsiz erişim var (Cochrane RevMan fiyat sayfası). Türkiye'nin bu listede olup olmadığı doğrulanmadı. |
| Comprehensive Meta-Analysis (CMA) | **Ücretli** (Biostat) | Akademik ve öğrenci lisansları var; güncel fiyat yayıncıdan teyit edilmeli. |

Slayta öneri: Logo yerine sade tablo; ücretsiz olanlar yeşil işaretli, "başlamak için JASP veya jamovi, ileri düzey için R metafor" tek cümlesi.

## 4. Konuşmacı notu malzemesi

1. **Termometre benzetmesi (benzetme):** Sabit etkiler bir odanın sıcaklığını beş kez ölçmek; rastgele etkiler beş şehrin ortalama sıcaklığını sormak.
2. **Oylama yapmayın, tartın (benzetme, dayanağı Borenstein ve ark., 2010):** "3 çalışma anlamlı, 2 değil" diye oy saymak yanıltır; meta-analiz her çalışmayı ne kadar kesinse o kadar ağırlıkla tartar.
3. **Elmas ve kareler (kaynaklı: Deeks ve ark., 2024):** Orman grafiğinde gözünüzü önce elmasa, sonra dikey çizgiye çevirin: elmas çizgiye değmiyorsa birleşik etki anlamlıdır.
4. **Güven aralığı ile tahmin aralığı (kaynaklı: IntHout ve ark., 2016):** Güven aralığı "ortalama nerede?" sorusunu, tahmin aralığı "benim takımımda ne olur?" sorusunu yanıtlar. Antrenör için ikincisi daha anlamlı olabilir.
5. **Spor bilimi cetveli farklı (kaynaklı: Hopkins ve ark., 2009):** Cohen'e göre 0.5 "orta" iken Hopkins ve ark. için orta eşik 0.60, büyük 1.20'dir; hangi cetveli kullandığınızı her zaman yazın.
6. **Asimetri alarmdır, kanıt değil (kaynaklı: Sterne ve ark., 2011):** Eğri huni, yayın yanlılığı olabileceğini söyler; ama küçük çalışmaların farklı sporcu grubu ya da zayıf yöntemi de aynı görüntüyü verir.

## 5. Kaynak tablosu

| # | Yazar (Yıl) | Başlık | Dergi/Yayıncı | Tür | Neyi destekliyor | Taban (görülen) | DOI/bağlantı |
|---|---|---|---|---|---|---|---|
| 1 | Borenstein, Hedges, Higgins, Rothstein (2010) | A basic introduction to fixed-effect and random-effects models for meta-analysis | Research Synthesis Methods, 1(2), 97-111 | Yöntem makalesi | Sabit/rastgele etkiler, ağırlıklandırma | Web (Scinapse, PMC atfı) | 10.1002/jrsm.12 |
| 2 | Borenstein, Hedges, Higgins, Rothstein (2021) | Introduction to meta-analysis (2. baskı) | John Wiley & Sons | Kitap | Mantık, etki büyüklüğü, modeller, heterojenlik, alt grup | Yayıncı ve kütüphane katalogları | ISBN 9781119558354 |
| 3 | Cohen (1988) | Statistical power analysis for the behavioral sciences (2. baskı) | Lawrence Erlbaum Associates, Hillsdale, NJ | Kitap | d için 0.2/0.5/0.8 eşikleri | Kütüphane katalogları | DOI yok |
| 4 | Deeks, Higgins, Altman, McKenzie, Veroniki (2024) | Chapter 10: Analysing data and undertaking meta-analyses | Cochrane Handbook for Systematic Reviews of Interventions, v6.5, Cochrane | Kılavuz | Ağırlıklandırma, heterojenlik, alt grup, meta-regresyon, duyarlılık, orman grafiği | cochrane.org | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current |
| 5 | Duval, Tweedie (2000) | Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis | Biometrics, 56(2), 455-463 | Yöntem makalesi | Kırp ve doldur | Web (UMN Experts, R belgeleri) | DOI aramada görülmedi |
| 6 | Egger, Davey Smith, Schneider, Minder (1997) | Bias in meta-analysis detected by a simple, graphical test | BMJ, 315(7109), 629-634 | Yöntem makalesi | Huni grafiği, Egger testi | PubMed/PMC (PMC2127453) | 10.1136/bmj.315.7109.629 |
| 7 | Hedges (1981) | Distribution theory for Glass's estimator of effect size and related estimators | Journal of Educational Statistics, 6(2), 107-128 | Yöntem makalesi | Hedges g, küçük örneklem düzeltmesi, ters varyans ağırlıkları | RePEc/IDEAS | 10.3102/10769986006002107 |
| 8 | Higgins, Thomas, Chandler, Cumpston, Li, Page, Welch (Eds.) (2019) | Cochrane handbook for systematic reviews of interventions (2. baskı) | Wiley-Blackwell, Hoboken, NJ | Kılavuz/kitap | Basılı el kitabı künyesi | Kütüphane katalogları | 10.1002/9781119536604 |
| 9 | Higgins, Thompson, Deeks, Altman (2003) | Measuring inconsistency in meta-analyses | BMJ, 327(7414), 557-560 | Yöntem makalesi | Cochran Q, I², 25/50/75 etiketleri | PubMed (PMID 12958120), PMC192859 | 10.1136/bmj.327.7414.557 |
| 10 | Hopkins, Marshall, Batterham, Hanin (2009) | Progressive statistics for studies in sports medicine and exercise science | Medicine and Science in Sports and Exercise, 41(1), 3-12 | Yöntem makalesi (spor) | Spor bilimine özgü etki büyüklüğü eşikleri | VU kurum arşivi, BISp-SURF | 10.1249/MSS.0b013e31818cb278 |
| 11 | IntHout, Ioannidis, Rovers, Goeman (2016) | Plea for routinely presenting prediction intervals in meta-analysis | BMJ Open, 6(7), e010247 | Yöntem makalesi | Tahmin aralığı, τ² ve I² yorum güçlüğü | PubMed (PMID 27406637), PMC4947751 | 10.1136/bmjopen-2015-010247 (bkz. bölüm 7) |
| 12 | Riley, Higgins, Deeks (2011) | Interpretation of random effects meta-analyses | BMJ, 342, d549 | Yöntem makalesi | Rastgele etkiler yorumu, tahmin aralığı | doi.org kaydı (aramada) | 10.1136/bmj.d549 |
| 13 | Sterne, Sutton, Ioannidis ve ark. (2011) | Recommendations for examining and interpreting funnel plot asymmetry in meta-analyses of randomised controlled trials | BMJ, 343, d4002 | Yöntem makalesi/kılavuz | Huni asimetrisinin sınırları | LSHTM arşivi | 10.1136/bmj.d4002 |
| 14 | Üstün, Eryılmaz (2014) | Etkili araştırma sentezleri yapabilmek için bir araştırma yöntemi: Meta-analiz | Eğitim ve Bilim, 39(174), 1-32 | Yöntem makalesi (Türkçe, hakemli) | Türkçe giriş: modeller, heterojenlik, yayın yanlılığı, yazılımlar | TR Dizin | 10.15390/EB.2014.3379 |
| 15 | Viechtbauer (2010) | Conducting meta-analyses in R with the metafor package | Journal of Statistical Software, 36(3), 1-48 | Yöntem makalesi (yazılım) | R metafor | DOAJ, CRAN | 10.18637/jss.v036.i03 |

Bilimsel sayılmayan web kaynakları (yazılım bilgisi için): Cochrane RevMan fiyat sayfası (https://revman.cochrane.org/info/pricing), jamovi 2017 modül duyurusu (https://jamovi.org/news/2017/11/23/new-modules.html), Biostat CMA akademik fiyat sayfası (https://meta-analysis.com/pages/academic_rates).

## 6. Kaynakça (APA 7, alfabetik)

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2010). A basic introduction to fixed-effect and random-effects models for meta-analysis. *Research Synthesis Methods, 1*(2), 97-111. https://doi.org/10.1002/jrsm.12

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2021). *Introduction to meta-analysis* (2nd ed.). John Wiley & Sons.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Deeks, J. J., Higgins, J. P. T., Altman, D. G., McKenzie, J. E., & Veroniki, A. A. (2024). Chapter 10: Analysing data and undertaking meta-analyses. In J. P. T. Higgins, J. Thomas, J. Chandler, M. Cumpston, T. Li, M. J. Page, & V. A. Welch (Eds.), *Cochrane handbook for systematic reviews of interventions* (Version 6.5). Cochrane. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455-463.

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109), 629-634. https://doi.org/10.1136/bmj.315.7109.629

Hedges, L. V. (1981). Distribution theory for Glass's estimator of effect size and related estimators. *Journal of Educational Statistics, 6*(2), 107-128. https://doi.org/10.3102/10769986006002107

Higgins, J. P. T., Thomas, J., Chandler, J., Cumpston, M., Li, T., Page, M. J., & Welch, V. A. (Eds.). (2019). *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley-Blackwell. https://doi.org/10.1002/9781119536604

Higgins, J. P. T., Thompson, S. G., Deeks, J. J., & Altman, D. G. (2003). Measuring inconsistency in meta-analyses. *BMJ, 327*(7414), 557-560. https://doi.org/10.1136/bmj.327.7414.557

Hopkins, W. G., Marshall, S. W., Batterham, A. M., & Hanin, J. (2009). Progressive statistics for studies in sports medicine and exercise science. *Medicine and Science in Sports and Exercise, 41*(1), 3-12. https://doi.org/10.1249/MSS.0b013e31818cb278

IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), Article e010247. https://bmjopen.bmj.com/content/6/7/e010247

Riley, R. D., Higgins, J. P. T., & Deeks, J. J. (2011). Interpretation of random effects meta-analyses. *BMJ, 342*, Article d549. https://doi.org/10.1136/bmj.d549

Sterne, J. A. C., Sutton, A. J., Ioannidis, J. P. A., Terrin, N., Jones, D. R., Lau, J., Carpenter, J., Rücker, G., Harbord, R. M., Schmid, C. H., Tetzlaff, J., Deeks, J. J., Peters, J., Macaskill, P., Schwarzer, G., Duval, S., Altman, D. G., Moher, D., & Higgins, J. P. T. (2011). Recommendations for examining and interpreting funnel plot asymmetry in meta-analyses of randomised controlled trials. *BMJ, 343*, Article d4002. https://doi.org/10.1136/bmj.d4002

Üstün, U., & Eryılmaz, A. (2014). Etkili araştırma sentezleri yapabilmek için bir araştırma yöntemi: Meta-analiz. *Eğitim ve Bilim, 39*(174), 1-32. https://doi.org/10.15390/EB.2014.3379

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software, 36*(3), 1-48. https://doi.org/10.18637/jss.v036.i03

## 7. Doğrulanamayanlar ve sınırlar

- **Tam metin açılamadı.** WebFetch tüm alan adlarında (sportsci.org, cochrane.org, trdizin.gov.tr) DNS hatası verdi. İçerik iddiaları arama sonuçlarındaki özetlere, başlık sayfalarına ve ikincil alıntılara dayanıyor. Dalga 2 bunu bilerek kullanmalı.
- **Sterne ve ark. (2011) listesinin yazar sırası:** İlk üç yazar (Sterne, Sutton, Ioannidis) aramada doğrulandı. Kaynakçadaki tam 19 yazarlı liste aramada görülmedi; dalga 2 ya bunu "Sterne, J. A. C., Sutton, A. J., Ioannidis, J. P. A., ... Higgins, J. P. T." biçiminde tam liste doğrulanarak yazmalı ya da tam listeyi teyit etmeli. **Bu bir doğrulama açığıdır.**
- **"Asimetri testleri için en az 10 çalışma" önerisi** Sterne ve ark. (2011) ile Cochrane'e sık atfedilir, ama bu oturumda kaynak metninde görülmedi. Slaytta sayı olarak yazılmamalı ya da önce doğrulanmalı.
- **IntHout ve ark. (2016) DOI'si** (10.1136/bmjopen-2015-010247) arama sonucunda açıkça görülmedi; makale sayfası (bmjopen.bmj.com/content/6/7/e010247), PMID 27406637 ve PMC4947751 doğrulandı. Kaynakçada bu yüzden URL verildi.
- **Duval ve Tweedie (2000) DOI'si** aramada görülmedi; künye (Biometrics 56(2), 455-463) doğrulandı.
- **Cochrane I² bantları (%0-40 / 30-60 / 50-90 / 75-100):** 5.0.1 sürümüne atfen ikincil kaynaklarda doğrulandı. Güncel v6.5 Bölüm 10 metni açılamadı; bir 2025 eleştirisi farklı kategoriler aktarıyor ama bu da doğrulanamadı. Slaytta "Cochrane'in kaba rehberi" diye sunulabilir, sürüm notu konuşmacı notunda kalmalı.
- **Cochrane v6.5 bölüm künyesi:** Yazarlar (Deeks, Higgins, Altman, McKenzie, Veroniki) ve "Version 6.5, 2024" doğrulandı; bölüm başlığındaki resmi atıf satırı açılamadı. Bir kütüphane kaydı aynı bölümü v6.4 (2023) için veriyor.
- **Meta-regresyon "en az 10 çalışma" kuralı:** 5.1 arşiv metni ve güncel bölümden bir alıntı (posta listesi aracılığıyla) görüldü; Viechtbauer'in aynı yerde bu kuralın ampirik dayanağı olmadığını söylediği de görüldü. Kesin kural gibi sunulmamalı.
- **Cohen (1988) "daha iyi dayanak yokken" uyarısı:** İkincil kaynaklardan görüldü, sayfa numarası doğrulanmadı. Doğrudan alıntı yapılmamalı, yorumlayarak aktarılmalı.
- **Hopkins ve ark. (2009) etiketleri:** 0.20/0.60/1.20/2.0/4.0 sayıları doğrulandı; "küçük, orta, büyük, çok büyük, son derece büyük" etiketlerinin bir kısmı Hopkins'in 2010 tarihli Sportscience makalesinden geliyor olabilir. Ayrıca yazar sırası MSSE'de Hopkins, Marshall, Batterham, Hanin; Sportscience kopyasında farklı. Kaynakçada dergi sırası kullanıldı.
- **Higgins ve ark. (2003) 25/50/75 etiketleri:** "tentatively" (çekinceli) ifadesiyle ikincil alıntılardan doğrulandı.
- **JASP:** Meta-analiz modülü için yalnız 2025 arXiv ön baskıları (Meta-Analysis with JASP, Part I ve II) bulundu; yazarları doğrulanmadığı için kaynak listesine alınmadı. Lisans bilgisi Wikipedia'dan (GNU AGPL).
- **Türkçe güç çalışması (Türkiye Klinikleri Biyoistatistik Dergisi, "Evaluating the power of meta-analyses for mean differences")** ve Türkçe Cochran Q simülasyon çalışması aramada göründü ama yazar/yıl/cilt bilgisi doğrulanamadığı için listeye alınmadı.
- **Spor odaklı yöntem kaynağı:** SPORTDiscus erişilemediği için Hopkins ve ark. (2009) dışında spor bilimine özgü bir meta-analiz yöntem makalesi aranamadı.
- **Kurgu orman grafiği verisi** bu iş için üretildi; hiçbir gerçek çalışmayı temsil etmez.

## 8. Zaman

- Başlangıç (UTC): 20:07:22
- Bitiş (UTC): 20:11:17
