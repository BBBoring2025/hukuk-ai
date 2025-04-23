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
    os.makedirs(ROOT_DIR / "uploads", exist_ok=True)
    os.makedirs(ROOT_DIR / "reports", exist_ok=True)
    
    # API sunucusunu başlat
    print("Sözleşme Analizi API başlatılıyor...")
    app_script = ROOT_DIR / "app.py"
    if app_script.exists():
        os.chdir(ROOT_DIR)
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001", "--reload"])
    else:
        print(f"Hata: {app_script} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
