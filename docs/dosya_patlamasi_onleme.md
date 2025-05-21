# 20Mayis Hukuk AI Projesi - Dosya Patlaması Önleme Kılavuzu

Bu dokümanda, projede yaşanan dosya patlaması sorununu önlemek için izlenmesi gereken pratikler belirtilmiştir.

## Genel Kurallar

1. **Node Modülleri**: 
   - `node_modules` klasörleri çok büyük olabilir ve projenin boyutunu gereksiz şekilde artırır.
   - Yerel geliştirme sırasında `npm ci` veya `yarn install --frozen-lockfile` komutlarını kullanın.
   - Docker kullanıyorsanız, multi-stage build ile modülleri ayırın.

2. **Build Klasörleri**:
   - `build` ve `dist` klasörleri .gitignore'a eklenmiştir ve bunları repositorye eklemeyin.
   - CI/CD süreçleri için build işlemlerini build sunucularında yapın.

3. **Günlük Dosyaları**:
   - Günlük (log) dosyaları sınırlı boyutta tutulmalıdır.
   - Logrotate veya benzer bir çözüm kullanarak günlükleri düzenli olarak arşivleyin ve eskilerini silin.

4. **Git LFS Kullanımı**:
   - Büyük dosyalar için Git LFS (Large File Storage) kullanın.
   - ML modelleri, büyük veri setleri vb. için LFS kullanılması önerilir.

5. **Docker Temizliği**:
   - Kullanılmayan docker imajlarını ve container'ları düzenli olarak temizleyin.
   - `docker system prune` komutu ile düzenli temizlik yapın.

## Otomatik Temizlik

Projede oluşturduğumuz scriptler ile düzenli temizlik yapılabilir:

1. **Manuel Temizlik**: 
   ```bash
   ./scripts/cleanup.sh
   ```

2. **Otomatik Temizlik (Cron)**:
   - Crontab'a şu satırı ekleyin:
   ```
   0 1 * * * /Users/ozdenserkansenalp/Desktop/20mayishukukai/scripts/auto_cleanup.sh > /Users/ozdenserkansenalp/Desktop/20mayishukukai/logs/cleanup.log 2>&1
   ```
   - Bu ayar her gece saat 01:00'de otomatik temizlik yapar.

## Kaynakların İzlenmesi

Düzenli olarak disk kullanımını izleyin:

```bash
du -h -d 2 /Users/ozdenserkansenalp/Desktop/20mayishukukai
```

## Destek

Sorun yaşandığında temizlik scriptlerini çalıştırmayı deneyin. Eğer sorun devam ederse, yazılım ekibine bildirin.
