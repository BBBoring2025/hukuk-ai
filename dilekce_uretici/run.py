import os
import sys
from pathlib import Path
import subprocess
import pkg_resources

# Gerekli paketleri kontrol et ve kur
required_packages = [
    'fastapi==0.104.1',
    'uvicorn==0.23.2',
    'python-docx==0.8.11',
    'docxtpl==0.16.7',
    'docx2pdf==0.1.8',
    'python-multipart==0.0.6',
    'pydantic==2.4.2',
    'jinja2==3.1.2'
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

# Ana çalıştırma fonksiyonu
def main():
    # Proje kök dizinini ayarla
    root_dir = Path(__file__).resolve().parent
    
    # Gerekli paketleri kur
    install_packages()
    
    # Gerekli dizinleri oluştur
    os.makedirs(root_dir / "templates", exist_ok=True)
    os.makedirs(root_dir / "output", exist_ok=True)
    os.makedirs(root_dir / "static", exist_ok=True)
    
    # Şablon dosyalarını oluştur
    print("Şablon dosyaları oluşturuluyor...")
    setup_script = root_dir / "setup.py"
    if setup_script.exists():
        subprocess.run([sys.executable, str(setup_script)])
    
    # API sunucusunu başlat
    print("Dilekçe Üretici API başlatılıyor...")
    app_script = root_dir / "app.py"
    if app_script.exists():
        os.chdir(root_dir)
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    else:
        print(f"Hata: {app_script} dosyası bulunamadı!")

if __name__ == "__main__":
    main()
