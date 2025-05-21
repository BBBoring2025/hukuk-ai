import json
import random
from typing import Dict, List, Any

class MockAIService:
    """
    Gerçek AI modellerini simüle eden mock servis.
    Disk alanı kısıtlamaları nedeniyle gerçek Llama 3 modeli yerine kullanılır.
    """
    
    def __init__(self):
        # Örnek hukuki terimler ve yanıtlar
        self.legal_terms = [
            "kıdem tazminatı", "ihbar tazminatı", "iş akdi feshi", "boşanma davası",
            "nafaka", "velayet", "kira sözleşmesi", "tahliye", "tüketici hakları",
            "ayıplı mal", "iade hakkı", "ceza hukuku", "idari yargı", "icra takibi"
        ]
        
        # Örnek yanıtlar
        self.responses = {
            "kıdem tazminatı": "Kıdem tazminatı, işçinin işyerinde çalıştığı süreye bağlı olarak işten ayrılırken hak ettiği tazminattır. Her bir yıl için 30 günlük brüt ücret tutarında hesaplanır.",
            "ihbar tazminatı": "İhbar tazminatı, iş sözleşmesinin feshinde bildirim süresine uyulmaması durumunda ödenen tazminattır. Çalışma süresine göre 2-8 haftalık ücret tutarında hesaplanır.",
            "iş akdi feshi": "İş akdi feshi, işçi veya işveren tarafından iş sözleşmesinin sona erdirilmesidir. Haklı nedenle fesih veya bildirimli fesih olarak ikiye ayrılır.",
            "boşanma davası": "Boşanma davası, evlilik birliğinin yasal olarak sona erdirilmesi için açılan davadır. Zina, hayata kast, pek kötü muamele, suç işleme, terk, akıl hastalığı, evlilik birliğinin sarsılması gibi nedenlerle açılabilir.",
            "nafaka": "Nafaka, aile hukukundan doğan bakım yükümlülüğüdür. İştirak (çocuk) nafakası, yoksulluk nafakası, tedbir nafakası gibi türleri vardır.",
            "velayet": "Velayet, çocuğun bakım ve eğitimini üstlenme hak ve sorumluluğudur. Çocuğun üstün yararı gözetilerek belirlenir.",
            "kira sözleşmesi": "Kira sözleşmesi, kiraya verenin bir şeyin kullanılmasını veya kullanmayla birlikte ondan yararlanılmasını kiracıya bırakmayı, kiracının da buna karşılık kararlaştırılan kira bedelini ödemeyi üstlendiği sözleşmedir.",
            "tahliye": "Tahliye, kiralanan gayrimenkulün boşaltılmasıdır. Kira sözleşmesinin sona ermesi, kiracının kira bedelini ödememesi, kiralananı özenle kullanmaması gibi nedenlerle talep edilebilir.",
            "tüketici hakları": "Tüketici hakları, tüketicilerin mal ve hizmet satın alırken korunmasını sağlayan haklardır. Ayıplı mal ve hizmetlerde ücretsiz onarım, yenisiyle değiştirme, bedel iadesi, bedel indirimi gibi seçimlik haklar içerir.",
            "ayıplı mal": "Ayıplı mal, sözleşmeye aykırı olan, standartlara uymayan veya ambalajında belirtilen özellikleri taşımayan ürünlerdir. Tüketici, ücretsiz onarım, yenisiyle değiştirme, bedel iadesi, bedel indirimi haklarına sahiptir.",
            "iade hakkı": "İade hakkı, tüketicinin satın aldığı mal veya hizmeti belirli koşullar altında iade etme hakkıdır. Mesafeli sözleşmelerde 14 gün içinde sebep göstermeksizin iade hakkı bulunmaktadır.",
            "ceza hukuku": "Ceza hukuku, suç ve cezaları düzenleyen hukuk dalıdır. Suçun unsurları, ceza sorumluluğu, ceza türleri gibi konuları içerir.",
            "idari yargı": "İdari yargı, idarenin işlem ve eylemlerinden doğan uyuşmazlıkları çözümleyen yargı koludur. İdare mahkemeleri, vergi mahkemeleri ve Danıştay idari yargı organlarıdır.",
            "icra takibi": "İcra takibi, bir alacağın zorla tahsili için yapılan yasal işlemdir. İlamsız icra ve ilamlı icra olmak üzere ikiye ayrılır."
        }
        
        # Örnek risk faktörleri
        self.risk_factors = {
            "kira": [
                {"pattern": "süresiz", "risk": "critical", "message": "Kira süresi belirtilmemiş veya süresiz olarak tanımlanmış"},
                {"pattern": "sözlü", "risk": "critical", "message": "Sözlü anlaşmaya atıf yapılmış, yazılı olarak netleştirilmeli"},
                {"pattern": "artış", "risk": "medium", "message": "Kira artış oranı belirtilmemiş veya yasal sınırları aşıyor"},
                {"pattern": "depozito", "risk": "medium", "message": "Depozito miktarı belirtilmemiş veya yasal sınırları aşıyor"},
                {"pattern": "tahliye", "risk": "low", "message": "Tahliye koşulları belirtilmemiş veya yasal düzenlemelere aykırı"}
            ],
            "is": [
                {"pattern": "süresiz", "risk": "critical", "message": "İş sözleşmesi süresi belirtilmemiş"},
                {"pattern": "deneme", "risk": "medium", "message": "Deneme süresi 2 aydan uzun belirlenmiş"},
                {"pattern": "fazla mesai", "risk": "medium", "message": "Fazla mesai ücreti belirtilmemiş"},
                {"pattern": "izin", "risk": "low", "message": "Yıllık izin süresi belirtilmemiş"},
                {"pattern": "fesih", "risk": "low", "message": "Fesih bildirimi süresi belirtilmemiş"}
            ],
            "ticari": [
                {"pattern": "ödeme", "risk": "critical", "message": "Ödeme koşulları net belirtilmemiş"},
                {"pattern": "teslimat", "risk": "medium", "message": "Teslimat süresi ve koşulları belirtilmemiş"},
                {"pattern": "cezai şart", "risk": "medium", "message": "Cezai şart oranı çok yüksek belirlenmiş"},
                {"pattern": "mücbir sebep", "risk": "low", "message": "Mücbir sebep halleri belirtilmemiş"},
                {"pattern": "uyuşmazlık", "risk": "low", "message": "Uyuşmazlık çözüm yöntemi belirtilmemiş"}
            ]
        }
    
    def generate_petition(self, template_id: str, user_data: Dict, recipient_data: Dict, content_data: Dict) -> Dict:
        """
        Dilekçe üretme işlemini simüle eder
        """
        petition_id = f"petition_{random.randint(10000, 99999)}"
        
        return {
            "id": petition_id,
            "file_path": f"output/{petition_id}.pdf",
            "created_at": "2025-04-01T12:00:00Z",
            "template_id": template_id,
            "template_name": "Simüle Edilmiş Dilekçe"
        }
    
    def analyze_contract(self, text: str, contract_type: str) -> Dict:
        """
        Sözleşme analizi işlemini simüle eder
        """
        # Basit bir risk analizi yap
        words = text.lower().split()
        total_words = len(words)
        
        # Rastgele sayıda madde oluştur (5-10 arası)
        num_clauses = random.randint(5, 10)
        clauses = []
        
        # Risk sayaçları
        critical_issues = 0
        medium_issues = 0
        low_issues = 0
        info_notes = 0
        
        # Maddeleri oluştur
        for i in range(1, num_clauses + 1):
            # Madde içeriği için metinden rastgele bir bölüm al
            start_idx = random.randint(0, max(0, total_words - 50))
            end_idx = min(start_idx + random.randint(20, 50), total_words)
            clause_content = " ".join(words[start_idx:end_idx])
            
            # Risk faktörlerini kontrol et
            issues = []
            suggestions = []
            
            risk_level = "info"
            
            if contract_type in self.risk_factors:
                for factor in self.risk_factors[contract_type]:
                    if factor["pattern"] in clause_content:
                        issues.append({
                            "type": factor["risk"],
                            "message": factor["message"]
                        })
                        
                        suggestions.append(f"Öneri: {factor['message']} konusunu netleştirin.")
                        
                        # En yüksek risk seviyesini belirle
                        if factor["risk"] == "critical" and risk_level != "critical":
                            risk_level = "critical"
                            critical_issues += 1
                        elif factor["risk"] == "medium" and risk_level not in ["critical"]:
                            risk_level = "medium"
                            medium_issues += 1
                        elif factor["risk"] == "low" and risk_level not in ["critical", "medium"]:
                            risk_level = "low"
                            low_issues += 1
            
            # Eğer hiç sorun bulunamazsa
            if not issues:
                risk_level = "info"
                info_notes += 1
            
            clauses.append({
                "id": f"clause_{i}",
                "clause_number": str(i),
                "title": f"Madde {i}",
                "content": clause_content,
                "risk_level": risk_level,
                "issues": issues,
                "suggestions": suggestions
            })
        
        # Genel risk seviyesini belirle
        if critical_issues > 0:
            risk_level = "Yüksek Risk"
        elif medium_issues > 0:
            risk_level = "Orta Risk"
        else:
            risk_level = "Düşük Risk"
        
        # Yasal uyumluluk kontrolü
        legal_compliance = {}
        required_clauses = []
        
        if contract_type == "kira":
            required_clauses = ["taraflar", "kira konusu", "kira süresi", "kira bedeli", "ödeme şekli"]
        elif contract_type == "is":
            required_clauses = ["taraflar", "iş tanımı", "çalışma süresi", "ücret", "fesih"]
        elif contract_type == "ticari":
            required_clauses = ["taraflar", "konu", "bedel", "teslimat", "ödeme"]
        
        for clause in required_clauses:
            legal_compliance[clause] = clause in text.lower() or random.random() > 0.3
        
        # Özet oluştur
        summary = f"""
        Sözleşme Analiz Özeti:
        
        Bu {contract_type} sözleşmesi {num_clauses} madde içermektedir.
        Genel risk seviyesi: {risk_level}
        
        Tespit edilen sorunlar:
        - Kritik sorunlar: {critical_issues}
        - Orta seviye sorunlar: {medium_issues}
        - Düşük seviye notlar: {low_issues}
        
        Yasal uyumluluk:
        """
        
        missing_clauses = [clause for clause, found in legal_compliance.items() if not found]
        if missing_clauses:
            summary += f"Aşağıdaki zorunlu maddeler eksik veya yeterince açık değil:\n"
            for clause in missing_clauses:
                summary += f"- {clause}\n"
        else:
            summary += "Tüm zorunlu maddeler sözleşmede bulunmaktadır.\n"
        
        if critical_issues > 0:
            summary += "\nÖnemli uyarı: Bu sözleşmede kritik sorunlar bulunmaktadır. İmzalamadan önce bir hukuk uzmanına danışmanız önerilir."
        
        return {
            "id": f"analysis_{random.randint(10000, 99999)}",
            "created_at": "2025-04-01T12:00:00Z",
            "contract_type": contract_type,
            "risk_level": risk_level,
            "total_clauses": num_clauses,
            "critical_issues": critical_issues,
            "medium_issues": medium_issues,
            "low_issues": low_issues,
            "info_notes": info_notes,
            "clauses": clauses,
            "legal_compliance": legal_compliance,
            "summary": summary
        }
    
    def chat_response(self, query: str, session_id: str) -> Dict:
        """
        Chatbot yanıtı üretme işlemini simüle eder
        """
        # Sorgu içinde hukuki terim var mı kontrol et
        response = "Üzgünüm, sorunuzu anlayamadım. Lütfen hukuki bir konuda soru sorun."
        
        for term in self.legal_terms:
            if term in query.lower():
                response = self.responses.get(term, "Bu konu hakkında detaylı bilgi için bir avukata danışmanızı öneririm.")
                break
        
        # Eğer hiçbir terim bulunamazsa, genel bir yanıt ver
        if response == "Üzgünüm, sorunuzu anlayamadım. Lütfen hukuki bir konuda soru sorun.":
            # Rastgele bir terimi öner
            random_term = random.choice(self.legal_terms)
            response = f"Sorunuzu tam olarak anlayamadım. Belki '{random_term}' hakkında soru sormak isteyebilirsiniz? Bu konuda size yardımcı olabilirim."
        
        # Rastgele öneriler oluştur
        suggestions = []
        for _ in range(3):
            term = random.choice(self.legal_terms)
            suggestions.append(f"{term.capitalize()} hakkında bilgi alabilir miyim?")
        
        # Rastgele ilgili konular oluştur
        related_topics = random.sample(self.legal_terms, min(3, len(self.legal_terms)))
        
        # Rastgele referanslar oluştur
        references = [
            {"title": "Türk Borçlar Kanunu", "url": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6098.pdf"},
            {"title": "Türk Medeni Kanunu", "url": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf"},
            {"title": "İş Kanunu", "url": "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4857.pdf"}
        ]
        
        # Rastgele araçlar oluştur
        tools = [
            {
                "name": "Dilekçe Oluştur",
                "description": "Bu konuyla ilgili dilekçe oluşturmak için tıklayın",
                "url": "/dilekce-uretici"
            },
            {
                "name": "Sözleşme Analizi",
                "description": "Sözleşmenizi analiz etmek için tıklayın",
                "url": "/sozlesme-analizi"
            }
        ]
        
        return {
            "response": response,
            "session_id": session_id,
            "suggestions": suggestions,
            "related_topics": related_topics,
            "references": references,
            "tools": tools
        }

# Singleton instance
mock_ai_service = MockAIService()
