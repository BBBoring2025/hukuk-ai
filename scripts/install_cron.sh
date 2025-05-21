#!/bin/bash

# Bu script, gerekli crontab girişini ekler
# Crontab formatı: dakika saat gün ay haftanın_günü komut

# Mevcut crontab'ı kontrol et
crontab -l > /tmp/current_crontab 2>/dev/null || echo "" > /tmp/current_crontab

# Temizlik görevimiz zaten eklenmiş mi?
if grep -q "20mayishukukai/scripts/deep_clean.sh" /tmp/current_crontab; then
  echo "Temizlik görevi zaten crontab'da mevcut."
else
  # Crontab'a ekle - Her gece saat 2'de çalışacak şekilde
  echo "# Her gece saat 2'de 20mayishukukai klasörünü temizle" >> /tmp/current_crontab
  echo "0 2 * * * /Users/ozdenserkansenalp/Desktop/20mayishukukai/scripts/deep_clean.sh > /Users/ozdenserkansenalp/Desktop/20mayishukukai/logs/cleanup.log 2>&1" >> /tmp/current_crontab
  
  # Yeni crontab'ı yükle
  crontab /tmp/current_crontab
  echo "Temizlik görevi crontab'a eklendi."
fi

# Geçici dosyaları temizle
rm -f /tmp/current_crontab

echo "Kurulum tamamlandı. Her gece saat 2'de otomatik temizlik yapılacak."
