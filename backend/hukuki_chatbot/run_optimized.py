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
    os.makedirs(ROOT_DIR / "sessions", exist_ok=True)
    os.makedirs(ROOT_DIR / "knowledge", exist_ok=True)
    
    # API sunucusunu başlat (Gunicorn ile)
    print("Hukuki Chatbot API başlatılıyor (Gunicorn ile)...")
    gunicorn_config = ROOT_DIR / "gunicorn_config.py"
    if gunicorn_config.exists():
        os.chdir(ROOT_DIR)
        subprocess.run(["gunicorn", "-c", "gunicorn_config.py", "app:app"])
    else:
        print(f"Hata: {gunicorn_config} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
