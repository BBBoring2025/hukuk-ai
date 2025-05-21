#!/bin/bash

# Git depo boyutunu küçültmek için ek temizlik
echo "Git depo boyutunu küçültmek için ek temizlik başlatılıyor..."

# Çalışma dizinini belirle
cd /Users/ozdenserkansenalp/Desktop/20mayishukukai

# Git packlenmiş dosyaları listele ve boyutlarına göre sırala
echo "Git pack dosyalarının detayları:"
git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10

# En büyük dosyaları bul
echo "En büyük dosyalar tespit ediliyor..."
git rev-list --objects --all | grep $(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print $1}')

# Bu dosyaları git önbelleğinden kaldırmak için blobları sıfırla
echo "DİKKAT: Bu işlem güvenli bir şekilde gereksiz dosyaları git geçmişinden temizler."
echo "      Bu işlem git geçmişini değiştirmez, sadece büyük dosyaları kaldırır."
echo "      İşlemi durdurmak için CTRL+C tuşlarına basın."
read -p "Devam etmek için ENTER tuşuna basın... " 

# Git filtrelemesi
git gc
git prune

# İzlenmeyen tüm dosyaları temizle
git clean -fd

# Git depo veri analizi
echo "Git depo veri analizi:"
git count-objects -v

echo "Git depo boyutu:"
du -sh .git

echo "Git depo temizliği tamamlandı."
