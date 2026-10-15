# BRIEF · d3-ulusal-analiz-a · Ulusal dergi 1 ile 5 analizi

**Plan:** `plan/2026-10-14-plan.md`, iş 3. Dalga 2 (4 analiz işi paralel).

## İş
Aşağıdaki 5 derginin **2021 ile 2025** (tam yıllar) arasında yayımladığı çalışmaları incele: dergi profili + örneklemli içerik analizi + dergi bazlı eğilim özeti.

## Dergiler
1. Gazi Beden Eğitimi ve Spor Bilimleri Dergisi
2. CBÜ Beden Eğitimi ve Spor Bilimleri Dergisi
3. Spor Bilimleri Araştırmaları Dergisi (JSSR)
4. Spor Hekimliği Dergisi (Turkish Journal of Sports Medicine)
5. Türk Spor ve Egzersiz Dergisi

Notlar: Spor Hekimliği Dergisi DergiPark'ta değil, kendi sitesinde yayımlanıyor (journalofsportsmedicine.org). Seçim işinde JSSR'nin 'pedagoji' ataması zayıf bulundu; kodlamada derginin gerçek konu dağılımını göster.

Dergi künyeleri (ISSN, web adresi, dizin) için `isler/d1-ulusal-secim/SONUC.md` dosyasını oku (yalnız okuma).

## Yöntem (her dergi için)
1. **Dergi profili:** 2021 ile 2025 arası yılda kaç sayı/makale yayımlandığı (bulunabilirse, kaynağıyla; bulunamazsa "doğrulanamadı"), yayın dili, makale türleri.
2. **Örneklem:** her yıl için **en az 4 araştırma makalesi** (dergi başına en az 20). Seçimi bir yıla ya da tek sayıya yığma; mümkünse yılın farklı sayılarından al. Editoryal, düzeltme, kongre özeti alma. Nasıl seçtiğini yaz.
3. **Kodlama:** her makaleyi aşağıdaki şemayla, özetinden (gerekirse tam metinden) kodla. Özetten çıkarılamayan alan "belirsiz". Tahmin etme.
4. **İkincil kaynak:** bu dergi hakkında yayımlanmış içerik analizi/bibliyometri çalışması varsa bul, bulgularını 2 ile 3 cümleyle özetle, künyesini ver.
5. **Dergi eğilim özeti (5 ile 8 cümle):** baskın konu, baskın yaklaşım ve desen, tipik örneklem, yıllar içindeki değişim, dikkat çeken boşluk.

## Kodlama şeması (değiştirme, aynen kullan)
| Alan | Kategoriler |
|---|---|
| Yıl | 2021, 2022, 2023, 2024, 2025 |
| Konu alanı | beden eğitimi ve öğretimi · antrenman ve performans · egzersiz fizyolojisi · sağlık ve fiziksel aktivite · spor psikolojisi · spor sosyolojisi · spor yönetimi ve ekonomisi · rekreasyon ve boş zaman · hareket ve motor gelişim · biyomekanik · uyarlanmış/engelli sporu · diğer |
| Yaklaşım | nicel · nitel · karma · derleme/meta-analiz · kuramsal/kavramsal |
| Desen | betimsel tarama · ilişkisel tarama · deneysel · yarı deneysel · ölçek geliştirme/uyarlama · fenomenoloji · durum çalışması · doküman/içerik analizi · sistematik derleme · meta-analiz · bibliyometrik · diğer |
| Örneklem | ilkokul/ortaokul/lise öğrencisi · üniversite öğrencisi · beden eğitimi öğretmeni/aday · elit sporcu · amatör sporcu · antrenör · sedanter yetişkin · yaşlı · özel gereksinimli birey · doküman · diğer |
| Örneklem büyüklüğü | <30 · 30 ile 100 · 101 ile 300 · 301 ile 1000 · >1000 · belirsiz |
| Veri toplama | ölçek/anket · test ve ölçüm · görüşme · gözlem · doküman · cihaz/laboratuvar · karma |
| Analiz | betimsel · parametrik · parametrik olmayan · regresyon/YEM · içerik/tematik analiz · meta-analitik · diğer |
| Dil | Türkçe · İngilizce · diğer |

## Kaynaklar ve erişim
Kabuktan (curl) dışarı erişim KAPALI. **Yalnız WebSearch ve WebFetch kullan** (dergi sitesi, DergiPark sayı sayfaları, yayıncı sayfaları, PubMed, Google Akademik sonuçları). Bir sayfa açılmazsa arama sonuçlarından ilerle. Makale künyesi ya da kodu uydurma; doğrulayamadığın makaleyi örnekleme alma.

## Çıktılar (yalnız bu klasöre)
- `isler/d3-ulusal-analiz-a/kodlama.md`: tek Markdown tablo, her satır bir makale. Sütunlar: `dergi | yıl | yazar(lar) | başlık | konu | yaklaşım | desen | örneklem | n_aralık | veri_toplama | analiz | dil | DOI/bağlantı`. Sütun adlarını ve kategori yazımını şemadaki gibi tut (sentez işi bu tabloları birleştirecek).
- `isler/d3-ulusal-analiz-a/SONUC.md`: her dergi için profil + frekans özeti (konu, yaklaşım, desen, örneklem için sayılar) + eğilim özeti + ikincil kaynak; en sonda 5 derginin kısa karşılaştırması; "nerede takıldım / neyi yapamadım" bölümü (kaç makale kodlandı, hangi yıllarda eksik kaldı).

## Kurallar
- **Yalnız `isler/d3-ulusal-analiz-a/` klasörüne yaz.** Başka dosyaya dokunma, git komutu çalıştırma.
- **Her dergiyi bitirir bitirmez** kodlama.md ve SONUC.md'yi güncelle (kesintide iş kaybolmasın).
- Em dash (uzun tire) hiçbir yerde kullanma. Türkçe yaz.
- Bitince kısa özet döndür: dergi başına kodlanan makale sayısı, eksikler.
