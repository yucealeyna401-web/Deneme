# SONUC · m3 · Meta-analiz istatistiği (slayt 7, 8, 9)

> Durum: TAMAMLANDI. Hesaplama betiği: `isler/m3-meta-analiz/hesap.py`. Bölüm sırası BRIEF'teki yapıya göre (1 ile 7).

## 1. Hedef durumu

- **Doğrulanmış kaynak: 25** (künyesi Crossref ile eşleşti; 20'si ayrıca PubMed, Europe PMC, TR Dizin ya da DergiPark kaydıyla).
- **Türkçe hakemli yöntem kaynağı: 3** (Üstün ve Eryılmaz, 2014; Dinçer, 2018; Göktaş, 2023). Hedef (en az 2) tuttu. Ek 2 Türkçe kitap/çeviri yalnız ikincil künye düzeyinde, sayılmadı.
- **Kanıt düzeyi dağılımı:** tam metin okundu **10** (Page 2021, Campbell 2020, Clarke 2018, Lakens 2013, Rücker 2008, Higgins 2003, IntHout 2016, Debray 2018, Lin 2020, Dinçer 2018) · özet okundu **9** (Hopkins 2009, Borenstein 2010, DerSimonian ve Laird 1986, Higgins ve Thompson 2002, Borenstein 2017, Egger 1997, Duval ve Tweedie 2000, Üstün ve Eryılmaz 2014, Göktaş 2023) · yalnız künye doğrulandı **6** (Glass 1976, Hedges 1981, Cohen 1988, Sterne 2011, Cochrane El Kitabı bölüm 10, Borenstein 2021).
- **BRIEF'in 10 başlığı:** hepsi yazıldı (bölüm 3.1 ile 3.10). Kurgu forest verisi (6 çalışma, DL rastgele etkiler, Q, τ², I², tahmin aralığı) ve kurgu funnel verisi (14 nokta, Egger testi) Python ile hesaplandı.
- **Açık kalanlar:** Cochrane El Kitabı güncel metni (site engelli), "en az 10 çalışma" kuralının birincil kaynağı, Hopkins eşikleri (bölüm 6).


## 2. Erişim notu

- Crossref API (`api.crossref.org`): ÇALIŞIYOR. Künyeler buradan eşleştirildi. Arka arkaya isteklerde bir kez 429 (çok istek) alındı, beklenip yeniden denendi.
- Europe PMC REST (`www.ebi.ac.uk`): ÇALIŞIYOR. Açık erişim tam metinler (fullTextXML) buradan okundu: IntHout ve ark. (2016), Lakens (2013), Rücker ve ark. (2008), Page ve ark. (2021), Campbell ve ark. (2020), Clarke (2018).
- PubMed E-utilities: ÇALIŞIYOR. Özetler (efetch) buradan okundu: Egger ve ark. (1997), Borenstein ve ark. (2010, 2017), Higgins ve Thompson (2002), Duval ve Tweedie (2000), DerSimonian ve Laird (1986), Hopkins ve ark. (2009). Sterne ve ark. (2011) ve Riley ve ark. (2011) için PubMed'de özet yok (yalnız künye).
- PMC (`pmc.ncbi.nlm.nih.gov`): ÇALIŞIYOR ama kimi sayfalar reCAPTCHA döndürdü. Higgins ve ark. (2003) tam metni, Lin ve ark. (2020) ve Debray ve ark. (2018) tam metinleri buradan okundu. Egger ve ark. (1997) PMC kaydı yalnız taranmış sayfa görüntüsü (metin yok), bu yüzden özet düzeyinde kaldı.
- DergiPark: ÇALIŞIYOR (makale sayfası meta verisi ve PDF). TR Dizin arama API'si (`search.trdizin.gov.tr/api/...`): ÇALIŞIYOR.
- **ENGELLİ:** `training.cochrane.org` her adresi `www.cochrane.org`'a yönlendiriyor ve `www.cochrane.org`, `community.cochrane.org`, `training-noproxy.cochrane.org` vekil sunucuda 403 (WebFetch'te de çözümlenmiyor). **Cochrane El Kitabı metni bu oturumda doğrudan okunamadı.** El Kitabı ifadeleri yalnız onu birebir alıntılayan hakemli makalelerden (Rücker ve ark., 2008) aktarıldı; sürüm bilgisi web aramasıyla görüldü.
- **ENGELLİ:** `www.bmj.com` (Sterne ve ark., 2011 tam metni), `researchonline.lshtm.ac.uk`, `educationandscience.ted.org.tr` (Üstün ve Eryılmaz, 2014 tam metni), `www.sportsci.org` (Hopkins ve ark., 2009 serbest sürümü).
- Web araması (WebSearch): çalışıyor; yalnız sürüm bilgisi ve ipucu için kullanıldı, hiçbir künye yalnız aramaya dayanmıyor.

## 3. İçerik

> Biçim: her kavram için **Ne demek** (sade Türkçe) ve **Neden önemli** (yorumda). Doğrudan alıntılar İngilizce, tırnak içinde, denetim için. Kanıt düzeyi kaynak tablosunda (bölüm 5).

### 3.1 Tanım ve terimin kökeni (slayt 7)

- **Ne demek:** Meta-analiz, aynı soruyu inceleyen iki ya da daha çok çalışmanın etki tahminlerini istatistiksel olarak birleştirip tek bir nicel özet üreten tekniktir. PRISMA 2020 sözlüğü birebir: "Meta-analysis of effect estimates: A statistical technique used to synthesise results when study effect estimates and their variances are available, yielding a quantitative summary of results" (Page ve ark., 2021, Box 1 "Glossary of terms"). Türkçe tanım: "bir konu, tema ya da çalışma alanı hakkındaki benzer çalışmaların belirli ölçütler altında gruplanıp, bu çalışmalara ait nicel bulguların birleştirilerek yorumlanmasına, uygulamanın etkisini belirlemeye meta-analiz denir" (Dinçer, 2018, s. 186, Dinçer 2014'ten aktararak). Göktaş (2023) da meta-analizi "belirli bir konuda yapılmış olan çalışmaların bulgularını sistematik bir çerçevede birleştiren ... nicel bir inceleme yöntemi" olarak tanımlar (öz).
- **Neden önemli:** Tanımdaki iki koşul uygulamanın sınırını çizer: (1) her çalışmadan bir etki tahmini **ve onun varyansı** gerekir; (2) çıktı nicel bir özettir. Nitel veriyle meta-analiz yapılmaz (Dinçer, 2018, s. 186). Bu, "meta-analiz = istatistiksel sentez tekniği" demektir, bir derleme türü değil (tuzak 2).
- **Terimin kökeni:** Terimi Gene V. Glass ortaya attı ve 1976'da AERA başkanlık konuşmasında "analizlerin analizi" olarak kullandı. Clarke (2018) birebir: "The term meta-analysis was coined by Gene Glass in the mid-1970s and used in his American Educational Research Association presidential address in April 1976, describing it as 'the analysis of analyses'". Konuşmanın yayımlanmış hâli: Glass (1976), *Educational Researcher, 5*(10), 3-8 (künye Crossref ile doğrulandı; metin okunmadı). Clarke (2018) aynı yerde Pearson'ın 1904'te tifo aşısı çalışmalarını birleştirdiğini de not eder; yani yöntemin fikri terimden eskidir.
- **Cochrane El Kitabı bölüm 10 ve Borenstein ve ark. (2021):** El Kitabı'nın güncel sürümü 6.5 (2024), bölüm 10 yazarları Deeks, Higgins, Altman, McKenzie ve Veroniki (web aramasıyla görüldü; site engelli olduğu için tanım cümlesi birebir alınamadı). Basılı 2019 sürümünde bölüm 10 künyesi Crossref ile doğrulandı (s. 241-284). Borenstein ve ark. (2021) 2. baskı künyesi Crossref ile doğrulandı, metin okunmadı. **Slayttaki tanım için birebir doğrulanmış kaynak olarak Page ve ark. (2021) önerilir**; El Kitabı ve Borenstein ek atıf olarak verilebilir ama bunlardan cümle alıntılanmamalı.

### 3.2 Sistematik derlemeyle ilişkisi ve uygulanma koşulları (slayt 7)

- **Ne demek:** Sistematik derleme bir **süreçtir** (soru, protokol, arama, seçim, yanlılık değerlendirmesi, sentez); meta-analiz bu sürecin sentez adımında kullanılabilecek **istatistiksel tekniklerden biridir**. PRISMA 2020 birebir: "Systematic review: A review that uses explicit, systematic methods to collate and synthesise findings of studies that address a clearly formulated question" ve "Statistical synthesis: The combination of quantitative results of two or more studies. This encompasses meta-analysis of effect estimates ... and other methods, such as combining P values, calculating the range and distribution of observed effects, and vote counting based on the direction of effect" (Page ve ark., 2021, Box 1).
- **Her SR'de gerekmez:** PRISMA 2020, sentez içermeyen derlemelerin de kapsamda olduğunu yazar: "... or do not include synthesis (for example, because only one eligible study is identified)" (Page ve ark., 2021). Meta-analiz yapılamayan ya da uygun olmayan durumlar için ayrı bir raporlama kılavuzu vardır: "The SWiM guideline is intended for use in systematic reviews examining the quantitative effects of interventions for which meta-analysis of effect estimates is not possible, or not appropriate, for a least some outcomes" (Campbell ve ark., 2020; "a least" yazım hatası kaynakta böyle).
- **Ne zaman uygun değil (elma ile armut):** SWiM birebir: "Such situations may arise when effect estimates are incompletely reported or because characteristics of studies (such as study designs, intervention types, or outcomes) are too diverse to yield a meaningful summary estimate of effect" (Campbell ve ark., 2020). Türkçe kaynakta aynı eleştiri: farklı durumlardaki çalışmaları tek sonuçta birleştirmenin "elmalar ve armutlar" sorunu olarak anıldığı ve yanlış bulgulara yol açabileceği (Dinçer, 2018, s. 185; Borenstein ve ark.'nın Türkçe çevirisine dayanarak).
- **Ne zaman uygun (sade özet, yukarıdaki iki kaynaktan çıkarım):** (a) çalışmalar benzer PICO sorusunu soruyor; (b) sonuç aynı ya da dönüştürülebilir bir etki ölçüsüyle raporlanmış ve her çalışmadan etki tahmini ile varyansı alınabiliyor; (c) klinik ve yöntemsel çeşitlilik tek bir özet etkiyi anlamsız kılacak kadar büyük değil. Koşullar sağlanmazsa yapılandırılmış anlatısal sentez (SWiM) seçilir (Campbell ve ark., 2020; Page ve ark., 2021).
- **SR olmadan yapılan meta-analizin sorunu (tuzak 2):** İstatistik, girdinin seçilme biçimini düzeltemez. Çalışmalar sistematik ve önceden tanımlı bir aramayla değil de eldekilerden ya da yayımlanmış "olumlu" sonuçlardan seçilirse özet etki yanlı olur. Bunun ampirik işareti: Egger ve ark. (1997) sekiz "meta-analiz ve sonraki büyük deneme" çiftinin dördünde uyuşmazlık buldu ve "In all cases discordance was due to meta-analyses showing larger effects" (özet). (Not: Egger ve ark. bunu SR yapılmamasına değil, genel olarak yanlılığa bağlar; "SR olmadan" yorumu bu raporun çıkarımıdır, slaytta "seçim yanlılığı istatistikle düzelmez" diye genel söylenmeli.)
- **Neden önemli (yorumda):** Dinleyici "meta-analiz = SR" ya da "SR'de mutlaka meta-analiz olur" sanmamalı. Bir SR'nin meta-analiz içermemesi bir eksiklik değil, çoğu zaman doğru karardır; tersine, sistematik arama olmadan yapılan bir meta-analizin dar güven aralığı yanıltıcı bir kesinlik izlenimi verir.

### 3.3 Etki büyüklüğü (ES), Cohen's d ve Hedges' g (slayt 8)

- **Ne demek (ES):** Etkinin **ne kadar büyük** olduğunu ölçek biriminden bağımsız gösteren sayı. Standartlaştırılmış ortalama farkı (SMD): iki grubun ortalama farkı, ortak standart sapmaya bölünür. Lakens (2013) birebir: "Cohen's d is used to describe the standardized mean difference of an effect. This value can be used to compare effects across studies, even when the dependent variables are measured in different ways".
- **Neden p değeri yetmez:** p yalnız "sıfır etki varsayımı altında bu veri ne kadar şaşırtıcı?" sorusunu yanıtlar; etkinin büyüklüğünü ve pratik önemini söylemez, örneklem büyüdükçe küçük farklar da anlamlı çıkar. ES ise pratik önemi iletir ve çalışmalar arası birleştirmeyi mümkün kılar: "Such standardized effect sizes allow researchers to communicate the practical significance of their results ..., instead of only reporting the statistical significance" ve "effect sizes allow researchers to draw meta-analytic conclusions by comparing standardized effect sizes across studies" (Lakens, 2013). Spor bilimi yönünden Hopkins ve ark. (2009, özet), çıkarımda "precision of estimation ... in preference to null-hypothesis testing, which is inadequate for assessing clinical or practical importance" yaklaşımını savunur. **Meta-analiz p değerlerini değil, ES ve varyanslarını birleştirir** (Page ve ark., 2021, Box 1 tanımı).
- **Cohen's d ve Hedges' g (tuzak 5):** d küçük örneklemde gerçek etkiyi hafifçe **büyük tahmin eder** (yukarı yanlı); Hedges' g bu yanlılığı düzelten çarpanla elde edilir. Lakens (2013) birebir: "the formula for Cohen's d_s, which is based on sample averages gives a biased estimate of the population effect size (Hedges and Olkin, 1985), especially for small samples (n < 20)" ve "the correction for Cohen's d is known as Hedges' g". Formül (Lakens, 2013, denklem 4): **g = d × [1 − 3 / (4(n1 + n2) − 9)]**. Kökeni: Hedges (1981), Glass'ın ES kestiricisinin dağılım kuramı (künye Crossref ile doğrulandı, metin okunmadı).
  - Sayısal sezgi (bu raporun hesabı, hesap.py): 10+10 kişilik bir çalışmada çarpan 0,958 (d = 1,10 iken g = 1,05); 40+40 kişide 0,990. Yani düzeltme küçük örneklemde anlamlı, büyük örneklemde ihmal edilebilir. Spor bilimlerinde grup başına 8 ile 15 kişilik deneyler yaygın olduğundan g tercih edilir.
- **Cohen'in 0,2 / 0,5 / 0,8 gelenekleri ve sınırı:** Lakens (2013) birebir: "A commonly used interpretation is to refer to effect sizes as small (d = 0.2), medium (d = 0.5), and large (d = 0.8) based on benchmarks suggested by Cohen (1988). However, these values are arbitrary and should not be interpreted rigidly" ve "Small effect sizes can have large consequences, such as an intervention that leads to a reliable reduction in suicide rates with an effect size of d = 0.1. The only reason to use these benchmarks is because findings are extremely novel, and cannot be compared to related findings in the literature". Cohen (1988) kitabının künyesi doğrulandı (Routledge yeniden basımı Crossref'te), sayfası okunmadı; bu yüzden eşikler Lakens (2013) aracılığıyla atfedilmeli: "(Cohen, 1988; aktaran Lakens, 2013)".
- **Hopkins ve ark. (2009) spor eşikleri:** Makalenin künyesi ve özeti doğrulandı; ancak özet eşik değerlerini içermiyor ve tam metin (MSSE ve sportsci.org) bu oturumda erişilemedi. Önceki koşunun aktardığı 0,20 / 0,60 / 1,20 / 2,0 / 4,0 değerleri **bu koşuda birebir doğrulanamadı**. Slayta sayı olarak konmamalı; yalnız "spor biliminde alana özgü daha yüksek eşikler önerilmiştir (Hopkins ve ark., 2009)" denebilir, o da m5/m6 kararı. Ayrıca sayfa aralığı kaynaklar arasında çelişkili: Crossref 3-12, PubMed 3-13.
- **Oran türü ölçütler (tek cümle):** İkili sonuçlarda (sakatlandı/sakatlanmadı) etki risk oranı (RR) ya da olasılık oranı (OR) ile verilir; burada "etki yok" değeri 0 değil **1**'dir ve analiz log ölçeğinde yapılır (PRISMA 2020 sözlüğü "risk ratio"yu nokta tahmini örneği olarak anar, Page ve ark., 2021; log ölçeği bilgisi standart yöntem bilgisidir, ayrı kaynakla birebir doğrulanmadı).
- **Neden önemli (yorumda):** Forest plotta okunan her sayı bir ES'dir. Dinleyicinin "g = 0,39 ne demek?" sorusuna "deney grubu kontrolden yaklaşık 0,4 standart sapma daha iyi" diye cevap verebilmesi, slayt 9'un okunabilmesinin ön koşulu.

### 3.4 %95 güven aralığı ve ağırlıklandırma (slayt 8)

- **Ne demek (GA):** Bir etki tahmininin ne kadar **kesin** olduğunu gösteren aralık. Dar GA = kesin tahmin (genellikle büyük örneklem); geniş GA = belirsiz tahmin. PRISMA 2020 bir "sonucu" tam da böyle tanımlar: "Result: The combination of a point estimate (such as a mean difference, risk ratio, or proportion) and a measure of its precision (such as a confidence/credible interval)" (Page ve ark., 2021, Box 1). GA "etki yok" değerini (SMD için 0, OR/RR için 1) içeriyorsa o tahmin tek başına istatistiksel olarak anlamlı değildir.
- **Ne demek (ters varyans ağırlığı):** Meta-analiz basit ortalama almaz; her çalışmaya **varyansının tersi** kadar ağırlık verir. Rücker ve ark. (2008) birebir: "we always use inverse variance weights, that is, w_i = 1/s_i² if the fixed effect model is used, and w_i = 1/(s_i² + τ²) if the random effects model is used". Varyans küçükse (kesin, büyük çalışma) ağırlık büyüktür.
- **Neden önemli (yorumda):** (1) Forest plotta kare boyutu bu ağırlıktır; "kaç çalışma anlamlı?" diye oy saymak yerine çalışmalar kesinliklerine göre tartılır. (2) Birleştirme toplam bilgiyi artırdığı için özet GA tek tek çalışmalarınkinden daralır: kurgu örnekte (bölüm 3.7) altı çalışmanın üçünün GA'sı 0'ı içerirken özet GA 0,05 ile 0,74 aralığında kalıyor. (3) Formüldeki τ² terimi, bir sonraki maddedeki model seçiminin ağırlıkları nasıl değiştirdiğini açıklar.

### 3.5 Sabit etkiler ve rastgele etkiler modeli (slayt 8; tuzak 3)

- **Ne demek:**
  - **Sabit etki (fixed-effect):** Bütün çalışmaların altında **tek bir gerçek etki** vardır; gözlenen farkların tamamı örnekleme hatasıdır.
  - **Rastgele etkiler (random-effects):** Gerçek etki çalışmadan çalışmaya **değişir** (farklı yaş, branş, protokol); özet, bu gerçek etkiler dağılımının **ortalamasıdır**. DerSimonian ve Laird (1986, özet) yaklaşımı böyle tanımlar: "This approach incorporates the heterogeneity of effects in the analysis of the overall treatment efficacy" ve "We suggest a simple noniterative procedure for characterizing the distribution of treatment effects in a series of studies".
  - Borenstein ve ark. (2010, özet) birebir: "The fact that these two models employ similar sets of formulas to compute statistics, and sometimes yield similar estimates for the various parameters, may lead people to believe that the models are interchangeable. In fact, though, the models represent fundamentally different assumptions about the data" ve "the model serves to place the analysis in context. It provides a framework for the goals of the analysis as well as for the interpretation of the statistics".
- **Ağırlıklara etkisi:** Rastgele etkiler ağırlığı 1/(s_i² + τ²) olduğundan (Rücker ve ark., 2008), τ² > 0 iken her çalışmaya aynı sabit eklenir ve ağırlıklar **birbirine yaklaşır**: büyük çalışmaların payı azalır, küçüklerinki artar; özet GA genişler. Kurgu örnekte en büyük çalışma F'nin ağırlığı sabit etkide %30,9 iken rastgele etkilerde %23,4; en küçük çalışma A'nınki %7,4'ten %10,6'ya çıkıyor; özet GA 0,14 ile 0,63'ten 0,05 ile 0,74'e genişliyor (hesap.py).
- **Seçim teste göre değil varsayıma göre (tuzak 3):** Cochrane El Kitabı 5.0.1, bölüm 9.5.4 birebir (Rücker ve ark., 2008'in aktarımıyla): "The choice between a fixed-effect and a random-effects meta-analysis should never be made on the basis of a statistical test of heterogeneity". Model, verinin nasıl üretildiğine dair **önceden** yapılan varsayımla (ve protokolde) seçilir: çalışmalar aynı popülasyon ve protokolle yapılmış "kopyalar" değilse ve sonuç başka ortamlara genellenecekse rastgele etkiler daha gerçekçidir (Borenstein ve ark., 2010, özetteki "factors to consider when choosing between the two models" vurgusu; ayrıntılı ölçütler tam metinde, okunmadı).
- **Rastgele etkiler heterojenliği açıklamaz:** Model, heterojenliği yalnız belirsizliğe (daha geniş GA) yansıtır; nedenini bulmak için alt grup analizi ya da meta-regresyon gerekir (bölüm 3.6 son madde). Bu ifade DerSimonian ve Laird'in (1986, özet) "The model can be extended to include relevant covariates which would reduce the heterogeneity" cümlesiyle uyumlu: açıklama için ek değişken gerekir.
- **Neden önemli (yorumda):** Aynı veri iki modelde farklı soru yanıtlar: sabit etki "ortak etki nedir?", rastgele etkiler "etkilerin ortalaması nedir ve ne kadar yayılıyor?". Modelin "heterojenlik anlamlı çıktı, rastgeleye geçtik" diye seçildiği bir makale yöntemsel olarak zayıftır.

### 3.6 Heterojenlik: Q, τ², I², tahmin aralığı (slayt 8; tuzak 4)

- **Cochran Q · Ne demek:** Her çalışmanın özet etkiden sapmasının, ağırlıkla çarpılmış karelerinin toplamı; "farklar şansla açıklanabilir mi?" testidir. "Q, under the null hypothesis of no heterogeneity follows a χ² distribution with k − 1 degrees of freedom" (Rücker ve ark., 2008). **Neden önemli:** Az çalışmada gücü düşüktür; anlamsız Q homojenlik kanıtı değildir. Higgins ve ark. (2003) birebir: "The test is known to be poor at detecting true heterogeneity among studies as significant. Meta-analyses often include small numbers of studies, and the power of the test in such circumstances is low". Kurgu örnekte Q = 9,16, sd = 5, p = 0,10: test anlamsız ama I² %45 (bölüm 3.7).
- **τ² (tau kare) · Ne demek:** Gerçek etkilerin çalışmalar arası **varyansı**; etki ölçüsünün biriminin karesindedir (τ ise aynı birimde, SMD için standart sapma birimi). Rücker ve ark. (2008) DerSimonian-Laird moment kestiricisini verir: τ² = max{0, [Q − (k − 1)] / [Σw_i − Σw_i²/Σw_i]}. **Neden önemli:** Heterojenliğin **mutlak** büyüklüğüdür ve çalışmaların örneklem büyüklüğünden etkilenmez: "As precision increases, while estimates of the heterogeneity variance τ² remain unchanged on average, estimates of I² increase rapidly to nearly 100%" ve "τ², rather than I², is the appropriate measure for this purpose" (Rücker ve ark., 2008, özet).
- **I² · Ne demek:** Toplam gözlenen değişkenliğin örnekleme hatasından değil gerçek farklılıktan kaynaklanan **yüzdesi**. Higgins ve Thompson (2002, özet) birebir: "I² is a transformation of (H) that describes the proportion of total variation in study estimates that is due to heterogeneity". Formül: I² = max{0, (Q − sd) / Q} × %100 (Rücker ve ark., 2008; Higgins ve ark., 2003).
  - **Kaba etiketler (Higgins ve ark., 2003, birebir, tam metin):** "A naive categorisation of values for I² would not be appropriate for all circumstances, although we would tentatively assign adjectives of low, moderate, and high to I² values of 25%, 50%, and 75%". Yani etiketler "tentatively" (çekinceyle) verildi, kesin eşik değil.
  - **Cochrane'in örtüşen aralıkları (El Kitabı 5.0.1, Rücker ve ark., 2008 Tablo 3'teki birebir aktarım):** "0% to 40% might not be important; 30% to 60% may represent moderate heterogeneity; 50% to 90% may represent substantial heterogeneity; 75% to 100% considerable heterogeneity". El Kitabı bunları "a rough guide to interpretation" olarak sunar ve "thresholds for the interpretation of I² can be misleading, since the importance of inconsistency depends on several factors" uyarısını yapar (aynı aktarım). **Sınır:** Bu birebir ifade 5.0.1 sürümüne aittir; güncel 6.5 sürümündeki metin site engeli nedeniyle okunamadı. Aralıkların güncel sürümde de aynı olduğu web arama özetlerinde görüldü ama birebir doğrulanmadı. Slaytta "Cochrane El Kitabı'nın kaba rehberi (sürüm 5.0.1; aktaran Rücker ve ark., 2008)" diye atıf önerilir.
  - **I² mutlak ölçü değil (Borenstein ve ark., 2017, özet, birebir):** "If an intervention yields a mean effect size of 50 points, we want to know if the effect size in different populations varies from 40 to 60, or from 10 to 90 ... While there is a common belief that the I² statistic provides this information, it actually does not. In this example, if we are told that I² is 50%, we have no way of knowing if the effects range from 40 to 60, or from 10 to 90". Çözüm önerileri: "if we want to communicate the predicted range of effects, then we should simply report this range".
  - **Çalışma sayısı ve kesinliğe duyarlılık:** I² kesinliğe (çalışmaların büyüklüğüne) bağlıdır; aynı τ² ile çalışmalar büyüdükçe I² %100'e yaklaşır (Rücker ve ark., 2008). Higgins ve ark. (2003) I²'nin "Does not inherently depend on the number of studies in the meta-analysis" olduğunu yazar; ancak az çalışmada I² tahmininin kendisi belirsizdir ve GA'sı geniştir (Higgins ve ark., 2003, "Can be accompanied by an uncertainty interval"). Kısa söylem: **I² oran, τ² büyüklük.**
- **Tahmin aralığı (prediction interval, PI) · Ne demek:** "Benzer yeni bir ortamda gerçek etki büyük olasılıkla nerede olur?" sorusunun cevabı. IntHout ve ark. (2016, özet, birebir): "This variability is reflected by measures like τ² or I², but their clinical interpretation is not straightforward. A prediction interval is less complicated: it presents the expected range of true effects in similar studies". **Neden önemli:** GA "ortalama etki nerede?" der, PI "etkiler ne kadar yayılıyor?" der. Heterojenlik varsa PI, GA'dan geniştir ve farklı sonuca götürebilir: Cochrane veri tabanındaki anlamlı ve heterojen 479 meta-analizin "%72,4"ünde PI etkinin sıfır ya da ters yönde olabileceğini gösterdi (IntHout ve ark., 2016: "In 72.4% of 479 statistically significant (random-effects p<0.05) meta-analyses ... the 95% prediction interval suggested that the intervention effect could be null or even be in the opposite direction"). Öneri: "Prediction intervals should be routinely reported to allow more informative inferences in meta-analyses". Sınırı: az ve küçük çalışmaya dayanırsa PI de belirsizdir ve normallik varsayımına dayanır (IntHout ve ark., 2016, "Strengths and limitations").
- **Alt grup analizi ve meta-regresyon (bir cümle):** Heterojenliğin kaynağını aramak için çalışmalar bir özelliğe göre gruplanır (alt grup, ör. elit ve amatör) ya da etki sürekli bir çalışma özelliğine (ör. antrenman haftası) göre regrese edilir (meta-regresyon); bunlar çalışma düzeyinde gözlemsel karşılaştırmalardır, nedensellik kanıtı sayılmaz (bu son ifade genel yöntem bilgisidir, bu koşuda birebir kaynakla doğrulanmadı; dayanaklar: DerSimonian ve Laird, 1986 özetindeki "covariates" fikri; Higgins ve ark., 2003 tam metninde tedavi süresine göre açıklanan heterojenlik örneği: I² %50'den %13'e).

### 3.7 Forest plot nasıl okunur ve kurgu veri (slayt 9)

**Okuma anahtarı** (genel düzen; gerçek bir örnek: IntHout ve ark., 2016, Şekil 1, nazal polip için steroid ve plasebo, SMD forest plotu, elmasın altında tahmin aralığını gösteren dikdörtgenle: "We present it in figure 1 as a rectangle below the diamond for the 95% CI"):

| Öğe | Ne demek | Yorumda neden önemli |
|---|---|---|
| Satır | Bir çalışma (adı solda, sayısal ES ve %95 GA sağda) | Hangi çalışmaların dahil edildiğini şeffaf gösterir |
| Kare | Çalışmanın nokta tahmini (ES) | Etkinin yönü ve büyüklüğü |
| Kare boyutu | Çalışmanın meta-analizdeki ağırlığı (ters varyans; Rücker ve ark., 2008) | Büyük kare = kesin çalışma; sonucu en çok o belirler |
| Yatay çizgi | Çalışmanın %95 GA'sı | Uzun çizgi = belirsiz tahmin; çizgi dikey sıfır çizgisini kesiyorsa çalışma tek başına anlamsız |
| Dikey çizgi | "Etki yok" değeri (SMD için 0, OR/RR için 1) | Sağ/sol tarafın hangi grubu desteklediği eksende yazılı olmalı |
| Elmas | Özet etki: ortası nokta tahmini, iki ucu %95 GA | Elmas sıfır çizgisine değmiyorsa özet etki anlamlı |
| Elmasın altındaki çubuk/dikdörtgen | %95 tahmin aralığı (IntHout ve ark., 2016) | Yeni bir ortamda etkinin ne kadar değişebileceği |
| Alt bilgi | Model, Q (sd, p), τ², I² | Heterojenliğin hem oranını hem büyüklüğünü okumak için |

**EĞİTİM AMAÇLI KURGU VERİ. Gerçek çalışmalar değildir; slaytta "Kurgu veri · eğitim amaçlı" etiketi zorunlu.**
Senaryo (kurgu): pliometrik antrenmanın dikey sıçrama yüksekliğine etkisi, deney ve kontrol grubu son test karşılaştırması. Etki ölçüsü Hedges' g (pozitif = deney grubu lehine). Her çalışmada gruplar eşit büyüklükte (n/2 + n/2). Cohen d değerleri seçildi; g, SE, GA, ağırlıklar ve özet aşağıdaki betikle **gerçekten hesaplandı**: `isler/m3-meta-analiz/hesap.py` (yalnız Python standart kütüphanesi; çalıştırma: `python3 hesap.py`).

Formüller (betikteki): d'nin varyansı v_d = (n1 + n2)/(n1·n2) + d²/[2(n1 + n2)]; J = 1 − 3/(4·sd − 1), sd = n1 + n2 − 2 (Lakens 2013 denklem 4 ile özdeş); g = J·d; v_g = J²·v_d; %95 GA = g ± 1,96·SE. Sabit etki ağırlığı 1/v, DerSimonian-Laird τ² ve rastgele etkiler ağırlığı 1/(v + τ²) (Rücker ve ark., 2008 formülleri); I² = (Q − sd)/Q; tahmin aralığı = özet ± t(k−2; 0,975)·√(τ² + SE²) (t dağılımı, k − 2 serbestlik derecesi; bkz. bölüm 6 sınır notu).

Betiğin çekirdeği:

```python
def hedges(d, n1, n2):
    df = n1 + n2 - 2
    J = 1 - 3 / (4 * df - 1)
    vd = (n1 + n2) / (n1 * n2) + d * d / (2 * (n1 + n2))
    return J * d, J * J * vd, J

def meta(ys, vs):
    k = len(ys); w = [1 / v for v in vs]
    fe = sum(wi * y for wi, y in zip(w, ys)) / sum(w)
    Q = sum(wi * (y - fe) ** 2 for wi, y in zip(w, ys))
    C = sum(w) - sum(wi * wi for wi in w) / sum(w)
    tau2 = max(0.0, (Q - (k - 1)) / C)                 # DerSimonian-Laird
    I2 = max(0.0, (Q - (k - 1)) / Q) * 100
    ws = [1 / (v + tau2) for v in vs]                  # rastgele etkiler ağırlığı
    re = sum(wi * y for wi, y in zip(ws, ys)) / sum(ws)
    se_re = (1 / sum(ws)) ** 0.5
    tc = t_crit(k - 2)                                 # t(k-2; 0.975)
    pi = (re - tc * (tau2 + se_re**2) ** 0.5, re + tc * (tau2 + se_re**2) ** 0.5)
    ...
```

Betiğin çıktısı (birebir):

```text
FOREST (KURGU) · Hedges g · DerSimonian-Laird
| Çalışma | n (deney+kontrol) | Cohen d | J | Hedges g | SE | %95 GA | Ağırlık SE (%) | Ağırlık RE (%) |
|---|---|---|---|---|---|---|---|---|
| Çalışma A | 20 | 1.10 | 0.958 | 1.05 | 0.460 | 0.15 ile 1.95 | 7.4 | 10.6 |
| Çalışma B | 24 | -0.20 | 0.966 | -0.19 | 0.395 | -0.97 ile 0.58 | 10.0 | 13.0 |
| Çalışma C | 60 | 0.35 | 0.987 | 0.35 | 0.257 | -0.16 ile 0.85 | 23.7 | 21.0 |
| Çalışma D | 32 | 0.95 | 0.975 | 0.93 | 0.364 | 0.21 ile 1.64 | 11.8 | 14.5 |
| Çalışma E | 40 | -0.10 | 0.980 | -0.10 | 0.310 | -0.71 ile 0.51 | 16.2 | 17.4 |
| Çalışma F | 80 | 0.50 | 0.990 | 0.50 | 0.225 | 0.05 ile 0.94 | 30.9 | 23.4 |
Sabit etki özeti: g = 0.39, %95 GA 0.14 ile 0.63
Rastgele etkiler (DL) özeti: g = 0.39, SE = 0.176, %95 GA 0.05 ile 0.74, z = 2.23, p = 0.0260
Q = 9.16 (sd = 5), p = 0.103; tau^2 = 0.0819; tau = 0.286; I^2 = 45.4%
%95 tahmin aralığı (t, sd = k-2 = 4, t = 2.776): -0.54 ile 1.33
```

**m7 için çizime hazır tablo (kurgu, yuvarlanmış):**

| Çalışma (kurgu) | n | Hedges' g | %95 GA | Ağırlık, rastgele etkiler (%) |
|---|---|---|---|---|
| Çalışma A | 20 | 1,05 | 0,15 ile 1,95 | 10,6 |
| Çalışma B | 24 | −0,19 | −0,97 ile 0,58 | 13,0 |
| Çalışma C | 60 | 0,35 | −0,16 ile 0,85 | 21,0 |
| Çalışma D | 32 | 0,93 | 0,21 ile 1,64 | 14,5 |
| Çalışma E | 40 | −0,10 | −0,71 ile 0,51 | 17,4 |
| Çalışma F | 80 | 0,50 | 0,05 ile 0,94 | 23,4 |
| **Özet (rastgele etkiler, DL)** | **256** | **0,39** | **0,05 ile 0,74** | **100** |
| %95 tahmin aralığı | | | **−0,54 ile 1,33** | |

Alt bilgi satırı: Rastgele etkiler (DerSimonian-Laird) · Q = 9,16, sd = 5, p = 0,10 · τ² = 0,082 (τ = 0,29) · I² = %45 · Özet z = 2,23, p = 0,026. (Karşılaştırma için sabit etki özeti: g = 0,39, %95 GA 0,14 ile 0,63.)

Not: tabloda eksi işareti olarak matematik eksi (−) kullanıldı; slayt dosyasında normal kısa çizgi (-) de olur, uzun tire değil.

**Bu kurgu veriyle anlatılacak öğretici noktalar:**
1. B, C ve E tek başına anlamsız (çizgileri 0'ı kesiyor), ama elmas 0'ı kesmiyor: birleştirme kesinliği artırır.
2. A'nın etkisi en büyük ama çizgisi en uzun ve karesi en küçük; F en dar GA'lı, en büyük kare. Büyük etki ile güvenilir etki aynı şey değil.
3. Q anlamsız (p = 0,10) ama I² %45 ve τ = 0,29 SMD: altı çalışmayla Q testinin gücü düşük (Higgins ve ark., 2003). "Heterojenlik yok" denemez.
4. Özet GA tamamen pozitif (0,05 ile 0,74), ama tahmin aralığı (−0,54 ile 1,33) sıfırı içeriyor: ortalama etki olumlu, yine de yeni bir takımda/ortamda etkinin sıfır, hatta olumsuz olması dışlanamaz (IntHout ve ark., 2016'daki örüntünün aynısı).
5. Ağırlık kayması: rastgele etkilerde F'nin payı %30,9'dan %23,4'e iniyor, A'nınki %7,4'ten %10,6'ya çıkıyor (bölüm 3.5).

### 3.8 Funnel plot, yayın yanlılığı, Egger testi, trim-and-fill (slayt 9; tuzak 6)

- **Funnel plot · Ne demek:** Her çalışmanın ES'si yatay eksende, kesinliği (genellikle standart hata, ters çevrilmiş eksende; ya da örneklem büyüklüğü) dikey eksende gösterilir. Debray ve ark. (2018, tam metin) birebir: "for each included study of the meta-analysis, the estimate of the reported effect size is plotted against a measure of precision or sample size. The premise is that the scatter of plots should reflect a funnel shape, if small-study effects do not exist (provided that effect sizes are not substantially affected by the presence of between-study heterogeneity)". Egger ve ark. (1997, özet) ilk tanımda "plots of effect estimates against sample size" der.
- **Simetri beklentisi:** Büyük (kesin) çalışmalar tepede özet etkinin çevresinde dar, küçük çalışmalar tabanda geniş ve **iki yana simetrik** dağılır. "However, when small studies are predominately in one direction (usually the direction of larger effect sizes), asymmetry will ensue" (Debray ve ark., 2018).
- **Asimetrinin nedenleri (asimetri ≠ yayın yanlılığı):** Lin ve ark. (2020, tam metin) birebir: "Such asymmetry is sometimes termed as small-study effect, rather than publication bias, to remind meta-analysts that publication bias may not be the only cause of the asymmetry. Many other factors may also lead to an asymmetrical funnel plot (e.g., due to heterogeneity or simply by chance)" (bu cümle için Sterne ve ark., 2011'e atıf yapıyorlar). Yani nedenler: yayın yanlılığı, küçük çalışma etkileri (ör. küçük çalışmalarda daha düşük yöntem kalitesi ya da farklı popülasyon), gerçek heterojenlik, şans. Sterne ve ark. (2011) bu konudaki temel öneri makalesidir (künye Crossref ve PubMed ile doğrulandı, 19 yazar); **tam metni bu oturumda okunamadı** (bmj.com engelli, PubMed'de özet yok), bu yüzden içerik iddiaları Lin ve ark. (2020) ve Debray ve ark. (2018) üzerinden verildi.
- **Egger testi · Ne demek:** Asimetriyi regresyonla ölçer. Egger ve ark. (1997, özet) birebir: "Degree of funnel plot asymmetry as measured by the intercept from regression of standard normal deviates against precision". Yani g/SE, 1/SE'ye karşı regrese edilir; kesişim 0'dan uzaklaştıkça asimetri artar. Ampirik bulgu: dergilerdeki meta-analizlerin %38'inde, Cochrane derlemelerinin %13'ünde asimetri yanlılığa işaret etti (Egger ve ark., 1997, özet: "In 14 (38%) journal meta-analyses and 5 (13%) Cochrane reviews, funnel plot asymmetry indicated that there was bias").
  - **Sınırı:** Az ve küçük çalışmada gücü düşüktür. Egger ve ark. (1997, özet) birebir: "as the capacity to detect bias will be limited when meta-analyses are based on a limited number of small trials the results from such analyses should be treated with considerable caution". Debray ve ark. (2018): "our results demonstrate that the performance of funnel plot asymmetry tests is rather poor. Most tests yield inadequate type-I error rates or suffer from low power" (sağkalım verisi bağlamında).
- **Trim-and-fill · Ne demek:** Huni grafiğinin asimetrisinden "eksik" çalışma sayısını sıra tabanlı bir yöntemle kestirir, simetriyi bozan çalışmaları kırpar, eksik tarafı ayna görüntüleriyle doldurur ve düzeltilmiş özet etkiyi verir. Duval ve Tweedie (2000, özet) birebir: "nonparametric methods for estimating the number of missing studies that might exist in a meta-analysis and the effect that these studies might have had on its outcome. These are simple rank-based data augmentation techniques, which formalize the use of funnel plots". Lin ve ark. (2020) da yöntemi "Estimating the suppressed studies and thus correcting small-study effects based on funnel plot's asymmetry" diye özetler.
  - **Sınırı:** Yöntem, asimetrinin **tümünü** eksik (yayımlanmamış) çalışmalara bağlar; asimetri heterojenlik ya da şanstan kaynaklanıyorsa "düzeltme" yanıltıcı olur. Bu çıkarım yukarıdaki iki birebir ifadenin (trim-and-fill'in asimetriye dayanması ve asimetrinin başka nedenleri olabilmesi) birleşimidir (Duval ve Tweedie, 2000; Lin ve ark., 2020); ayrı bir kaynakta birebir okunmadı. Düzeltilmiş değer bir **duyarlılık analizi** olarak sunulmalı, "gerçek etki" diye değil.
- **En az çalışma sayısı (tuzak 6) · DURUM: birincil kaynaktan birebir DOĞRULANAMADI.** Birincil kaynaklar (Sterne ve ark., 2011; Cochrane El Kitabı) bu oturumda okunamadı. Hakemli ikincil kaynakta birebir görülen ifade: "Guidelines for conducting funnel plot asymmetry tests recommend to include at least 10 studies to maintain sufficient power for distinguishing chance from real asymmetry" (Debray ve ark., 2018; atıf yaptıkları kaynaklar Sterne ve ark., 2011; Sterne, Egger ve Moher'in Cochrane El Kitabı bölümü; Egger ve ark., 1997). Web arama özetleri aynı kuralın El Kitabı 5.1, bölüm 10.4.3.1'de "As a rule of thumb, tests for funnel plot asymmetry should be used only when there are at least 10 studies included in the meta-analysis" biçiminde geçtiğini gösteriyor, ama sayfa açılamadı. **Öneri (m5/m6):** Slayta ya hiç sayı koyma ("az çalışmada testlerin gücü düşüktür", Egger ve ark., 1997 birebir dayanağıyla) ya da "kılavuzlar genellikle en az 10 çalışma önerir (Debray ve ark., 2018)" diye ikincil atıfla koy. "Sterne ve ark. (2011) 10 çalışma der" diye birincil atıf yapma.

**EĞİTİM AMAÇLI KURGU FUNNEL VERİSİ (14 çalışma). Gerçek değildir; slaytta "Kurgu veri" etiketi zorunlu.** Aynı senaryo (pliometri, Hedges' g). Tasarım: büyük çalışmalar 0,40 civarında toplanıyor; küçük çalışmalarda (SE ≥ 0,26) etkiler sağa kaymış, sol alt köşe seyrek (tek nokta: No 12). Hesaplar hesap.py ile.

```text
FUNNEL (KURGU) · 14 çalışma
| No | Hedges g | SE |
|---|---|---|
| 1 | 0.42 | 0.08 |
| 2 | 0.36 | 0.10 |
| 3 | 0.47 | 0.12 |
| 4 | 0.30 | 0.14 |
| 5 | 0.52 | 0.16 |
| 6 | 0.38 | 0.18 |
| 7 | 0.58 | 0.21 |
| 8 | 0.24 | 0.23 |
| 9 | 0.66 | 0.26 |
| 10 | 0.50 | 0.28 |
| 11 | 0.74 | 0.31 |
| 12 | 0.20 | 0.33 |
| 13 | 0.86 | 0.36 |
| 14 | 0.70 | 0.39 |
Sabit etki özeti (huni ekseninin ortası): g = 0.43; RE (DL) g = 0.43; Q = 7.30, I^2 = 0.0%, tau^2 = 0.0000
Egger regresyonu: kesişim = 0.71 (SE 0.40), t = 1.75, sd = 12, p = 0.106; eğim = 0.33
```

Çizim notu (m7): yatay eksen Hedges' g (−0,4 ile 1,4 arası yeter), dikey eksen SE ters çevrilmiş (0 tepede, 0,45 tabanda); dikey çizgi özet g = 0,43; huni sınırları özet ± 1,96·SE (iki eğik çizgi). Funnel verisi forest verisinden bağımsız ikinci bir kurgu kümedir (forest 6 çalışma, funnel 14 çalışma); slaytta karıştırılmamalı.

**Bu kurgu veriyle anlatılacak öğretici noktalar:**
1. Göz asimetri görüyor (küçük çalışmalar sağda), Egger kesişimi 0,71 ama **p = 0,11, anlamsız**: 14 çalışmada bile test gücü sınırlı (Egger ve ark., 1997; Debray ve ark., 2018). "Test anlamsız, demek ki yanlılık yok" denemez; tersine, anlamlı olsaydı da "kesin yayın yanlılığı" denemezdi (Lin ve ark., 2020).
2. Bu veride I² = %0: asimetri heterojenlikten değil; geriye yayın yanlılığı, küçük çalışma etkileri ya da şans kalır. Ayırt etmek için çalışmaların yöntem kalitesine ve kayıtlı ama yayımlanmamış çalışmalara (kayıt sistemleri) bakılır.

### 3.9 Güçlü ve sınırlı yönler (slayt 9 sonu ya da slayt 10 tablosu için)

| Güçlü yön | Dayanak |
|---|---|
| Kesinlik artışı: birleşik tahminin GA'sı tek çalışmalarınkinden dar; tek başına anlamsız küçük çalışmalar birlikte bilgi verir | Ters varyans ağırlıklandırma (Rücker ve ark., 2008); kurgu örnek bölüm 3.7 |
| Tutarlılığı sınama: etkinin ortamlar arasında ne kadar değiştiği (τ², I², tahmin aralığı) nicel olarak görülür | Higgins ve ark. (2003); IntHout ve ark. (2016) |
| Heterojenliğin kaynağını araştırma (alt grup, meta-regresyon) | DerSimonian ve Laird (1986, özet: "covariates"); Higgins ve ark. (2003) tedavi süresi örneği |
| Şeffaf ve tekrarlanabilir nicel özet; PRISMA ile raporlanabilir | Page ve ark. (2021) |
| Türkçe kaynakta: araştırma sentezi yolları arasında en etkililerinden biri olarak konumlanır | Üstün ve Eryılmaz (2014, öz) |

| Sınırlı yön | Ne demek | Dayanak |
|---|---|---|
| Çöp girer, çöp çıkar | Birincil çalışmalar yanlıysa birleştirme yanlılığı ortadan kaldırmaz, daha kesin görünen yanlı bir sonuç üretir; bu yüzden SR içinde yanlılık riski değerlendirmesi gerekir | Egger ve ark. (1997): uyuşmazlıkların hepsinde meta-analiz daha büyük etki gösterdi; Üstün ve Eryılmaz (2014, öz: "birincil çalışmaların kalitesi gibi geçerlikle ilgili sorunlar") |
| Yayın yanlılığı | Yayımlanmış literatür "olumlu" sonuçlara kayıksa özet şişer; testleri zayıf | Egger ve ark. (1997); Debray ve ark. (2018); Lin ve ark. (2020) |
| Heterojenlik (elma ile armut) | Çok farklı çalışmaların ortalaması anlamsız olabilir; o zaman meta-analiz yerine SWiM | Campbell ve ark. (2020); Dinçer (2018, s. 185) |
| I²'nin yanlış okunması | I² oran; büyük çalışmalarda şişer, mutlak yayılımı söylemez | Rücker ve ark. (2008); Borenstein ve ark. (2017) |
| Ekolojik yanılgı | Meta-regresyon çalışma düzeyindeki ortalamaları ilişkilendirir; çalışma düzeyindeki ilişki bireyler için geçerli sayılamaz | **Bu koşuda okunan bir kaynakla birebir doğrulanmadı**; m5 kullanacaksa kaynak bulunmalı ya da madde çıkarılmalı |

### 3.10 Türkçe kaynaklar (Bölüm G gereği; en az 2)

| Kaynak | Ne içeriyor | Doğrulama | Kanıt düzeyi |
|---|---|---|---|
| Üstün ve Eryılmaz (2014), *Eğitim ve Bilim, 39*(174), 1-32 | Meta-analizin güçlü/zayıf yönleri, sabit ve rastgele etkiler, ES ölçüleri, yayın yanlılığı, birincil çalışma kalitesi, heterojenlik, ara değişken ve güç analizi, yazılımlar, raporlama standartları (öz) | Crossref (DOI 10.15390/EB.2014.3379; Crossref'te İngilizce başlıkla), TR Dizin kaydı (id 224530, Türkçe başlık ve öz) | özet okundu (tam metin sitesi engelli) |
| Dinçer (2018), *Bartın Üniversitesi Eğitim Fakültesi Dergisi, 7*(1), 176-190 | Meta-analiz, meta-sentez ve betimsel içerik analizinin ayrımı; Türkçe meta-analiz tanımı (s. 186); "elmalar ve armutlar" eleştirisi (s. 185); nitel veriyle meta-analiz yapılamayacağı (s. 186) | Crossref (DOI 10.14686/buefad.363159), DergiPark makale sayfası meta verisi | tam metin okundu (DergiPark PDF) |
| Göktaş (2023), *e-Şarkiyat İlmi Araştırmaları Dergisi, 15*(2), 732-746 | Meta-analizin tanımı, temel kavramlar, sabit ve rastgele etkiler modeli, etki büyüklüğünün yorumu, huni grafiği, uygulama aşamaları (öz ve bölüm başlıkları) | Crossref (DOI 10.26791/sarkiat.1349791), DergiPark meta verisi (cilt, sayı, sayfa), TR Dizin kaydı (id 1217798) | özet okundu (PDF'nin gövde metni yazı tipi kodlaması nedeniyle okunamadı; yalnız bölüm başlıkları görüldü) |
| Dinçer (2014) kitabı *Eğitim bilimlerinde uygulamalı meta-analiz* ve Borenstein ve ark.'nın Türkçe çevirisi *Meta-analize giriş* (çev. S. Dinçer, 2013, Anı Yayıncılık) | Türkçe ders kitabı ve çeviri | Yalnız Dinçer (2018) kaynakçasındaki künyeyle görüldü; yayıncı kaydı ve ISBN doğrulanmadı | yalnız künye (ikincil); kaynakçaya girmeden önce doğrulanmalı |

Sunuma önerilen Türkçe kaynaklar: **Üstün ve Eryılmaz (2014)** (meta-analiz yöntemine giriş, TR Dizin kayıtlı) ve **Dinçer (2018)** (Türkçe tanım ve "elma ile armut" eleştirisi, tam metin okundu). Göktaş (2023) yedek.

## 4. Sunuma önerilen çekirdek

### Slayt metnine girecek kısa ifadeler (8)

1. **Meta-analiz, çalışmaların etki tahminlerini ve varyanslarını birleştirerek nicel bir özet üreten istatistiksel tekniktir** (Page ve ark., 2021). Terim: Glass (1976), "analizlerin analizi" (Clarke, 2018).
2. **Her sistematik derleme meta-analiz içermez; çalışmalar çok farklıysa ya da veri eksikse meta-analizsiz sentez (SWiM) yapılır** (Campbell ve ark., 2020; Page ve ark., 2021).
3. **p değeri "var mı?", etki büyüklüğü "ne kadar?" sorusunu yanıtlar; meta-analiz etki büyüklüklerini birleştirir** (Lakens, 2013).
4. **Hedges' g, Cohen's d'nin küçük örneklem düzeltmeli biçimidir; 0,2 / 0,5 / 0,8 bağlamsız kaba geleneklerdir** (Cohen, 1988, aktaran Lakens, 2013).
5. **Sabit etki "tek gerçek etki", rastgele etkiler "etkilerin dağılımı" varsayar; seçim heterojenlik testine göre yapılmaz** (Borenstein ve ark., 2010; Cochrane El Kitabı 5.0.1, aktaran Rücker ve ark., 2008).
6. **I² bir orandır, heterojenliğin büyüklüğü değil; τ² ve tahmin aralığı birlikte raporlanmalı** (Borenstein ve ark., 2017; IntHout ve ark., 2016; Rücker ve ark., 2008).
7. **Forest plot: kare = çalışma etkisi, kare boyutu = ağırlık, çizgi = %95 GA, elmas = özet etki.** (Kurgu veri.)
8. **Funnel plot asimetrisi bir alarmdır, yayın yanlılığının kanıtı değil: heterojenlik ve şans da asimetri üretir** (Lin ve ark., 2020; Egger ve ark., 1997).

### Sunucu notu malzemesi

- **Slayt 7 (yaklaşık 55 sn):** "Sistematik derleme bir süreç, meta-analiz o sürecin içinde kullanılabilecek bir hesap tekniği" ayrımıyla aç. PRISMA 2020 sözlüğündeki iki tanımı yan yana göster (Page ve ark., 2021, Box 1). "Ne zaman yapılmaz" için SWiM'in birebir gerekçesi: çalışma tasarımları, müdahaleler ya da sonuçlar anlamlı bir özet için fazla farklıysa (Campbell ve ark., 2020). Türkçe "elma ile armut" eleştirisini Dinçer'den (2018) an. Sistematik arama yapılmadan seçilen çalışmaların meta-analizi için: "istatistik, seçim yanlılığını düzeltmez".
- **Slayt 8 (yaklaşık 1 dk 35 sn):** Sırayla: ES (ne kadar?), g (küçük örneklem düzeltmesi; 10+10 kişide çarpan 0,958), ağırlık (kesin çalışma daha çok söz hakkı alır), model (tek etki mi, dağılım mı?), heterojenlik üçlüsü. Benzetme önerisi (açıkça benzetme olarak söylenmeli): sabit etki aynı odanın sıcaklığını beş kez ölçmek, rastgele etkiler beş şehrin ortalama sıcaklığını sormak. I² için Borenstein ve ark.'nın (2017) örneği çok öğretici: "I² %50" bilgisi etkilerin 40 ile 60 mı, 10 ile 90 mı yayıldığını söylemez.
- **Slayt 9 (yaklaşık 1 dk 15 sn):** Kurgu forest plotta gözü önce elmasa, sonra sıfır çizgisine, sonra tahmin aralığına götür. Mesaj: "ortalama olumlu (GA 0,05 ile 0,74), ama yeni bir takımda etki sıfır ya da olumsuz olabilir (PI −0,54 ile 1,33)". Gerçek bir örnek istenirse IntHout ve ark.'nın (2016) Şekil 1'i: Cochrane'den alınmış steroid ve plasebo forest plotu, SMD −0,51, tahmin aralığı −1,60 ile 0,58. Funnel plotta: "Egger p = 0,11, ama göz asimetri görüyor: test zayıf; anlamlı çıksaydı da kesin yanlılık demezdik".
- **Dekan sorarsa:** "En az 10 çalışma kuralı nereden?" Cevap: kılavuzlarda geçen bir başparmak kuralı; hakemli bir yöntem makalesi "Guidelines ... recommend to include at least 10 studies" diye aktarıyor (Debray ve ark., 2018). Birincil kaynak (Sterne ve ark., 2011; Cochrane El Kitabı) bu çalışmada okunamadı.

## 5. Kaynak tablosu

| # | Kısa ad | APA 7 künye | DOI | Doğrulama yolu | Kanıt düzeyi | Türkçe |
|---|---|---|---|---|---|---|
| 1 | Page ve ark., 2021 | Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. | 10.1136/bmj.n71 | Crossref (26 yazar), PubMed 33782057, Europe PMC PMC8005924 | tam metin okundu (Box 1 ve kapsam bölümü) | Hayır |
| 2 | Campbell ve ark., 2020 | Campbell, M., McKenzie, J. E., Sowden, A., Katikireddi, S. V., Brennan, S. E., Ellis, S., Hartmann-Boyce, J., Ryan, R., Shepperd, S., Thomas, J., Welch, V., & Thomson, H. (2020). Synthesis without meta-analysis (SWiM) in systematic reviews: Reporting guideline. *BMJ, 368*, l6890. | 10.1136/bmj.l6890 | Crossref, PubMed 31948937, PMC7190266 | tam metin okundu | Hayır |
| 3 | Clarke, 2018 | Clarke, M. (2018). Partially systematic thoughts on the history of systematic reviews. *Systematic Reviews, 7*, Article 176. | 10.1186/s13643-018-0833-3 | Crossref, PubMed 30368251, PMC6204283 | tam metin okundu | Hayır |
| 4 | Glass, 1976 | Glass, G. V. (1976). Primary, secondary, and meta-analysis of research. *Educational Researcher, 5*(10), 3-8. | 10.3102/0013189X005010003 | Crossref | yalnız künye doğrulandı | Hayır |
| 5 | Lakens, 2013 | Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: A practical primer for t-tests and ANOVAs. *Frontiers in Psychology, 4*, Article 863. | 10.3389/fpsyg.2013.00863 | Crossref, PubMed 24324449, PMC3840331 | tam metin okundu | Hayır |
| 6 | Hedges, 1981 | Hedges, L. V. (1981). Distribution theory for Glass's estimator of effect size and related estimators. *Journal of Educational Statistics, 6*(2), 107-128. | 10.3102/10769986006002107 | Crossref | yalnız künye doğrulandı | Hayır |
| 7 | Cohen, 1988 | Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates. | (basılı 1988 baskısının DOI'si yok; Routledge 2013 e-kitap yeniden basımı 10.4324/9780203771587) | Crossref (yeniden basım kaydı); 1988 baskı bilgisi Lakens (2013) kaynakçasından | yalnız künye doğrulandı | Hayır |
| 8 | Hopkins ve ark., 2009 | Hopkins, W. G., Marshall, S. W., Batterham, A. M., & Hanin, J. (2009). Progressive statistics for studies in sports medicine and exercise science. *Medicine & Science in Sports & Exercise, 41*(1), 3-12. | 10.1249/MSS.0b013e31818cb278 | Crossref (s. 3-12), PubMed 19092709 (s. 3-13: çelişki) | özet okundu | Hayır |
| 9 | Borenstein ve ark., 2010 | Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2010). A basic introduction to fixed-effect and random-effects models for meta-analysis. *Research Synthesis Methods, 1*(2), 97-111. | 10.1002/jrsm.12 | Crossref, PubMed 26061376 | özet okundu | Hayır |
| 10 | DerSimonian ve Laird, 1986 | DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials, 7*(3), 177-188. | 10.1016/0197-2456(86)90046-2 | Crossref, PubMed 3802833 | özet okundu | Hayır |
| 11 | Rücker ve ark., 2008 | Rücker, G., Schwarzer, G., Carpenter, J. R., & Schumacher, M. (2008). Undue reliance on I² in assessing heterogeneity may mislead. *BMC Medical Research Methodology, 8*, Article 79. | 10.1186/1471-2288-8-79 | Crossref, PubMed 19036172, PMC2648991 | tam metin okundu | Hayır |
| 12 | Higgins ve Thompson, 2002 | Higgins, J. P. T., & Thompson, S. G. (2002). Quantifying heterogeneity in a meta-analysis. *Statistics in Medicine, 21*(11), 1539-1558. | 10.1002/sim.1186 | Crossref, PubMed 12111919 | özet okundu | Hayır |
| 13 | Higgins ve ark., 2003 | Higgins, J. P. T., Thompson, S. G., Deeks, J. J., & Altman, D. G. (2003). Measuring inconsistency in meta-analyses. *BMJ, 327*(7414), 557-560. | 10.1136/bmj.327.7414.557 | Crossref, PubMed 12958120, PMC192859 | tam metin okundu | Hayır |
| 14 | Borenstein ve ark., 2017 | Borenstein, M., Higgins, J. P. T., Hedges, L. V., & Rothstein, H. R. (2017). Basics of meta-analysis: I² is not an absolute measure of heterogeneity. *Research Synthesis Methods, 8*(1), 5-18. | 10.1002/jrsm.1230 | Crossref, PubMed 28058794 | özet okundu | Hayır |
| 15 | IntHout ve ark., 2016 | IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), Article e010247. | 10.1136/bmjopen-2015-010247 | Crossref, PubMed 27406637, Europe PMC PMC4947751 | tam metin okundu (çevrimiçi ek okunmadı) | Hayır |
| 16 | Egger ve ark., 1997 | Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109), 629-634. | 10.1136/bmj.315.7109.629 | Crossref, PubMed 9310563 | özet okundu (PMC kaydı taranmış görüntü) | Hayır |
| 17 | Sterne ve ark., 2011 | Sterne, J. A. C., Sutton, A. J., Ioannidis, J. P. A., Terrin, N., Jones, D. R., Lau, J., Carpenter, J., Rücker, G., Harbord, R. M., Schmid, C. H., Tetzlaff, J., Deeks, J. J., Peters, J., Macaskill, P., Schwarzer, G., Duval, S., Altman, D. G., Moher, D., & Higgins, J. P. T. (2011). Recommendations for examining and interpreting funnel plot asymmetry in meta-analyses of randomised controlled trials. *BMJ, 343*, d4002. | 10.1136/bmj.d4002 | Crossref (19 yazar, sıra birebir), PubMed 21784880 | yalnız künye doğrulandı | Hayır |
| 18 | Duval ve Tweedie, 2000 | Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455-463. | 10.1111/j.0006-341X.2000.00455.x | Crossref, PubMed 10877304 | özet okundu | Hayır |
| 19 | Debray ve ark., 2018 | Debray, T. P. A., Moons, K. G. M., & Riley, R. D. (2018). Detecting small-study effects and funnel plot asymmetry in meta-analysis of survival data: A comparison of new and existing tests. *Research Synthesis Methods, 9*(1), 41-50. | 10.1002/jrsm.1266 | Crossref, PMC5873397 | tam metin okundu | Hayır |
| 20 | Lin ve ark., 2020 | Lin, L., Shi, L., Chu, H., & Murad, M. H. (2020). The magnitude of small-study effects in the Cochrane Database of Systematic Reviews: An empirical study of nearly 30 000 meta-analyses. *BMJ Evidence-Based Medicine, 25*(1), 27-32. | 10.1136/bmjebm-2019-111191 | Crossref, PubMed 31273125, PMC6942244 | tam metin okundu | Hayır |
| 21 | Deeks ve ark., 2024 (Cochrane El Kitabı bölüm 10) | Deeks, J. J., Higgins, J. P. T., Altman, D. G., McKenzie, J. E., & Veroniki, A. A. (2024). Chapter 10: Analysing data and undertaking meta-analyses. In J. P. T. Higgins, J. Thomas, J. Chandler, M. Cumpston, T. Li, M. J. Page, & V. A. Welch (Eds.), *Cochrane handbook for systematic reviews of interventions* (Version 6.5). Cochrane. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10 | (çevrimiçi sürümde DOI yok; 2019 basılı bölüm 10.1002/9781119536604.ch10, s. 241-284) | Basılı bölüm Crossref; sürüm 6.5 ve bölüm yazarları yalnız web aramasıyla (site engelli); 6.5 editör listesi doğrulanmadı | yalnız künye doğrulandı | Hayır |
| 22 | Borenstein ve ark., 2021 | Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2021). *Introduction to meta-analysis* (2nd ed.). Wiley. | 10.1002/9781119558378 | Crossref | yalnız künye doğrulandı | Hayır |
| 23 | Üstün ve Eryılmaz, 2014 | Üstün, U., & Eryılmaz, A. (2014). Etkili araştırma sentezleri yapabilmek için bir araştırma yöntemi: Meta-analiz. *Eğitim ve Bilim, 39*(174), 1-32. | 10.15390/EB.2014.3379 | Crossref, TR Dizin (id 224530) | özet okundu | **Evet** |
| 24 | Dinçer, 2018 | Dinçer, S. (2018). Eğitim bilimleri araştırmalarında içerik analizi: Meta-analiz, meta-sentez, betimsel içerik analizi. *Bartın Üniversitesi Eğitim Fakültesi Dergisi, 7*(1), 176-190. | 10.14686/buefad.363159 | Crossref (iki dilli başlık), DergiPark | tam metin okundu | **Evet** |
| 25 | Göktaş, 2023 | Göktaş, E. (2023). Nicel bir sistematik inceleme yöntemi: Meta analiz. *e-Şarkiyat İlmi Araştırmaları Dergisi, 15*(2), 732-746. | 10.26791/sarkiat.1349791 | Crossref, DergiPark, TR Dizin (id 1217798) | özet okundu | **Evet** |

Not: Kaynakça ~25 sınırı için m5'e öneri: sunumda kesin gerekenler 1, 2, 4 (ya da 3), 5, 9, 11, 13, 14, 15, 16, 19 ya da 20, 23, 24. Diğerleri yedek. Glass (1976) yalnız künye düzeyinde olduğundan "Clarke, 2018'e göre" biçiminde birlikte anılması önerilir.

## 6. Doğrulanamayanlar ve sınırlar

- **Cochrane El Kitabı metni okunamadı** (cochrane.org alan adları engelli). Etkileri: (a) bölüm 10'un tanım cümlesi birebir alınamadı, tanım için Page ve ark. (2021) kullanıldı; (b) I² örtüşen aralıkları ve "model seçimi teste göre yapılmaz" cümlesi yalnız **5.0.1 sürümünden**, Rücker ve ark. (2008) birebir aktarımıyla doğrulandı; güncel 6.5 metninde aynen durup durmadığı doğrulanmadı; (c) 6.5 sürümünün editör listesi ve bölüm 10'un "son güncelleme" tarihi (web aramasında "Kasım 2024") doğrulanmadı. **Bakılacak yer:** cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10, bölüm 10.10.2 (heterojenlik) ve 10.10.4 (sabit ve rastgele etkiler); bölüm 13 (eksik sonuçlar nedeniyle yanlılık, funnel testleri). Ağ izni verilirse 10 dakikalık bir doğrulama yeter.
- **"En az 10 çalışma" kuralı (tuzak 6):** birincil kaynaktan doğrulanamadı; yalnız hakemli ikincil kaynakta birebir (Debray ve ark., 2018). Slayta konacaksa ikincil atıfla.
- **Sterne ve ark. (2011):** künye tam (19 yazar, Crossref ile birebir), içerik okunmadı. Asimetri nedenleri iddiası Lin ve ark. (2020) üzerinden verildi (Lin ve ark. bu cümlede Sterne ve ark.'na atıf yapıyor).
- **Hopkins ve ark. (2009) eşikleri** (0,20 / 0,60 / 1,20 / 2,0 / 4,0): tam metin erişilemedi, özet sayıları içermiyor. Doğrulanmadı; slayta sayı konmamalı. Sayfa aralığı çelişkisi: Crossref 3-12, PubMed 3-13 (yayıncı sayfasından bakılmalı).
- **Cohen (1988)** eşikleri: kitap okunmadı; Lakens (2013) aktarımıyla verildi.
- **Glass (1976) ve Hedges (1981):** yalnız künye; içerik iddiası Clarke (2018) ve Lakens (2013) üzerinden.
- **Borenstein ve ark. (2010, 2017, 2021):** 2010 ve 2017 için yalnız özet; 2021 kitabı okunmadı. Özet dışındaki ayrıntılar (ör. model seçiminin ölçütleri) bunlara atfedilmemeli.
- **Tahmin aralığı formülü:** betikte t dağılımı k − 2 serbestlik derecesiyle kullanıldı. Bu yaygın yaklaşımdır (Higgins, Thompson ve Spiegelhalter, 2009, *JRSS A, 172*(1), 137-159, DOI 10.1111/j.1467-985X.2008.00552.x, künye Crossref ile doğrulandı, metin okunmadı; bu yüzden kaynak tablosuna alınmadı). IntHout ve ark. (2016) formülü çevrimiçi ekte veriyor, ek okunmadı. Metindeki örnekleri (steroid örneğinde "t-distribution with 6 degrees of freedom") bu yaklaşımla uyumlu görünüyor ama çalışma sayısı tam metinde bu oturumda teyit edilmedi. Ayrıca IntHout ve ark. örneklerinde DL değil Hartung-Knapp/Sidik-Jonkman düzeltmesi kullanıyor; kurgu veride BRIEF gereği DL kullanıldı.
- **Ekolojik yanılgı:** okunan kaynakla doğrulanmadı (bölüm 3.9).
- **Üstün ve Eryılmaz (2014):** tam metin sitesi engelli; yalnız TR Dizin özeti. **Göktaş (2023):** PDF gövde metni kodlama nedeniyle okunamadı; yalnız öz ve bölüm başlıkları.
- **Dinçer (2014) kitabı ve Borenstein ve ark. Türkçe çevirisi (2013):** yalnız Dinçer (2018) kaynakçasından görüldü; kaynakçaya girmeden önce ISBN ve yayıncı doğrulanmalı.
- **Kurgu veriler** bu iş için üretildi; hiçbir gerçek çalışmayı temsil etmez. Hesaplar bağımsız bir kütüphaneyle (statsmodels/metafor) çapraz denetlenmedi (ortamda yüklü değil); betik standart formülleri uygular, t kritik değeri (sd = 4 için 2,776) ve Q'nun p değeri bilinen tablo değerleriyle tutarlı.
- **Önceki koşudan (s3) düzeltilenler:** s3'teki forest verisinde heterojenlik neredeyse sıfırdı (I² ≈ %2), bu yüzden τ² ve tahmin aralığı öğretilemiyordu; yeni veride I² %45. s3'te Duval ve Tweedie DOI'si ve Sterne yazar listesi açıktı, ikisi de bu koşuda Crossref ile kapatıldı. s3'te Cochrane I² aralıkları "ikincil kaynaklardan" diye geçiyordu; bu koşuda aktaran hakemli kaynak (Rücker ve ark., 2008) tam metinden belirlendi.

## 7. Zaman

- Başlangıç: 12:11 UTC (2026-11-23)
- Bitiş: 12:29 UTC (2026-11-23)
