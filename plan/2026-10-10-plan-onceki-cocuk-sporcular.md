# Plan · 2026-10-10

> FAZ 1 çıktısı. Girdi: `sen/01-isler.md`.
> Konu: Çocuk sporcuların psikolojik esenliği. Aşırı antrenman, performans baskısı, tükenmişlik ve sporu bırakma.
> Güncelleme: kullanıcının kaynak şartları (yıl kotası, özgün çalışma önceliği, veri tabanları) eklendi.
> Bu plan yazıldıktan sonra DURDU. Kullanıcı okuyup `koş` demeden hiçbir iş başlamaz.

## Bölüm A · İşler

Kullanıcının verdiği beş odak (erken uzmanlaşma, ebeveyn ve antrenör baskısı, tükenmişlik, spordan ayrılma, koruyucu etmenler) dört araştırma işine bölündü. Literatürde birlikte çalışılan konular aynı işe kondu: erken uzmanlaşma ile aşırı antrenman, tükenmişlik ile spordan ayrılma.

| # | İş | Girdisi | Çıktısı | YAZACAĞI dosyalar |
|---|---|---|---|---|
| 1 | Erken uzmanlaşma ve aşırı antrenman: tanımlar, yaygınlık, psikolojik sonuçlar, kılavuz önerileri (ör. AAP, IOC uzlaşı bildirgeleri) | web araması, bilimsel kaynaklar | kaynaklı tema özeti | `isler/1-erken-uzmanlasma/SONUC.md` |
| 2 | Ebeveyn ve antrenör baskısı: performans baskısı, motivasyon iklimi (görev ve ego odaklı), algılanan baskının kaygı ve esenliğe etkisi | web araması, bilimsel kaynaklar | kaynaklı tema özeti | `isler/2-ebeveyn-antrenor-baskisi/SONUC.md` |
| 3 | Tükenmişlik ve spordan ayrılma: tükenmişlik modelleri ve ölçümü, bırakma oranları ve nedenleri, tükenmişlikten bırakmaya giden yol | web araması, bilimsel kaynaklar | kaynaklı tema özeti | `isler/3-tukenmislik-birakma/SONUC.md` |
| 4 | Koruyucu etmenler: temel psikolojik ihtiyaçlar (öz belirleme kuramı), sosyal destek, çok sporlu gelişim, dinlenme, müdahale çalışmaları | web araması, bilimsel kaynaklar | kaynaklı tema özeti | `isler/4-koruyucu-etmenler/SONUC.md` |
| 5 | Dört tema özetini tek bir Türkçe literatür derlemesinde birleştir: temalar arası bağlantılar, ortak bulgular, çelişkiler, araştırma boşlukları, uygulamaya dönük öneriler, birleşik kaynakça | 1, 2, 3, 4'ün SONUC.md dosyaları | literatür derlemesi | `isler/5-derleme/SONUC.md` |
| 6 | Koşu raporu ve filo defteri satırı | 5'in çıktısı, tüm SONUC.md dosyaları | rapor + defter satırı | `ciktilar/2026-10-10-rapor.md`, `sen/01-isler.md` |

**Her araştırma çalışanı için ortak kurallar (1-4):**

*Kaynak kotası (kullanıcı şartı, kesin):*
- Her tema için **en az 5 çalışma 2022-2026** yıllarından, **en az 5 çalışma 2021 ve öncesinden** (2021 dahil). Yani her SONUC.md en az 10 kaynak, toplam derlemede en az 40.
- Böylece her yayın yılı iki kotadan birine girer, boşta kalan yıl yok.
- Güncel çalışmalar öncelikli: bulgular anlatılırken önce 2022-2026 çalışmaları, eski çalışmalar temel ve karşılaştırma için.
- Kota tutmazsa çalışan bunu SONUC.md'nin başına açıkça yazar ("2022-2026: 3/5 bulunabildi"), eksik kaynağı uydurarak tamamlamaz.

*Kaynak türü:*
- **Öncelik özgün araştırma makalelerinde** (kesitsel, boylamsal, deneysel, nitel çalışmalar). Kotaya sayılan kaynaklar özgün araştırma olmalı.
- Sistematik derleme, meta analiz ve uzlaşı bildirgeleri yalnız bağlam için, kotaya sayılmaz ve ayrı bir "bağlam kaynakları" başlığında listelenir.
- Türkiye'de yapılmış çalışmalar ve lisansüstü tezler aranır; bulunursa dahil edilir.

*Veri tabanları (öncelik sırasıyla):* PubMed, SPORTDiscus, Scopus, Google Akademik, Web of Science, YÖK Ulusal Tez Merkezi.
- Her kaynağın yanına hangi veri tabanında bulunduğu ya da doğrulandığı yazılır.
- Erişim notu: SPORTDiscus, Scopus ve Web of Science abonelik gerektirir; çalışanın doğrudan erişimi olmayabilir. Erişilemeyen veri tabanı SONUC.md'de "erişilemedi" diye belirtilir. Bu durumda kayıt PubMed, Google Akademik, DOI ya da dergi sayfası üzerinden doğrulanır.

*Doğrulama ve dürüstlük:*
- Yalnız gerçek, doğrulanabilir kaynak. Her kaynak için yazar, yıl, başlık, dergi, çalışma türü, örneklem (sayı, yaş, spor dalı, ülke) ve DOI ya da bağlantı.
- Doğrulanamayan kaynak listeye girmez, "doğrulanamadı" diye ayrıca not edilir.
- Her bulgunun yanında hangi kaynağa dayandığı yazılır. Kaynaksız iddia yok.
- Diğer çalışanların klasörünü okumaz, yazmaz. Yalnız kendi klasörüne yazar.
- Çıktı Türkçe, em dash yok.

**İş 5 için ek kural:** derleme birleşik kaynakçada kotayı tema tema tablo halinde gösterir (tema · 2022-2026 sayısı · 2021 ve öncesi sayısı · özgün mü). Aynı makale birden çok temada geçiyorsa kaynakçada bir kez yazılır.

## Bölüm B · Bağımlılık haritası

**Veri bağımlılığı:**

```text
1 → 5
2 → 5
3 → 5
4 → 5
5 → 6
```

**Yazma çakışması:**

```text
yok
```

İşler 1-5 ayrı klasörlere yazıyor, kesişim yok. 6 numaralı iş `isler/` dışına, ortak dosyalara (`ciktilar/` ve `sen/01-isler.md`) yazıyor; izolasyon sınırının dışı olduğu için kendi sıralı dalgasında.

**Anlamsal örtüşme notu:** Temalar birbirine değiyor (ör. ebeveyn baskısı tükenmişliğin bir nedeni, koruyucu etmenler her temada geçiyor). Bu bir yazma çakışması değil, çalışanlar aynı dosyaya yazmıyor. Örtüşmenin tekrar ve tutarsızlık olarak toplanması iş 5'in görevi.

## Bölüm C · Dalgalar

| Dalga | İşler | Aynı anda mı | Neden |
|---|---|---|---|
| 1 | 1, 2, 3, 4 | **evet** | dördü de yalnız web kaynaklarını okuyor, birbirini beklemiyor, yazdıkları klasörler ayrı. 4 iş, üst sınırda |
| 2 | 5 | tek | dört tema özetinin hepsine muhtaç |
| 3 | 6 | **SIRALI** | `isler/` dışına, ortak dosyalara yazıyor |

## Bölüm D · Paralelleştirilmeyenler ve nedeni

| İş | Neden sıralı |
|---|---|
| 5 | veri bağımlılığı: 1, 2, 3 ve 4'ün çıktısını okuyor |
| 6 | izolasyon dışı yazma: `ciktilar/` ve `sen/01-isler.md` ortak dosyalar |
| (birleştirme) | Beş odak dört işe indirildi. Beşinci bir paralel iş açılsaydı 4 çalışan sınırı aşılırdı ya da tek işlik ek bir dalga doğardı. Filo defterindeki ders (tek işlik dalga genel oranı düşürüyor) bu kararda kullanıldı |

## Bölüm E · Tahmini kazanç

| | Süre |
|---|---|
| Hepsi sırayla koşarsa | 1 + 2 + 3 + 4 + 5 |
| Dalgalarla koşarsa | dalga 1'in en uzun işi + 5 |
| Kazanç | bilinmiyor |

Saniye cinsinden süre bilinmiyor, uydurulmadı. Web araştırması önceki koşudaki yerel okuma işlerinden (40-91 sn) belirgin biçimde uzun sürecektir. Dalga 2 tek iş olduğu ve sentez de uzun süreceği için genel kazanç dalga 1 içindeki kazançtan düşük çıkacak. Gerçek değerler raporun D bölümünde yazılacak.

## Bölüm F · Onay

Koşmadan önce kontrol et:

- [ ] İşler doğru anlaşılmış mı (özellikle beş odağın dört işe bölünüşü)
- [ ] Kaynak kotası ve veri tabanı önceliği doğru yazılmış mı
- [ ] "YAZACAĞI dosyalar" sütunu eksiksiz mi
- [ ] Aynı dosyaya yazan iki iş aynı dalgada mı (değil)
- [ ] Geri alınamaz bir iş paralel dalgaya düşmüş mü (geri alınamaz iş yok, hepsi okuma ve yeni dosya yazma)

**Varsayımlar, koşmadan önce değiştirmek istersen söyle:**
- Derleme dili Türkçe, kaynaklar İngilizce ve Türkçe literatürden.
- Yaş aralığı yaklaşık 6-18 yaş (çocuk ve ergen sporcular).
- Kaynak kotası tema başına uygulanır (her temada 5 + 5). Kullanıcı şartı toplam için de olabilirdi; tema başına uygulamak daha sıkı ve toplamı da karşılar.
- Hedef okur: akademik ama anlaşılır, uygulayıcıya (antrenör, ebeveyn) yönelik öneriler bölümü dahil.
- Kaynakça biçimi APA 7.

Onaydan sonra `koş`.
