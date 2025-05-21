from fastapi import FastAPI, HTTPException, Request, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import json
import uuid
import datetime
import asyncio
import re
import nltk
from nltk.tokenize import word_tokenize
import random
import logging
import aiofiles

# NLTK'yi hazırla
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Modelleri tanımla
class ChatMessage(BaseModel):
    role: str  # "user" veya "assistant"
    content: str
    timestamp: Optional[str] = None

class ChatSession(BaseModel):
    id: str
    user_id: Optional[str] = None
    title: str
    messages: List[ChatMessage]
    created_at: str
    updated_at: str
    category: Optional[str] = None

class UserQuery(BaseModel):
    query: str
    session_id: Optional[str] = None
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    suggestions: List[str]
    related_topics: List[str]
    references: List[Dict[str, str]]
    tools: List[Dict[str, Any]]

# Uygulama oluştur
app = FastAPI(title="Türkiye Hukuk AI Platformu - Hukuki Chatbot API")

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
os.makedirs("sessions", exist_ok=True)
os.makedirs("knowledge", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Loglama
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bilgi tabanı
legal_knowledge = {
    "is_hukuku": {
        "kidem_tazminati": {
            "description": "Kıdem tazminatı, işçinin işyerinde çalıştığı süreye bağlı olarak işten ayrılırken hak ettiği tazminattır.",
            "calculation": "Her bir yıl için 30 günlük brüt ücret tutarında hesaplanır.",
            "eligibility": "En az 1 yıl çalışmış olmak ve belirli fesih koşullarının sağlanması gerekir.",
            "references": ["4857 Sayılı İş Kanunu", "1475 Sayılı İş Kanunu Madde 14"]
        },
        "ihbar_tazminati": {
            "description": "İhbar tazminatı, iş sözleşmesinin feshinde bildirim süresine uyulmaması durumunda ödenen tazminattır.",
            "calculation": "Çalışma süresine göre 2-8 haftalık ücret tutarında hesaplanır.",
            "eligibility": "Belirsiz süreli iş sözleşmelerinde, işveren tarafından bildirim süresine uyulmadan yapılan fesihlerde hak edilir.",
            "references": ["4857 Sayılı İş Kanunu Madde 17"]
        },
        "ise_iade": {
            "description": "İşe iade davası, haksız fesih durumunda işçinin işe geri dönmek için açtığı davadır.",
            "eligibility": "En az 6 ay kıdemi olan ve 30+ işçi çalıştıran işyerlerinde çalışan işçiler açabilir.",
            "time_limit": "Fesih bildiriminden itibaren 1 ay içinde açılmalıdır.",
            "references": ["4857 Sayılı İş Kanunu Madde 18-21"]
        },
        "yillik_izin": {
            "description": "Yıllık ücretli izin, işçinin her çalışma yılı için hak ettiği ücretli tatil süresidir.",
            "calculation": "1-5 yıl arası çalışma için 14 gün, 5-15 yıl arası için 20 gün, 15+ yıl için 26 gün.",
            "eligibility": "İşyerinde en az 1 yıl çalışmış olmak gerekir.",
            "references": ["4857 Sayılı İş Kanunu Madde 53-60"]
        }
    },
    "tuketici_hukuku": {
        "ayipli_mal": {
            "description": "Ayıplı mal, ambalajında, etiketinde veya reklam ve ilanlarında belirtilen nitelikleri taşımayan mallardır.",
            "consumer_rights": "Ücretsiz onarım, yenisiyle değiştirme, bedel iadesi veya indirim talep edilebilir.",
            "time_limit": "Malın tesliminden itibaren 2 yıl içinde bildirilmelidir.",
            "references": ["6502 Sayılı Tüketicinin Korunması Hakkında Kanun Madde 8-12"]
        },
        "cayma_hakki": {
            "description": "Cayma hakkı, tüketicinin herhangi bir gerekçe göstermeden ve cezai şart ödemeden sözleşmeden dönme hakkıdır.",
            "time_limit": "Mesafeli sözleşmelerde mal teslimine ilişkin sözleşmelerde malın tesliminden itibaren 14 gün içinde kullanılabilir.",
            "exceptions": "Özel üretim ürünler, hızlı bozulan mallar, dijital içerikler gibi istisnalar vardır.",
            "references": ["6502 Sayılı Tüketicinin Korunması Hakkında Kanun Madde 48-49", "Mesafeli Sözleşmeler Yönetmeliği"]
        },
        "tuketici_hakem_heyeti": {
            "description": "Tüketici hakem heyetleri, tüketici uyuşmazlıklarını çözmek için kurulan idari kuruluşlardır.",
            "jurisdiction": "Belirli parasal sınırların altındaki uyuşmazlıklar için zorunlu başvuru merciidir.",
            "application": "İlçe veya il tüketici hakem heyetlerine yazılı veya elektronik ortamda başvurulabilir.",
            "references": ["6502 Sayılı Tüketicinin Korunması Hakkında Kanun Madde 66-72"]
        }
    },
    "kira_hukuku": {
        "kira_artisi": {
            "description": "Kira artışı, kira sözleşmelerinde belirli dönemlerde yapılan kira bedeli güncellemesidir.",
            "limit": "Konut kiralarında artış oranı, bir önceki kira yılında TÜFE'nin on iki aylık ortalamasına göre değişen orandan fazla olamaz.",
            "application": "Kira artışı, kira sözleşmesinde belirtilen dönemlerde uygulanır.",
            "references": ["6098 Sayılı Türk Borçlar Kanunu Madde 344"]
        },
        "kira_tahliye": {
            "description": "Kira tahliyesi, kiracının kiralanan gayrimenkulü boşaltması işlemidir.",
            "landlord_termination": "Konut ve çatılı işyeri kiralarında, kiraya veren, 10 yıllık sürenin sonunda sebep göstermeden feshedebilir.",
            "tenant_termination": "Kiracı, belirsiz süreli kira sözleşmelerini 3 aylık fesih bildirim süresine uyarak feshedebilir.",
            "references": ["6098 Sayılı Türk Borçlar Kanunu Madde 347-349"]
        },
        "depozito": {
            "description": "Depozito, kiralanan gayrimenkulde oluşabilecek hasarlara karşı güvence olarak alınan bedeldir.",
            "limit": "Genellikle 2-3 aylık kira bedeli tutarında olur.",
            "return": "Kiracı, kiralananı sözleşme koşullarına uygun şekilde geri verdiğinde, kiraya veren depozitoyu faizi ile birlikte geri vermekle yükümlüdür.",
            "references": ["6098 Sayılı Türk Borçlar Kanunu Madde 342"]
        }
    },
    "aile_hukuku": {
        "bosanma": {
            "description": "Boşanma, evlilik birliğinin yasal olarak sona erdirilmesidir.",
            "grounds": "Zina, hayata kast, pek kötü davranış, suç işleme, terk, akıl hastalığı ve evlilik birliğinin sarsılması gibi nedenlerle açılabilir.",
            "process": "Dava açılması, duruşmalar ve karar aşamalarından oluşur.",
            "references": ["4721 Sayılı Türk Medeni Kanunu Madde 161-166"]
        },
        "nafaka": {
            "description": "Nafaka, aile hukukundan doğan bakım yükümlülüğüdür.",
            "types": "İştirak (çocuk) nafakası, yoksulluk nafakası ve tedbir nafakası olarak üçe ayrılır.",
            "calculation": "Tarafların ekonomik durumları, ihtiyaçları ve yaşam standartları göz önünde bulundurularak belirlenir.",
            "references": ["4721 Sayılı Türk Medeni Kanunu Madde 175-176"]
        },
        "velayet": {
            "description": "Velayet, çocuğun bakım ve eğitimini sağlama, onu temsil etme ve mallarını yönetme hakkı ve yükümlülüğüdür.",
            "determination": "Boşanma durumunda çocuğun üstün yararı gözetilerek anne veya babaya verilebilir.",
            "joint_custody": "Türk hukukunda ortak velayet, istisnai durumlarda kabul edilmektedir.",
            "references": ["4721 Sayılı Türk Medeni Kanunu Madde 335-351"]
        }
    }
}

# Yasal referanslar
legal_references = {
    "4857 Sayılı İş Kanunu": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4857.pdf",
    "6098 Sayılı Türk Borçlar Kanunu": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6098.pdf",
    "6502 Sayılı Tüketicinin Korunması Hakkında Kanun": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6502.pdf",
    "4721 Sayılı Türk Medeni Kanunu": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf",
    "1475 Sayılı İş Kanunu": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.1475.pdf",
    "Mesafeli Sözleşmeler Yönetmeliği": "https://www.resmigazete.gov.tr/eskiler/2014/11/20141127-6.htm"
}

# Sık sorulan sorular ve yanıtları
faqs = {
    "is_hukuku": [
        {
            "question": "İşten çıkarıldım, haklarım nelerdir?",
            "answer": "İşten çıkarılma durumunda kıdem tazminatı, ihbar tazminatı, kullanılmayan izin ücreti gibi haklarınız olabilir. Ayrıca haksız fesih durumunda işe iade davası açma hakkınız da bulunabilir."
        },
        {
            "question": "Kıdem tazminatı nasıl hesaplanır?",
            "answer": "Kıdem tazminatı, her bir tam yıl için 30 günlük brüt ücret tutarında hesaplanır. Bir yıldan artan süreler için de orantılı ödeme yapılır."
        },
        {
            "question": "İşe iade davası açmak için ne kadar sürem var?",
            "answer": "İşe iade davası, fesih bildiriminin tebliğinden itibaren 1 ay içinde açılmalıdır."
        }
    ],
    "tuketici_hukuku": [
        {
            "question": "Satın aldığım ürün ayıplı çıktı, ne yapabilirim?",
            "answer": "Ayıplı mal durumunda ücretsiz onarım, yenisiyle değiştirme, bedel iadesi veya indirim talep edebilirsiniz. Bu talebinizi malın tesliminden itibaren 2 yıl içinde iletmelisiniz."
        },
        {
            "question": "İnternetten aldığım ürünü iade edebilir miyim?",
            "answer": "Mesafeli sözleşmelerde (internet alışverişi gibi), malın tesliminden itibaren 14 gün içinde herhangi bir gerekçe göstermeden ve cezai şart ödemeden cayma hakkınız bulunmaktadır."
        },
        {
            "question": "Tüketici hakem heyetine nasıl başvurabilirim?",
            "answer": "Tüketici hakem heyetine başvuru, ikametgahınızın bulunduğu veya tüketici işleminin yapıldığı yerdeki heyete yazılı olarak veya e-Devlet üzerinden elektronik ortamda yapılabilir."
        }
    ],
    "kira_hukuku": [
        {
            "question": "Ev sahibi kira artışını nasıl yapabilir?",
            "answer": "Konut kiralarında artış oranı, bir önceki kira yılında TÜFE'nin on iki aylık ortalamasına göre değişen orandan fazla olamaz. Kira artışı, kira sözleşmesinde belirtilen dönemlerde uygulanır."
        },
        {
            "question": "Kiracı olarak evi ne zaman boşaltmak zorundayım?",
            "answer": "Kira sözleşmesinin süresi dolduğunda otomatik olarak boşaltma zorunluluğu yoktur. Ancak 10 yıllık sürenin sonunda ev sahibi sebep göstermeden tahliye talep edebilir."
        },
        {
            "question": "Depozito ne zaman geri alınır?",
            "answer": "Kiracı, kiralananı sözleşme koşullarına uygun şekilde geri verdiğinde, kiraya veren depozitoyu faizi ile birlikte geri vermekle yükümlüdür."
        }
    ],
    "aile_hukuku": [
        {
            "question": "Boşanma davası nasıl açılır?",
            "answer": "Boşanma davası, eşlerden birinin yerleşim yeri veya davalının yerleşim yeri mahkemesinde açılabilir. Dava dilekçesi, evlilik cüzdanı ve gerekli delillerle birlikte mahkemeye sunulur."
        },
        {
            "question": "Nafaka miktarı nasıl belirlenir?",
            "answer": "Nafaka miktarı, tarafların ekonomik durumları, ihtiyaçları ve yaşam standartları göz önünde bulundurularak mahkeme tarafından belirlenir."
        },
        {
            "question": "Velayet kime verilir?",
            "answer": "Velayet, boşanma durumunda çocuğun üstün yararı gözetilerek anne veya babaya verilebilir. Mahkeme, çocuğun yaşı, cinsiyeti, eğitim durumu, ebeveynlerin koşulları gibi faktörleri değerlendirir."
        }
    ]
}

# Aktif WebSocket bağlantıları
active_connections = {}

# Oturum yönetimi
async def get_or_create_session(session_id=None, user_id=None):
    """Mevcut oturumu getir veya yeni oturum oluştur"""
    if session_id:
        session_file = f"sessions/{session_id}.json"
        if os.path.exists(session_file):
            async with aiofiles.open(session_file, "r", encoding="utf-8") as f:
                session_data = json.loads(await f.read())
                return ChatSession(**session_data)
    
    # Yeni oturum oluştur
    session_id = str(uuid.uuid4())
    now = datetime.datetime.now().isoformat()
    session = ChatSession(
        id=session_id,
        user_id=user_id,
        title="Yeni Sohbet",
        messages=[],
        created_at=now,
        updated_at=now
    )
    
    # Oturumu kaydet
    await save_session(session)
    
    return session

async def save_session(session: ChatSession):
    """Oturumu kaydet"""
    session_file = f"sessions/{session.id}.json"
    async with aiofiles.open(session_file, "w", encoding="utf-8") as f:
        await f.write(json.dumps(session.dict(), ensure_ascii=False, indent=2))

async def add_message_to_session(session: ChatSession, role: str, content: str):
    """Oturuma mesaj ekle"""
    message = ChatMessage(
        role=role,
        content=content,
        timestamp=datetime.datetime.now().isoformat()
    )
    session.messages.append(message)
    session.updated_at = datetime.datetime.now().isoformat()
    
    # Oturum başlığını güncelle (ilk kullanıcı mesajı ise)
    if role == "user" and len(session.messages) == 1:
        # İlk 30 karakteri başlık olarak kullan
        session.title = content[:30] + ("..." if len(content) > 30 else "")
    
    await save_session(session)
    return message

# Sohbet işleme fonksiyonları
async def process_query(query: UserQuery):
    """Kullanıcı sorgusunu işle ve yanıt oluştur"""
    # Oturumu al veya oluştur
    session = await get_or_create_session(query.session_id, query.user_id)
    
    # Kullanıcı mesajını oturuma ekle
    await add_message_to_session(session, "user", query.query)
    
    # Yanıt oluştur
    response, suggestions, related_topics, references, tools = await generate_response(query.query, session)
    
    # Asistan mesajını oturuma ekle
    await add_message_to_session(session, "assistant", response)
    
    return ChatResponse(
        response=response,
        session_id=session.id,
        suggestions=suggestions,
        related_topics=related_topics,
        references=references,
        tools=tools
    )

async def generate_response(query: str, session: ChatSession):
    """Sorguya yanıt oluştur"""
    # Sorguyu analiz et
    category, topic, intent = analyze_query(query)
    
    # Yanıt oluştur
    response = ""
    suggestions = []
    related_topics = []
    references = []
    tools = []
    
    # Kategori ve konu bazlı yanıt oluştur
    if category and topic and topic in legal_knowledge.get(category, {}):
        topic_info = legal_knowledge[category][topic]
        
        # Temel bilgileri ekle
        response += f"{topic_info['description']} "
        
        # İntent'e göre ek bilgiler ekle
        if intent == "calculation" and "calculation" in topic_info:
            response += f"\n\n{topic_info['calculation']} "
        elif intent == "eligibility" and "eligibility" in topic_info:
            response += f"\n\n{topic_info['eligibility']} "
        elif intent == "time_limit" and "time_limit" in topic_info:
            response += f"\n\n{topic_info['time_limit']} "
        elif intent == "process" and "process" in topic_info:
            response += f"\n\n{topic_info['process']} "
        
        # Referansları ekle
        if "references" in topic_info:
            response += f"\n\nYasal Dayanaklar: {', '.join(topic_info['references'])}"
            for ref in topic_info["references"]:
                if ref in legal_references:
                    references.append({"title": ref, "url": legal_references[ref]})
        
        # İlgili konuları ekle
        for related_topic in legal_knowledge.get(category, {}):
            if related_topic != topic:
                related_topics.append(related_topic.replace("_", " ").title())
                if len(related_topics) >= 3:
                    break
        
        # Önerileri ekle
        if category in faqs:
            for faq in faqs[category]:
                if topic in faq["question"].lower():
                    suggestions.append(faq["question"])
                    if len(suggestions) >= 3:
                        break
        
        # Araçları ekle
        if category == "is_hukuku" and topic == "kidem_tazminati":
            tools.append({
                "type": "calculator",
                "name": "Kıdem Tazminatı Hesaplama",
                "description": "Kıdem tazminatınızı hesaplamak için bu aracı kullanabilirsiniz."
            })
        elif category == "tuketici_hukuku":
            tools.append({
                "type": "petition",
                "name": "Tüketici Şikayet Dilekçesi Oluştur",
                "description": "Tüketici şikayet dilekçesi oluşturmak için bu aracı kullanabilirsiniz."
            })
        elif category == "kira_hukuku":
            tools.append({
                "type": "contract_analysis",
                "name": "Kira Sözleşmesi Analizi",
                "description": "Kira sözleşmenizi analiz etmek için bu aracı kullanabilirsiniz."
            })
    else:
        # Bilgi tabanında doğrudan eşleşme yoksa, benzer soruları ara
        matched_faq = find_similar_faq(query)
        if matched_faq:
            response = matched_faq["answer"]
            category = get_category_from_faq(matched_faq)
            
            # Kategori bazlı öneriler ve ilgili konular
            if category:
                for faq in faqs.get(category, [])[:3]:
                    if faq["question"] != matched_faq["question"]:
                        suggestions.append(faq["question"])
                
                for topic in list(legal_knowledge.get(category, {}).keys())[:3]:
                    related_topics.append(topic.replace("_", " ").title())
        else:
            # Genel yanıt
            response = "Üzgünüm, bu konuda spesifik bir bilgim yok. Lütfen sorunuzu daha açık bir şekilde ifade eder misiniz? Örneğin, hangi hukuk alanıyla ilgili bilgi almak istediğinizi belirtebilirsiniz."
            
            # Genel öneriler
            suggestions = [
                "İşten çıkarıldım, haklarım nelerdir?",
                "Satın aldığım ürün ayıplı çıktı, ne yapabilirim?",
                "Ev sahibi kira artışını nasıl yapabilir?"
            ]
            
            # Genel ilgili konular
            related_topics = ["İş Hukuku", "Tüketici Hukuku", "Kira Hukuku"]
    
    # Yanıtı döndür
    return response, suggestions, related_topics, references, tools

def analyze_query(query: str):
    """Sorguyu analiz et ve kategori, konu ve niyet belirle"""
    query_lower = query.lower()
    
    # Kategori belirleme
    category = None
    if any(keyword in query_lower for keyword in ["iş", "işçi", "işveren", "çalışan", "kıdem", "ihbar", "tazminat", "işten çıkarma", "maaş"]):
        category = "is_hukuku"
    elif any(keyword in query_lower for keyword in ["tüketici", "ürün", "ayıp", "iade", "değişim", "garanti", "satın alma", "alışveriş"]):
        category = "tuketici_hukuku"
    elif any(keyword in query_lower for keyword in ["kira", "kiracı", "ev sahibi", "konut", "tahliye", "depozito", "kontrat"]):
        category = "kira_hukuku"
    elif any(keyword in query_lower for keyword in ["boşanma", "nafaka", "velayet", "evlilik", "çocuk", "aile"]):
        category = "aile_hukuku"
    
    # Konu belirleme
    topic = None
    if category == "is_hukuku":
        if any(keyword in query_lower for keyword in ["kıdem", "tazminat", "işten çıkarma"]):
            topic = "kidem_tazminati"
        elif any(keyword in query_lower for keyword in ["ihbar", "bildirim", "süre"]):
            topic = "ihbar_tazminati"
        elif any(keyword in query_lower for keyword in ["işe iade", "geri dönme", "haksız fesih"]):
            topic = "ise_iade"
        elif any(keyword in query_lower for keyword in ["izin", "tatil", "yıllık"]):
            topic = "yillik_izin"
    elif category == "tuketici_hukuku":
        if any(keyword in query_lower for keyword in ["ayıp", "bozuk", "arızalı", "hatalı"]):
            topic = "ayipli_mal"
        elif any(keyword in query_lower for keyword in ["cayma", "vazgeçme", "iade", "internet", "online"]):
            topic = "cayma_hakki"
        elif any(keyword in query_lower for keyword in ["hakem", "şikayet", "başvuru"]):
            topic = "tuketici_hakem_heyeti"
    elif category == "kira_hukuku":
        if any(keyword in query_lower for keyword in ["artış", "zam", "yükseltme"]):
            topic = "kira_artisi"
        elif any(keyword in query_lower for keyword in ["tahliye", "çıkarma", "boşaltma"]):
            topic = "kira_tahliye"
        elif any(keyword in query_lower for keyword in ["depozito", "teminat"]):
            topic = "depozito"
    elif category == "aile_hukuku":
        if any(keyword in query_lower for keyword in ["boşanma", "ayrılma"]):
            topic = "bosanma"
        elif any(keyword in query_lower for keyword in ["nafaka", "ödeme", "destek"]):
            topic = "nafaka"
        elif any(keyword in query_lower for keyword in ["velayet", "çocuk", "bakım"]):
            topic = "velayet"
    
    # Niyet belirleme
    intent = None
    if any(keyword in query_lower for keyword in ["nasıl", "ne şekilde", "hangi yöntemle"]):
        intent = "process"
    elif any(keyword in query_lower for keyword in ["hesapla", "miktar", "tutar", "ne kadar"]):
        intent = "calculation"
    elif any(keyword in query_lower for keyword in ["hak", "koşul", "şart", "kimler"]):
        intent = "eligibility"
    elif any(keyword in query_lower for keyword in ["süre", "zaman", "ne zaman", "tarih"]):
        intent = "time_limit"
    
    return category, topic, intent

def find_similar_faq(query: str):
    """Benzer SSS sorusunu bul"""
    query_lower = query.lower()
    best_match = None
    best_score = 0
    
    for category, category_faqs in faqs.items():
        for faq in category_faqs:
            # Basit benzerlik skoru hesapla
            question_lower = faq["question"].lower()
            score = calculate_similarity(query_lower, question_lower)
            
            if score > best_score and score > 0.5:  # Eşik değeri
                best_score = score
                best_match = faq
                best_match["category"] = category  # Kategori bilgisini ekle
    
    return best_match

def calculate_similarity(text1: str, text2: str):
    """İki metin arasındaki benzerliği hesapla"""
    # Basit kelime örtüşmesi
    words1 = set(word_tokenize(text1))
    words2 = set(word_tokenize(text2))
    
    if not words1 or not words2:
        return 0
    
    common_words = words1.intersection(words2)
    return len(common_words) / max(len(words1), len(words2))

def get_category_from_faq(faq):
    """SSS'den kategori bilgisini al"""
    return faq.get("category") if faq else None

# API Endpoint'leri
@app.get("/")
async def root():
    return {"message": "Türkiye Hukuk AI Platformu - Hukuki Chatbot API"}

@app.post("/query", response_model=ChatResponse)
async def query(query: UserQuery):
    """Kullanıcı sorgusunu işle"""
    try:
        return await process_query(query)
    except Exception as e:
        logger.error(f"Query processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Sorgu işlenirken bir hata oluştu: {str(e)}")

@app.get("/sessions/{user_id}", response_model=List[ChatSession])
async def get_user_sessions(user_id: str):
    """Kullanıcının oturumlarını getir"""
    sessions = []
    
    if os.path.exists("sessions"):
        for filename in os.listdir("sessions"):
            if filename.endswith(".json"):
                try:
                    async with aiofiles.open(f"sessions/{filename}", "r", encoding="utf-8") as f:
                        session_data = json.loads(await f.read())
                        if session_data.get("user_id") == user_id:
                            sessions.append(ChatSession(**session_data))
                except Exception as e:
                    logger.error(f"Error reading session file {filename}: {str(e)}")
    
    # Oturumları son güncelleme tarihine göre sırala
    sessions.sort(key=lambda s: s.updated_at, reverse=True)
    
    return sessions

@app.get("/session/{session_id}", response_model=ChatSession)
async def get_session(session_id: str):
    """Belirli bir oturumu getir"""
    session_file = f"sessions/{session_id}.json"
    
    if not os.path.exists(session_file):
        raise HTTPException(status_code=404, detail="Oturum bulunamadı")
    
    try:
        async with aiofiles.open(session_file, "r", encoding="utf-8") as f:
            session_data = json.loads(await f.read())
            return ChatSession(**session_data)
    except Exception as e:
        logger.error(f"Error reading session file {session_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Oturum yüklenirken bir hata oluştu: {str(e)}")

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """Belirli bir oturumu sil"""
    session_file = f"sessions/{session_id}.json"
    
    if not os.path.exists(session_file):
        raise HTTPException(status_code=404, detail="Oturum bulunamadı")
    
    try:
        os.remove(session_file)
        return {"message": "Oturum başarıyla silindi"}
    except Exception as e:
        logger.error(f"Error deleting session file {session_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Oturum silinirken bir hata oluştu: {str(e)}")

@app.get("/categories")
async def get_categories():
    """Hukuk kategorilerini getir"""
    return {
        "categories": [
            {"id": "is_hukuku", "name": "İş Hukuku"},
            {"id": "tuketici_hukuku", "name": "Tüketici Hukuku"},
            {"id": "kira_hukuku", "name": "Kira Hukuku"},
            {"id": "aile_hukuku", "name": "Aile Hukuku"}
        ]
    }

@app.get("/topics/{category}")
async def get_topics(category: str):
    """Belirli bir kategorideki konuları getir"""
    if category not in legal_knowledge:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    topics = []
    for topic_id, topic_data in legal_knowledge[category].items():
        topics.append({
            "id": topic_id,
            "name": topic_id.replace("_", " ").title(),
            "description": topic_data.get("description", "")
        })
    
    return {"topics": topics}

@app.get("/faqs/{category}")
async def get_faqs(category: str):
    """Belirli bir kategorideki SSS'leri getir"""
    if category not in faqs:
        raise HTTPException(status_code=404, detail="Kategori bulunamadı")
    
    return {"faqs": faqs[category]}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """WebSocket bağlantısı"""
    await websocket.accept()
    active_connections[client_id] = websocket
    
    try:
        while True:
            data = await websocket.receive_text()
            try:
                query_data = json.loads(data)
                user_query = UserQuery(**query_data)
                response = await process_query(user_query)
                await websocket.send_json(response.dict())
            except Exception as e:
                logger.error(f"WebSocket error: {str(e)}")
                await websocket.send_json({"error": str(e)})
    except WebSocketDisconnect:
        if client_id in active_connections:
            del active_connections[client_id]

# Ana uygulama
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
