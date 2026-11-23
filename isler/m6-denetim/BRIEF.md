# BRIEF · m6 · Bağımsız bilimsel denetim

> Plan: `plan/2026-11-23-plan.md` · Dalga 3 (tek) · Çıktı: `isler/m6-denetim/SONUC.md` ve `isler/m6-denetim/slaytlar-son.md` · Bu klasör dışına yazma, git commit yapma. m5'in dosyasını DEĞİŞTİRME.

## Rol
Sen metni yazmamış, titiz bir hakemsin. Dinleyici bir dekan; tek bir uydurma künye ya da kavram hatası sunumu çürütür. Amacın hataları bulmak ve düzeltilmiş son sürümü üretmek.

## Girdi
- `isler/m5-sunum-icerigi/slaytlar.md` ve `SONUC.md`
- Kaynak ararken: `isler/m1-...`, `m2-...`, `m3-...`, `m4-...` SONUC.md dosyaları
- `plan/2026-11-23-plan.md` (tuzak listesi, süre bütçesi, Bölüm G), `sen/kaynak/2026-11-23-sunum-gorevi.md`
- Erişim: `curl` ile api.crossref.org, Europe PMC, eutils/pmc.ncbi, doi.org, dergipark.org.tr, training.cochrane.org, crd.york.ac.uk, jbi-global-wiki.refined.site açık; WebSearch (ToolSearch ile `select:WebSearch`).

## Denetim listesi (her biri için geçti/kaldı + kanıt)
1. **Künye doğrulama:** kaynakçadaki HER kaynak için Crossref (`https://api.crossref.org/works/<DOI>`) ya da DergiPark/PubMed kaydı ile yazar listesi, yıl, başlık, dergi, cilt, sayı, sayfa, DOI eşleşmesi. DOI'siz kitap ve resmi belgeler için yayıncı/resmi sayfa. Tablo halinde.
2. **Atıf eşleşmesi:** her metin içi atıf kaynakçada; kaynakçadaki her kaynak en az bir slaytta anılıyor. Yazar sayısına göre APA 7 biçimi (1, 2, 3+ yazar; "ve ark.").
3. **Bilimsel ifade denetimi:** plandaki 10 tuzak; ayrıca her istatistik ifadesi (I², τ², d/g, model seçimi, funnel yorumu), PRISMA ifadesi, derleme türü tanımları. Şüpheli her iddiayı kaynağının kendi metninde kontrol et (tam metin açık erişimse oku).
4. **Makale örnekleri:** slayt 11'deki her makalenin sınıfı yöntem metniyle tutarlı mı (Europe PMC/PMC tam metninden bir kez daha bak).
5. **Görev uyumu:** görevdeki A ile E maddelerinin hepsi karşılanmış mı; her slaytta başlık, metin, görsel önerisi, metin içi kaynak, sunucu notu, süre var mı; 3 bilgi sorusu ve cevabı var mı; 4 karşılaştırma sorusu cevaplanmış mı; etik kurul izni koşullu anlatılmış mı.
6. **Sınırlar:** slayt sayısı ≤ 15; süre toplamı 14:45 ile 15:00 (15:00'ı aşmaz); konuşma metni kelime sayısı ≈ süre × 130 (±%15); en az 4 Türkçe kaynak anılıyor; kaynak sayısı ≤ ~25.
7. **Biçim:** em dash ve en dash yok (grep ile say); "taradım" gibi yanlış beyan yok; kurgu veriler etiketli.

## Çıktı
- `slaytlar-son.md`: m5 metninin bütün düzeltmeler uygulanmış tam son sürümü (aynı yapı). m7 bunu kullanacak.
- `SONUC.md`: denetim tablosu (madde · sonuç · kanıt), yapılan her düzeltmenin listesi (slayt · eski · yeni · gerekçe/kaynak), doğrulanamayan ve sunumdan çıkarılan kaynaklar, sunucunun sunumdan önce kontrol etmesi gerekenler, zaman.
- Kesinti dersi: önce denetim tablosunu yaz, sonra düzeltmeleri uygula.
- Em dash ve en dash yok.

## Bitince döndür
Kaç kaynak doğrulandı/düzeltildi/çıkarıldı, kaç bilimsel ifade düzeltildi, son süre ve slayt sayısı, açık sorunlar.

## Ana oturumdan ek notlar (dalga 2 sonrası)

- **Cochrane El Kitabı artık erişilebilir** (training.cochrane.org → www.cochrane.org, 200). m5 El Kitabı'nı kaynakçaya almadı; model seçimi cümlesi 5.0.1 sürümünden ikincil atıfla (akt. Rücker ve ark., 2008) geliyor. Güncel sürümün ilgili bölümünü (bölüm 10) oku: cümle güncel sürümde de varsa, ikincil atıfı güncel bölüm künyesiyle değiştirmek daha savunulabilir (kaynak sayısı 26 olabilir). I² yorum aralıklarını da güncel metinden doğrula.
- m5'in açık bıraktıkları (m5 SONUC.md): Barengo son yazar biçimi ("Correa Bautista, J. E."; yayıncı sayfasıyla karşılaştır) · Sterne ve ark. (2019) RoB 2 beş alanı (yalnız künye düzeyinde) · PROSPERO kapsamı (güncel site) · PRISMA akış şemasının Türkçe kutu metinleri.
- **Okuma kuralı:** konuşma metnindeki parantez içi atıflar sesli okunmaz; kelime sayısını atıflar hariç say. Bu kural slaytlar-son.md'de süre tablosunun altında açıkça dursun.
