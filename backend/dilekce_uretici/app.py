from fastapi import FastAPI, UploadFile, File, Form, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
import os
import sys
import json
import uuid
import shutil
from datetime import datetime
from pathlib import Path

# Mock AI servisi için import
sys.path.append('/home/ubuntu/hukuk_ai_projesi_uygulama/ai_components')
from mock_ai_service_optimized import optimized_mock_ai_service as mock_ai_service

app = FastAPI(title="Dilekçe Üretici API", description="Hukuki dilekçe üretimi için API")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm originlere izin ver (geliştirme için)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dizin yapısı
BASE_DIR = Path("/home/ubuntu/hukuk_ai_projesi_uygulama")
TEMPLATES_DIR = BASE_DIR / "dilekce_uretici" / "templates"
OUTPUT_DIR = BASE_DIR / "output"

# Dizinleri oluştur
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Örnek şablonlar
TEMPLATES = {
    "tuketici": [
        {
            "id": "tuketici_sikayet",
            "name": "Tüketici Şikayet Dilekçesi",
            "description": "Ayıplı mal veya hizmet için tüketici hakem heyetine başvuru",
            "fields": [
                {"name": "ad_soyad", "label": "Adınız Soyadınız", "type": "text", "required": True},
                {"name": "tc_kimlik", "label": "T.C. Kimlik No", "type": "text", "required": True},
                {"name": "adres", "label": "Adresiniz", "type": "textarea", "required": True},
                {"name": "telefon", "label": "Telefon", "type": "text", "required": True},
                {"name": "eposta", "label": "E-posta", "type": "email", "required": False},
                {"name": "muhatap_ad", "label": "Şikayet Edilen Firma/Kişi", "type": "text", "required": True},
                {"name": "muhatap_adres", "label": "Şikayet Edilen Adres", "type": "textarea", "required": True},
                {"name": "urun_hizmet", "label": "Ürün/Hizmet Adı", "type": "text", "required": True},
                {"name": "satin_alma_tarihi", "label": "Satın Alma Tarihi", "type": "date", "required": True},
                {"name": "sikayet_konusu", "label": "Şikayet Konusu", "type": "select", "required": True, 
                 "options": ["Ayıplı Mal", "Ayıplı Hizmet", "Teslim Edilmeyen Ürün", "Cayma Hakkı", "Diğer"]},
                {"name": "sikayet_detay", "label": "Şikayet Detayı", "type": "textarea", "required": True},
                {"name": "talep", "label": "Talebiniz", "type": "checkbox", "required": True, 
                 "options": ["Bedel İadesi", "Yenisi ile Değiştirme", "Ücretsiz Onarım", "Bedel İndirimi"]}
            ]
        },
        {
            "id": "tuketici_iade",
            "name": "Mesafeli Satış Cayma Hakkı Dilekçesi",
            "description": "İnternet üzerinden yapılan alışverişlerde 14 günlük cayma hakkı kullanımı",
            "fields": [
                {"name": "ad_soyad", "label": "Adınız Soyadınız", "type": "text", "required": True},
                {"name": "tc_kimlik", "label": "T.C. Kimlik No", "type": "text", "required": True},
                {"name": "adres", "label": "Adresiniz", "type": "textarea", "required": True},
                {"name": "telefon", "label": "Telefon", "type": "text", "required": True},
                {"name": "eposta", "label": "E-posta", "type": "email", "required": False},
                {"name": "muhatap_ad", "label": "Satıcı Firma Adı", "type": "text", "required": True},
                {"name": "muhatap_adres", "label": "Satıcı Firma Adresi", "type": "textarea", "required": True},
                {"name": "siparis_no", "label": "Sipariş Numarası", "type": "text", "required": True},
                {"name": "siparis_tarihi", "label": "Sipariş Tarihi", "type": "date", "required": True},
                {"name": "teslim_tarihi", "label": "Teslim Tarihi", "type": "date", "required": True},
                {"name": "urun_adi", "label": "Ürün Adı", "type": "text", "required": True},
                {"name": "iade_nedeni", "label": "İade Nedeni", "type": "textarea", "required": False},
                {"name": "iban", "label": "İade için IBAN Numarası", "type": "text", "required": True}
            ]
        }
    ],
    "is": [
        {
            "id": "is_fesih",
            "name": "İş Akdi Fesih Dilekçesi",
            "description": "İş sözleşmesinin işçi tarafından feshi için dilekçe",
            "fields": [
                {"name": "ad_soyad", "label": "Adınız Soyadınız", "type": "text", "required": True},
                {"name": "tc_kimlik", "label": "T.C. Kimlik No", "type": "text", "required": True},
                {"name": "adres", "label": "Adresiniz", "type": "textarea", "required": True},
                {"name": "telefon", "label": "Telefon", "type": "text", "required": True},
                {"name": "eposta", "label": "E-posta", "type": "email", "required": False},
                {"name": "muhatap_ad", "label": "İşveren/Şirket Adı", "type": "text", "required": True},
                {"name": "muhatap_adres", "label": "İşveren/Şirket Adresi", "type": "textarea", "required": True},
                {"name": "ise_baslama_tarihi", "label": "İşe Başlama Tarihi", "type": "date", "required": True},
                {"name": "fesih_tarihi", "label": "Fesih Tarihi", "type": "date", "required": True},
                {"name": "fesih_nedeni", "label": "Fesih Nedeni", "type": "select", "required": True, 
                 "options": ["İstifa", "Emeklilik", "Sağlık Nedenleri", "Haklı Nedenle Fesih", "Diğer"]},
                {"name": "fesih_detay", "label": "Fesih Nedeni Detayı", "type": "textarea", "required": False},
                {"name": "talepler", "label": "Talepleriniz", "type": "checkbox", "required": False, 
                 "options": ["Kıdem Tazminatı", "İhbar Tazminatı", "Yıllık İzin Ücreti", "Fazla Mesai Ücreti", "Diğer Alacaklar"]}
            ]
        },
        {
            "id": "is_mobbing",
            "name": "İşyerinde Psikolojik Taciz (Mobbing) Şikayet Dilekçesi",
            "description": "İşyerinde yaşanan psikolojik taciz (mobbing) için şikayet dilekçesi",
            "fields": [
                {"name": "ad_soyad", "label": "Adınız Soyadınız", "type": "text", "required": True},
                {"name": "tc_kimlik", "label": "T.C. Kimlik No", "type": "text", "required": True},
                {"name": "adres", "label": "Adresiniz", "type": "textarea", "required": True},
                {"name": "telefon", "label": "Telefon", "type": "text", "required": True},
                {"name": "eposta", "label": "E-posta", "type": "email", "required": False},
                {"name": "muhatap_ad", "label": "Şikayet Edilen Kurum", "type": "text", "required": True},
                {"name": "muhatap_adres", "label": "Kurum Adresi", "type": "textarea", "required": True},
                {"name": "gorev", "label": "Göreviniz/Pozisyonunuz", "type": "text", "required": True},
                {"name": "ise_baslama_tarihi", "label": "İşe Başlama Tarihi", "type": "date", "required": True},
                {"name": "mobbing_yapan", "label": "Psikolojik Tacizi Uygulayan Kişi(ler)", "type": "text", "required": True},
                {"name": "mobbing_detay", "label": "Yaşanan Olayların Detayı", "type": "textarea", "required": True},
                {"name": "mobbing_tarihleri", "label": "Olayların Gerçekleştiği Tarihler", "type": "text", "required": True},
                {"name": "taniklar", "label": "Varsa Tanıklar", "type": "textarea", "required": False},
                {"name": "deliller", "label": "Varsa Deliller", "type": "textarea", "required": False}
            ]
        }
    ],
    "kira": [
        {
            "id": "kira_tahliye",
            "name": "Kira Sözleşmesi Fesih ve Tahliye Dilekçesi",
            "description": "Kiracı tarafından kira sözleşmesinin feshi ve tahliye taahhüdü",
            "fields": [
                {"name": "ad_soyad", "label": "Adınız Soyadınız", "type": "text", "required": True},
                {"name": "tc_kimlik", "label": "T.C. Kimlik No", "type": "text", "required": True},
                {"name": "adres", "label": "Adresiniz (Kiralanan)", "type": "textarea", "required": True},
                {"name": "telefon", "label": "Telefon", "type": "text", "required": True},
                {"name": "eposta", "label": "E-posta", "type": "email", "required": False},
                {"name": "muhatap_ad", "label": "Ev Sahibi Adı Soyadı", "type": "text", "required": True},
                {"name": "muhatap_adres", "label": "Ev Sahibi Adresi", "type": "textarea", "required": True},
                {"name": "kira_baslangic", "label": "Kira Sözleşmesi Başlangıç Tarihi", "type": "date", "required": True},
                {"name": "tahliye_tarihi", "label": "Tahliye Tarihi", "type": "date", "required": True},
                {"name": "fesih_nedeni", "label": "Fesih Nedeni", "type": "select", "required": True, 
                 "options": ["Taşınma", "Ekonomik Nedenler", "Mücbir Sebep", "Diğer"]},
                {"name": "fesih_detay", "label": "Fesih Nedeni Detayı", "type": "textarea", "required": False},
                {"name": "depozito_iadesi", "label": "Depozito İadesi Talep Ediliyor mu?", "type": "radio", "required": True, 
                 "options": ["Evet", "Hayır"]}
            ]
        }
    ]
}

# Veri modelleri
class UserData(BaseModel):
    ad_soyad: str
    tc_kimlik: str
    adres: str
    telefon: str
    eposta: Optional[str] = None

class RecipientData(BaseModel):
    muhatap_ad: str
    muhatap_adres: str

class PetitionRequest(BaseModel):
    template_id: str
    user_data: Dict[str, Any]
    recipient_data: Dict[str, Any]
    content_data: Dict[str, Any]

class PetitionResponse(BaseModel):
    id: str
    file_path: str
    created_at: str
    template_id: str
    template_name: str

# API endpoint'leri
@app.get("/")
def read_root():
    return {"message": "Dilekçe Üretici API'ye Hoş Geldiniz"}

@app.get("/templates/{category_id}")
def get_templates(category_id: str):
    if category_id not in TEMPLATES:
        raise HTTPException(status_code=404, detail=f"Kategori bulunamadı: {category_id}")
    return TEMPLATES[category_id]

@app.post("/generate-petition", response_model=PetitionResponse)
async def generate_petition(petition_request: PetitionRequest):
    try:
        # Mock AI servisi ile dilekçe oluştur
        result = mock_ai_service.generate_petition(
            petition_request.template_id,
            petition_request.user_data,
            petition_request.recipient_data,
            petition_request.content_data
        )
        
        # Örnek bir PDF dosyası oluştur (gerçek uygulamada burada dilekçe oluşturulur)
        petition_id = result["id"]
        file_path = f"{OUTPUT_DIR}/{petition_id}.pdf"
        
        # Örnek PDF oluştur (gerçek uygulamada burada docx şablonu doldurulur ve PDF'e dönüştürülür)
        # Bu örnekte sadece boş bir dosya oluşturuyoruz
        with open(file_path, "w") as f:
            f.write(f"Bu bir örnek dilekçedir. ID: {petition_id}\n")
            f.write(f"Şablon: {petition_request.template_id}\n")
            f.write(f"Kullanıcı: {petition_request.user_data.get('ad_soyad', 'Belirtilmemiş')}\n")
            f.write(f"Muhatap: {petition_request.recipient_data.get('muhatap_ad', 'Belirtilmemiş')}\n")
            f.write(f"Oluşturulma Tarihi: {datetime.now().isoformat()}\n")
            f.write("\n--- İçerik ---\n")
            for key, value in petition_request.content_data.items():
                f.write(f"{key}: {value}\n")
        
        # Yanıt oluştur
        template_name = "Bilinmeyen Şablon"
        for category in TEMPLATES.values():
            for template in category:
                if template["id"] == petition_request.template_id:
                    template_name = template["name"]
                    break
        
        return {
            "id": petition_id,
            "file_path": file_path,
            "created_at": datetime.now().isoformat(),
            "template_id": petition_request.template_id,
            "template_name": template_name
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dilekçe oluşturulurken hata: {str(e)}")

@app.get("/download/{petition_id}")
async def download_petition(petition_id: str):
    file_path = f"{OUTPUT_DIR}/{petition_id}.pdf"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Dilekçe bulunamadı: {petition_id}")
    
    return FileResponse(
        path=file_path,
        filename=f"dilekce_{petition_id}.pdf",
        media_type="application/pdf"
    )

# Uygulama başlatma
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
