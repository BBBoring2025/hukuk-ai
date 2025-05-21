import os
import json
import hashlib
import time
from pathlib import Path
from typing import Dict, Any, Optional

class CacheManager:
    """
    Basit bir önbellek yöneticisi.
    AI yanıtlarını önbelleğe alarak performansı artırır.
    """
    
    def __init__(self, cache_dir: str = None, ttl: int = 3600):
        """
        Önbellek yöneticisini başlatır.
        
        Args:
            cache_dir: Önbellek dosyalarının saklanacağı dizin
            ttl: Önbellek öğelerinin yaşam süresi (saniye)
        """
        if cache_dir is None:
            cache_dir = Path("/home/ubuntu/hukuk_ai_projesi_uygulama/cache")
        
        self.cache_dir = Path(cache_dir)
        self.ttl = ttl
        
        # Önbellek dizinini oluştur
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def _generate_key(self, data: Dict[str, Any]) -> str:
        """
        Verilen veriler için benzersiz bir anahtar oluşturur.
        
        Args:
            data: Anahtar oluşturmak için kullanılacak veriler
            
        Returns:
            Benzersiz bir anahtar
        """
        # Veriyi JSON'a dönüştür ve hash'le
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.md5(json_str.encode(), usedforsecurity=False).hexdigest()
    
    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Önbellekten veri alır.
        
        Args:
            key: Veri anahtarı
            
        Returns:
            Önbellekteki veri veya None
        """
        cache_file = self.cache_dir / f"{key}.json"
        
        if not cache_file.exists():
            return None
        
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cache_data = json.load(f)
            
            # TTL kontrolü
            if time.time() - cache_data["timestamp"] > self.ttl:
                # Süresi dolmuş, dosyayı sil
                os.remove(cache_file)
                return None
            
            return cache_data["data"]
        except Exception as e:
            print(f"Önbellek okuma hatası: {str(e)}")
            return None
    
    def set(self, key: str, data: Dict[str, Any]) -> None:
        """
        Veriyi önbelleğe kaydeder.
        
        Args:
            key: Veri anahtarı
            data: Kaydedilecek veri
        """
        cache_file = self.cache_dir / f"{key}.json"
        
        try:
            cache_data = {
                "timestamp": time.time(),
                "data": data
            }
            
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Önbellek yazma hatası: {str(e)}")
    
    def get_or_set(self, key_data: Dict[str, Any], generator_func) -> Dict[str, Any]:
        """
        Önbellekte veri varsa getirir, yoksa oluşturup kaydeder.
        
        Args:
            key_data: Anahtar oluşturmak için kullanılacak veriler
            generator_func: Veri yoksa çağrılacak fonksiyon
            
        Returns:
            Önbellekteki veya yeni oluşturulan veri
        """
        key = self._generate_key(key_data)
        cached_data = self.get(key)
        
        if cached_data is not None:
            return cached_data
        
        # Veri yoksa oluştur
        new_data = generator_func()
        self.set(key, new_data)
        return new_data
    
    def clear(self) -> None:
        """
        Tüm önbelleği temizler.
        """
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                os.remove(cache_file)
            except Exception as e:
                print(f"Önbellek temizleme hatası: {str(e)}")
    
    def clear_expired(self) -> None:
        """
        Süresi dolmuş önbellek öğelerini temizler.
        """
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cache_data = json.load(f)
                
                # TTL kontrolü
                if time.time() - cache_data["timestamp"] > self.ttl:
                    os.remove(cache_file)
            except Exception as e:
                print(f"Önbellek temizleme hatası: {str(e)}")

# Singleton instance
cache_manager = CacheManager()
