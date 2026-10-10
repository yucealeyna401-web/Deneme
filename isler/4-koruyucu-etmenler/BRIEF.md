# BRIEF · Koruyucu etmenler

> Plan: `plan/2026-10-10-plan.md`, dalga 1. Bu iş dalgadaki diğer üç işle aynı anda koşuyor.
> Genel konu: Çocuk sporcuların psikolojik esenliği. Aşırı antrenman, performans baskısı, tükenmişlik ve sporu bırakma.

## İş ne

Çocuk ve ergen sporcuları tükenmişlik, kaygı ve spordan ayrılmaya karşı koruyan etmenler. Odak: temel psikolojik ihtiyaçların doyumu (özerklik, yetkinlik, ilişkili olma; öz belirleme kuramı), içsel motivasyon, sosyal destek (ebeveyn, antrenör, takım arkadaşı), görev odaklı motivasyon iklimi, özerklik destekleyici antrenör, çok sporlu katılım, dinlenme ve iyileşme, psikolojik dayanıklılık (resilience), müdahale çalışmaları (antrenör ya da ebeveyn eğitimi programları).

## Girdisi

Web ve bilimsel veri tabanları. Repodaki başka dosyalar girdi değil.

## Çıktısı ve nereye yazacak

Tek dosya: `isler/4-koruyucu-etmenler/SONUC.md`. Bu dosyayı dalga 2'deki derleme işi okuyacak; o yüzden kaynak tablosu eksiksiz ve doğru olmalı.

## Arama için başlangıç anahtar kelimeleri (yalnız başlangıç, genişlet)

basic psychological needs youth athletes burnout protective, autonomy supportive coaching adolescent athletes, social support youth athletes wellbeing, resilience young athletes, intervention coach education youth sport wellbeing

## Kaynak şartları (kullanıcı şartı, kesin)

- **En az 5 özgün araştırma 2022-2026** yıllarından, **en az 5 özgün araştırma 2021 ve öncesinden** (2021 dahil). Toplam en az 10. Daha fazlası iyi; hedef 6+6 civarı.
- **Güncel çalışmalar öncelikli:** bulguları anlatırken önce 2022-2026 çalışmaları gelir, eskiler temel ve karşılaştırma için.
- **Özgün araştırma öncelikli:** kesitsel, boylamsal, deneysel, nitel çalışmalar. Kotaya YALNIZ özgün araştırma sayılır. Sistematik derleme, meta analiz, uzlaşı bildirgesi kotaya sayılmaz; en fazla 3 tane, ayrı "Bağlam kaynakları" başlığında.
- Türkiye'de yapılmış çalışmalar ve lisansüstü tezler aranır, bulunursa dahil edilir.
- Çocuk ve ergen sporcular (yaklaşık 6-18 yaş). Yetişkin örneklemli çalışma kotaya sayılmaz.

## Veri tabanları (öncelik sırası)

PubMed, SPORTDiscus, Scopus, Google Akademik, Web of Science, YÖK Ulusal Tez Merkezi.

- Önce PubMed'i dene (pubmed.ncbi.nlm.nih.gov arama sayfası ya da eutils.ncbi.nlm.nih.gov E-utilities API). Sonra Google Akademik ve web araması.
- SPORTDiscus, Scopus ve Web of Science abonelik ister; erişemezsen "erişilemedi" diye not et, zaman kaybetme.
- YÖK Tez (tez.yok.gov.tr) için bir deneme yap; erişemezsen not et.
- Her kaynağı doğrula: DOI'yi api.crossref.org/works/<DOI> ya da doi.org üzerinden, veya PubMed kaydından kontrol et. Yazar, yıl, başlık, dergi gerçekten eşleşmeli.

## Dürüstlük

- Yalnız gerçek ve doğrulanmış kaynak. Hafızandan kaynak yazma; her biri bu oturumda bir aramayla ya da kayıtla doğrulanmış olmalı.
- Doğrulayamadığın kaynağı listeye koyma; "Doğrulanamayanlar" başlığında ayrıca not et.
- Kota tutmazsa SONUC.md'nin en başına açıkça yaz ("2022-2026: 3/5 bulunabildi"). Uydurarak tamamlama.
- Her bulgunun yanında dayandığı kaynak (Yazar, Yıl) yazılır. Kaynaksız iddia yok.
- Bulgu özetini makalenin özetinden (abstract) ya da tam metninden al; okumadığın bir sonucu yazma.

## İzolasyon

- YALNIZ kendi klasörüne yaz: `isler/4-koruyucu-etmenler/`. Başka hiçbir yere dosya yazma, başka işlerin klasörlerini okuma.
- Yalnız tek dosya üret: `isler/4-koruyucu-etmenler/SONUC.md`.

## SONUC.md yapısı (Türkçe, em dash (uzun tire) HİÇBİR yerde yok; ayraç olarak nokta, virgül, iki nokta ya da orta nokta · kullan)

1. **Kota durumu:** 2022-2026 sayısı / 2021 ve öncesi sayısı, kota tuttu mu.
2. **Veri tabanı erişimi:** her veri tabanı için erişildi / erişilemedi.
3. **Temel bulgular:** alt başlıklar halinde, önce güncel çalışmalar; her cümlede (Yazar, Yıl).
4. **Kaynak tablosu:** # · Yazar (Yıl) · Başlık · Dergi · Tür (kesitsel/boylamsal/deneysel/nitel/tez) · Örneklem (n, yaş, spor, ülke) · Ana bulgu (tek cümle) · Veri tabanı · DOI/bağlantı.
5. **Bağlam kaynakları** (derleme, meta analiz, en fazla 3, kotaya sayılmaz).
6. **Kaynakça (APA 7).**
7. **Doğrulanamayanlar ve sınırlar:** ne bulunamadı, nerede takıldın.
8. **Zaman:** başlarken ve bitirirken `date -u +%H:%M:%S` çalıştır, ikisini de yaz.

## Bitince ne döndür

Tek paragraf: kota durumu (x/5, y/5), kaç kaynak, erişilemeyen veri tabanları, başlangıç ve bitiş saati.
