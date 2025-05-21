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
    
    # API sunucusunu başlat
    print("Dilekçe Üretici API başlatılıyor...")
    app_script = ROOT_DIR / "app.py"
    if app_script.exists():
        os.chdir(ROOT_DIR)
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    else:
        print(f"Hata: {app_script} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
