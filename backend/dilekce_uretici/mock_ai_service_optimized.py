import sys
from pathlib import Path

# Önbellek yöneticisini import et
sys.path.append('/home/ubuntu/hukuk_ai_projesi_uygulama/ai_components')
from mock_ai_service import MockAIService
from cache_manager import cache_manager

class OptimizedMockAIService(MockAIService):
    """
    Önbellek kullanarak optimize edilmiş mock AI servisi.
    """
    
    def __init__(self):
        super().__init__()
    
    def generate_petition(self, template_id, user_data, recipient_data, content_data):
        """
        Önbellekli dilekçe üretme işlemi
        """
        key_data = {
            "function": "generate_petition",
            "template_id": template_id,
            "user_data": user_data,
            "recipient_data": recipient_data,
            "content_data": content_data
        }
        
        return cache_manager.get_or_set(
            key_data,
            lambda: super().generate_petition(template_id, user_data, recipient_data, content_data)
        )
    
    def analyze_contract(self, text, contract_type):
        """
        Önbellekli sözleşme analizi işlemi
        """
        # Metin çok uzun olabilir, bu yüzden hash'ini kullan
        import hashlib
        text_hash = hashlib.md5(text.encode(), usedforsecurity=False).hexdigest()
        
        key_data = {
            "function": "analyze_contract",
            "text_hash": text_hash,
            "contract_type": contract_type
        }
        
        return cache_manager.get_or_set(
            key_data,
            lambda: super().analyze_contract(text, contract_type)
        )
    
    def chat_response(self, query, session_id):
        """
        Önbellekli chatbot yanıtı işlemi
        """
        key_data = {
            "function": "chat_response",
            "query": query
        }
        
        return cache_manager.get_or_set(
            key_data,
            lambda: super().chat_response(query, session_id)
        )

# Singleton instance
optimized_mock_ai_service = OptimizedMockAIService()
