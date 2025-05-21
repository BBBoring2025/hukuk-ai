import os
import sys
from pathlib import Path

# Mock AI servisi için import
sys.path.append('/home/ubuntu/hukuk_ai_projesi_uygulama/ai_components')
from mock_ai_service import mock_ai_service

# Örnek şablonlar için dizin
TEMPLATES_DIR = Path("/home/ubuntu/hukuk_ai_projesi_uygulama/dilekce_uretici/templates")
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Örnek şablonlar oluştur
def create_sample_templates():
    # Tüketici şikayeti şablonu
    tuketici_sikayet = """
    Tüketici Hakem Heyeti Başkanlığı'na
    
    ŞİKAYET EDEN: {{user_data.ad_soyad}}
    T.C. Kimlik No: {{user_data.tc_kimlik}}
    Adres: {{user_data.adres}}
    Telefon: {{user_data.telefon}}
    E-posta: {{user_data.eposta}}
    
    ŞİKAYET EDİLEN: {{recipient_data.muhatap_ad}}
    Adres: {{recipient_data.muhatap_adres}}
    
    KONU: {{content_data.urun_hizmet}} ile ilgili {{content_data.sikayet_konusu}} hakkında şikayet
    
    Sayın Başkanlık,
    
    {{recipient_data.muhatap_ad}} firmasından {{content_data.satin_alma_tarihi}} tarihinde {{content_data.urun_hizmet}} satın aldım. Ancak aşağıda belirtilen sorunlarla karşılaştım:
    
    {{content_data.sikayet_detay}}
    
    Bu nedenle, 6502 sayılı Tüketicinin Korunması Hakkında Kanun kapsamında aşağıdaki talebimin değerlendirilmesini arz ederim:
    
    {% for talep in content_data.talep %}
    - {{talep}}
    {% endfor %}
    
    Gereğini saygılarımla arz ederim.
    
    Tarih: {{current_date}}
    Ad Soyad: {{user_data.ad_soyad}}
    İmza:
    
    EKLER:
    1. Fatura/Fiş Fotokopisi
    2. Ürün Görselleri
    """
    
    # İş akdi fesih şablonu
    is_fesih = """
    {{recipient_data.muhatap_ad}}
    {{recipient_data.muhatap_adres}}
    
    KONU: İş Akdi Fesih Bildirimi
    
    Sayın İlgili,
    
    Şirketinizde {{content_data.ise_baslama_tarihi}} tarihinden bu yana çalışmaktayım. İş Kanunu'nun ilgili maddeleri uyarınca, iş akdimi {{content_data.fesih_tarihi}} tarihi itibariyle feshetmek istediğimi bildiririm.
    
    Fesih gerekçem: {{content_data.fesih_nedeni}}
    
    {{content_data.fesih_detay}}
    
    {% if content_data.talepler %}
    Bu fesih bildirimi ile birlikte aşağıdaki yasal haklarımın tarafıma ödenmesini talep ediyorum:
    
    {% for talep in content_data.talepler %}
    - {{talep}}
    {% endfor %}
    {% endif %}
    
    İş ilişkimizin sonlandırılması sürecinde göstereceğiniz anlayış için teşekkür ederim.
    
    Gereğini bilgilerinize arz ederim.
    
    Tarih: {{current_date}}
    Ad Soyad: {{user_data.ad_soyad}}
    T.C. Kimlik No: {{user_data.tc_kimlik}}
    Adres: {{user_data.adres}}
    İmza:
    """
    
    # Kira tahliye şablonu
    kira_tahliye = """
    {{recipient_data.muhatap_ad}}
    {{recipient_data.muhatap_adres}}
    
    KONU: Kira Sözleşmesi Fesih ve Tahliye Bildirimi
    
    Sayın {{recipient_data.muhatap_ad}},
    
    {{user_data.adres}} adresinde bulunan ve {{content_data.kira_baslangic}} tarihinden bu yana kiracısı olduğum gayrimenkulü, {{content_data.tahliye_tarihi}} tarihinde tahliye edeceğimi bildiririm.
    
    Tahliye gerekçem: {{content_data.fesih_nedeni}}
    
    {{content_data.fesih_detay}}
    
    {% if content_data.depozito_iadesi == "Evet" %}
    Tahliye işleminin ardından, sözleşme başlangıcında ödemiş olduğum depozitonun tarafıma iade edilmesini talep ediyorum.
    {% endif %}
    
    Kiralama sürecinde göstermiş olduğunuz anlayış için teşekkür ederim.
    
    Gereğini bilgilerinize arz ederim.
    
    Tarih: {{current_date}}
    Ad Soyad: {{user_data.ad_soyad}}
    T.C. Kimlik No: {{user_data.tc_kimlik}}
    Telefon: {{user_data.telefon}}
    İmza:
    """
    
    # Şablonları dosyalara kaydet
    with open(TEMPLATES_DIR / "tuketici_sikayet.txt", "w", encoding="utf-8") as f:
        f.write(tuketici_sikayet)
    
    with open(TEMPLATES_DIR / "is_fesih.txt", "w", encoding="utf-8") as f:
        f.write(is_fesih)
    
    with open(TEMPLATES_DIR / "kira_tahliye.txt", "w", encoding="utf-8") as f:
        f.write(kira_tahliye)
    
    print("Örnek şablonlar oluşturuldu.")

if __name__ == "__main__":
    create_sample_templates()
