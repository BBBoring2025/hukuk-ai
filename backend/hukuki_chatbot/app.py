from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
import os
import sys
import json
import uuid
from datetime import datetime
from pathlib import Path

# Mock AI servisi için import
sys.path.append('/home/ubuntu/hukuk_ai_projesi_uygulama/ai_components')
from mock_ai_service_optimized import optimized_mock_ai_service as mock_ai_service

app = FastAPI(title="Hukuki Chatbot API", description="Hukuki sorulara yanıt veren chatbot API")

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
SESSIONS_DIR = BASE_DIR / "hukuki_chatbot" / "sessions"
KNOWLEDGE_DIR = BASE_DIR / "hukuki_chatbot" / "knowledge"

# Dizinleri oluştur
os.makedirs(SESSIONS_DIR, exist_ok=True)
os.makedirs(KNOWLEDGE_DIR, exist_ok=True)

# Aktif WebSocket bağlantıları
active_connections: Dict[str, WebSocket] = {}

# Veri modelleri
class ChatRequest(BaseModel):
    query: str
    session_id: str

class ChatResponse(BaseModel):
    response: str
    session_id: str
    suggestions: List[str]
    related_topics: List[str]
    references: List[Dict[str, str]]
    tools: List[Dict[str, str]]

class Message(BaseModel):
    role: str  # "user" veya "assistant"
    content: str
    timestamp: str

class Session(BaseModel):
    id: str
    created_at: str
    updated_at: str
    messages: List[Message]

# Oturum yönetimi
def get_session(session_id: str) -> Optional[Session]:
    session_path = SESSIONS_DIR / f"{session_id}.json"
    if not os.path.exists(session_path):
        return None
    
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)
    
    return Session(**session_data)

def create_session(session_id: str) -> Session:
    now = datetime.now().isoformat()
    session = Session(
        id=session_id,
        created_at=now,
        updated_at=now,
        messages=[
            Message(
                role="assistant",
                content="Merhaba! Ben Türkiye Hukuk AI Platformu'nun hukuki chatbot'uyum. Size nasıl yardımcı olabilirim?",
                timestamp=now
            )
        ]
    )
    
    save_session(session)
    return session

def save_session(session: Session):
    session.updated_at = datetime.now().isoformat()
    session_path = SESSIONS_DIR / f"{session.id}.json"
    
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(session.dict(), f, ensure_ascii=False, indent=2)

def add_message_to_session(session_id: str, message: Message):
    session = get_session(session_id)
    if not session:
        session = create_session(session_id)
    
    session.messages.append(message)
    save_session(session)

# API endpoint'leri
@app.get("/")
def read_root():
    return {"message": "Hukuki Chatbot API'ye Hoş Geldiniz"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Kullanıcı mesajını oturuma ekle
        user_message = Message(
            role="user",
            content=request.query,
            timestamp=datetime.now().isoformat()
        )
        add_message_to_session(request.session_id, user_message)
        
        # Mock AI servisi ile yanıt oluştur
        response = mock_ai_service.chat_response(request.query, request.session_id)
        
        # Asistan yanıtını oturuma ekle
        assistant_message = Message(
            role="assistant",
            content=response["response"],
            timestamp=datetime.now().isoformat()
        )
        add_message_to_session(request.session_id, assistant_message)
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chatbot yanıtı oluşturulurken hata: {str(e)}")

@app.get("/session/{session_id}", response_model=Session)
async def get_session_endpoint(session_id: str):
    session = get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Oturum bulunamadı: {session_id}")
    
    return session

@app.post("/session")
async def create_session_endpoint():
    session_id = f"session_{uuid.uuid4().hex}"
    session = create_session(session_id)
    return {"session_id": session_id}

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    session_path = SESSIONS_DIR / f"{session_id}.json"
    if not os.path.exists(session_path):
        raise HTTPException(status_code=404, detail=f"Oturum bulunamadı: {session_id}")
    
    os.remove(session_path)
    return {"message": f"Oturum silindi: {session_id}"}

# WebSocket endpoint'i
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    active_connections[session_id] = websocket
    
    try:
        # Oturum kontrolü
        session = get_session(session_id)
        if not session:
            session = create_session(session_id)
            await websocket.send_json({"type": "session_created", "session_id": session_id})
        
        # Önceki mesajları gönder
        await websocket.send_json({"type": "history", "messages": [msg.dict() for msg in session.messages]})
        
        # Mesaj döngüsü
        while True:
            data = await websocket.receive_text()
            
            try:
                # JSON verisini ayrıştır
                message_data = json.loads(data)
                query = message_data.get("query", "")
                
                if not query:
                    await websocket.send_json({"type": "error", "message": "Geçersiz sorgu"})
                    continue
                
                # Kullanıcı mesajını oturuma ekle
                user_message = Message(
                    role="user",
                    content=query,
                    timestamp=datetime.now().isoformat()
                )
                add_message_to_session(session_id, user_message)
                
                # Kullanıcıya mesajın alındığını bildir
                await websocket.send_json({"type": "message_received", "message": user_message.dict()})
                
                # Mock AI servisi ile yanıt oluştur
                response = mock_ai_service.chat_response(query, session_id)
                
                # Asistan yanıtını oturuma ekle
                assistant_message = Message(
                    role="assistant",
                    content=response["response"],
                    timestamp=datetime.now().isoformat()
                )
                add_message_to_session(session_id, assistant_message)
                
                # Yanıtı gönder
                await websocket.send_json({
                    "type": "response",
                    "message": assistant_message.dict(),
                    "suggestions": response["suggestions"],
                    "related_topics": response["related_topics"],
                    "references": response["references"],
                    "tools": response["tools"]
                })
                
            except json.JSONDecodeError:
                await websocket.send_json({"type": "error", "message": "Geçersiz JSON formatı"})
            except Exception as e:
                await websocket.send_json({"type": "error", "message": f"Hata: {str(e)}"})
    
    except WebSocketDisconnect:
        if session_id in active_connections:
            del active_connections[session_id]
    except Exception as e:
        print(f"WebSocket hatası: {str(e)}")
        if session_id in active_connections:
            del active_connections[session_id]

# Uygulama başlatma
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
# ------------------------------------------------------------------
@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}
# ------------------------------------------------------------------
