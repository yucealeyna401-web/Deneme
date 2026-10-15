# BRIEF · d1 · 10 ulusal dergi seçimi

**Plan:** `plan/2026-10-14-plan.md`, iş 1. Dalga 1 (iş 2 ile paralel).

## İş
Beden eğitimi ve spor bilimleri alanında nitelikli **10 ulusal dergi + 3 yedek** seç ve her birinin dizin bilgisini teyit et. Bu liste bir yüksek lisans ödevinde kullanılacak; ardından her derginin 2021 ile 2025 arası yayınları analiz edilecek.

## Seçim ölçütleri
- Türkiye'de yayımlanıyor (yayıncı Türkiye'de). "Uluslararası" adlı ama Türkiye'de yayımlanan dergiler ulusal sayılır.
- **TR Dizin'de güncel olarak dizinli** (2025/2026 itibarıyla). Teyit edilemezse "doğrulanamadı" yaz; teyitsiz dergiyi ilk 10'a koyma, yedeğe al.
- 2021 ile 2025 arasında kesintisiz yayımlanmış (her yıl sayı çıkmış).
- Artı puan: ESCI, Scopus, SPORTDiscus, EBSCO gibi uluslararası dizinlerde de yer alması; köklü olması; alanda sık atıf alması.
- **Alt alan dengesi (ilk 10 için zorunlu):** en az 3 beden eğitimi ve öğretimi/pedagoji ağırlıklı, en az 2 egzersiz ve antrenman bilimi, en az 1 spor psikolojisi/sosyolojisi, en az 1 spor yönetimi/rekreasyon; geri kalan genel spor bilimleri. Genel kapsamlı dergiyi ağırlıklı yayımladığı alana göre say, gerekçesini yaz.

## Kaynaklar ve erişim
Bu ortamda kabuktan (curl) dışarı erişim KAPALI. DergiPark, TR Dizin, Scimago doğrudan açılmıyor. **Yalnız WebSearch ve WebFetch kullan.** WebFetch de açmazsa arama sonuç özetlerinden teyit et ve kaynağını yaz. Bilgi uydurma: bulamadığın alana "doğrulanamadı" yaz.

## Her dergi için kart
Tam ad · kısaltma · yayıncı/kurum · ISSN / e-ISSN · kuruluş yılı · yılda sayı · dizinler (TR Dizin teyit kaynağı ile) · varsa uluslararası dizinler · kapsam (1 cümle) · ağırlıklı alt alan · web adresi (DergiPark bağlantısı) · seçim gerekçesi (1 ile 2 cümle) · bu dergi üzerine yayımlanmış içerik analizi/bibliyometri çalışması varsa künyesi.

## Çıktı
`isler/d1-ulusal-secim/SONUC.md`:
1. Başta özet tablo: # · dergi · ağırlıklı alt alan · TR Dizin (teyitli/doğrulanamadı) · diğer dizinler.
2. Alt alan dengesi kontrolü (zorunlu kotalar tutuyor mu).
3. 10 dergi kartı, sonra 3 yedek kart.
4. Elenen ama düşünülen dergiler ve eleme nedeni (kısa).
5. "Nerede takıldım / neyi yapamadım" bölümü.

## Kurallar
- **Yalnız `isler/d1-ulusal-secim/` klasörüne yaz.** Başka hiçbir dosyaya dokunma, git komutu çalıştırma.
- Ara çıktıyı erken kaydet: ilk 5 dergiyi bulunca SONUC.md'yi yaz, sonra güncelle.
- Em dash (uzun tire) hiçbir yerde kullanma. Türkçe yaz.
- Bitince kısa bir özet döndür: 10 dergi adı ve doğrulanamayan noktalar.
