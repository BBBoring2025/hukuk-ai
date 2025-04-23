from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Depends, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import json
import shutil
import uuid
import datetime
import tempfile
import uvicorn
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import PyPDF2
from docx import Document
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# NLTK ve spaCy modellerini indir
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Modelleri tanımla
class ContractAnalysisRequest(BaseModel):
    contract_type: str
    analysis_scope: List[str]
    analysis_depth: str
    additional_info: Optional[Dict[str, Any]] = None

class ContractClause(BaseModel):
    id: str
    clause_number: str
    title: Optional[str] = None
    content: str
    risk_level: str  # "critical", "medium", "low", "info"
    issues: List[Dict[str, str]]
    suggestions: List[str]

class ContractAnalysisResponse(BaseModel):
    id: str
    created_at: str
    contract_type: str
    risk_level: str  # 0-100 risk score
    total_clauses: int
    critical_issues: int
    medium_issues: int
    low_issues: int
    info_notes: int
    clauses: List[ContractClause]
    legal_compliance: Dict[str, bool]
    summary: str

# Uygulama oluştur
app = FastAPI(title="Türkiye Hukuk AI Platformu - Sözleşme Analizi API")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gerçek uygulamada belirli domainlere izin verilmeli
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Statik dosyalar için klasör
os.makedirs("static", exist_ok=True)
os.makedirs("uploads", exist_ok=True)
os.makedirs("analysis", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Örnek sözleşme şablonları ve kurallar
contract_rules = {
    "kira": {
        "required_clauses": [
            "taraflar", "kira konusu", "kira süresi", "kira bedeli", "ödeme şekli", 
            "depozito", "tahliye", "fesih", "tebligat", "uyuşmazlık çözümü"
        ],
        "risk_patterns": [
            {"pattern": r"süresiz", "risk": "critical", "message": "Kira süresi belirtilmemiş veya süresiz olarak tanımlanmış"},
            {"pattern": r"sözlü", "risk": "critical", "message": "Sözlü anlaşmaya atıf yapılmış, yazılı olarak netleştirilmeli"},
            {"pattern": r"(artış|zam)(.{0,30})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Kira artış oranı belirtilmemiş"},
            {"pattern": r"(depozito|teminat)(.{0,30})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Depozito miktarı belirtilmemiş"},
            {"pattern": r"(tahliye|boşaltma)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Tahliye koşulları belirtilmemiş"},
            {"pattern": r"(onarım|tamirat)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "low", "message": "Onarım ve tamirat sorumluluğu belirtilmemiş"}
        ],
        "legal_references": {
            "6098 Sayılı Borçlar Kanunu": ["kira sözleşmesi", "tahliye", "fesih"],
            "6570 Sayılı Gayrimenkul Kiraları Hakkında Kanun": ["kira artışı", "tahliye"],
            "634 Sayılı Kat Mülkiyeti Kanunu": ["ortak alanlar", "aidat"]
        }
    },
    "is": {
        "required_clauses": [
            "taraflar", "iş tanımı", "çalışma süresi", "ücret", "sosyal haklar", 
            "izin", "fesih", "gizlilik", "rekabet yasağı", "uyuşmazlık çözümü"
        ],
        "risk_patterns": [
            {"pattern": r"(deneme süresi)(.{0,30})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Deneme süresi belirtilmemiş"},
            {"pattern": r"(fazla mesai|fazla çalışma)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Fazla mesai ücreti belirtilmemiş"},
            {"pattern": r"(fesih|ihbar)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Fesih koşulları belirtilmemiş"},
            {"pattern": r"(izin|tatil)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "İzin süreleri belirtilmemiş"},
            {"pattern": r"(gizlilik|sır saklama)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "low", "message": "Gizlilik hükümleri belirtilmemiş"},
            {"pattern": r"(rekabet yasağı)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "low", "message": "Rekabet yasağı hükümleri belirtilmemiş"}
        ],
        "legal_references": {
            "4857 Sayılı İş Kanunu": ["iş sözleşmesi", "fesih", "kıdem tazminatı"],
            "6098 Sayılı Borçlar Kanunu": ["hizmet sözleşmesi", "rekabet yasağı"],
            "6331 Sayılı İş Sağlığı ve Güvenliği Kanunu": ["iş güvenliği", "sağlık"]
        }
    },
    "satis": {
        "required_clauses": [
            "taraflar", "satış konusu", "bedel", "ödeme şekli", "teslim", 
            "ayıp", "garanti", "mülkiyet devri", "fesih", "uyuşmazlık çözümü"
        ],
        "risk_patterns": [
            {"pattern": r"(teslim|teslimat)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Teslim koşulları belirtilmemiş"},
            {"pattern": r"(ayıp|kusur|hata)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Ayıplı mal durumunda sorumluluk belirtilmemiş"},
            {"pattern": r"(garanti|teminat)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Garanti koşulları belirtilmemiş"},
            {"pattern": r"(ödeme|bedel)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Ödeme koşulları belirtilmemiş"},
            {"pattern": r"(fesih|iptal)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Fesih koşulları belirtilmemiş"},
            {"pattern": r"(mülkiyet|sahiplik)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Mülkiyet devri koşulları belirtilmemiş"}
        ],
        "legal_references": {
            "6098 Sayılı Borçlar Kanunu": ["satış sözleşmesi", "ayıp", "teslim"],
            "6502 Sayılı Tüketicinin Korunması Hakkında Kanun": ["tüketici", "ayıplı mal", "garanti"],
            "6102 Sayılı Türk Ticaret Kanunu": ["ticari satış", "taşıma"]
        }
    },
    "hizmet": {
        "required_clauses": [
            "taraflar", "hizmet konusu", "süre", "bedel", "ödeme şekli", 
            "yükümlülükler", "gizlilik", "fikri mülkiyet", "fesih", "uyuşmazlık çözümü"
        ],
        "risk_patterns": [
            {"pattern": r"(hizmet kapsamı|iş tanımı)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Hizmet kapsamı net olarak belirtilmemiş"},
            {"pattern": r"(süre|zaman)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Hizmet süresi belirtilmemiş"},
            {"pattern": r"(ödeme|bedel)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "critical", "message": "Ödeme koşulları belirtilmemiş"},
            {"pattern": r"(gizlilik|sır saklama)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Gizlilik hükümleri belirtilmemiş"},
            {"pattern": r"(fikri mülkiyet|telif)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Fikri mülkiyet hakları belirtilmemiş"},
            {"pattern": r"(fesih|iptal)(.{0,50})(belirtilmemiştir|yoktur)", "risk": "medium", "message": "Fesih koşulları belirtilmemiş"}
        ],
        "legal_references": {
            "6098 Sayılı Borçlar Kanunu": ["hizmet sözleşmesi", "vekalet"],
            "6102 Sayılı Türk Ticaret Kanunu": ["ticari hizmet", "acentelik"],
            "5846 Sayılı Fikir ve Sanat Eserleri Kanunu": ["telif", "fikri mülkiyet"]
        }
    }
}

# Sözleşme analiz fonksiyonları
def extract_text_from_file(file_path):
    """Dosyadan metin çıkar"""
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == '.pdf':
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    elif file_ext == '.docx':
        doc = Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    
    elif file_ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    else:
        raise ValueError(f"Desteklenmeyen dosya formatı: {file_ext}")

def identify_contract_type(text):
    """Sözleşme türünü belirle"""
    # Basit anahtar kelime tabanlı sınıflandırma
    keywords = {
        "kira": ["kira", "kiralanan", "gayrimenkul", "taşınmaz", "konut", "işyeri", "kiracı", "kiraya veren"],
        "is": ["iş sözleşmesi", "hizmet akdi", "işçi", "işveren", "çalışma", "ücret", "maaş", "izin", "fazla mesai"],
        "satis": ["satış", "alım", "satım", "mal", "ürün", "satıcı", "alıcı", "bedel", "teslim", "mülkiyet"],
        "hizmet": ["hizmet", "danışmanlık", "bakım", "onarım", "destek", "servis", "proje", "iş", "eser"]
    }
    
    scores = {}
    for contract_type, words in keywords.items():
        score = 0
        for word in words:
            score += text.lower().count(word.lower()) * 10  # Her kelime için 10 puan
        scores[contract_type] = score
    
    # En yüksek skora sahip sözleşme türünü döndür
    return max(scores.items(), key=lambda x: x[1])[0]

def extract_clauses(text):
    """Sözleşme maddelerini çıkar"""
    # Madde başlıklarını bul
    clause_patterns = [
        r'(?:MADDE|Madde)\s+(\d+)[:\s-]+(.+?)(?=(?:MADDE|Madde)\s+\d+|$)',  # MADDE 1: Başlık
        r'(?:Madde|MADDE)\s+(\d+)[:\s-]+',  # Madde 1: (başlıksız)
        r'(\d+)[:\s-]+(.+?)(?=\d+[:\s-]+|$)'  # 1: Başlık
    ]
    
    clauses = []
    remaining_text = text
    
    for pattern in clause_patterns:
        matches = re.finditer(pattern, text, re.DOTALL)
        for match in matches:
            if len(match.groups()) >= 2:
                clause_number = match.group(1)
                title = match.group(2).strip()
                content = match.group(0)
            else:
                clause_number = match.group(1)
                title = None
                content = match.group(0)
            
            clauses.append({
                "id": str(uuid.uuid4()),
                "clause_number": clause_number,
                "title": title,
                "content": content,
                "risk_level": "info",
                "issues": [],
                "suggestions": []
            })
            
            # Eşleşen metni kaldır
            remaining_text = remaining_text.replace(match.group(0), "", 1)
    
    # Eğer hiç madde bulunamadıysa, metni paragraflar halinde böl
    if not clauses and remaining_text.strip():
        paragraphs = re.split(r'\n\s*\n', remaining_text)
        for i, para in enumerate(paragraphs):
            if para.strip():
                clauses.append({
                    "id": str(uuid.uuid4()),
                    "clause_number": str(i+1),
                    "title": None,
                    "content": para.strip(),
                    "risk_level": "info",
                    "issues": [],
                    "suggestions": []
                })
    
    return clauses

def analyze_contract(contract_type, text, clauses, analysis_scope, analysis_depth):
    """Sözleşmeyi analiz et"""
    # Sözleşme türüne göre kuralları al
    rules = contract_rules.get(contract_type, contract_rules["kira"])  # Varsayılan olarak kira kurallarını kullan
    
    # Gerekli maddeleri kontrol et
    required_clauses = rules["required_clauses"]
    missing_clauses = []
    
    # Mevcut maddeleri kontrol et
    found_clauses = set()
    for clause in clauses:
        for req_clause in required_clauses:
            if clause["title"] and req_clause.lower() in clause["title"].lower():
                found_clauses.add(req_clause)
                break
            elif req_clause.lower() in clause["content"].lower():
                found_clauses.add(req_clause)
                break
    
    # Eksik maddeleri bul
    for req_clause in required_clauses:
        if req_clause not in found_clauses:
            missing_clauses.append(req_clause)
    
    # Her madde için risk analizi yap
    total_risk_score = 0
    critical_issues = 0
    medium_issues = 0
    low_issues = 0
    info_notes = 0
    
    for clause in clauses:
        clause_risks = []
        clause_suggestions = []
        highest_risk = "info"
        
        # Eksik madde kontrolü
        for missing in missing_clauses:
            if missing.lower() in clause["content"].lower():
                clause_risks.append({
                    "type": "missing_clause",
                    "message": f"'{missing}' maddesi eksik veya yeterince detaylı değil"
                })
                clause_suggestions.append(f"'{missing}' maddesini ekleyin veya detaylandırın")
                highest_risk = "critical"
                critical_issues += 1
        
        # Risk kalıplarını kontrol et
        for risk_pattern in rules["risk_patterns"]:
            if re.search(risk_pattern["pattern"], clause["content"], re.IGNORECASE):
                clause_risks.append({
                    "type": "risk_pattern",
                    "message": risk_pattern["message"]
                })
                
                # Risk seviyesine göre öneri ekle
                if risk_pattern["risk"] == "critical":
                    suggestion = f"{risk_pattern['message']}. Bu maddeyi acilen düzeltmeniz önerilir."
                    critical_issues += 1
                elif risk_pattern["risk"] == "medium":
                    suggestion = f"{risk_pattern['message']}. Bu maddeyi gözden geçirmeniz önerilir."
                    medium_issues += 1
                else:
                    suggestion = f"{risk_pattern['message']}. Bu maddeyi iyileştirmeniz önerilir."
                    low_issues += 1
                
                clause_suggestions.append(suggestion)
                
                # En yüksek risk seviyesini belirle
                if risk_pattern["risk"] == "critical" and highest_risk != "critical":
                    highest_risk = "critical"
                elif risk_pattern["risk"] == "medium" and highest_risk not in ["critical"]:
                    highest_risk = "medium"
                elif risk_pattern["risk"] == "low" and highest_risk not in ["critical", "medium"]:
                    highest_risk = "low"
        
        # Madde risk seviyesini güncelle
        clause["risk_level"] = highest_risk
        clause["issues"] = clause_risks
        clause["suggestions"] = clause_suggestions
        
        # Risk puanını hesapla
        if highest_risk == "critical":
            total_risk_score += 30
        elif highest_risk == "medium":
            total_risk_score += 15
        elif highest_risk == "low":
            total_risk_score += 5
        else:
            info_notes += 1
    
    # Toplam risk puanını normalize et (0-100 arası)
    max_possible_score = len(clauses) * 30
    if max_possible_score > 0:
        normalized_risk_score = min(100, int((total_risk_score / max_possible_score) * 100))
    else:
        normalized_risk_score = 0
    
    # Yasal uyumluluk kontrolü
    legal_compliance = {}
    for law, keywords in rules["legal_references"].items():
        compliant = True
        for keyword in keywords:
            if keyword.lower() not in text.lower():
                compliant = False
                break
        legal_compliance[law] = compliant
    
    # Özet oluştur
    summary = f"Bu {contract_type} sözleşmesi analiz edilmiş olup, toplam risk skoru {normalized_risk_score}/100'dür. "
    summary += f"Sözleşmede {critical_issues} kritik, {medium_issues} orta ve {low_issues} düşük seviyeli risk tespit edilmiştir. "
    
    if missing_clauses:
        summary += f"Eksik maddeler: {', '.join(missing_clauses)}. "
    
    if normalized_risk_score >= 70:
        summary += "Bu sözleşme yüksek risk taşımaktadır ve kullanılmadan önce hukuki danışmanlık almanız önerilir."
    elif normalized_risk_score >= 40:
        summary += "Bu sözleşme orta seviyede risk taşımaktadır ve önerilen düzeltmelerin yapılması tavsiye edilir."
    else:
        summary += "Bu sözleşme düşük risk taşımaktadır, ancak önerilen iyileştirmeleri değerlendirmeniz faydalı olacaktır."
    
    return {
        "risk_level": str(normalized_risk_score),
        "total_clauses": len(clauses),
        "critical_issues": critical_issues,
        "medium_issues": medium_issues,
        "low_issues": low_issues,
        "info_notes": info_notes,
        "clauses": clauses,
        "legal_compliance": legal_compliance,
        "summary": summary
    }

# API Endpoint'leri
@app.get("/")
async def root():
    return {"message": "Türkiye Hukuk AI Platformu - Sözleşme Analizi API"}

@app.post("/upload", response_model=Dict[str, str])
async def upload_contract(file: UploadFile = File(...)):
    """Sözleşme dosyasını yükle"""
    # Dosya uzantısını kontrol et
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ['.pdf', '.docx', '.txt', '.md']:
        raise HTTPException(status_code=400, detail="Desteklenmeyen dosya formatı. Lütfen PDF, DOCX, TXT veya MD dosyası yükleyin.")
    
    # Dosyayı kaydet
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}{file_ext}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"file_id": file_id, "file_path": file_path}

@app.post("/analyze/{file_id}", response_model=ContractAnalysisResponse)
async def analyze_contract_file(
    file_id: str, 
    request: ContractAnalysisRequest
):
    """Sözleşmeyi analiz et"""
    # Dosyayı bul
    file_path = None
    for ext in ['.pdf', '.docx', '.txt', '.md']:
        temp_path = f"uploads/{file_id}{ext}"
        if os.path.exists(temp_path):
            file_path = temp_path
            break
    
    if not file_path:
        raise HTTPException(status_code=404, detail="Dosya bulunamadı")
    
    try:
        # Dosyadan metin çıkar
        text = extract_text_from_file(file_path)
        
        # Sözleşme türünü belirle (eğer belirtilmemişse)
        contract_type = request.contract_type
        if not contract_type or contract_type == "auto":
            contract_type = identify_contract_type(text)
        
        # Maddeleri çıkar
        clauses = extract_clauses(text)
        
        # Sözleşmeyi analiz et
        analysis_result = analyze_contract(
            contract_type, 
            text, 
            clauses, 
            request.analysis_scope, 
            request.analysis_depth
        )
        
        # Analiz sonucunu oluştur
        response = ContractAnalysisResponse(
            id=file_id,
            created_at=datetime.datetime.now().isoformat(),
            contract_type=contract_type,
            **analysis_result
        )
        
        # Analiz sonucunu kaydet
        with open(f"analysis/{file_id}.json", "w", encoding="utf-8") as f:
            f.write(response.model_dump_json(indent=2))
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analiz sırasında hata oluştu: {str(e)}")

@app.get("/analysis/{analysis_id}", response_model=ContractAnalysisResponse)
async def get_analysis(analysis_id: str):
    """Analiz sonucunu getir"""
    file_path = f"analysis/{analysis_id}.json"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Analiz sonucu bulunamadı")
    
    with open(file_path, "r", encoding="utf-8") as f:
        analysis = json.load(f)
    
    return analysis

@app.get("/contract-types")
async def get_contract_types():
    """Desteklenen sözleşme türlerini listele"""
    return list(contract_rules.keys())

@app.get("/suggestions/{contract_type}/{clause_type}")
async def get_suggestions(contract_type: str, clause_type: str):
    """Belirli bir sözleşme türü ve madde için öneriler getir"""
    if contract_type not in contract_rules:
        raise HTTPException(status_code=404, detail="Sözleşme türü bulunamadı")
    
    rules = contract_rules[contract_type]
    
    if clause_type not in rules["required_clauses"]:
        raise HTTPException(status_code=404, detail="Madde türü bulunamadı")
    
    # Örnek öneriler (gerçek uygulamada daha kapsamlı olmalı)
    suggestions = {
        "taraflar": "Tarafların tam adı, adresi, TC kimlik/vergi numarası gibi bilgileri eksiksiz belirtilmelidir.",
        "kira konusu": "Kiralanan gayrimenkulün açık adresi, tapu bilgileri ve özellikleri detaylı olarak belirtilmelidir.",
        "kira süresi": "Kira başlangıç ve bitiş tarihleri net olarak belirtilmelidir.",
        "kira bedeli": "Kira bedeli rakam ve yazı ile belirtilmeli, ödeme para birimi açıkça yazılmalıdır.",
        "ödeme şekli": "Ödeme tarihi, yöntemi ve gecikme durumunda uygulanacak faiz oranı belirtilmelidir.",
        "depozito": "Depozito miktarı, iade koşulları ve zamanı belirtilmelidir.",
        "tahliye": "Tahliye koşulları ve prosedürü detaylı olarak belirtilmelidir.",
        "fesih": "Sözleşmenin fesih koşulları ve bildirim süreleri belirtilmelidir.",
        "tebligat": "Tarafların tebligat adresleri ve adres değişikliği bildirimi zorunluluğu belirtilmelidir.",
        "uyuşmazlık çözümü": "Uyuşmazlık durumunda başvurulacak mahkeme veya tahkim yolu belirtilmelidir."
    }
    
    return {"clause_type": clause_type, "suggestion": suggestions.get(clause_type, "Öneri bulunamadı")}

# Ana uygulama
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
