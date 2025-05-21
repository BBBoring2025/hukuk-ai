# Türkiye Hukuk AI Platformu Teknik Dokümantasyonu

Bu dokümantasyon, Türkiye Hukuk AI Platformu'nun teknik altyapısını, mimarisini, kullanılan teknolojileri ve geliştirme süreçlerini detaylı olarak açıklamaktadır.

## 1. Sistem Mimarisi

### 1.1. Genel Mimari Yapı

Türkiye Hukuk AI Platformu, modern ve ölçeklenebilir bir mikroservis mimarisi kullanmaktadır. Sistem, üç ana modülden oluşmaktadır:

1. **Dilekçe Üretici Modülü**
2. **Sözleşme Analizi Modülü**
3. **Hukuki Chatbot Modülü**

Her modül, kendi bağımsız API'sine sahiptir ve ortak bir frontend üzerinden kullanıcılara sunulmaktadır.

![Sistem Mimarisi](https://i.imgur.com/placeholder.png)

### 1.2. Teknoloji Yığını

#### 1.2.1. Backend Teknolojileri

- **Programlama Dili**: Python 3.10+
- **API Framework**: FastAPI 0.104.1
- **Web Sunucusu**: Uvicorn 0.23.2
- **Veritabanı**: PostgreSQL 15
- **Önbellek**: Redis 7.0
- **Arama Motoru**: Elasticsearch 8.10
- **Mesaj Kuyruğu**: RabbitMQ 3.12
- **Konteynerizasyon**: Docker, Docker Compose

#### 1.2.2. Frontend Teknolojileri

- **Framework**: React 18
- **UI Kütüphanesi**: Material-UI (MUI) 5.14
- **Durum Yönetimi**: Redux Toolkit
- **Form Yönetimi**: Formik, Yup
- **HTTP İstemcisi**: Axios
- **Grafik ve Görselleştirme**: Chart.js, React-PDF

#### 1.2.3. AI ve NLP Teknolojileri

- **Büyük Dil Modeli**: Fine-tuned Llama 3 (8B parametreli model)
- **Alternatif API**: OpenAI API (GPT-4)
- **NLP İşleme**: spaCy (tr_core_news_sm modeli)
- **Vektör Veritabanı**: Pinecone
- **Metin Analizi**: NLTK, Scikit-learn
- **OCR**: Tesseract OCR, PyPDF2

#### 1.2.4. DevOps ve Altyapı

- **CI/CD**: GitHub Actions
- **Bulut Altyapısı**: AWS (EC2, S3, RDS)
- **Alternatif Bulut**: Digital Ocean
- **Monitoring**: Prometheus, Grafana
- **Loglama**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **CDN**: Cloudflare

### 1.3. Sistem Bileşenleri

#### 1.3.1. API Gateway

- Tüm istemci isteklerini karşılar
- Kimlik doğrulama ve yetkilendirme
- İstek yönlendirme ve yük dengeleme
- Rate limiting ve güvenlik kontrolleri

#### 1.3.2. Kullanıcı Yönetim Servisi

- Kullanıcı kaydı ve kimlik doğrulama
- Profil yönetimi
- Abonelik ve ödeme entegrasyonu
- KVKK uyumlu veri yönetimi

#### 1.3.3. Dilekçe Üretici Servisi

- Dilekçe şablonları yönetimi
- Kullanıcı girdilerine göre dilekçe oluşturma
- PDF oluşturma ve dışa aktarma
- Dilekçe geçmişi ve versiyonlama

#### 1.3.4. Sözleşme Analizi Servisi

- Belge yükleme ve işleme
- Sözleşme türü tanıma
- Madde çıkarımı ve risk analizi
- Öneri ve düzeltme oluşturma

#### 1.3.5. Hukuki Chatbot Servisi

- Kullanıcı sorgu analizi
- Bağlam yönetimi ve oturum takibi
- Yanıt oluşturma ve referans sağlama
- Kullanıcı geri bildirimi ve öğrenme

#### 1.3.6. Veri Depolama Servisi

- Kullanıcı belgeleri yönetimi
- Şifreli depolama
- Yedekleme ve arşivleme
- KVKK uyumlu veri saklama ve silme

## 2. Modül Detayları

### 2.1. Dilekçe Üretici Modülü

#### 2.1.1. Mimari

Dilekçe Üretici Modülü, kullanıcıların hızlı ve kolay bir şekilde profesyonel dilekçeler oluşturmasını sağlayan bir servistir.

```
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Kullanıcı        |----->|  Dilekçe          |----->|  Şablon           |
|  Arayüzü          |      |  İşleme Motoru    |      |  Veritabanı       |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
                                    |
                                    v
                           +-------------------+      +-------------------+
                           |                   |      |                   |
                           |  AI Metin         |----->|  PDF              |
                           |  Geliştirme       |      |  Oluşturma        |
                           |                   |      |                   |
                           +-------------------+      +-------------------+
```

#### 2.1.2. Veri Modeli

**Dilekçe Şablonu**
```json
{
  "id": "uuid",
  "title": "string",
  "category": "string",
  "subcategory": "string",
  "template_content": "string",
  "required_fields": ["string"],
  "optional_fields": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime",
  "is_active": "boolean"
}
```

**Kullanıcı Dilekçesi**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "template_id": "uuid",
  "title": "string",
  "content": "string",
  "field_values": {"key": "value"},
  "status": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "pdf_url": "string"
}
```

#### 2.1.3. API Endpointleri

| Endpoint | Metod | Açıklama |
|----------|-------|----------|
| `/api/petitions/templates` | GET | Tüm dilekçe şablonlarını listeler |
| `/api/petitions/templates/{id}` | GET | Belirli bir şablonun detaylarını getirir |
| `/api/petitions/templates/categories` | GET | Şablon kategorilerini listeler |
| `/api/petitions/create` | POST | Yeni dilekçe oluşturur |
| `/api/petitions/{id}` | GET | Dilekçe detaylarını getirir |
| `/api/petitions/{id}` | PUT | Dilekçeyi günceller |
| `/api/petitions/{id}` | DELETE | Dilekçeyi siler |
| `/api/petitions/{id}/export` | GET | Dilekçeyi PDF olarak dışa aktarır |
| `/api/petitions/user/{user_id}` | GET | Kullanıcının dilekçelerini listeler |

#### 2.1.4. İş Akışı

1. Kullanıcı, dilekçe kategorisi ve türü seçer
2. Sistem, uygun şablonu yükler
3. Kullanıcı, gerekli alanları doldurur
4. AI, girilen bilgilere göre dilekçeyi optimize eder
5. Kullanıcı, önizlemeyi kontrol eder ve düzenlemeler yapar
6. Sistem, dilekçeyi PDF formatında oluşturur
7. Kullanıcı, dilekçeyi indirir veya kaydeder

### 2.2. Sözleşme Analizi Modülü

#### 2.2.1. Mimari

Sözleşme Analizi Modülü, kullanıcıların yükledikleri sözleşmeleri analiz ederek risk değerlendirmesi ve öneriler sunan bir servistir.

```
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Belge            |----->|  Metin            |----->|  Sözleşme Türü    |
|  Yükleme          |      |  Çıkarma (OCR)    |      |  Tanıma           |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
                                                              |
                                                              v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Rapor            |<-----|  Risk             |<-----|  Madde            |
|  Oluşturma        |      |  Değerlendirme    |      |  Analizi          |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
```

#### 2.2.2. Veri Modeli

**Sözleşme**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "file_url": "string",
  "file_type": "string",
  "content": "string",
  "contract_type": "string",
  "status": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Analiz Sonucu**
```json
{
  "id": "uuid",
  "contract_id": "uuid",
  "risk_level": "integer",
  "summary": "string",
  "clauses": [
    {
      "clause_number": "string",
      "content": "string",
      "risk_level": "string",
      "issues": [{"type": "string", "message": "string"}],
      "suggestions": ["string"]
    }
  ],
  "legal_compliance": {"law": "boolean"},
  "created_at": "datetime"
}
```

#### 2.2.3. API Endpointleri

| Endpoint | Metod | Açıklama |
|----------|-------|----------|
| `/api/contracts/upload` | POST | Sözleşme dosyası yükler |
| `/api/contracts/{id}` | GET | Sözleşme detaylarını getirir |
| `/api/contracts/{id}` | DELETE | Sözleşmeyi siler |
| `/api/contracts/user/{user_id}` | GET | Kullanıcının sözleşmelerini listeler |
| `/api/contracts/analyze/{id}` | POST | Sözleşme analizi başlatır |
| `/api/contracts/analysis/{id}` | GET | Analiz sonuçlarını getirir |
| `/api/contracts/analysis/{id}/report` | GET | Analiz raporunu PDF olarak dışa aktarır |

#### 2.2.4. İş Akışı

1. Kullanıcı, sözleşme dosyasını yükler (PDF, DOCX, TXT)
2. Sistem, dosyadan metni çıkarır (OCR gerekirse)
3. AI, sözleşme türünü otomatik olarak tanır
4. Sistem, sözleşmeyi maddelere ayırır
5. AI, her maddeyi analiz eder ve risk değerlendirmesi yapar
6. Sistem, genel risk skoru ve özet oluşturur
7. Kullanıcıya detaylı analiz raporu sunulur

### 2.3. Hukuki Chatbot Modülü

#### 2.3.1. Mimari

Hukuki Chatbot Modülü, kullanıcıların hukuki sorularını yanıtlayan ve rehberlik sağlayan bir servistir.

```
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Kullanıcı        |----->|  Sorgu            |----->|  Bağlam           |
|  Arayüzü          |      |  Analizi          |      |  Yönetimi         |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
                                                              |
                                                              v
+-------------------+      +-------------------+      +-------------------+
|                   |      |                   |      |                   |
|  Yanıt            |<-----|  Bilgi            |<-----|  Hukuki           |
|  Oluşturma        |      |  Çıkarımı         |      |  Bilgi Tabanı     |
|                   |      |                   |      |                   |
+-------------------+      +-------------------+      +-------------------+
```

#### 2.3.2. Veri Modeli

**Sohbet Oturumu**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "category": "string"
}
```

**Sohbet Mesajı**
```json
{
  "id": "uuid",
  "session_id": "uuid",
  "role": "string",
  "content": "string",
  "timestamp": "datetime"
}
```

**Hukuki Bilgi**
```json
{
  "id": "uuid",
  "category": "string",
  "topic": "string",
  "content": "string",
  "references": ["string"],
  "keywords": ["string"],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

#### 2.3.3. API Endpointleri

| Endpoint | Metod | Açıklama |
|----------|-------|----------|
| `/api/chat/query` | POST | Kullanıcı sorgusunu işler |
| `/api/chat/sessions/{user_id}` | GET | Kullanıcının sohbet oturumlarını listeler |
| `/api/chat/session/{id}` | GET | Belirli bir oturumun detaylarını getirir |
| `/api/chat/session/{id}` | DELETE | Sohbet oturumunu siler |
| `/api/chat/categories` | GET | Hukuk kategorilerini listeler |
| `/api/chat/topics/{category}` | GET | Belirli bir kategorideki konuları listeler |
| `/api/chat/faqs/{category}` | GET | Belirli bir kategorideki SSS'leri listeler |

#### 2.3.4. İş Akışı

1. Kullanıcı, hukuki bir soru sorar
2. Sistem, soruyu analiz eder ve kategorisini belirler
3. AI, soruyla ilgili hukuki bilgileri bilgi tabanından çıkarır
4. Sistem, kullanıcının önceki sorularını ve bağlamı değerlendirir
5. AI, anlaşılır ve doğru bir yanıt oluşturur
6. Sistem, ilgili yasal referansları ve ek bilgileri ekler
7. Kullanıcıya yanıt, öneriler ve ilgili konular sunulur

## 3. Veri Güvenliği ve KVKK Uyumluluğu

### 3.1. Veri Şifreleme

- **Aktarım Şifrelemesi**: TLS 1.3 protokolü ile tüm veri aktarımları şifrelenir
- **Depolama Şifrelemesi**: AES-256 algoritması ile veritabanı ve dosya depolama şifrelenir
- **Uçtan Uca Şifreleme**: Hassas belgeler için uçtan uca şifreleme uygulanır

### 3.2. Kimlik Doğrulama ve Yetkilendirme

- **JWT Tabanlı Kimlik Doğrulama**: JSON Web Token kullanılarak güvenli kimlik doğrulama
- **Rol Tabanlı Erişim Kontrolü**: Kullanıcı rollerine göre erişim yetkilendirmesi
- **İki Faktörlü Kimlik Doğrulama**: Hassas işlemler için 2FA desteği
- **OAuth 2.0 Entegrasyonu**: Sosyal medya ve diğer servislerle güvenli kimlik doğrulama

### 3.3. Veri Saklama ve İmha

- **Veri Minimizasyonu**: Sadece gerekli kişisel verilerin toplanması
- **Otomatik Veri İmha**: Saklama süresi dolan verilerin otomatik silinmesi
- **Kullanıcı Veri Silme**: Kullanıcıların kendi verilerini silme hakkı
- **Veri Saklama Politikası**: KVKK uyumlu veri saklama süreleri ve politikaları

### 3.4. Güvenlik İzleme ve Loglama

- **Güvenlik Logları**: Tüm sistem erişimleri ve işlemleri loglanır
- **Anormal Davranış Tespiti**: Şüpheli aktiviteleri tespit eden izleme sistemi
- **Düzenli Güvenlik Taramaları**: Otomatik güvenlik açığı taramaları
- **Penetrasyon Testleri**: Düzenli sızma testleri ile güvenlik değerlendirmesi

## 4. Ölçeklenebilirlik ve Performans

### 4.1. Yatay Ölçeklendirme

- **Konteynerizasyon**: Docker ile servis konteynerizasyonu
- **Orchestration**: Kubernetes ile konteyner yönetimi
- **Otomatik Ölçeklendirme**: Yük bazlı otomatik ölçeklendirme
- **Bölge Replikasyonu**: Farklı coğrafi bölgelerde servis replikasyonu

### 4.2. Önbellek Stratejisi

- **Redis Önbellek**: Sık erişilen veriler için Redis önbellek
- **CDN Entegrasyonu**: Statik içerikler için CDN kullanımı
- **Veritabanı Önbelleği**: Veritabanı sorguları için önbellek mekanizmaları
- **Önbellek İnvalidasyonu**: Akıllı önbellek geçersiz kılma stratejileri

### 4.3. Veritabanı Optimizasyonu

- **İndeksleme**: Veritabanı sorgularını hızlandırmak için optimum indeksleme
- **Sharding**: Büyük veri setleri için veritabanı sharding
- **Read Replicas**: Okuma işlemleri için replikalar
- **Bağlantı Havuzu**: Veritabanı bağlantı havuzu optimizasyonu

### 4.4. API Optimizasyonu

- **Rate Limiting**: API isteklerini sınırlama
- **Pagination**: Büyük veri setleri için sayfalama
- **Asenkron İşlemler**: Uzun süren işlemler için asenkron işleme
- **Batch İşlemler**: Toplu işlemler için batch API'ler

## 5. Geliştirme ve Dağıtım Süreci

### 5.1. Geliştirme Ortamı

- **Geliştirme Ortamı**: Yerel Docker tabanlı geliştirme ortamı
- **Test Ortamı**: Staging sunucuları
- **Üretim Ortamı**: Bulut tabanlı üretim ortamı
- **CI/CD Pipeline**: GitHub Actions ile sürekli entegrasyon ve dağıtım

### 5.2. Kod Kalitesi ve Test

- **Birim Testleri**: Pytest ile birim testleri
- **Entegrasyon Testleri**: API ve servis entegrasyon testleri
- **UI Testleri**: Selenium ve Cypress ile UI testleri
- **Kod Kalite Kontrolleri**: ESLint, Pylint, Black ile kod kalite kontrolleri
- **Kod İnceleme**: Pull request ve kod inceleme süreci

### 5.3. Dağıtım Süreci

- **Sürüm Yönetimi**: Semantic versioning
- **Feature Flags**: Yeni özellikleri kontrollü açma
- **Blue-Green Deployment**: Kesintisiz dağıtım
- **Rollback Mekanizması**: Hızlı geri alma mekanizması
- **Canary Releases**: Kademeli özellik yayınlama

### 5.4. İzleme ve Hata Ayıklama

- **Uygulama İzleme**: Prometheus ile metrik toplama
- **Görselleştirme**: Grafana ile metrik görselleştirme
- **Log Yönetimi**: ELK Stack ile merkezi log yönetimi
- **Hata İzleme**: Sentry ile hata izleme ve raporlama
- **Performans İzleme**: New Relic ile uygulama performans izleme

## 6. Kurulum ve Yapılandırma

### 6.1. Sistem Gereksinimleri

#### 6.1.1. Minimum Donanım Gereksinimleri

- **CPU**: 4 çekirdek
- **RAM**: 8 GB
- **Disk**: 100 GB SSD
- **Ağ**: 100 Mbps

#### 6.1.2. Önerilen Donanım Gereksinimleri

- **CPU**: 8 çekirdek
- **RAM**: 16 GB
- **Disk**: 250 GB SSD
- **Ağ**: 1 Gbps

#### 6.1.3. Yazılım Gereksinimleri

- **İşletim Sistemi**: Ubuntu 22.04 LTS
- **Docker**: 24.0+
- **Docker Compose**: 2.20+
- **Python**: 3.10+
- **Node.js**: 18.0+
- **PostgreSQL**: 15+
- **Redis**: 7.0+

### 6.2. Kurulum Adımları

#### 6.2.1. Temel Kurulum

```bash
# Repo'yu klonla
git clone https://github.com/hukuk-ai-platform/platform.git
cd platform

# Ortam değişkenlerini yapılandır
cp .env.example .env
nano .env

# Docker imajlarını oluştur ve başlat
docker-compose up -d
```

#### 6.2.2. Veritabanı Kurulumu

```bash
# Veritabanı migrasyonlarını çalıştır
docker-compose exec api python manage.py migrate

# Temel verileri yükle
docker-compose exec api python manage.py loaddata initial_data
```

#### 6.2.3. AI Modellerini Yapılandırma

```bash
# AI modellerini indir
docker-compose exec ai-service python download_models.py

# Model yapılandırmasını güncelle
docker-compose exec ai-service python configure_models.py
```

### 6.3. Yapılandırma Seçenekleri

#### 6.3.1. Temel Yapılandırma

```yaml
# config.yaml
app:
  name: "Türkiye Hukuk AI Platformu"
  environment: "production"
  debug: false
  secret_key: "your-secret-key"

database:
  host: "db"
  port: 5432
  name: "hukuk_ai_db"
  user: "hukuk_ai_user"
  password: "your-db-password"

redis:
  host: "redis"
  port: 6379
  db: 0

ai:
  model_type: "local"  # "local" veya "api"
  local_model_path: "/app/models/llama3-8b-turkish-legal"
  api_key: ""  # API kullanılacaksa
  temperature: 0.7
  max_tokens: 2048
```

#### 6.3.2. Gelişmiş Yapılandırma

```yaml
# advanced_config.yaml
security:
  jwt_expiration: 86400  # 24 saat
  refresh_token_expiration: 604800  # 7 gün
  password_hash_algorithm: "bcrypt"
  cors_origins: ["https://example.com"]
  rate_limit: 100  # istek/dakika

storage:
  provider: "s3"  # "local", "s3" veya "azure"
  bucket: "hukuk-ai-files"
  region: "eu-central-1"
  access_key: "your-access-key"
  secret_key: "your-secret-key"

email:
  provider: "smtp"
  host: "smtp.example.com"
  port: 587
  username: "noreply@example.com"
  password: "your-email-password"
  from_email: "noreply@example.com"
  use_tls: true
```

### 6.4. Bakım ve Güncelleme

#### 6.4.1. Rutin Bakım

```bash
# Veritabanı yedekleme
docker-compose exec db pg_dump -U hukuk_ai_user hukuk_ai_db > backup_$(date +%Y%m%d).sql

# Log rotasyonu
docker-compose exec api python manage.py rotate_logs

# Önbellek temizleme
docker-compose exec redis redis-cli FLUSHALL
```

#### 6.4.2. Sistem Güncelleme

```bash
# Güncellemeleri çek
git pull origin main

# Docker imajlarını güncelle
docker-compose build

# Servisleri yeniden başlat
docker-compose down
docker-compose up -d

# Veritabanı migrasyonlarını çalıştır
docker-compose exec api python manage.py migrate
```

## 7. API Dokümantasyonu

### 7.1. Kimlik Doğrulama

#### 7.1.1. Kullanıcı Kaydı

**Endpoint:** `POST /api/auth/register`

**İstek:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "name": "John Doe",
  "user_type": "individual"
}
```

**Yanıt:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "John Doe",
  "user_type": "individual",
  "created_at": "2025-04-01T12:00:00Z"
}
```

#### 7.1.2. Giriş

**Endpoint:** `POST /api/auth/login`

**İstek:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Yanıt:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

### 7.2. Dilekçe Üretici API

#### 7.2.1. Dilekçe Şablonları Listesi

**Endpoint:** `GET /api/petitions/templates`

**Yanıt:**
```json
{
  "templates": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "title": "İş Mahkemesi Dava Dilekçesi",
      "category": "iş_hukuku",
      "subcategory": "dava_dilekçesi",
      "required_fields": ["davacı_bilgileri", "davalı_bilgileri", "talep"],
      "created_at": "2025-03-15T10:30:00Z"
    },
    {
      "id": "550e8400-e29b-41d4-a716-446655440002",
      "title": "Tüketici Hakem Heyeti Başvuru Dilekçesi",
      "category": "tüketici_hukuku",
      "subcategory": "hakem_heyeti",
      "required_fields": ["başvuran_bilgileri", "karşı_taraf_bilgileri", "talep"],
      "created_at": "2025-03-16T14:45:00Z"
    }
  ],
  "total": 2,
  "page": 1,
  "per_page": 10
}
```

#### 7.2.2. Dilekçe Oluşturma

**Endpoint:** `POST /api/petitions/create`

**İstek:**
```json
{
  "template_id": "550e8400-e29b-41d4-a716-446655440001",
  "title": "İşe İade Davası",
  "field_values": {
    "davacı_bilgileri": {
      "ad_soyad": "Ahmet Yılmaz",
      "tc_kimlik": "12345678901",
      "adres": "Örnek Mah. Test Sok. No:1 Ankara"
    },
    "davalı_bilgileri": {
      "ad_soyad": "XYZ Şirketi",
      "adres": "Sanayi Mah. Fabrika Sok. No:10 Ankara"
    },
    "talep": "İşe iade ve tazminat talebi"
  }
}
```

**Yanıt:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440003",
  "template_id": "550e8400-e29b-41d4-a716-446655440001",
  "title": "İşe İade Davası",
  "status": "created",
  "created_at": "2025-04-01T15:30:00Z",
  "preview_url": "/api/petitions/550e8400-e29b-41d4-a716-446655440003/preview"
}
```

### 7.3. Sözleşme Analizi API

#### 7.3.1. Sözleşme Yükleme

**Endpoint:** `POST /api/contracts/upload`

**İstek:**
```
Content-Type: multipart/form-data

file: [binary data]
title: Kira Sözleşmesi
```

**Yanıt:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440004",
  "title": "Kira Sözleşmesi",
  "file_type": "pdf",
  "status": "uploaded",
  "created_at": "2025-04-01T16:45:00Z",
  "file_id": "file-550e8400-e29b-41d4-a716-446655440004"
}
```

#### 7.3.2. Sözleşme Analizi

**Endpoint:** `POST /api/contracts/analyze/550e8400-e29b-41d4-a716-446655440004`

**İstek:**
```json
{
  "contract_type": "kira",
  "analysis_scope": ["general", "legal", "missing"],
  "analysis_depth": "standard"
}
```

**Yanıt:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440005",
  "contract_id": "550e8400-e29b-41d4-a716-446655440004",
  "status": "processing",
  "estimated_completion_time": "2025-04-01T17:00:00Z"
}
```

### 7.4. Hukuki Chatbot API

#### 7.4.1. Soru Sorma

**Endpoint:** `POST /api/chat/query`

**İstek:**
```json
{
  "query": "İşten çıkarıldım, haklarım nelerdir?",
  "session_id": "550e8400-e29b-41d4-a716-446655440006",
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Yanıt:**
```json
{
  "response": "İşten çıkarılma durumunda sahip olduğunuz haklar şunlardır: 1. Kıdem tazminatı: En az 1 yıl çalışmış olmanız ve belirli koşulların sağlanması gerekir. 2. İhbar tazminatı: İşveren tarafından bildirim süresine uyulmadan yapılan fesihlerde hak edilir. 3. Kullanılmayan izin ücreti: Hak edilmiş ancak kullanılmamış yıllık izinlerinizin ücreti. 4. İşe iade davası: Haksız fesih durumunda, belirli koşulları sağlıyorsanız açabilirsiniz.",
  "session_id": "550e8400-e29b-41d4-a716-446655440006",
  "suggestions": [
    "Kıdem tazminatı nasıl hesaplanır?",
    "İşe iade davası açmak için ne kadar sürem var?",
    "İhbar tazminatı ne kadardır?"
  ],
  "related_topics": [
    "Kıdem Tazminatı",
    "İhbar Tazminatı",
    "İşe İade"
  ],
  "references": [
    {
      "title": "4857 Sayılı İş Kanunu",
      "url": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4857.pdf"
    }
  ],
  "tools": [
    {
      "type": "calculator",
      "name": "Kıdem Tazminatı Hesaplama",
      "description": "Kıdem tazminatınızı hesaplamak için bu aracı kullanabilirsiniz."
    }
  ]
}
```

## 8. Hata Kodları ve Çözümleri

### 8.1. API Hata Kodları

| Kod | Hata | Açıklama | Çözüm |
|-----|------|----------|-------|
| 400 | Bad Request | İstek formatı hatalı | İstek parametrelerini kontrol edin |
| 401 | Unauthorized | Kimlik doğrulama başarısız | Giriş yapın veya token'ı yenileyin |
| 403 | Forbidden | Yetkisiz erişim | Kullanıcı yetkilerini kontrol edin |
| 404 | Not Found | Kaynak bulunamadı | URL'yi kontrol edin |
| 422 | Unprocessable Entity | Geçersiz veri | Gönderilen verileri kontrol edin |
| 429 | Too Many Requests | İstek limiti aşıldı | Daha az istek gönderin |
| 500 | Internal Server Error | Sunucu hatası | Sistem yöneticisiyle iletişime geçin |

### 8.2. Yaygın Hatalar ve Çözümleri

#### 8.2.1. Bağlantı Hataları

- **Hata**: API'ye bağlanılamıyor
- **Çözüm**: Ağ bağlantınızı ve sunucu durumunu kontrol edin

#### 8.2.2. Kimlik Doğrulama Hataları

- **Hata**: Token süresi dolmuş
- **Çözüm**: Refresh token ile yeni bir access token alın

#### 8.2.3. Dosya İşleme Hataları

- **Hata**: Dosya yüklenemiyor
- **Çözüm**: Dosya boyutunu ve formatını kontrol edin

#### 8.2.4. AI İşleme Hataları

- **Hata**: AI yanıt üretemiyor
- **Çözüm**: Sorguyu basitleştirin veya daha açık hale getirin

## 9. Entegrasyon Kılavuzu

### 9.1. Frontend Entegrasyonu

#### 9.1.1. React Entegrasyonu

```jsx
import axios from 'axios';

// API istemcisi oluştur
const api = axios.create({
  baseURL: 'https://api.hukuk-ai.com',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Kimlik doğrulama interceptor'ı
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Dilekçe şablonlarını getir
const fetchTemplates = async () => {
  try {
    const response = await api.get('/api/petitions/templates');
    return response.data.templates;
  } catch (error) {
    console.error('Şablonlar getirilemedi:', error);
    throw error;
  }
};

// Dilekçe oluştur
const createPetition = async (templateId, title, fieldValues) => {
  try {
    const response = await api.post('/api/petitions/create', {
      template_id: templateId,
      title,
      field_values: fieldValues,
    });
    return response.data;
  } catch (error) {
    console.error('Dilekçe oluşturulamadı:', error);
    throw error;
  }
};
```

#### 9.1.2. Chatbot Entegrasyonu

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChatComponent = ({ userId }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(false);

  // Yeni oturum oluştur veya mevcut oturumu yükle
  useEffect(() => {
    const loadSession = async () => {
      try {
        const response = await axios.get(`/api/chat/sessions/${userId}`);
        if (response.data.length > 0) {
          setSessionId(response.data[0].id);
          setMessages(response.data[0].messages);
        } else {
          // Yeni oturum oluştur
          const newSession = await axios.post('/api/chat/session', { user_id: userId });
          setSessionId(newSession.data.id);
        }
      } catch (error) {
        console.error('Oturum yüklenemedi:', error);
      }
    };

    loadSession();
  }, [userId]);

  // Mesaj gönder
  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('/api/chat/query', {
        query: input,
        session_id: sessionId,
        user_id: userId,
      });

      const botMessage = { role: 'assistant', content: response.data.response };
      setMessages([...messages, userMessage, botMessage]);
      setLoading(false);
    } catch (error) {
      console.error('Mesaj gönderilemedi:', error);
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.role}`}>
            {msg.content}
          </div>
        ))}
        {loading && <div className="loading">Yanıt oluşturuluyor...</div>}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Hukuki sorunuzu yazın..."
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage} disabled={loading}>
          Gönder
        </button>
      </div>
    </div>
  );
};

export default ChatComponent;
```

### 9.2. Mobil Entegrasyonu

#### 9.2.1. React Native Entegrasyonu

```jsx
import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';
import axios from 'axios';

const MobileChatComponent = ({ userId, sessionId }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('https://api.hukuk-ai.com/api/chat/query', {
        query: input,
        session_id: sessionId,
        user_id: userId,
      });

      const botMessage = { role: 'assistant', content: response.data.response };
      setMessages([...messages, userMessage, botMessage]);
      setLoading(false);
    } catch (error) {
      console.error('Mesaj gönderilemedi:', error);
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={messages}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <View style={[styles.messageBubble, item.role === 'user' ? styles.userBubble : styles.botBubble]}>
            <Text style={styles.messageText}>{item.content}</Text>
          </View>
        )}
      />
      {loading && <Text style={styles.loading}>Yanıt oluşturuluyor...</Text>}
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          value={input}
          onChangeText={setInput}
          placeholder="Hukuki sorunuzu yazın..."
        />
        <Button title="Gönder" onPress={sendMessage} disabled={loading} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
  messageBubble: {
    padding: 10,
    borderRadius: 10,
    marginVertical: 5,
    maxWidth: '80%',
  },
  userBubble: {
    backgroundColor: '#DCF8C6',
    alignSelf: 'flex-end',
  },
  botBubble: {
    backgroundColor: '#FFFFFF',
    alignSelf: 'flex-start',
  },
  messageText: {
    fontSize: 16,
  },
  loading: {
    alignSelf: 'center',
    marginVertical: 10,
    color: '#888',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 10,
  },
  input: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#DDD',
    borderRadius: 5,
    padding: 10,
    marginRight: 10,
  },
});

export default MobileChatComponent;
```

### 9.3. Webhook Entegrasyonu

```javascript
// Webhook handler örneği
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

// Yeni dilekçe oluşturulduğunda tetiklenen webhook
app.post('/webhooks/petition-created', (req, res) => {
  const { petition_id, user_id, title, created_at } = req.body;
  
  console.log(`Yeni dilekçe oluşturuldu: ${title}`);
  
  // Kendi sisteminizde işlem yapın
  // Örneğin: veritabanına kaydet, bildirim gönder, vb.
  
  res.status(200).json({ status: 'success' });
});

// Sözleşme analizi tamamlandığında tetiklenen webhook
app.post('/webhooks/contract-analysis-completed', (req, res) => {
  const { analysis_id, contract_id, user_id, risk_level } = req.body;
  
  console.log(`Sözleşme analizi tamamlandı: ${contract_id}, Risk: ${risk_level}`);
  
  // Kendi sisteminizde işlem yapın
  
  res.status(200).json({ status: 'success' });
});

app.listen(3000, () => {
  console.log('Webhook sunucusu çalışıyor: http://localhost:3000');
});
```

## 10. Sürüm Geçmişi ve Yol Haritası

### 10.1. Sürüm Geçmişi

| Sürüm | Tarih | Değişiklikler |
|-------|-------|---------------|
| 1.0.0 | 2025-04-01 | İlk sürüm |
| 1.0.1 | 2025-04-15 | Hata düzeltmeleri |
| 1.1.0 | 2025-05-01 | Yeni dilekçe şablonları eklendi |
| 1.2.0 | 2025-06-01 | Sözleşme analizi iyileştirmeleri |
| 1.3.0 | 2025-07-01 | Chatbot bilgi tabanı genişletildi |

### 10.2. Gelecek Sürüm Planı

| Sürüm | Planlanan Tarih | Planlanan Özellikler |
|-------|----------------|----------------------|
| 1.4.0 | 2025-08-01 | Mobil uygulama desteği |
| 1.5.0 | 2025-09-01 | Avukat eşleştirme sistemi |
| 2.0.0 | 2025-10-01 | Yeni AI modeli entegrasyonu |
| 2.1.0 | 2025-11-01 | Çoklu dil desteği |
| 2.2.0 | 2025-12-01 | Gelişmiş analitik paneli |

### 10.3. Uzun Vadeli Yol Haritası

- **2026 Q1**: Blockchain tabanlı belge doğrulama
- **2026 Q2**: Sesli asistan entegrasyonu
- **2026 Q3**: Mahkeme kararları analiz motoru
- **2026 Q4**: Yapay zeka destekli hukuki tahmin sistemi
- **2027 Q1**: Sanal gerçeklik duruşma simülasyonu

## 11. Lisans ve Telif Hakkı

© 2025 Türkiye Hukuk AI Platformu. Tüm hakları saklıdır.

Bu dokümantasyon ve ilgili yazılım, Türkiye Hukuk AI Platformu'nun özel mülkiyetidir. İzinsiz kopyalanması, dağıtılması veya kullanılması yasaktır.

---

**Son Güncelleme:** 1 Nisan 2025
