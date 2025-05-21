#!/bin/bash

# Watchdog script - dosya patlamasını önlemek için devamlı izleme
# Bu script arkaplanda çalışarak dosya sistemini izler ve gereksiz dosyaları otomatik temizler
# Kullanım: ./scripts/watchdog.sh &

PROJECT_DIR="/Users/ozdenserkansenalp/Desktop/20mayishukukai"
LOG_FILE="$PROJECT_DIR/logs/watchdog.log"
CHECK_INTERVAL=3600  # Saniye cinsinden kontrol aralığı (1 saat)
MAX_SIZE_MB=1000     # Klasörün MB cinsinden maksimum boyutu

# Log dizini oluştur
mkdir -p "$PROJECT_DIR/logs"

echo "Watchdog başlatıldı - $(date)" > "$LOG_FILE"

cleanup_if_needed() {
    # Mevcut klasör boyutunu hesapla
    current_size=$(du -sm "$PROJECT_DIR" | awk '{print $1}')
    
    echo "$(date) - Mevcut boyut: ${current_size}MB (Maksimum: ${MAX_SIZE_MB}MB)" >> "$LOG_FILE"
    
    # Eğer boyut limiti aşılmışsa temizlik yap
    if [ "$current_size" -gt "$MAX_SIZE_MB" ]; then
        echo "$(date) - Boyut limiti aşıldı! Temizlik yapılıyor..." >> "$LOG_FILE"
        "$PROJECT_DIR/scripts/deep_clean.sh" >> "$LOG_FILE" 2>&1
        
        # Temizlik sonrası yeni boyut
        new_size=$(du -sm "$PROJECT_DIR" | awk '{print $1}')
        echo "$(date) - Temizlik sonrası yeni boyut: ${new_size}MB" >> "$LOG_FILE"
        
        # Eğer hala limit aşılmışsa git temizliği de yap
        if [ "$new_size" -gt "$MAX_SIZE_MB" ]; then
            echo "$(date) - Hala boyut limiti aşılıyor! Git temizliği yapılıyor..." >> "$LOG_FILE"
            "$PROJECT_DIR/scripts/git_deep_clean.sh" >> "$LOG_FILE" 2>&1
            
            # Git temizliği sonrası yeni boyut
            final_size=$(du -sm "$PROJECT_DIR" | awk '{print $1}')
            echo "$(date) - Git temizliği sonrası yeni boyut: ${final_size}MB" >> "$LOG_FILE"
        fi
    fi
    
    # Gereksiz dosyaları hemen temizle
    find "$PROJECT_DIR" -name ".DS_Store" -type f -delete
    find "$PROJECT_DIR" -name "*.tmp" -type f -delete
    find "$PROJECT_DIR" -name "*.swp" -type f -delete
    find "$PROJECT_DIR" -name "*~" -type f -delete
}

# Ana döngü
echo "Watchdog izleme başladı..." >> "$LOG_FILE"
while true; do
    cleanup_if_needed
    sleep $CHECK_INTERVAL
done
