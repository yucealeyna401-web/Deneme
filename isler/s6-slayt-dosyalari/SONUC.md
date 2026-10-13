# SONUC · Slayt dosyaları (iş s6)

## Ne oldu

- Çalışan, `uret.py` üretim betiğini yazdı (897 satır), ancak betiği çalıştırıp denetimi yapamadan oturum kullanım sınırına takıldı (API 429, "session limit"). SONUC.md yazamadı.
- Sınır kalktıktan sonra ana oturum betiği **değiştirmeden** çalıştırdı: "25 slayt yazildi". Denetimi ve bu dosyayı ana oturum yazdı.

## Üretilenler

- `project/deck.json`: başlık "Meta-analiz, Sistematik Derleme ve Derleme", 25 slayt, 9 bölüm, yazı tipleri Source Serif 4, IBM Plex Sans, IBM Plex Sans Condensed.
- `project/slides/*.html`: 25 dosya.
- Sıra: cover, acilis-soru, yol-haritasi, uc-tur, diger-turler, kanit-piramidi, pico, protokol-kayit, arama, prisma, yanlilik-grade, etki-buyuklugu, modeller-heterojenlik, orman-grafigi, huni-grafigi, ornek-fifa, ornek-turkiye, etik, elestirel, ozet, tesekkur, tartisma, kaynakca-1, kaynakca-2, kaynakca-3.
- Şemalar: karşılaştırma tablosu (uc-tur), kanıt piramidi, PRISMA 2020 akış şeması, orman grafiği (eğitim amaçlı kurgu veri), huni grafiği.

## Denetim (ana oturum, betikle)

| Kontrol | Sonuç |
|---|---|
| Her dosyada tek `<section>`, id = dosya adı | geçti (25/25) |
| `order` ile dosyalar birebir | geçti |
| `<aside>` son çocuk, 200 ile 4.000 karakter | geçti (961 ile 1.688 karakter) |
| 24px altında yazı | yok |
| margin, z-index, em, var(, class=, img | yok |
| Em dash | yok |
| Öğe sayısı ≤ 200 | geçti (en çok 86, orman grafiği) |
| Konuşmacı notu sayısı (s5'te 25) | 25/25 |
| Kaynakça: s5'teki 30 künyenin slaytlarda bulunması | 30/30 |
| Slayt sayısı 20 ile 25 | 25 |

Görsel (ekran) denetimi yapılmadı; düzen taşmaları yalnız yayımlanan sunumda görülebilir.

## Zaman

Çalışan başlangıcı 20:22 UTC civarı (2026-10-10), sınır nedeniyle yarıda kaldı. Ana oturum tamamlaması 2026-10-13, 11:15 ile 11:20 UTC.
