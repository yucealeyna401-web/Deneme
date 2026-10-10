# BRIEF · Slayt dosyaları (Slides biçiminde)

> Plan: `plan/2026-10-10-plan.md`, dalga 3. Tek iş. Girdisi dalga 2'nin slayt metni.
> Genel konu: Bilimsel Araştırma Yöntemleri ve Araştırma Etiği dersi sunumu: "Meta-analiz, sistematik derleme ve derleme". Beden eğitimi ve spor alanında yüksek lisans sınıfı.

## İş ne

`isler/s5-sunum-icerigi/slaytlar.md` dosyasındaki 20 ile 25 slaytı, Claude Slides biçiminde slayt dosyalarına çevir. **Yayımlama yapma**; yalnız dosyaları hazırla. Yayımlamayı ana oturum yapacak.

Kullanıcı isteği: görünüm önceki sunuma **benzer** olsun, birebir kopya şart değil. Asıl önemli olan içerik: ayrıntılı konuşmacı notları ve eksiksiz kaynakça. **Konuşmacı notlarını ve kaynakçayı slaytlar.md'den eksiksiz aktar, kısaltma.**

## Girdisi (yalnız okuma)

- `isler/s5-sunum-icerigi/slaytlar.md` (içerik, notlar, kaynakça)
- `isler/s6-slayt-dosyalari/referans/onceki-slaytlar/*.html` (önceki sunumdan stil örnekleri: kapak, yol haritası, kavram kartları, büyük sayılar, akış zinciri, teşekkür, kaynakça, kapanış)
- `isler/s6-slayt-dosyalari/referans/kurallar/format.md` (izinli HTML/CSS alt kümesinin tamamı; KESİN uy), `layout.md`, `diagrams.md` (şemalar ve bağlayıcılar için)

## Çıktısı ve nereye yazacak

YALNIZ `isler/s6-slayt-dosyalari/` altına. Commit/push yapma.

1. `isler/s6-slayt-dosyalari/project/deck.json`, tam olarak bu biçimde:
   `{"v":4,"createdOnFiles":{"v":1,"at":"<şimdi, RFC 3339 UTC>"},"lists":"css","title":"Meta-analiz, Sistematik Derleme ve Derleme","order":[...slayt id'leri sırayla...],"sections":{"s1":{"description":"<tek cümle>","start":"cover"}, ...},"faces":{...},"designSystems":[]}`
   `sections`: slaytlar.md'deki bölümler; ilki `cover` ile başlar. `faces`: kullandığın yazı tipleri (en fazla 4), anahtar = aile adı küçük harf ve boşluk yerine `-`, değer `{"family":"...","href":"https://fonts.googleapis.com/css2?..."}`. Önceki sunumda: Source Serif 4 (`https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap`) ve IBM Plex Sans (`https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap`). Aynılarını ya da benzer akademik bir çift kullanabilirsin.
2. Her slayt için `isler/s6-slayt-dosyalari/project/slides/<id>.html`. Id: `[A-Za-z0-9_-]{1,64}`, Türkçe karakter yok. Kapak id'si `cover`.
3. `isler/s6-slayt-dosyalari/SONUC.md`: slayt sayısı, id listesi, hangi şemaları çizdin, format kurallarından saptığın yer var mı, slaytlar.md'den aktaramadığın bir şey var mı, başlangıç ve bitiş saati (`date -u +%H:%M:%S`).

## Slayt dosyası kuralları (kesin)

- Her dosya TAM OLARAK BİR `<section id="<id>" ...>`; öncesinde ya da sonrasında hiçbir şey yok (`<html>`, `<head>`, `<style>`, `<link>` yok). `id` dosya adıyla aynı.
- 1920×1080 tuval; bütün stiller satır içi (`style=""`) ve `format.md` alt kümesinden. `margin`, `z-index`, `em`, `var()`, `class` yok. Her section'da `background`. İçerik slaytlarında `padding:128px 128px 160px`; alt bilgi satırı (kaynak + sayfa no) `position:absolute;left:128px;bottom:64px;width:1664px` tek satır, 24px.
- Yazı boyutu her yerde en az 24px. Bir slaytta en fazla 200 öğe.
- Konuşmacı notu: section'ın SON çocuğu olan tek `<aside>`, düz metin, en fazla 4.000 karakter. slaytlar.md'deki notu tam aktar (başına "Süre: N saniye." ekli). 4.000'i aşarsa en az önemli cümleleri kısalt ve SONUC.md'ye yaz.
- Görsel yok (`<img>` kullanma; dosya yüklenemiyor). Şemaları `<div>` kutular, `<x-shape>`, `<x-connector>`, tablolar ve gerekirse `<svg aria-label="...">` ile çiz (svg içinde `<text>` kullanma; etiketler svg üstüne `position:absolute` `<p>`).
- **Çizilmesi gereken şemalar:** PRISMA 2020 akış şeması (tanımlama, tarama, dahil etme kutuları ve dışlanan kayıt kutuları; sayılar yerine "n = ..." yer tutucu ya da slaytlar.md'deki örnek sayılar), kanıt piramidi, orman grafiği (slaytlar.md'deki kurgu veriyle: her çalışma için kare ve güven aralığı çizgisi, dikey etkisizlik çizgisi, alttaki elmas; "eğitim amaçlı kurgu veri" ibaresi görünür), huni grafiği (basit, simetrik ve asimetrik fark anlaşılsın), karşılaştırma tablosu (geleneksel derleme, sistematik derleme, meta-analiz).
- Metin yalnız boşlukta kırılır: kutuyu en uzun kelimeye göre boyutlandır (karakter başına ~0,6 × font-size). Dikey alan 824px; sığmazsa yazıyı küçültme, slaytı ikiye böl ama toplam 25'i geçme.
- Kaynakça slaytları: tam APA 7 künyeler, 24px, slayt başına en fazla ~9 künye; sığmazsa üç slayta böl.
- Tasarım: bir koyu, bir açık ton, 1 ile 2 vurgu rengi; iki arka plan tonu ve bir vurgu (statement) slaytı; metin arka planla en az 4,5:1 kontrast. Aynı türdeki slaytlar aynı iskeleti paylaşır; başlık hep aynı yerde. Önceki sunumun paleti: koyu #1F2A37, açık #F7F5F0, ikinci açık #ECE8DF, kart #FDFCF9, vurgu turuncu #D9632B / #B04A16, ikinci vurgu mavi #2F6F8F. Benzer bir palet kullan; istersen vurgu rengini değiştir (ör. konu için mavi/yeşil ağırlıklı), ama önceki sunumun sakin akademik havası kalsın.
- Em dash (uzun tire) HİÇBİR yerde yok.

## Bitmeden önce kendi denetimin

Küçük bir Python betiğiyle (betiği `isler/s6-slayt-dosyalari/` içinde tut) şunları kontrol et ve sonucu SONUC.md'ye yaz: her dosyada tek `<section>`, id = dosya adı, `order` ile dosyalar birebir eşleşiyor, `<aside>` son çocuk ve ≤ 4.000 karakter, 24px altında font-size yok, yasak CSS (`margin`, `z-index`, `em`, `var(`, `class=`) yok, em dash yok, slayt sayısı 20 ile 25 arası.

## Bitince ne döndür

Tek paragraf: slayt sayısı, çizilen şemalar, denetim sonucu, başlangıç ve bitiş saati.
