# BRIEF · Sunum içeriği (slayt metni, konuşmacı notları, tartışma, kaynakça)

> Plan: `plan/2026-10-10-plan.md`, dalga 2. Tek iş. Dalga 1'in dört çıktısını birleştirir.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi sunumu: "Meta-analiz, sistematik derleme ve derleme".
> Dinleyici: beden eğitimi ve spor alanında yüksek lisans öğrencileri ve dersin hocası. Bazı öğrenciler konuyu ilk kez duyuyor; hoca uzman. Sunan kişi yüksek lisans öğrencisi.
> Süre: ~20 dk. Yaklaşık 15 dk anlatım + 5 dk tartışma.

## İş ne

Dalga 1'in bulgularını **20 ile 25 slaytlık** bir sunumun eksiksiz içeriğine dönüştür. Görsel tasarım YAPMA (o iş s6'nın); sen her slaytın ne söyleyeceğini, nasıl gösterileceğini ve sunanın ne konuşacağını yazarsın.

Kullanıcının önceki sunumda en çok beğendiği şeyler: **ayrıntılı konuşmacı notları ve eksiksiz kaynakça.** Bu işin kalitesi buna göre ölçülür.

## Girdisi (yalnız okuma)

- `isler/s1-kavramlar-etik/SONUC.md` (derleme türleri, kanıt piramidi, etik)
- `isler/s2-sistematik-surec/SONUC.md` (PICO, PROSPERO, arama, PRISMA 2020, yanlılık riski, GRADE, AMSTAR 2)
- `isler/s3-meta-analiz-yontemi/SONUC.md` (etki büyüklüğü, modeller, I², orman ve huni grafiği)
- `isler/s4-spor-ornekleri/SONUC.md` (beden eğitimi ve spordan örnek çalışmalar)

Bir dosya yoksa ya da boşsa o kısmı "girdi yok" diye işaretle, uydurma.

## Önerilen akış (esnek; 20 ile 25 slayt arasında kal)

1. **Açılış (2 ile 3 slayt):** kapak (köşeli parantezli yer tutucular: [Adınız Soyadınız], [Ders hocası: Unvan Ad Soyad], [Üniversite, Enstitü, Anabilim Dalı], [Tarih]); dinleyiciyi yakalayan bir açılış (spordan tanıdık bir soru: "tek çalışma mı, yirmi çalışma mı?"); yol haritası ve ana mesaj.
2. **Kavramlar (3 ile 4 slayt):** üç türün karşılaştırması (tablo), diğer derleme türleri, kanıt piramidi ve eleştirisi.
3. **Sistematik derleme nasıl yapılır (4 ile 5 slayt):** PICO (spor örneği), protokol ve kayıt, arama stratejisi (kullanıcının saydığı tabanlar: PubMed, SPORTDiscus, Google Akademik, Web of Science, YÖK Tez; Google Akademik'in sınırı), tarama ve PRISMA 2020 akış şeması, yanlılık riski ve GRADE.
4. **Meta-analiz (4 slayt):** mantık ve etki büyüklüğü, sabit ve rastgele etkiler ve heterojenlik, orman grafiği okuma (s3'ün kurgu verisiyle; slaytta "eğitim amaçlı kurgu veri" ibaresi), huni grafiği ve yayın yanlılığı.
5. **Beden eğitimi ve spordan örnekler (2 ile 3 slayt):** s4'ün kartlarından en öğretici olanlar; en az biri Türkiye kaynaklı.
6. **Etik ve eleştirel bakış (1 ile 2 slayt):** derlemelerde araştırma etiği, güçlü ve zayıf yönler.
7. **Kapanış (2 slayt):** özet ve ana mesaja dönüş; teşekkür.
8. **Tartışma (1 slayt):** 5 dakika için 4 ile 6 soru. Sorular düşündürücü olsun, evet/hayır olmasın; en az biri etik, en az biri spor alanına özgü.
9. **Kaynakça (2 ile 3 slayt):** sunumda anılan her kaynak **tam APA 7 künyesiyle** (DOI dahil). Slayt başına en fazla ~9 künye sığar; ona göre böl.

## Her slayt için yazacakların (`slaytlar.md`)

```
## <sıra>. <slayt-id> · <bölüm>
**Başlık:** ...
**Üst etiket:** (küçük bölüm etiketi, ör. "Sistematik derleme")
**İçerik:** slaytta görünecek metin. Kısa: madde başına en fazla ~12 kelime, en fazla 5 madde, ya da tablo / kart / büyük sayı.
**Görsel öneri:** tablo, kart dizisi, akış şeması, piramit, orman grafiği vb. Şema ise kutuların metnini tam yaz.
**Alt bilgi (kaynak satırı):** slaytta anılan kaynaklar (Yazar, Yıl).
**Süre:** saniye.
**Konuşmacı notu:** 120 ile 250 kelime. Sunanın ağzından, doğal Türkçe, sınıfa söylenecek cümleler tırnak içinde. Kavramı bilmeyen öğrenci için bir benzetme ya da spor örneği; uzman hoca için bir ayrıntı ya da sınırlılık. Hoca sorarsa verilecek kısa cevaplar. Hangi kaynağa dayandığı (Yazar, Yıl). Önceki sunumdaki not üslubu iyi bir örnek: "Süre: 60 saniye. ..." diye başlar, sonra konuşma metni, sonra "Uzman için not:".
```

Süreleri topla: anlatım slaytlarının toplamı 14 ile 16 dk, tartışma slaytı 5 dk. Toplamı dosyanın başına yaz.

## Kesin kurallar

- **Yalnız dalga 1'de doğrulanmış kaynakları kullan.** Yeni kaynak ekleme, hafızadan künye yazma. Bir bilgi hiçbir SONUC.md'de kaynaklı değilse slayta koyma.
- **Çelişki denetimi:** aynı kaynak birden çok SONUC.md'de farklı künyeyle (yıl, cilt, sayfa, DOI, yazar sırası) geçiyorsa `SONUC.md` dosyanda "Çelişkiler" başlığında listele, hangisini neden seçtiğini yaz. Çözemediğini konuşmacı notuna "sunumdan önce kontrol edin" diye ekle.
- Kurgu örnekler (PICO örnek sorusu, orman grafiği verisi) slaytta açıkça "örnek" / "eğitim amaçlı kurgu veri" diye işaretli olmalı.
- Sayısal bulgular (etki büyüklüğü, %, n) yalnız kaynak SONUC.md'de yazdığı gibi.
- Dürüstlük notu: dalga 1 çalışanları SPORTDiscus, Web of Science ve YÖK Tez'e doğrudan erişemediyse, ilgili konuşmacı notuna sunana "bu tabanları kendi üniversite erişiminizle kontrol edin; taramadığınız tabanı taradım demeyin" uyarısını ekle.
- Türkçe, yüksek lisans düzeyi ama sade. Terimlerin İngilizcesini ilk geçtiği yerde parantezde ver (ör. orman grafiği (forest plot)).
- **Em dash (uzun tire) HİÇBİR yerde yok.** Ayraç: nokta, virgül, iki nokta ya da orta nokta (·).

## Çıktısı ve nereye yazacak

YALNIZ kendi klasörüne: `isler/s5-sunum-icerigi/`. Başka yere yazma, commit/push yapma.

1. `isler/s5-sunum-icerigi/slaytlar.md`: dosya başında slayt sayısı, toplam süre, bölüm listesi (bölüm adı + tek cümle açıklama + başladığı slayt-id); sonra her slayt yukarıdaki yapıda; en sonda "Tam kaynakça (APA 7, alfabetik)".
2. `isler/s5-sunum-icerigi/SONUC.md`: ne yaptın, slayt sayısı ve toplam süre, kullanılan kaynak sayısı, Çelişkiler, girdide eksik olan ve sunuma giremeyen konular, başlangıç ve bitiş saati (`date -u +%H:%M:%S`).

## Bitince ne döndür

Tek paragraf: slayt sayısı, toplam süre, kaynak sayısı, çözülemeyen çelişki sayısı, başlangıç ve bitiş saati.
