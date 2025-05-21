#!/bin/bash

# Bu script crontab'a eklemek için kullanılabilir
# Örnek kullanım: 
# crontab -e 
# ve aşağıdaki satırı ekleyin:
# 0 1 * * * /Users/ozdenserkansenalp/Desktop/20mayishukukai/scripts/auto_cleanup.sh > /Users/ozdenserkansenalp/Desktop/20mayishukukai/logs/cleanup.log 2>&1

cd /Users/ozdenserkansenalp/Desktop/20mayishukukai
./scripts/cleanup.sh

# Git LFS (Large File Storage) optimizasyonu
git gc
git prune

# Git depoyu sıkıştırma
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Node modüllerinin yeniden oluşmasını önlemek için
# Eğer bu bir geliştirme ortamıysa ve frontend'in çalışması gerekiyorsa bu komutu kaldırın
touch frontend/node_modules/.keep

# Disk kullanım raporunu oluştur
echo "Temizlik sonrası disk kullanımı:"
du -h -d 2 . > logs/disk_usage_report.txt
cat logs/disk_usage_report.txt
