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

app = FastAPI(title="Sözleşme Analizi API", description="Hukuki sözleşme analizi için API")

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
UPLOADS_DIR = BASE_DIR / "sozlesme_analizi" / "uploads"
REPORTS_DIR = BASE_DIR / "sozlesme_analizi" / "reports"

# Dizinleri oluştur
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# Veri modelleri
class AnalysisRequest(BaseModel):
    contract_type: str
    analysis_scope: Optional[str] = "full"
    analysis_depth: Optional[str] = "detailed"

class AnalysisResponse(BaseModel):
    id: str
    created_at: str
    contract_type: str
    risk_level: str
    total_clauses: int
    critical_issues: int
    medium_issues: int
    low_issues: int
    info_notes: int
    clauses: List[Dict[str, Any]]
    legal_compliance: Dict[str, bool]
    summary: str

# API endpoint'leri
@app.get("/")
def read_root():
    return {"message": "Sözleşme Analizi API'ye Hoş Geldiniz"}

@app.post("/analyze-contract", response_model=AnalysisResponse)
async def analyze_contract(
    contract_file: UploadFile = File(...),
    contract_type: str = Form(...),
    analysis_scope: str = Form("full"),
    analysis_depth: str = Form("detailed")
):
    try:
        # Dosyayı kaydet
        file_id = f"contract_{uuid.uuid4().hex}"
        file_path = UPLOADS_DIR / f"{file_id}{os.path.splitext(contract_file.filename)[1]}"
        
        with open(file_path, "wb") as f:
            content = await contract_file.read()
            f.write(content)
        
        # Dosya içeriğini oku
        with open(file_path, "r", errors="ignore") as f:
            contract_text = f.read()
        
        # Mock AI servisi ile analiz et
        analysis_result = mock_ai_service.analyze_contract(contract_text, contract_type)
        
        # Analiz raporunu kaydet
        report_id = analysis_result["id"]
        report_path = REPORTS_DIR / f"{report_id}.json"
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(analysis_result, f, ensure_ascii=False, indent=2)
        
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sözleşme analizi sırasında hata: {str(e)}")

@app.post("/analyze-text", response_model=AnalysisResponse)
async def analyze_text(
    contract_text: str = Form(...),
    contract_type: str = Form(...),
    analysis_scope: str = Form("full"),
    analysis_depth: str = Form("detailed")
):
    try:
        # Mock AI servisi ile analiz et
        analysis_result = mock_ai_service.analyze_contract(contract_text, contract_type)
        
        # Analiz raporunu kaydet
        report_id = analysis_result["id"]
        report_path = REPORTS_DIR / f"{report_id}.json"
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(analysis_result, f, ensure_ascii=False, indent=2)
        
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sözleşme analizi sırasında hata: {str(e)}")

@app.get("/report/{report_id}")
async def get_report(report_id: str):
    report_path = REPORTS_DIR / f"{report_id}.json"
    if not os.path.exists(report_path):
        raise HTTPException(status_code=404, detail=f"Rapor bulunamadı: {report_id}")
    
    with open(report_path, "r", encoding="utf-8") as f:
        report = json.load(f)
    
    return report

@app.get("/download-report/{report_id}")
async def download_report(report_id: str):
    report_path = REPORTS_DIR / f"{report_id}.json"
    if not os.path.exists(report_path):
        raise HTTPException(status_code=404, detail=f"Rapor bulunamadı: {report_id}")
    
    return FileResponse(
        path=report_path,
        filename=f"sozlesme_analiz_raporu_{report_id}.json",
        media_type="application/json"
    )

# Uygulama başlatma
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
# ------------------------------------------------------------------
@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}
# ------------------------------------------------------------------
