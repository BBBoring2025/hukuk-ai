# Türkiye Hukuk AI Platformu Kurulum Kılavuzu

Bu kılavuz, Türkiye Hukuk AI Platformu'nun kurulumu için adım adım talimatlar içerir.

## Sistem Gereksinimleri

- İşletim Sistemi: Ubuntu 20.04 LTS veya üzeri
- RAM: En az 4GB
- Disk: En az 20GB boş alan
- CPU: En az 2 çekirdek

## Manuel Kurulum

### 1. Gerekli Paketlerin Kurulumu

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip nodejs npm nginx supervisor
```

### 2. Python Bağımlılıklarının Kurulumu

```bash
pip3 install fastapi uvicorn gunicorn pydantic python-docx docxtpl docx2pdf nltk PyPDF2 spacy scikit-learn numpy aiofiles python-multipart
```

### 3. Frontend Bağımlılıklarının Kurulumu

```bash
cd frontend
npm install
```

### 4. Nginx Yapılandırması

```bash
sudo cp config/nginx.conf /etc/nginx/nginx.conf
sudo systemctl restart nginx
```

### 5. Supervisor Yapılandırması

```bash
sudo cp config/supervisor.conf /etc/supervisor/conf.d/hukuk_ai_platformu.conf
sudo supervisorctl reread
sudo supervisorctl update
```

## Docker ile Kurulum

### 1. Docker ve Docker Compose Kurulumu

```bash
# Docker kurulumu
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce

# Docker Compose kurulumu
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 2. Docker Compose ile Çalıştırma

```bash
docker-compose up -d
```

## Servis Yönetimi

### Servisleri Başlatma

```bash
./scripts/run.sh
```

### Servisleri Durdurma

```bash
sudo supervisorctl stop all
```

### Servis Durumunu Kontrol Etme

```bash
sudo supervisorctl status
```

## Sorun Giderme

### Log Dosyaları

- Backend logları: `logs/` dizininde
- Nginx logları: `/var/log/nginx/`
- Supervisor logları: `/var/log/supervisor/`

### Yaygın Sorunlar ve Çözümleri

1. **Port çakışması**: Eğer 8000, 8001, 8002 veya 80 portları başka uygulamalar tarafından kullanılıyorsa, yapılandırma dosyalarında port numaralarını değiştirin.

2. **Bağımlılık hataları**: Eksik bağımlılıklar için `pip install -r backend/requirements.txt` komutunu çalıştırın.

3. **Nginx hataları**: `sudo nginx -t` komutu ile Nginx yapılandırmasını test edin.
