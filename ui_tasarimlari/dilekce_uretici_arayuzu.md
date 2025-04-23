# Türkiye Hukuk AI Platformu - Dilekçe Üretici Modülü Arayüzü

## Genel Tasarım Prensipleri

- **Kullanıcı Dostu**: Hukuk bilgisi olmayan kullanıcılar için bile anlaşılır
- **Adım Adım Rehberlik**: Kullanıcıyı süreç boyunca yönlendiren akış
- **Hata Önleme**: Kullanıcıların hata yapmasını engelleyen tasarım
- **Mobil Uyumlu**: Tüm cihazlarda sorunsuz çalışan responsive tasarım
- **Profesyonel Görünüm**: Hukuki dokümanların ciddiyetini yansıtan arayüz

## Dilekçe Üretici Ana Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Üretici               ||
|  |                                      ||
|  |  Hızlı ve doğru dilekçeler oluşturun ||
|  +--------------------------------------+|
|                                          |
|  +----------------+  +----------------+  |
|  |  Popüler       |  |  Tüm Dilekçe   |  |
|  |  Dilekçeler    |  |  Kategorileri  |  |
|  +----------------+  +----------------+  |
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Kategorileri          ||
|  |                                      ||
|  | [Tüketici] [İş Hukuku] [Aile]        ||
|  | [Kira] [İdari] [Ceza] [Diğer]        ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Son Oluşturulan Dilekçeler    ||
|  |                                      ||
|  | - Tüketici Şikayet Dilekçesi         ||
|  | - İş Akdi Fesih İtiraz Dilekçesi     ||
|  | - Kira Tespit Davası Dilekçesi       ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluştur               ||
|  |                                      ||
|  | [Yeni Dilekçe Oluştur]               ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Dilekçe Oluşturma Süreci

### Adım 1: Dilekçe Türü Seçimi

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluştur - Adım 1/4    ||
|  |        Dilekçe Türü Seçimi           ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Kategori Seçin                ||
|  |                                      ||
|  | [Tüketici] [İş Hukuku] [Aile]        ||
|  | [Kira] [İdari] [Ceza] [Diğer]        ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Türü Seçin            ||
|  |                                      ||
|  | [ Arama Kutusu ]                     ||
|  |                                      ||
|  | - Tüketici Şikayet Dilekçesi         ||
|  | - Ayıplı Mal İade Dilekçesi          ||
|  | - Abonelik İptal Dilekçesi           ||
|  | - Kredi Kartı İtiraz Dilekçesi       ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Seçilen Dilekçe Hakkında      ||
|  |                                      ||
|  | Tüketici Şikayet Dilekçesi           ||
|  | Bu dilekçe, satın alınan mal veya    ||
|  | hizmetle ilgili şikayetleri ilgili   ||
|  | kurumlara iletmek için kullanılır.   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Geri]                [Devam Et]     ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

### Adım 2: Kişisel Bilgiler

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluştur - Adım 2/4    ||
|  |        Kişisel Bilgiler              ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Sahibi Bilgileri      ||
|  |                                      ||
|  | Ad Soyad: [                      ]   ||
|  | T.C. Kimlik No: [                ]   ||
|  | Adres: [                         ]   ||
|  | Telefon: [                       ]   ||
|  | E-posta: [                       ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Muhatap Bilgileri             ||
|  |                                      ||
|  | Muhatap Türü: [Kurum] [Şirket] [Kişi]||
|  | Muhatap Adı: [                   ]   ||
|  | Adres: [                         ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Bilgilerimi Kaydet] (Opsiyonel)     ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Geri]                [Devam Et]     ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

### Adım 3: Dilekçe İçeriği

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluştur - Adım 3/4    ||
|  |        Dilekçe İçeriği               ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Olay Bilgileri                ||
|  |                                      ||
|  | Satın Alınan Ürün/Hizmet:            ||
|  | [                                 ]   ||
|  |                                      ||
|  | Satın Alma Tarihi:                   ||
|  | [                                 ]   ||
|  |                                      ||
|  | Şikayet Konusu:                      ||
|  | [                                 ]   ||
|  |                                      ||
|  | Olay Detayı:                         ||
|  | [                                 ]   ||
|  | [                                 ]   ||
|  | [                                 ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Talepler                      ||
|  |                                      ||
|  | [✓] Ürün değişimi                    ||
|  | [✓] Ücret iadesi                     ||
|  | [ ] Onarım                           ||
|  | [ ] Tazminat                         ||
|  | [ ] Diğer: [                     ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Geri]                [Devam Et]     ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

### Adım 4: Önizleme ve İndirme

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Oluştur - Adım 4/4    ||
|  |        Önizleme ve İndirme           ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Önizleme              ||
|  |                                      ||
|  | +----------------------------------+ ||
|  | |                                  | ||
|  | |                                  | ||
|  | |      Dilekçe Önizleme Alanı      | ||
|  | |                                  | ||
|  | |                                  | ||
|  | +----------------------------------+ ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Düzenleme Seçenekleri         ||
|  |                                      ||
|  | [Metni Düzenle] [Formatı Değiştir]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        İndirme Seçenekleri           ||
|  |                                      ||
|  | [PDF İndir] [Word İndir] [E-posta]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Geri]                [Tamamla]      ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Tamamlama Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Dilekçe Başarıyla Oluşturuldu ||
|  |                                      ||
|  |            ✓                         ||
|  |                                      ||
|  |  Tüketici Şikayet Dilekçeniz hazır!  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Dilekçeniz Kaydedildi         ||
|  |                                      ||
|  | Dilekçenize "Hesabım > Dilekçelerim" ||
|  | bölümünden her zaman erişebilirsiniz.||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sonraki Adımlar               ||
|  |                                      ||
|  | 1. Dilekçeyi imzalayın               ||
|  | 2. Belirtilen adrese gönderin        ||
|  | 3. Sonucu takip edin                 ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Ne Yapmak İstersiniz?         ||
|  |                                      ||
|  | [Yeni Dilekçe] [Ana Sayfaya Dön]     ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Mobil Görünüm Uyarlamaları

- Tek sütun düzeni
- Daha büyük dokunmatik hedefler
- Adım adım görünüm (tek ekranda tek adım)
- Kaydırılabilir formlar
- Otomatik form doldurma desteği

## Erişilebilirlik Özellikleri

- Yüksek kontrast renk seçenekleri
- Ekran okuyucu uyumluluğu
- Klavye navigasyonu
- Büyütülebilir metin
- Hata mesajları ve yardım ipuçları

## Kullanıcı Deneyimi İyileştirmeleri

- Otomatik kaydetme
- İlerleme göstergesi
- Bağlam duyarlı yardım
- Akıllı form doldurma önerileri
- Dilekçe şablonları arasında kolay geçiş

## Özelleştirme Seçenekleri

- Farklı dilekçe formatları
- Kurumsal şablonlar (avukatlar için)
- Ek belge ekleme
- Özel başlık ve altbilgi
- Yazı tipi ve stil seçenekleri
