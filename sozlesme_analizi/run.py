import os
import sys
from pathlib import Path
import subprocess
import pkg_resources

# Gerekli paketleri kontrol et ve kur
required_packages = [
    'fastapi==0.104.1',
    'uvicorn==0.23.2',
    'python-multipart==0.0.6',
    'pydantic==2.4.2',
    'nltk==3.8.1',
    'PyPDF2==3.0.1',
    'python-docx==0.8.11',
    'spacy==3.7.2',
    'scikit-learn==1.3.2',
    'numpy==1.26.0'
]

def install_packages():
    """Gerekli paketleri kur"""
    print("Gerekli paketler kontrol ediliyor ve kuruluyor...")
    
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = []
    
    for package in required_packages:
        package_name = package.split('==')[0]
        if package_name.lower() not in installed:
            missing.append(package)
    
    if missing:
        print(f"Kurulacak paketler: {missing}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
        print("Paketler başarıyla kuruldu.")
    else:
        print("Tüm gerekli paketler zaten kurulu.")

    # NLTK verilerini indir
    try:
        import nltk
        nltk.download('punkt')
        print("NLTK verileri başarıyla indirildi.")
    except Exception as e:
        print(f"NLTK verileri indirilirken hata oluştu: {str(e)}")

    # spaCy modelini indir
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "tr_core_news_sm"])
        print("spaCy Türkçe modeli başarıyla indirildi.")
    except Exception as e:
        print(f"spaCy modeli indirilirken hata oluştu: {str(e)}")

# Ana çalıştırma fonksiyonu
def main():
    # Proje kök dizinini ayarla
    root_dir = Path(__file__).resolve().parent
    
    # Gerekli paketleri kur
    install_packages()
    
    # Gerekli dizinleri oluştur
    os.makedirs(root_dir / "uploads", exist_ok=True)
    os.makedirs(root_dir / "analysis", exist_ok=True)
    os.makedirs(root_dir / "static", exist_ok=True)
    
    # API sunucusunu başlat
    print("Sözleşme Analizi API başlatılıyor...")
    app_script = root_dir / "app.py"
    if app_script.exists():
        os.chdir(root_dir)
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001", "--reload"])
    else:
        print(f"Hata: {app_script} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
