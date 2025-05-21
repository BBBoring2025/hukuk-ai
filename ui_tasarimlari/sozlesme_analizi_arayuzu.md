# Türkiye Hukuk AI Platformu - Sözleşme Analizi Modülü Arayüzü

## Genel Tasarım Prensipleri

- **Sezgisel Kullanım**: Karmaşık hukuki analizleri basit ve anlaşılır şekilde sunan arayüz
- **Görsel Geri Bildirim**: Risk seviyelerini ve önemli noktaları görsel olarak vurgulayan tasarım
- **Detaylı Raporlama**: Kapsamlı ancak anlaşılır analiz raporları sunan yapı
- **Karşılaştırmalı Görünüm**: Orijinal metin ve analiz sonuçlarını yan yana gösterme imkanı
- **Kullanıcı Segmentine Göre Uyarlama**: Avukat, KOBİ ve bireysel kullanıcılar için özelleştirilmiş görünümler

## Sözleşme Analizi Ana Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Analizi              ||
|  |                                      ||
|  |  Sözleşmelerinizi güvenle analiz edin||
|  +--------------------------------------+|
|                                          |
|  +----------------+  +----------------+  |
|  |  Yeni Analiz   |  |  Geçmiş        |  |
|  |  Başlat        |  |  Analizler     |  |
|  +----------------+  +----------------+  |
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Türleri              ||
|  |                                      ||
|  | [İş] [Kira] [Satış] [Hizmet]         ||
|  | [Abonelik] [Kredi] [Diğer]           ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Son Analizler                 ||
|  |                                      ||
|  | - Kira Sözleşmesi (2 saat önce)      ||
|  | - İş Sözleşmesi (1 gün önce)         ||
|  | - Satış Sözleşmesi (3 gün önce)      ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Hızlı Analiz                  ||
|  |                                      ||
|  | [Sözleşme Yükle veya Sürükle]        ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Sözleşme Analizi Süreci

### Adım 1: Sözleşme Yükleme

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Analizi - Adım 1/3   ||
|  |        Sözleşme Yükleme              ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Türü Seçin           ||
|  |                                      ||
|  | [İş] [Kira] [Satış] [Hizmet]         ||
|  | [Abonelik] [Kredi] [Diğer]           ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Yükle                ||
|  |                                      ||
|  | +--------------------------------+   ||
|  | |                                |   ||
|  | |  Dosyayı buraya sürükleyin     |   ||
|  | |  veya dosya seçmek için tıklayın|  ||
|  | |                                |   ||
|  | +--------------------------------+   ||
|  |                                      ||
|  | Desteklenen formatlar: PDF, DOCX, JPG||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        veya                          ||
|  |                                      ||
|  | [Kamera ile Tara] [URL Gir]          ||
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

### Adım 2: Analiz Parametreleri

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Analizi - Adım 2/3   ||
|  |        Analiz Parametreleri          ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Analiz Kapsamı                ||
|  |                                      ||
|  | [✓] Genel risk değerlendirmesi       ||
|  | [✓] Hukuki terminoloji kontrolü      ||
|  | [✓] Eksik madde kontrolü             ||
|  | [✓] Yasal uyumluluk kontrolü         ||
|  | [ ] Sektörel standartlara uygunluk   ||
|  | [ ] Detaylı finansal analiz          ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Analiz Derinliği              ||
|  |                                      ||
|  | [ ] Temel (Hızlı analiz)             ||
|  | [✓] Standart (Detaylı analiz)        ||
|  | [ ] Kapsamlı (Uzman seviyesi)        ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Ek Bilgiler (Opsiyonel)       ||
|  |                                      ||
|  | Sözleşme Tarafları:                  ||
|  | [                                 ]   ||
|  |                                      ||
|  | Sözleşme Amacı:                      ||
|  | [                                 ]   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Geri]                [Analizi Başlat]||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

### Adım 3: Analiz Sonuçları

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme Analizi - Adım 3/3   ||
|  |        Analiz Sonuçları              ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Genel Risk Değerlendirmesi    ||
|  |                                      ||
|  |  Risk Seviyesi: Orta                 ||
|  |  ███████████░░░░░░░░░  65%           ||
|  |                                      ||
|  |  Tespit Edilen Sorunlar: 8           ||
|  |  Kritik Sorunlar: 2                  ||
|  |  Öneriler: 5                         ||
|  +--------------------------------------+|
|                                          |
|  +----------------+  +----------------+  |
|  |  Orijinal      |  |  Analiz        |  |
|  |  Sözleşme      |  |  Sonuçları     |  |
|  +----------------+  +----------------+  |
|                                          |
|  +--------------------------------------+|
|  |        Sözleşme İçeriği ve Analiz    ||
|  |                                      ||
|  | +--------------------------------+   ||
|  | |                                |   ||
|  | |  Madde 5: Ödeme Koşulları      |   ||
|  | |  ...                           |   ||
|  | |  Ödemeler, fatura tarihinden   |   ||
|  | |  itibaren 30 gün içinde...     |   ||
|  | |                                |   ||
|  | +--------------------------------+   ||
|  |                                      ||
|  | +--------------------------------+   ||
|  | |                                |   ||
|  | |  ⚠️ Kritik Risk: Ödeme süresi  |   ||
|  | |  belirtilmiş ancak gecikme     |   ||
|  | |  durumunda uygulanacak faiz    |   ||
|  | |  oranı belirtilmemiştir.       |   ||
|  | |                                |   ||
|  | |  📝 Öneri: "Ödemelerin         |   ||
|  | |  gecikmesi durumunda aylık %X  |   ||
|  | |  faiz uygulanır" ifadesinin    |   ||
|  | |  eklenmesi önerilir.           |   ||
|  | |                                |   ||
|  | +--------------------------------+   ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Tespit Edilen Sorunlar        ||
|  |                                      ||
|  | 1. ⚠️ Madde 5: Gecikme faizi belir...||
|  | 2. ⚠️ Madde 8: Fesih koşulları bel...||
|  | 3. ⚡ Madde 12: Mücbir sebep tanım...||
|  | 4. ⚡ Madde 15: Uyuşmazlık çözüm y...||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Öneriler                      ||
|  |                                      ||
|  | 1. Gecikme faizi oranının belirtilm..||
|  | 2. Fesih koşullarının detaylandırıl..||
|  | 3. Mücbir sebep tanımının genişleti..||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Detaylı Rapor] [Düzeltme Önerileri] ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [PDF İndir] [Word İndir] [E-posta]   ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Detaylı Rapor Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Detaylı Analiz Raporu         ||
|  |        Kira Sözleşmesi               ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Rapor Özeti                   ||
|  |                                      ||
|  | Analiz Tarihi: 01.04.2025            ||
|  | Sözleşme Türü: Kira Sözleşmesi       ||
|  | Toplam Madde Sayısı: 18              ||
|  | Analiz Edilen Sayfa Sayısı: 5        ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Risk Dağılımı                 ||
|  |                                      ||
|  | Kritik Riskler: 2                    ||
|  | Orta Seviye Riskler: 4               ||
|  | Düşük Seviye Riskler: 2              ||
|  | Bilgi Notları: 5                     ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Madde Bazlı Analiz            ||
|  |                                      ||
|  | Madde 1: Taraflar                    ||
|  | ✓ Tarafların bilgileri eksiksiz      ||
|  |                                      ||
|  | Madde 2: Kira Konusu                 ||
|  | ✓ Gayrimenkul bilgileri eksiksiz     ||
|  |                                      ||
|  | Madde 3: Kira Süresi                 ||
|  | ⚠️ Kritik Risk: Kira başlangıç       ||
|  | tarihi belirtilmiş ancak bitiş       ||
|  | tarihi net değil                     ||
|  |                                      ||
|  | ...                                  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Yasal Uyumluluk               ||
|  |                                      ||
|  | ✓ 6098 Sayılı Borçlar Kanunu         ||
|  | ⚠️ 6570 Sayılı Gayrimenkul Kiraları  ||
|  | Hakkında Kanun                       ||
|  | ✓ 634 Sayılı Kat Mülkiyeti Kanunu    ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Benzer Sözleşmelerle          ||
|  |        Karşılaştırma                 ||
|  |                                      ||
|  | Standart kira sözleşmelerine göre:   ||
|  | - Depozito miktarı ortalamanın üstünde||
|  | - Kira artış oranı yasal sınırlar içinde||
|  | - Fesih koşulları standartlara uygun ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  | [Raporu İndir] [Düzeltme Önerileri]  ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Düzeltme Önerileri Ekranı

```
+------------------------------------------+
|  Logo   | Menü | Kullanıcı Profili       |
+------------------------------------------+
|                                          |
|  +--------------------------------------+|
|  |        Düzeltme Önerileri            ||
|  |        Kira Sözleşmesi               ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Kritik Düzeltmeler            ||
|  |                                      ||
|  | 1. Madde 3: Kira Süresi              ||
|  |                                      ||
|  | Mevcut Metin:                        ||
|  | "İşbu sözleşme imza tarihinde        ||
|  | başlar ve bir yıl süreyle geçerlidir."||
|  |                                      ||
|  | Önerilen Düzeltme:                   ||
|  | "İşbu sözleşme 01.05.2025 tarihinde  ||
|  | başlar ve 30.04.2026 tarihinde sona  ||
|  | erer."                               ||
|  |                                      ||
|  | [Düzeltmeyi Uygula]                  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Orta Seviye Düzeltmeler       ||
|  |                                      ||
|  | 2. Madde 8: Tahliye Koşulları        ||
|  |                                      ||
|  | Mevcut Metin:                        ||
|  | "Kiracı, kira süresinin bitiminde    ||
|  | gayrimenkulü tahliye etmekle         ||
|  | yükümlüdür."                         ||
|  |                                      ||
|  | Önerilen Düzeltme:                   ||
|  | "Kiracı, kira süresinin bitiminde    ||
|  | gayrimenkulü, teslim aldığı şekilde, ||
|  | normal aşınma ve yıpranma dışında    ||
|  | hasarsız olarak tahliye etmekle      ||
|  | yükümlüdür."                         ||
|  |                                      ||
|  | [Düzeltmeyi Uygula]                  ||
|  +--------------------------------------+|
|                                          |
|  +--------------------------------------+|
|  |        Tüm Düzeltmeleri Uygula       ||
|  |                                      ||
|  | [Tüm Düzeltmeleri Uygula]            ||
|  | [Düzeltilmiş Sözleşmeyi İndir]       ||
|  +--------------------------------------+|
|                                          |
+------------------------------------------+
|              Footer                      |
+------------------------------------------+
```

## Mobil Görünüm Uyarlamaları

- Tek sütun düzeni
- Analiz sonuçlarının sekmeler halinde gösterimi
- Dokunmatik ekrana optimize edilmiş kontroller
- Yakınlaştırma ve kaydırma özellikleri
- Yatay mod desteği (sözleşme ve analiz yan yana)

## Kullanıcı Segmentine Göre Özelleştirmeler

### Avukatlar İçin
- Detaylı yasal referanslar
- Madde bazlı derinlemesine analiz
- İçtihat karşılaştırmaları
- Profesyonel terminoloji
- Gelişmiş düzenleme araçları

### KOBİ'ler İçin
- Sektöre özel risk değerlendirmesi
- İş etkisi analizi
- Finansal etki değerlendirmesi
- Şirket politikalarıyla uyumluluk kontrolü
- Basitleştirilmiş hukuki açıklamalar

### Bireysel Kullanıcılar İçin
- Basit dilde açıklamalar
- Görsel risk göstergeleri
- Adım adım rehberlik
- Temel düzeyde düzeltme önerileri
- Eğitici içerikler ve ipuçları

## Erişilebilirlik Özellikleri

- Yüksek kontrast renk seçenekleri
- Ekran okuyucu uyumluluğu
- Klavye navigasyonu
- Büyütülebilir metin
- Alternatif metin açıklamaları

## Analiz Sonuçları Görselleştirme Seçenekleri

- Isı haritası (risk yoğunluğu)
- Çubuk grafik (madde bazlı risk dağılımı)
- Pasta grafik (risk kategorileri)
- Zaman çizelgesi (sözleşme süresi ve kritik tarihler)
- Karşılaştırma tabloları (benzer sözleşmelerle)
