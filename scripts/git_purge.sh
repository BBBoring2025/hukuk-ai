#!/bin/bash

# Git depo boyutunu küçültme scripti - DİKKAT: Bu script git geçmişini değiştirir!
# Kullanmadan önce mutlaka bir yedek alın.

echo "DİKKAT: Bu script git depo geçmişini kalıcı olarak değiştirir!"
echo "Devam etmek için ENTER tuşuna basın veya CTRL+C ile iptal edin..."
read

# Çalışma dizinini belirle
cd /Users/ozdenserkansenalp/Desktop/20mayishukukai

# 1. Önce tüm dosyaları stage'e ekleyelim ki şu anki durum korunsun
git add -A
git commit -m "Temizlik öncesi son durum" || true

# 2. Git reflog'u temizle
echo "Git reflog temizleniyor..."
git reflog expire --expire=now --all

# 3. Git depoyu sıkıştır
echo "Git depo sıkıştırılıyor..."
git gc --prune=now --aggressive

# 4. Orphaned commit'leri ve kullanılmayan objeleri temizle
echo "Orphaned commitler temizleniyor..."
git repack -a -d -f
git prune

# 5. Git geçmişini sıfırla - DİKKAT: Bu adım mevcut geçmişi siler!
echo "Git geçmişi sıfırlanıyor..."
git checkout --orphan temp_branch
git add -A
git commit -m "İlk commit - Temizlenmiş depo"
git branch -D main || true
git branch -m main
git push -f origin main || true

echo "Git depo temizliği tamamlandı."
echo "Yeni depo boyutu:"
du -sh .git
