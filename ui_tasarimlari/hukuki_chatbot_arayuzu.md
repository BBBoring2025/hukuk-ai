# Türkiye Hukuk AI Platformu - Hukuki Chatbot Modülü Arayüzü

## Genel Tasarım Prensipleri

- **Doğal Etkileşim**: Kullanıcıların doğal dilde soru sorabildiği sezgisel arayüz
- **Güvenilir Bilgi**: Yanıtların kaynağını ve güvenilirliğini gösteren şeffaf tasarım
- **Kişiselleştirilmiş Deneyim**: Kullanıcı segmentine ve geçmiş sorulara göre uyarlanabilen arayüz
- **Kolay Erişim**: Platformun her yerinden hızlıca erişilebilen chatbot
- **Yönlendirici Tasarım**: Kullanıcıyı doğru soruları sormaya teşvik eden yapı

## Chatbot Ana Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Hukuki Chatbot                ||
|  |                                      ||
|  |  Hukuki sorularınızı yanıtlıyoruz    ||
|  +--------------------------------------+|
|                                          |
|  +----------------+  +----------------+  |
|  |  Yeni Sohbet   |  |  Geçmiş        |  |
|  |                |  |  Sohbetler     |  |
|  +----------------+  +----------------+  |
|                                          |
|  +--------------------------------------+|
|  |        Popüler Konular               ||
|  |                                      ||
|  | [Tüketici Hakları] [İş Hukuku]       ||
|  | [Kira Hukuku] [Aile Hukuku]          ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Son Sohbetler                 ||
|  |                                      ||
|  | - İş akdi feshi hakkında (2 saat önce)||
|  | - Kira artış oranları (1 gün önce)   ||
|  | - Tüketici hakları (3 gün önce)      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Hızlı Başlangıç               ||
|  |                                      ||
|  | [Hukuki Sorunuzu Yazın...]           ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Chatbot Sohbet Arayüzü

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Hukuki Chatbot                ||
|  |                                      ||
|  |  Yeni Sohbet                         ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  |  Merhaba! Ben Hukuk AI asistanınız.  ||
|  |  Size nasıl yardımcı olabilirim?     ||
|  |                                      ||
|  |  Örnek sorular:                      ||
|  |  - Kira artış oranı ne kadar olabilir?||
|  |  - İşten çıkarılma durumunda haklarım?||
|  |  - Ayıplı mal iade süresi nedir?     ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  |  Kullanıcı:                          ||
|  |  İşveren beni sebepsiz işten çıkardı.||
|  |  Haklarım nelerdir?                  ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  |  Hukuk AI:                           ||
|  |  İşten sebepsiz çıkarılma durumunda  ||
|  |  aşağıdaki haklarınız bulunmaktadır: ||
|  |                                      ||
|  |  1. Kıdem Tazminatı: En az 1 yıl     ||
|  |  çalışmış olmanız halinde, her tam   ||
|  |  yıl için 30 günlük brüt ücretiniz   ||
|  |  tutarında tazminat alabilirsiniz.   ||
|  |                                      ||
|  |  2. İhbar Tazminatı: İş akdiniz      ||
|  |  bildirim süresine uyulmadan feshe-  ||
|  |  dilmişse, bu sürelere ilişkin ücret ||
|  |  tutarında tazminat alabilirsiniz.   ||
|  |                                      ||
|  |  3. İşe İade Davası: 30 veya daha    ||
|  |  fazla işçi çalıştıran işyerlerinde, ||
|  |  en az 6 aylık kıdeminiz varsa ve    ||
|  |  belirsiz süreli iş sözleşmesiyle    ||
|  |  çalışıyorsanız, fesih bildiriminin  ||
|  |  tebliğinden itibaren 1 ay içinde    ||
|  |  işe iade davası açabilirsiniz.      ||
|  |                                      ||
|  |  Kaynak: 4857 Sayılı İş Kanunu,      ||
|  |  Madde 17, 18-21                     ||
|  |                                      ||
|  |  Daha detaylı bilgi almak ister      ||
|  |  misiniz?                            ||
|  |                                      ||
|  |  [Kıdem Tazminatı] [İhbar Tazminatı] ||
|  |  [İşe İade Davası] [Dilekçe Oluştur] ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  |  Kullanıcı:                          ||
|  |  Kıdem tazminatı hesaplama yöntemi   ||
|  |  nedir?                              ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  |  Hukuk AI:                           ||
|  |  Kıdem tazminatı hesaplama yöntemi   ||
|  |  şu şekildedir:                      ||
|  |                                      ||
|  |  Kıdem Tazminatı = Günlük Brüt Ücret ||
|  |  x 30 x Çalışılan Yıl Sayısı         ||
|  |                                      ||
|  |  Günlük brüt ücret, aylık brüt       ||
|  |  ücretin 30'a bölünmesiyle bulunur.  ||
|  |  Brüt ücrete, temel ücrete ek olarak ||
|  |  düzenli ödenen tüm parasal haklar   ||
|  |  (ikramiye, yemek, yol yardımı vb.)  ||
|  |  dahil edilir.                       ||
|  |                                      ||
|  |  Bir yıldan artan süreler için de    ||
|  |  orantılı ödeme yapılır. Örneğin 3   ||
|  |  yıl 6 ay çalışma için 3,5 yıllık    ||
|  |  kıdem tazminatı hesaplanır.         ||
|  |                                      ||
|  |  Kıdem tazminatı, yasal tavan        ||
|  |  ücretle sınırlıdır.                 ||
|  |                                      ||
|  |  Hesaplama yapmak ister misiniz?     ||
|  |                                      ||
|  |  [Hesaplama Yap] [Dilekçe Oluştur]   ||
|  |  [Avukata Danış]                     ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |                                      ||
|  | [Sorunuzu yazın...]      [Gönder]    ||
|  |                                      ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Hesaplama Aracı Entegrasyonu

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Kıdem Tazminatı Hesaplama     ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Hesaplama Bilgileri           ||
|  |                                      ||
|  | İşe Başlama Tarihi:                  ||
|  | [01/01/2020                      ]   ||
|  |                                      ||
|  | İşten Ayrılma Tarihi:                ||
|  | [01/04/2025                      ]   ||
|  |                                      ||
|  | Aylık Brüt Ücret (TL):               ||
|  | [15000                           ]   ||
|  |                                      ||
|  | Ek Ödemeler (Aylık, TL):             ||
|  | [2000                            ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Hesaplama Sonucu              ||
|  |                                      ||
|  | Çalışma Süresi: 5 yıl 3 ay           ||
|  | Günlük Brüt Ücret: 566,67 TL         ||
|  | Kıdem Tazminatı: 89.250,00 TL        ||
|  |                                      ||
|  | Not: Bu hesaplama tahminidir ve      ||
|  | yasal tavan ücreti dikkate almaz.    ||
|  | Kesin hesaplama için bir avukata     ||
|  | danışmanız önerilir.                 ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Sohbete Dön] [Hesaplamayı Kaydet]   ||
|  | [Dilekçe Oluştur]                    ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Dilekçe Oluşturma Entegrasyonu

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluşturma             ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sohbet Bilgilerine Göre       ||
|  |        Dilekçe Oluştur               ||
|  |                                      ||
|  | Sohbetinize göre aşağıdaki dilekçe   ||
|  | türleri uygun olabilir:              ||
|  |                                      ||
|  | [✓] Kıdem Tazminatı Talep Dilekçesi  ||
|  | [ ] İhbar Tazminatı Talep Dilekçesi  ||
|  | [ ] İşe İade Davası Dilekçesi        ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Dilekçe Oluşturmaya Başla]          ||
|  | [Sohbete Dön]                        ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Avukata Danışma Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Avukata Danışma               ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Uzman Avukat Desteği          ||
|  |                                      ||
|  | Bazı hukuki konular uzman desteği    ||
|  | gerektirebilir. Sohbet içeriğinizi   ||
|  | bir avukata yönlendirmek ister misiniz?||
|  |                                      ||
|  | Avantajları:                         ||
|  | - Kişisel durumunuza özel tavsiye    ||
|  | - Yasal süreçlerde rehberlik         ||
|  | - Doküman inceleme ve değerlendirme  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Avukat Seçenekleri            ||
|  |                                      ||
|  | [✓] İş Hukuku Uzmanları              ||
|  | [ ] Aile Hukuku Uzmanları            ||
|  | [ ] Tüketici Hukuku Uzmanları        ||
|  | [ ] Gayrimenkul Hukuku Uzmanları     ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        İletişim Tercihi              ||
|  |                                      ||
|  | [ ] E-posta                          ||
|  | [✓] Telefon                          ||
|  | [ ] Video Görüşme                    ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Avukat Bul] [Sohbete Dön]           ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Geçmiş Sohbetler Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Geçmiş Sohbetler              ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sohbet Geçmişiniz             ||
|  |                                      ||
|  | [Ara...]                             ||
|  |                                      ||
|  | - İş akdi feshi hakkında             ||
|  |   01.04.2025, 14:30                  ||
|  |                                      ||
|  | - Kira artış oranları                ||
|  |   31.03.2025, 10:15                  ||
|  |                                      ||
|  | - Tüketici hakları                   ||
|  |   29.03.2025, 16:45                  ||
|  |                                      ||
|  | - Boşanma süreci                     ||
|  |   25.03.2025, 09:20                  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sohbet Etiketleri             ||
|  |                                      ||
|  | [İş Hukuku] [Kira] [Tüketici] [Aile] ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Yeni Sohbet] [Sohbetleri Yönet]     ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Mobil Görünüm Uyarlamaları

- Tam ekran sohbet arayüzü
- Kolay erişilebilir geri butonu
- Büyük dokunmatik hedefler
- Otomatik tamamlama önerileri
- Ses ile soru sorma seçeneği

## Kullanıcı Segmentine Göre Özelleştirmeler

### Avukatlar İçin
- Yasal referanslar ve içtihatlar
- Mesleki terminoloji
- Detaylı yasal analizler
- Mevzuat güncellemeleri
- Dava örnekleri

### KOBİ'ler İçin
- Şirket hukuku odaklı yanıtlar
- Sektöre özel düzenlemeler
- Çalışan-işveren ilişkileri
- Ticari sözleşme tavsiyeleri
- Vergi ve mali yükümlülükler

### Bireysel Kullanıcılar İçin
- Basit ve anlaşılır dil
- Günlük hayatta karşılaşılan sorunlar
- Adım adım yönlendirmeler
- Görsel destekli açıklamalar
- Pratik örnekler

## Chatbot Özellikleri

### Bilgi Kaynakları
- Türk kanunları ve mevzuatı
- Yargıtay ve Danıştay kararları
- Hukuki makaleler ve doktrin
- Güncel yasal değişiklikler
- Sık sorulan sorular veritabanı

### Yapay Zeka Yetenekleri
- Doğal dil anlama
- Bağlam farkındalığı
- Kişiselleştirilmiş yanıtlar
- Öğrenme ve iyileştirme
- Belirsizlik durumunda netleştirme soruları

### Entegrasyon Özellikleri
- Dilekçe üretici modülüyle entegrasyon
- Sözleşme analizi modülüyle entegrasyon
- Hesaplama araçları
- Takvim ve hatırlatıcılar
- Doküman paylaşımı

## Erişilebilirlik Özellikleri

- Ekran okuyucu uyumluluğu
- Ses ile soru sorma
- Yüksek kontrast modu
- Ayarlanabilir metin boyutu
- Klavye navigasyonu

## Güvenlik ve Gizlilik

- Uçtan uca şifreleme
- Sohbet geçmişi kontrolleri
- Otomatik oturum kapatma
- Veri minimizasyonu
- KVKK uyumlu veri saklama
