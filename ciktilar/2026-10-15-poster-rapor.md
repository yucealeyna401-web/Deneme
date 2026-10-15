# Rapor · 2026-10-15 · TÜBED Kongresi Posteri (2209/A)

## Bölüm A · Özet

| | |
|---|---|
| Koşulan iş | 5 (p1 ile p5) |
| Biten | 1 (p2-sablon) |
| Yapılamayan | 1 (p1-icerik: girdi dosyaları yok) |
| Atlanan (bağlı olduğu iş yapılamadı) | 3 (p3-metin, p4-sekiller, p5-poster) |
| Dalga sayısı | planlanan 3, koşulan 1 |

**Elle müdahale gerekiyor:** 2209/A proje önerisi ve sonuç raporu bu ortama gelmeden poster içeriği üretilemez. Hazır olan tek şey boş 70×90 şablon.

## Bölüm B · İş iş sonuç

### B1 · p1-icerik · İki dosyadan içerik çıkarma · **yapılamadı**
- **Ne üretti:** çıktı üretmedi.
- **Not:** repo, bütün dallar, dosya sistemi ve sohbet ekleri klasörleri tarandı; ne proje önerisi ne sonuç raporu var.

### B2 · p2-sablon · 70×90 cm poster şablonu · **bitti**
- **Ne üretti:** `isler/p2-sablon/sablon.html`, `deneme.pdf` (700×900 mm, tek sayfa, taşma yok), `onizleme.png`, `uret.js`.
- **Not:** başlık 84 pt, bölüm başlığı 48 pt, gövde 30 pt, kaynakça 21 pt. TÜBED'in resmi şablonu bulunamadı. Yazı tipi PDF'e Type 3 gömülüyor; matbaa itiraz ederse yeniden üretilmeli.

### B3 · p3-metin · Poster metni ve APA 7 kaynakça · **atlandı**
- **Ne üretti:** çıktı üretmedi. p1'e bağlı.

### B4 · p4-sekiller · Grafik, tablo, akış şeması · **atlandı**
- **Ne üretti:** çıktı üretmedi. p1'e bağlı.

### B5 · p5-poster · Dizgi, son PDF ve denetim · **atlandı**
- **Ne üretti:** çıktı üretmedi. p3 ve p4'e bağlı.

## Bölüm C · Yapılamayanlar

| İş | Ne oldu | Sonraki adım |
|---|---|---|
| p1-icerik | eksik girdi: 2209/A dosyaları yok | Proje önerisini ve sonuç raporunu `sen/kaynak/` klasörüne koy ya da sohbete ekle, sonra `koş` |
| p3-metin | atlandı (p1'e bağlı) | p1 bitince kendiliğinden koşar |
| p4-sekiller | atlandı (p1'e bağlı) | p1 bitince kendiliğinden koşar |
| p5-poster | atlandı (p3, p4'e bağlı) | p3 ve p4 bitince koşar, `uret.js` ile p2 şablonunu kullanır |

Zincir: **p1 yapılamadı → p3, p4 atlandı → p5 atlandı.**

Ayrıca kullanıcıdan hâlâ beklenenler: kongrenin tam adı, tarihi ve yeri; resmi şablon ya da logo şartı varsa o; dosyalarda yoksa yazarların kurumu ve e-postası.

## Bölüm D · Gerçekleşen zamanlama

| Dalga | İşler | Tahmin | Gerçek |
|---|---|---|---|
| 1 | p1, p2 | 8 dk | yaklaşık 6 dk (p1 hemen düştü, p2 yaklaşık 6 dk) |
| 2 | p3, p4 | 8 dk | koşulmadı |
| 3 | p5 | 10 dk | koşulmadı |

Paralellikten kazanç yok: dalga 1'de yalnız tek iş gerçekten koştu, bu yüzden ayrı çalışan açılmadı, p2 ana oturumda yapıldı.

## Bölüm E · Çakışma kontrolü

| Kontrol | Sonuç |
|---|---|
| Kendi klasörü dışına yazan çalışan | yok |
| Aynı dosyaya iki çalışanın yazması | yok |
| Eksik `SONUC.md` | yok (beş işin beşinde var: 1 bitti, 1 yapılamadı, 3 atlandı) |

## Bölüm F · Filo defteri girdisi

```
2026-10-15 · Poster koşusu girdi dosyası olmadan başlatıldı: "daha önce attığım" dosyalar önceki sohbette kalmış, bu oturuma gelmemişti. Yalnız içerikten bağımsız şablon işi bitti, zincirin geri kalanı atlandı. Ders: girdi dosyası gereken planlarda dosyalar `sen/kaynak/` altında yoksa `koş` öncesinde dur ve yalnız dosyasız koşabilecek işleri öner; kullanıcı dosyayı sohbete değil repoya koymalı, çünkü sohbetler arasında dosya taşınmıyor.
```
