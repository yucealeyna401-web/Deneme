# BRIEF · d7 · Sentez: ulusal ve uluslararası dergilerde son 5 yıl

**Plan:** `plan/2026-10-14-plan.md`, iş 7. Dalga 3 (tek).

## İş
Dalga 1 ve 2'nin çıktılarını birleştirip bir beden eğitimi ve spor yüksek lisans ödevine konacak **tek bir analiz metni** yaz: 10 ulusal ve 10 uluslararası dergide 2021 ile 2025 arasında nasıl çalışmalar yapıldığı.

## Girdiler (yalnız okuma)
- `isler/d1-ulusal-secim/SONUC.md`, `isler/d2-uluslararasi-secim/SONUC.md` (dergi künyeleri, seçim gerekçeleri)
- `isler/d3-ulusal-analiz-a/`, `isler/d4-ulusal-analiz-b/`, `isler/d5-uluslararasi-analiz-a/`, `isler/d6-uluslararasi-analiz-b/`: her birinde `SONUC.md` ve `kodlama.md`
Bir girdi eksik ya da boşsa onu atla, analizde "bu dergiler için veri yok" diye açıkça yaz; eksik veriyi tahminle doldurma.

## Yöntem
1. **Birleştirme betiği:** `isler/d7-sentez/birlestir.py` yaz ve HEMEN çalıştır. Dört `kodlama.md` tablosunu okusun, kategori yazımlarını normalize etsin (küçük/büyük harf, boşluk), birleşik tabloyu `isler/d7-sentez/birlesik.csv` olarak yazsın, frekans ve yüzde tablolarını `isler/d7-sentez/frekanslar.md` olarak üretsin: konu, yaklaşım, desen, örneklem, n aralığı, veri toplama, analiz, dil; her biri ulusal / uluslararası / toplam ve yıllara göre (2021 ile 2025). Python standart kütüphanesi yeterli. Normalize edilemeyen değerleri listele.
2. **Çelişki denetimi:** aynı makale iki yerde farklı künyeyle geçiyor mu, dergi künyeleri (d1/d2) ile analiz dosyaları çelişiyor mu, SONUC.md'lerdeki sayılar kodlama tablolarıyla tutuyor mu. Bulguyu analizde "veri kalitesi notu" olarak yaz.
3. **Analiz metni** `isler/d7-sentez/analiz.md`, ödev diliyle, Türkçe, akademik üslup. Bölümler:
   1. Giriş (amaç, kapsam: 20 dergi, 2021 ile 2025)
   2. Yöntem (dergi seçim ölçütleri; örneklemli içerik analizi; kodlama şeması; veri kaynakları ve erişim sınırlılığı: Web of Science/Scopus/TR Dizin'e doğrudan erişilemedi, web araması kullanıldı; kodlanan makale sayısı)
   3. Dergiler: ulusal ve uluslararası dergi tabloları (ad, yayıncı, dizin, Q/TR Dizin, alt alan, seçim gerekçesi kısaca)
   4. Bulgular: her dergi için kısa paragraf (3 ile 5 cümle) + toplu frekans tabloları (konu, yaklaşım, desen, örneklem, veri toplama, analiz) + yıllara göre eğilim
   5. Ulusal ve uluslararası karşılaştırma (benzerlikler, farklar; ör. nicel/tarama ağırlığı, deneysel çalışma oranı, nitel ve karma yöntem, derleme/meta-analiz, örneklem büyüklüğü, dil)
   6. Tartışma: öne çıkan ve az çalışılan alanlar, alanın yönelimi
   7. Yüksek lisans öğrencisi için çıkarımlar (hangi dergiye ne tür çalışma uygun; tez konusu için boşluklar)
   8. Sınırlılıklar (örneklem, erişim, doğrulanamayan dizin bilgileri: d1/d2'nin "doğrulanamadı" notlarını buraya taşı)
   9. Sonuç
   10. Kaynakça (APA 7): kodlanan makalelerin hepsi değil; dergi künyeleri, kullanılan ikincil bibliyometri çalışmaları ve analizde adı geçen örnek makaleler. **En az 5 Türkçe kaynak** kaynakçaya girsin (ulusal dergilerdeki örnek makaleler ve Türkçe bibliyometri çalışmaları).
4. Tablolarda sayı ve yüzde birlikte verilsin (n, %). Yüzdeler örneklem üzerinden; metinde "örneklemde" ifadesiyle yaz, genelleme yapma.

## Çıktılar (yalnız bu klasöre)
`birlestir.py`, `birlesik.csv`, `frekanslar.md`, `analiz.md`, `SONUC.md` (ne yaptın, kaç makale birleşti, hangi dergiler eksik, çelişki denetimi bulguları, neyi yapamadın).

## Kurallar
- **Yalnız `isler/d7-sentez/` klasörüne yaz.** Başka dosyaya dokunma, git kullanma.
- Önce betiği yaz ve çalıştır, ara çıktıları diske bırak; sonra analiz metnini bölüm bölüm yaz ve her bölümden sonra kaydet.
- Em dash (uzun tire) hiçbir yerde kullanma.
- Bitince kısa özet döndür.
