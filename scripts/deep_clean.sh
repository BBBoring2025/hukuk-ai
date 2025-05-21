#!/bin/bash

# Kapsamlı temizlik scripti - 20mayishukukai projesi için
echo "Kapsamlı temizlik başlatılıyor..."

# Çalışma dizinini belirle
PROJECT_DIR="/Users/ozdenserkansenalp/Desktop/20mayishukukai"
cd $PROJECT_DIR

# 1. Git Temizliği ve Optimizasyonu
echo "Git depo temizliği yapılıyor..."
# Git geçmişini temizle (Dikkat: Bu işlem git geçmişini değiştirir!)
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Büyük dosyaları git geçmişinden kaldır (isteğe bağlı, dikkatli kullanın)
# Bu işlem için BFG Repo-Cleaner kullanılabilir
# java -jar bfg.jar --strip-blobs-bigger-than 10M .

# 2. Geçici Dosya ve Klasörleri Temizle
echo "Geçici dosyalar temizleniyor..."
# Node.js ilgili dosyalar
find . -name "node_modules" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "package-lock.json" -type f -delete
find . -name "yarn.lock" -type f -delete
find . -name ".npm" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name ".yarn" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name ".pnpm" -type d -prune -exec rm -rf {} \; 2>/dev/null

# Build çıktıları
find . -name "build" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "dist" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.min.*" -type f -delete

# Python önbellek dosyaları
find . -name "__pycache__" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.pyc" -type f -delete
find . -name "*.pyo" -type f -delete
find . -name "*.pyd" -type f -delete
find . -name ".pytest_cache" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name ".coverage" -type f -delete
find . -name ".mypy_cache" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name ".tox" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.egg-info" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.egg" -type f -delete
find . -name ".eggs" -type d -prune -exec rm -rf {} \; 2>/dev/null

# Veri silme (dikkatli kullanın)
find . -path "*/data/tmp*" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -path "*/data/cache*" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -path "*/data/processed*" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.csv.tmp" -type f -delete
find . -name "*.csv.bak" -type f -delete

# Log dosyalarını temizle
find . -name "*.log" -type f -delete
find . -path "./logs/*" -type f -delete
mkdir -p logs

# Editor ve IDE dosyalarını temizle
find . -name ".DS_Store" -type f -delete
find . -name "._*" -type f -delete
find . -name "Thumbs.db" -type f -delete
find . -name "desktop.ini" -type f -delete
find . -name ".directory" -type f -delete
find . -name "*.swp" -type f -delete
find . -name "*.swo" -type f -delete
find . -name "*~" -type f -delete
find . -name ".idea" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name ".vscode" -type d -prune -exec rm -rf {} \; 2>/dev/null
find . -name "*.sublime-*" -type f -delete
find . -name ".project" -type f -delete
find . -name ".classpath" -type f -delete
find . -name ".settings" -type d -prune -exec rm -rf {} \; 2>/dev/null

# Docker temizliği
find . -name "*.BAK.yml" -type f -delete
find . -name "*.OLD.yml" -type f -delete
find . -name "docker-compose.*.yml" ! -name "docker-compose.yml" ! -name "docker-compose.override.yml" -type f -delete

# 3. Frontend Optimizasyonu
echo "Frontend temizleniyor..."
if [ -d "frontend" ]; then
  # Gereksiz frontend kaynak dosyalarını temizle
  find ./frontend -name "*.min.js.map" -type f -delete
  find ./frontend -name "*.min.css.map" -type f -delete
  find ./frontend -name "*.chunk.js.map" -type f -delete
fi

# 4. Backend Optimizasyonu
echo "Backend temizleniyor..."
if [ -d "backend" ]; then
  # Gereksiz backend dosyalarını temizle
  find ./backend -name "__pycache__" -type d -prune -exec rm -rf {} \; 2>/dev/null
  find ./backend -name "*.pyc" -type f -delete
  find ./backend -name ".env.*" ! -name ".env.example" -type f -delete
fi

# 5. Dosya İzinlerini Düzelt
echo "Dosya izinleri düzenleniyor..."
find . -type d -exec chmod 755 {} \; 2>/dev/null
find . -type f -exec chmod 644 {} \; 2>/dev/null
find ./scripts -name "*.sh" -type f -exec chmod 755 {} \; 2>/dev/null

# 6. Boş dizinleri kaldır
echo "Boş dizinler temizleniyor..."
find . -type d -empty -delete

echo "Temizlik tamamlandı!"

# Disk kullanımını göster
du -h -d 1 .
