import os
import sys
from pathlib import Path
import subprocess

# Proje kök dizinini ayarla
ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

# Ana çalıştırma fonksiyonu
def main():
    # Gerekli dizinleri oluştur
    os.makedirs(ROOT_DIR / "templates", exist_ok=True)
    os.makedirs(ROOT_DIR / "output", exist_ok=True)
    
    # Örnek şablonları oluştur
    setup_script = ROOT_DIR / "setup.py"
    if setup_script.exists():
        print("Şablonlar oluşturuluyor...")
        subprocess.run([sys.executable, setup_script])
    
    # API sunucusunu başlat (Gunicorn ile)
    print("Dilekçe Üretici API başlatılıyor (Gunicorn ile)...")
    gunicorn_config = ROOT_DIR / "gunicorn_config.py"
    if gunicorn_config.exists():
        os.chdir(ROOT_DIR)
        subprocess.run(["gunicorn", "-c", "gunicorn_config.py", "app:app"])
    else:
        print(f"Hata: {gunicorn_config} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
