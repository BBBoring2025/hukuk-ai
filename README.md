# Türkiye Hukuk AI Platformu

Türkiye Hukuk AI Platformu, avukatlar, KOBİ'ler ve bireysel kullanıcılar için hukuki süreçleri kolaylaştıran yapay zeka destekli bir platformdur.

## Özellikler

- **Dilekçe Üretici**: Hukuki dilekçeleri otomatik olarak oluşturur
- **Sözleşme Analizi**: Sözleşmeleri analiz eder ve risk değerlendirmesi yapar
- **Hukuki Chatbot**: Hukuki sorulara yanıt verir

## Kurulum

### Gereksinimler

- Python 3.10+
- Node.js 16+
- Nginx
- Supervisor

### Kurulum Adımları

1. Kurulum scriptini çalıştırın:
   ```
   sudo ./scripts/setup.sh
   ```

2. Servisleri başlatın:
   ```
   ./scripts/run.sh
   ```

### Docker ile Kurulum

1. Docker ve Docker Compose'u kurun
2. Aşağıdaki komutu çalıştırın:
   ```
   docker-compose up -d
   ```

## Kullanım

Tarayıcınızda `http://localhost` adresine giderek platformu kullanabilirsiniz.

## KVKK Uyumluluğu

Platform, KVKK (Kişisel Verilerin Korunması Kanunu) ile uyumludur. Detaylı bilgi için `backend/kvkk` dizinindeki belgelere bakabilirsiniz.

## Lisans

Bu proje özel lisans altında dağıtılmaktadır. Tüm hakları saklıdır.
# hukuk-ai
