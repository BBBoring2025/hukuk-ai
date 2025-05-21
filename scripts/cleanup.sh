#!/bin/bash

# Temizlik scripti - 20mayishukukai projesi

echo "Gereksiz dosyaları temizleme başlatılıyor..."

# Node.js modülleri ve build dosyalarını temizle
find . -name "node_modules" -type d -prune -exec rm -rf {} \;
find . -name "build" -type d -prune -exec rm -rf {} \;
find . -name "dist" -type d -prune -exec rm -rf {} \;

# Çeşitli günlük dosyalarını temizle
find . -name "*.log" -type f -delete
find . -path "./logs/*" -type f -delete

# Python derleme dosyalarını temizle
find . -name "__pycache__" -type d -prune -exec rm -rf {} \;
find . -name "*.pyc" -type f -delete
find . -name "*.pyo" -type f -delete
find . -name "*.pyd" -type f -delete

# macOS sistem dosyalarını temizle
find . -name ".DS_Store" -type f -delete
find . -name "._*" -type f -delete

# Eski ve geçici dosyaları temizle
find . -name "*.BAK" -type f -delete
find . -name "*.OLD" -type f -delete
find . -name "*.bak" -type f -delete
find . -name "*.old" -type f -delete
find . -name "*.tmp" -type f -delete
find . -name "*.swp" -type f -delete

# Docker geçici dosyalarını temizle
find . -name "docker-compose.*.yml" ! -name "docker-compose.yml" ! -name "docker-compose.override.yml" -type f -delete

# Git lock dosyalarını temizle
find ./.git -name "*.lock" -type f -delete

echo "Temizlik işlemi tamamlandı."

# Disk kullanımını göster
du -h -d 1 .

