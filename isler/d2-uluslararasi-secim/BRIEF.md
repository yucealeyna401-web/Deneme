# BRIEF · d2 · 10 uluslararası dergi seçimi

**Plan:** `plan/2026-10-14-plan.md`, iş 2. Dalga 1 (iş 1 ile paralel).

## İş
Beden eğitimi ve spor bilimleri alanında nitelikli **10 uluslararası dergi + 3 yedek** seç ve her birinin dizin ve Q değeri bilgisini teyit et. Bu liste bir yüksek lisans ödevinde kullanılacak; ardından her derginin 2021 ile 2025 arası yayınları analiz edilecek.

## Seçim ölçütleri
- Yayıncı Türkiye dışında. Türkiye'de yayımlanan dergi bu listeye girmez.
- **SSCI ya da SCIE'de dizinli** (Clarivate Master Journal List). Tercihen JCR ya da SJR'de **Q1 veya Q2** (kategori: Sport Sciences, Education & Educational Research, Hospitality Leisure Sport & Tourism vb.). Q değerinin kaynağını ve yılını yaz.
- Yağmacı dergi listelerinde olmamalı; 2021 ile 2025 arasında kesintisiz yayımlanmış.
- **Alt alan dengesi (ilk 10 için zorunlu):** en az 3 beden eğitimi ve öğretimi/pedagoji (ör. beden eğitimi pedagojisi dergileri), en az 2 egzersiz ve antrenman bilimi, en az 1 spor psikolojisi/sosyolojisi, en az 1 spor yönetimi/rekreasyon; geri kalan genel spor bilimleri/spor hekimliği. Yalnız yüksek etki faktörlü spor hekimliği dergileriyle doldurma; liste bir beden eğitimi ve spor yüksek lisans öğrencisinin alanını yansıtmalı.
- Artı puan: bir yüksek lisans öğrencisinin gerçekçi olarak okuyacağı ve atıf yapacağı dergi olması; Türkiye'den yazarların da yayın yapıyor olması (biliniyorsa not et).

## Kaynaklar ve erişim
Bu ortamda kabuktan (curl) dışarı erişim KAPALI. Clarivate, Scimago, Scopus doğrudan açılmıyor. **Yalnız WebSearch ve WebFetch kullan** (yayıncı sayfası, Scimago sayfası, MJL kaydı arama sonuçları). Bilgi uydurma: bulamadığın alana "doğrulanamadı" yaz; Q değeri teyit edilemiyorsa tahmin yazma.

## Her dergi için kart
Tam ad · kısaltma · yayıncı · ISSN / e-ISSN · kuruluş yılı · yılda sayı · dizin (SSCI/SCIE) · Q değeri, kategori, kaynak ve yıl · varsa etki faktörü/SJR değeri ve yılı · kapsam (1 cümle) · ağırlıklı alt alan · web adresi · açık erişim mi · seçim gerekçesi (1 ile 2 cümle) · bu dergi üzerine yayımlanmış içerik analizi/bibliyometri çalışması varsa künyesi.

## Çıktı
`isler/d2-uluslararasi-secim/SONUC.md`:
1. Başta özet tablo: # · dergi · yayıncı · ağırlıklı alt alan · dizin · Q (kaynak, yıl).
2. Alt alan dengesi kontrolü (zorunlu kotalar tutuyor mu).
3. 10 dergi kartı, sonra 3 yedek kart.
4. Elenen ama düşünülen dergiler ve eleme nedeni (kısa).
5. "Nerede takıldım / neyi yapamadım" bölümü.

## Kurallar
- **Yalnız `isler/d2-uluslararasi-secim/` klasörüne yaz.** Başka hiçbir dosyaya dokunma, git komutu çalıştırma.
- Ara çıktıyı erken kaydet: ilk 5 dergiyi bulunca SONUC.md'yi yaz, sonra güncelle.
- Em dash (uzun tire) hiçbir yerde kullanma. Türkçe yaz (dergi adları özgün dilinde).
- Bitince kısa bir özet döndür: 10 dergi adı ve doğrulanamayan noktalar.
