FROM python:3.10-slim

WORKDIR /app

# Gerekli paketleri kur
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Gerekli dizinleri oluştur
RUN mkdir -p logs cache

# Çalıştırma
CMD ["sh", "-c", "cd dilekce_uretici && python run_optimized.py"]
