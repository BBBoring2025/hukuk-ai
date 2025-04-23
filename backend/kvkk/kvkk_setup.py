import os
from pathlib import Path

# KVKK uyumluluk metinleri ve politikaları
BASE_DIR = Path("/home/ubuntu/hukuk_ai_projesi_uygulama")
KVKK_DIR = BASE_DIR / "kvkk"

# Dizini oluştur
os.makedirs(KVKK_DIR, exist_ok=True)

# Aydınlatma metni
def create_aydinlatma_metni():
    content = """# AYDINLATMA METNİ

## Türkiye Hukuk AI Platformu Kişisel Verilerin Korunması Aydınlatma Metni

**Veri Sorumlusu:** Türkiye Hukuk AI Platformu

### 1. Giriş

Türkiye Hukuk AI Platformu olarak kişisel verilerinizin güvenliği ve gizliliği konusunda azami hassasiyet göstermekteyiz. Bu Aydınlatma Metni, 6698 sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") kapsamında, kişisel verilerinizin işlenme amaçları, hukuki sebepleri, toplama yöntemi, kimlere aktarılabileceği ve KVKK'dan kaynaklanan haklarınız konusunda sizi bilgilendirmek amacıyla hazırlanmıştır.

### 2. İşlenen Kişisel Veriler

Platformumuz tarafından işlenen kişisel verileriniz aşağıdaki kategorilerde yer almaktadır:

- **Kimlik Bilgileri:** Ad, soyad, T.C. kimlik numarası
- **İletişim Bilgileri:** Adres, telefon numarası, e-posta adresi
- **Hukuki İşlem Bilgileri:** Dilekçe içerikleri, sözleşme metinleri, hukuki sorular ve yanıtlar
- **İşlem Güvenliği Bilgileri:** IP adresi, tarayıcı bilgileri, oturum bilgileri

### 3. Kişisel Verilerin İşlenme Amaçları

Kişisel verileriniz aşağıdaki amaçlar doğrultusunda işlenmektedir:

- Dilekçe üretme hizmetinin sağlanması
- Sözleşme analizi hizmetinin sağlanması
- Hukuki chatbot hizmetinin sağlanması
- Kullanıcı hesaplarının yönetilmesi
- Hizmet kalitesinin iyileştirilmesi
- Yasal yükümlülüklerin yerine getirilmesi
- Bilgi güvenliği süreçlerinin yürütülmesi

### 4. Kişisel Verilerin İşlenme Hukuki Sebepleri

Kişisel verileriniz, KVKK'nın 5. maddesinde belirtilen aşağıdaki hukuki sebeplere dayanarak işlenmektedir:

- Açık rızanızın bulunması
- Bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması
- Hukuki yükümlülüğümüzün yerine getirilmesi
- Bir hakkın tesisi, kullanılması veya korunması için veri işlemenin zorunlu olması
- İlgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla, veri sorumlusunun meşru menfaatleri için veri işlenmesinin zorunlu olması

### 5. Kişisel Verilerin Toplanma Yöntemi

Kişisel verileriniz, platformumuz üzerinden elektronik ortamda, formlar, dilekçe oluşturma araçları, sözleşme analiz araçları ve chatbot aracılığıyla toplanmaktadır.

### 6. Kişisel Verilerin Aktarılması

Kişisel verileriniz, hizmetlerimizin sağlanması amacıyla, yalnızca gerekli olduğu durumlarda ve yasal sınırlar çerçevesinde aşağıdaki alıcı gruplarına aktarılabilir:

- Yasal yükümlülüklerimiz kapsamında yetkili kamu kurum ve kuruluşları
- Hizmet alınan tedarikçiler (bulut hizmet sağlayıcıları, yazılım şirketleri)

Kişisel verileriniz, açık rızanız olmaksızın yurt dışına aktarılmamaktadır.

### 7. Kişisel Verilerin Saklanma Süresi

Kişisel verileriniz, hizmetlerimizin sağlanması amacıyla gerekli olan süre boyunca ve yasal saklama sürelerince saklanmaktadır. Bu sürelerin sona ermesinin ardından, kişisel verileriniz silinmekte, yok edilmekte veya anonim hale getirilmektedir.

### 8. İlgili Kişi Hakları

KVKK'nın 11. maddesi uyarınca, kişisel verilerinize ilişkin olarak aşağıdaki haklara sahipsiniz:

- Kişisel verilerinizin işlenip işlenmediğini öğrenme
- Kişisel verileriniz işlenmişse buna ilişkin bilgi talep etme
- Kişisel verilerinizin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme
- Yurt içinde veya yurt dışında kişisel verilerinizin aktarıldığı üçüncü kişileri bilme
- Kişisel verilerinizin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme
- KVKK'da öngörülen şartlar çerçevesinde kişisel verilerinizin silinmesini veya yok edilmesini isteme
- Kişisel verilerinizin düzeltilmesi, silinmesi veya yok edilmesi halinde bu işlemlerin kişisel verilerinizin aktarıldığı üçüncü kişilere bildirilmesini isteme
- İşlenen verilerinizin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle aleyhinize bir sonucun ortaya çıkmasına itiraz etme
- Kişisel verilerinizin kanuna aykırı olarak işlenmesi sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme

Bu haklarınızı kullanmak için, kvkk@hukukaiplatformu.com adresine e-posta göndererek veya platformumuzun "KVKK Başvuru Formu" aracılığıyla başvurabilirsiniz.

### 9. Veri Güvenliği

Kişisel verilerinizin güvenliğini sağlamak amacıyla, teknik ve idari tedbirler almaktayız. Bu kapsamda, veri tabanı güvenliği, şifreleme, erişim sınırlamaları, düzenli güvenlik değerlendirmeleri ve personel eğitimleri gibi önlemler uygulanmaktadır.

### 10. Çerezler ve Benzer Teknolojiler

Platformumuz, kullanıcı deneyimini iyileştirmek ve hizmet kalitesini artırmak amacıyla çerezler kullanmaktadır. Çerezler hakkında detaylı bilgi için "Çerez Politikası" sayfamızı ziyaret edebilirsiniz.

### 11. Değişiklikler

Bu Aydınlatma Metni, yasal düzenlemeler veya veri işleme faaliyetlerimizdeki değişiklikler doğrultusunda güncellenebilir. Güncellemeler platformumuz üzerinden duyurulacaktır.

### 12. İletişim

Kişisel verilerinizin işlenmesine ilişkin sorularınız için kvkk@hukukaiplatformu.com adresine e-posta gönderebilirsiniz.

Son güncelleme tarihi: 01.04.2025
"""
    
    with open(KVKK_DIR / "aydinlatma_metni.md", "w", encoding="utf-8") as f:
        f.write(content)

# Gizlilik politikası
def create_gizlilik_politikasi():
    content = """# GİZLİLİK POLİTİKASI

## Türkiye Hukuk AI Platformu Gizlilik Politikası

### 1. Giriş

Türkiye Hukuk AI Platformu olarak, kullanıcılarımızın gizliliğine saygı duyuyor ve kişisel verilerinizin korunmasına önem veriyoruz. Bu Gizlilik Politikası, platformumuzun kişisel verileri nasıl topladığını, kullandığını, paylaştığını ve koruduğunu açıklamaktadır.

Platformumuzu kullanarak, bu Gizlilik Politikası'nda belirtilen uygulamaları kabul etmiş sayılırsınız.

### 2. Toplanan Veriler

Platformumuz aşağıdaki kişisel verileri toplamaktadır:

#### a. Kullanıcı Tarafından Sağlanan Veriler
- Kayıt bilgileri (ad, soyad, e-posta adresi, telefon numarası)
- Profil bilgileri
- Dilekçe oluşturma, sözleşme analizi ve chatbot hizmetleri için girilen bilgiler
- İletişim formları aracılığıyla gönderilen mesajlar

#### b. Otomatik Olarak Toplanan Veriler
- IP adresi
- Tarayıcı türü ve dil ayarları
- Erişim zamanları ve tarihleri
- Tıklama verileri
- Çerezler aracılığıyla toplanan bilgiler

### 3. Verilerin Kullanımı

Topladığımız kişisel verileri aşağıdaki amaçlar için kullanmaktayız:

- Platformumuzun hizmetlerini sağlamak ve yönetmek
- Kullanıcı hesaplarını oluşturmak ve yönetmek
- Dilekçe üretme, sözleşme analizi ve hukuki chatbot hizmetlerini sunmak
- Platformumuzu geliştirmek ve iyileştirmek
- Kullanıcı deneyimini kişiselleştirmek
- Güvenlik ve doğrulama işlemlerini gerçekleştirmek
- Yasal yükümlülüklerimizi yerine getirmek
- Kullanıcı desteği sağlamak

### 4. Verilerin Paylaşımı

Kişisel verilerinizi, aşağıdaki durumlar dışında üçüncü taraflarla paylaşmamaktayız:

- Yasal zorunluluk durumunda (mahkeme kararı, yasal talep vb.)
- Platformumuzun hizmetlerini sağlamak için gerekli olan hizmet sağlayıcılarla (bulut depolama, ödeme işlemcileri vb.)
- Açık rızanızın bulunması halinde

Hizmet sağlayıcılarımızla yaptığımız sözleşmeler, kişisel verilerinizin güvenliğini ve gizliliğini korumak için gerekli önlemleri içermektedir.

### 5. Veri Güvenliği

Kişisel verilerinizin güvenliğini sağlamak için aşağıdaki teknik ve idari önlemleri almaktayız:

- SSL şifreleme teknolojisi
- Güvenli veri tabanı sistemleri
- Düzenli güvenlik denetimleri
- Erişim kontrolü ve yetkilendirme
- Personel eğitimi ve farkındalık programları
- Veri minimizasyonu ilkesinin uygulanması

### 6. Veri Saklama Süresi

Kişisel verilerinizi, hizmetlerimizin sağlanması için gerekli olan süre boyunca ve yasal saklama sürelerince saklamaktayız. Bu sürelerin sona ermesinin ardından, kişisel verileriniz silinmekte, yok edilmekte veya anonim hale getirilmektedir.

### 7. Kullanıcı Hakları

6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında, kişisel verilerinize ilişkin olarak aşağıdaki haklara sahipsiniz:

- Kişisel verilerinizin işlenip işlenmediğini öğrenme
- Kişisel verileriniz işlenmişse buna ilişkin bilgi talep etme
- Kişisel verilerinizin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme
- Kişisel verilerinizin aktarıldığı üçüncü kişileri bilme
- Kişisel verilerinizin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme
- Kişisel verilerinizin silinmesini veya yok edilmesini isteme
- İşlenen verilerinizin otomatik sistemler vasıtasıyla analiz edilmesi suretiyle aleyhinize bir sonucun ortaya çıkmasına itiraz etme
- Kişisel verilerinizin kanuna aykırı olarak işlenmesi sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme

Bu haklarınızı kullanmak için, kvkk@hukukaiplatformu.com adresine e-posta göndererek veya platformumuzun "KVKK Başvuru Formu" aracılığıyla başvurabilirsiniz.

### 8. Çerezler

Platformumuz, kullanıcı deneyimini iyileştirmek ve hizmet kalitesini artırmak amacıyla çerezler kullanmaktadır. Çerezler, tarayıcınız tarafından bilgisayarınızda saklanan küçük metin dosyalarıdır.

Kullandığımız çerez türleri:
- Zorunlu çerezler: Platformun temel işlevleri için gereklidir
- Performans çerezleri: Platformun performansını analiz etmek için kullanılır
- İşlevsellik çerezleri: Kullanıcı tercihlerini hatırlamak için kullanılır
- Hedefleme/reklam çerezleri: Kullanıcılara ilgi alanlarına göre içerik sunmak için kullanılır

Tarayıcı ayarlarınızı değiştirerek çerezleri reddedebilir veya çerez gönderildiğinde uyarı alabilirsiniz. Ancak, bazı çerezleri reddetmeniz durumunda platformumuzun bazı özellikleri düzgün çalışmayabilir.

### 9. Çocukların Gizliliği

Platformumuz, 18 yaşın altındaki kişilere yönelik değildir ve bilerek 18 yaşın altındaki kişilerden kişisel veri toplamamaktayız. 18 yaşın altındaki bir kişinin kişisel verilerini topladığımızı fark etmemiz durumunda, bu verileri derhal silmek için gerekli adımları atacağız.

### 10. Değişiklikler

Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. Politikada yapılan önemli değişiklikler, platformumuz üzerinden duyurulacak ve güncellenmiş politika yayınlanacaktır. Değişikliklerin yürürlüğe girdiği tarih, politikanın sonunda belirtilecektir.

### 11. İletişim

Gizlilik Politikası veya kişisel verilerinizin işlenmesine ilişkin sorularınız için kvkk@hukukaiplatformu.com adresine e-posta gönderebilirsiniz.

Son güncelleme tarihi: 01.04.2025
"""
    
    with open(KVKK_DIR / "gizlilik_politikasi.md", "w", encoding="utf-8") as f:
        f.write(content)

# KVKK başvuru formu
def create_kvkk_basvuru_formu():
    content = """# KVKK BAŞVURU FORMU

## Türkiye Hukuk AI Platformu Kişisel Verilerin Korunması Kanunu Başvuru Formu

6698 Sayılı Kişisel Verilerin Korunması Kanunu ("KVKK") kapsamında ilgili kişi olarak tanımlanan kişisel veri sahiplerine, KVKK'nın 11. maddesinde kişisel verilerinin işlenmesine ilişkin belirli haklar tanınmıştır.

KVKK'nın 13. maddesinin 1. fıkrası uyarınca, veri sorumlusu olan Platformumuza bu haklara ilişkin olarak yapılacak başvuruların yazılı olarak veya Kişisel Verilerin Korunması Kurulu ("Kurul") tarafından belirlenen diğer yöntemlerle tarafımıza iletilmesi gerekmektedir.

Bu formun ve talebinizin niteliğine göre sizlerden istenen bilgi ve belgelerin eksiksiz ve doğru olarak tarafımıza ulaştırılması gerekmektedir. İstenilen bilgi ve belgelerin gereği gibi sağlanmaması durumunda, Platformumuz tarafından talebinize istinaden yapılacak araştırmaların tam ve nitelikli şekilde yürütülmesinde aksaklıklar yaşanabilecektir. Bu durumda, Platformumuz kanuni haklarını saklı tuttuğunu beyan eder. Bu nedenle, başvurunuzun talebinizin niteliğine göre eksiksiz ve istenilen bilgileri ve belgeleri içerecek şekilde gönderilmesi gerekmektedir.

### BAŞVURU SAHİBİNİN İLETİŞİM BİLGİLERİ

| Bilgi | Açıklama |
|-------|----------|
| Ad Soyad | |
| T.C. Kimlik Numarası | |
| Telefon Numarası | |
| E-posta | |
| Adres | |

### LÜTFEN PLATFORMUMUZ İLE OLAN İLİŞKİNİZİ BELİRTİNİZ

☐ Kullanıcı  
☐ Çalışan  
☐ Eski Çalışan  
☐ İş Ortağı  
☐ Diğer: ...............

### KVKK KAPSAMINDAKİ TALEBİNİZİ DETAYLI OLARAK BELİRTİNİZ

...............................................................................
...............................................................................
...............................................................................
...............................................................................
...............................................................................

### LÜTFEN BAŞVURUNUZA VERECEĞİMİZ YANITIN TARAFINIZA BİLDİRİLME YÖNTEMİNİ SEÇİNİZ

☐ Adresime gönderilmesini istiyorum.  
☐ E-posta adresime gönderilmesini istiyorum.  
☐ Elden teslim almak istiyorum.

### AÇIKLAMA

Bu formu doldurarak, imzalayarak ve aşağıdaki iletişim kanallarımızdan birisi aracılığıyla Platformumuza ileterek başvurunuzu yapabilirsiniz:

1. **E-posta yoluyla:** kvkk@hukukaiplatformu.com adresine, konu kısmına "Kişisel Verilerin Korunması Kanunu Bilgi Talebi" yazarak
2. **Posta yoluyla:** [Adres] adresine, zarfın üzerine "Kişisel Verilerin Korunması Kanunu Kapsamında Bilgi Talebi" yazarak

Tarafımıza iletilmiş olan başvurularınız KVKK'nın 13. maddesinin 2. fıkrası gereğince, talebin niteliğine göre talebinizin bizlere ulaştığı tarihten itibaren 30 (otuz) gün içinde yanıtlandırılacaktır. Yanıtlarımız KVKK'nın 13. maddesi hükmü gereğince yazılı veya elektronik ortamdan tarafınıza ulaştırılacaktır.

### BAŞVURU SAHİBİ BEYANI

KVKK uyarınca yapmış olduğum bilgi edinme başvurusunun, yukarıda belirttiğim talep/talepler çerçevesinde değerlendirilerek sonuçlandırılmasını rica eder, işbu başvuruda tarafınıza sağlamış olduğum bilgi ve belgelerin doğru, güncel ve şahsıma ait olduğunu kabul, beyan ve taahhüt ederim.

| Bilgi | Açıklama |
|-------|----------|
| Başvuru Tarihi | |
| Başvuru Sahibi Adı Soyadı | |
| İmza | |
"""
    
    with open(KVKK_DIR / "kvkk_basvuru_formu.md", "w", encoding="utf-8") as f:
        f.write(content)

# Veri işleme politikası
def create_veri_isleme_politikasi():
    content = """# VERİ İŞLEME POLİTİKASI

## Türkiye Hukuk AI Platformu Kişisel Verilerin İşlenmesi ve Korunması Politikası

### 1. Amaç

Bu Politika'nın amacı, Türkiye Hukuk AI Platformu tarafından kişisel verilerin işlenmesinde benimsenen ilkeleri ortaya koymak ve KVKK'nın 10. maddesi kapsamında veri sorumluları tarafından yerine getirilmesi gereken aydınlatma yükümlülüğü ile 12. maddesi kapsamında veri sorumluları tarafından alınması gereken teknik ve idari tedbirlerin uygulanması için izlenecek yöntemleri belirlemektir.

### 2. Kapsam

Bu Politika; Platformumuzun kullanıcıları, çalışanları, çalışan adayları, hizmet sağlayıcıları ve diğer üçüncü kişilere ait kişisel verilerin işlenmesine ilişkin tüm faaliyetleri kapsar.

### 3. Tanımlar

**Açık Rıza:** Belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan rıza.

**İlgili Kişi:** Kişisel verisi işlenen gerçek kişi.

**Kişisel Veri:** Kimliği belirli veya belirlenebilir gerçek kişiye ilişkin her türlü bilgi.

**Kişisel Verilerin İşlenmesi:** Kişisel verilerin tamamen veya kısmen otomatik olan ya da herhangi bir veri kayıt sisteminin parçası olmak kaydıyla otomatik olmayan yollarla elde edilmesi, kaydedilmesi, depolanması, muhafaza edilmesi, değiştirilmesi, yeniden düzenlenmesi, açıklanması, aktarılması, devralınması, elde edilebilir hâle getirilmesi, sınıflandırılması ya da kullanılmasının engellenmesi gibi veriler üzerinde gerçekleştirilen her türlü işlem.

**Özel Nitelikli Kişisel Veri:** Kişilerin ırkı, etnik kökeni, siyasi düşüncesi, felsefi inancı, dini, mezhebi veya diğer inançları, kılık ve kıyafeti, dernek, vakıf ya da sendika üyeliği, sağlığı, cinsel hayatı, ceza mahkûmiyeti ve güvenlik tedbirleriyle ilgili verileri ile biyometrik ve genetik verileri.

**Veri İşleyen:** Veri sorumlusunun verdiği yetkiye dayanarak onun adına kişisel verileri işleyen gerçek veya tüzel kişi.

**Veri Sorumlusu:** Kişisel verilerin işleme amaçlarını ve vasıtalarını belirleyen, veri kayıt sisteminin kurulmasından ve yönetilmesinden sorumlu olan gerçek veya tüzel kişi.

### 4. Kişisel Verilerin İşlenmesinde Benimsenen Temel İlkeler

Platformumuz, kişisel verilerin işlenmesinde aşağıdaki ilkeleri benimsemektedir:

#### a. Hukuka ve Dürüstlük Kurallarına Uygun Olma
Platformumuz, kişisel verilerin işlenmesinde hukuksal düzenlemelerle getirilen ilkeler ile genel güven ve dürüstlük kuralına uygun hareket etmektedir.

#### b. Doğru ve Gerektiğinde Güncel Olma
Platformumuz, kişisel verilerin işlendiği süre boyunca doğru ve güncel olması için gerekli önlemleri almakta ve belirli sürelerle kişisel verilerin doğruluğunun ve güncelliğinin sağlanmasına ilişkin gerekli mekanizmaları kurmaktadır.

#### c. Belirli, Açık ve Meşru Amaçlar İçin İşlenme
Platformumuz, kişisel verilerin işlenme amaçlarını açıkça ortaya koymakta ve bu amaçların meşru olduğunu belirtmektedir.

#### d. İşlendikleri Amaçla Bağlantılı, Sınırlı ve Ölçülü Olma
Platformumuz, kişisel verileri belirlenen amaçların gerçekleştirilebilmesine elverişli bir biçimde işlemekte ve amacın gerçekleştirilmesiyle ilgili olmayan veya ihtiyaç duyulmayan kişisel verilerin işlenmesinden kaçınmaktadır.

#### e. İlgili Mevzuatta Öngörülen veya İşlendikleri Amaç İçin Gerekli Olan Süre Kadar Muhafaza Edilme
Platformumuz, kişisel verileri ancak ilgili mevzuatta belirtildiği veya işlendikleri amaç için gerekli olan süre kadar muhafaza etmektedir. Bu kapsamda, Platformumuz öncelikle ilgili mevzuatta kişisel verilerin saklanması için bir süre öngörülüp öngörülmediğini tespit etmekte, bir süre belirlenmişse bu süreye uygun davranmakta, bir süre belirlenmemişse kişisel verileri işlendikleri amaç için gerekli olan süre kadar saklamaktadır.

### 5. Kişisel Verilerin İşlenme Şartları

Platformumuz, kişisel verileri aşağıdaki şartlardan en az birine dayanarak işlemektedir:

- İlgili kişinin açık rızasının bulunması
- Kanunlarda açıkça öngörülmesi
- Fiili imkânsızlık nedeniyle rızasını açıklayamayacak durumda bulunan veya rızasına hukuki geçerlilik tanınmayan kişinin kendisinin ya da bir başkasının hayatı veya beden bütünlüğünün korunması için zorunlu olması
- Bir sözleşmenin kurulması veya ifasıyla doğrudan doğruya ilgili olması kaydıyla, sözleşmenin taraflarına ait kişisel verilerin işlenmesinin gerekli olması
- Veri sorumlusunun hukuki yükümlülüğünü yerine getirebilmesi için zorunlu olması
- İlgili kişinin kendisi tarafından alenileştirilmiş olması
- Bir hakkın tesisi, kullanılması veya korunması için veri işlemenin zorunlu olması
- İlgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla, veri sorumlusunun meşru menfaatleri için veri işlenmesinin zorunlu olması

### 6. Özel Nitelikli Kişisel Verilerin İşlenme Şartları

Platformumuz, özel nitelikli kişisel verileri aşağıdaki şartlara uygun olarak işlemektedir:

- İlgili kişinin açık rızasının bulunması
- Sağlık ve cinsel hayat dışındaki özel nitelikli kişisel veriler için kanunlarda açıkça öngörülmesi
- Sağlık ve cinsel hayata ilişkin kişisel veriler ise ancak kamu sağlığının korunması, koruyucu hekimlik, tıbbî teşhis, tedavi ve bakım hizmetlerinin yürütülmesi, sağlık hizmetleri ile finansmanının planlanması ve yönetimi amacıyla, sır saklama yükümlülüğü altında bulunan kişiler veya yetkili kurum ve kuruluşlar tarafından işlenmesi

### 7. Kişisel Verilerin Güvenliğinin Sağlanması

Platformumuz, kişisel verilerin hukuka aykırı olarak işlenmesini ve erişilmesini önlemek, kişisel verilerin muhafazasını sağlamak amacıyla uygun güvenlik düzeyini temin etmeye yönelik gerekli her türlü teknik ve idari tedbirleri almaktadır.

#### a. Teknik Tedbirler
- Ağ güvenliği ve uygulama güvenliği sağlanmaktadır.
- Bilgi teknolojileri sistemleri tedarik, geliştirme ve bakımı kapsamındaki güvenlik önlemleri alınmaktadır.
- Erişim logları düzenli olarak tutulmaktadır.
- Güncel anti-virüs sistemleri kullanılmaktadır.
- Güvenlik duvarları kullanılmaktadır.
- Kişisel veri içeren fiziksel ortamlara giriş çıkışlarla ilgili gerekli güvenlik önlemleri alınmaktadır.
- Kişisel veri içeren ortamların güvenliği sağlanmaktadır.
- Kişisel veriler yedeklenmekte ve yedeklenen kişisel verilerin güvenliği de sağlanmaktadır.
- Kullanıcı hesap yönetimi ve yetki kontrol sistemi uygulanmakta olup bunların takibi de yapılmaktadır.
- Log kayıtları kullanıcı müdahalesi olmayacak şekilde tutulmaktadır.
- Saldırı tespit ve önleme sistemleri kullanılmaktadır.
- Sızma testi uygulanmaktadır.
- Şifreleme yapılmaktadır.
- Veri kaybı önleme yazılımları kullanılmaktadır.

#### b. İdari Tedbirler
- Çalışanlar için veri güvenliği hükümleri içeren disiplin düzenlemeleri mevcuttur.
- Çalışanlar için veri güvenliği konusunda belli aralıklarla eğitim ve farkındalık çalışmaları yapılmaktadır.
- Erişim, bilgi güvenliği, kullanım, saklama ve imha konularında kurumsal politikalar hazırlanmış ve uygulamaya başlanmıştır.
- Gizlilik taahhütnameleri yapılmaktadır.
- İmzalanan sözleşmeler veri güvenliği hükümleri içermektedir.
- Kişisel veri güvenliği politika ve prosedürleri belirlenmiştir.
- Kişisel veri güvenliği sorunları hızlı bir şekilde raporlanmaktadır.
- Kişisel veri güvenliğinin takibi yapılmaktadır.
- Kişisel veri içeren fiziksel ortamların dış risklere (yangın, sel vb.) karşı güvenliği sağlanmaktadır.
- Kişisel veri içeren ortamların güvenliği sağlanmaktadır.
- Kişisel veriler mümkün olduğunca azaltılmaktadır.
- Kurum içi periyodik ve/veya rastgele denetimler yapılmakta ve yaptırılmaktadır.
- Mevcut risk ve tehditler belirlenmiştir.
- Özel nitelikli kişisel veri güvenliğine yönelik protokol ve prosedürler belirlenmiş ve uygulanmaktadır.
- Veri işleyen hizmet sağlayıcılarının veri güvenliği konusunda belli aralıklarla denetimi sağlanmaktadır.
- Veri işleyen hizmet sağlayıcılarının, veri güvenliği konusunda farkındalığı sağlanmaktadır.

### 8. Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi

Platformumuz, Türk Ceza Kanunu'nun 138. maddesinde ve KVKK'nın 7. maddesinde düzenlendiği üzere ilgili kanun hükümlerine uygun olarak işlenmiş olmasına rağmen, işlenmesini gerektiren sebeplerin ortadan kalkması hâlinde kişisel verileri re'sen veya ilgili kişinin talebi üzerine siler, yok eder veya anonim hâle getirir.

### 9. İlgili Kişilerin Hakları

KVKK'nın 11. maddesi uyarınca, kişisel verileri işlenen ilgili kişiler aşağıdaki haklara sahiptir:

- Kişisel veri işlenip işlenmediğini öğrenme
- Kişisel verileri işlenmişse buna ilişkin bilgi talep etme
- Kişisel verilerin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme
- Yurt içinde veya yurt dışında kişisel verilerin aktarıldığı üçüncü kişileri bilme
- Kişisel verilerin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme
- KVKK'nın 7. maddesinde öngörülen şartlar çerçevesinde kişisel verilerin silinmesini veya yok edilmesini isteme
- Kişisel verilerin düzeltilmesi, silinmesi veya yok edilmesi halinde bu işlemlerin kişisel verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme
- İşlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle kişinin kendisi aleyhine bir sonucun ortaya çıkmasına itiraz etme
- Kişisel verilerin kanuna aykırı olarak işlenmesi sebebiyle zarara uğraması hâlinde zararın giderilmesini talep etme

### 10. Veri Sorumlusuna Başvuru

İlgili kişiler, KVKK'nın 11. maddesinde belirtilen hakları kapsamında taleplerini, yazılı olarak veya kayıtlı elektronik posta (KEP) adresi, güvenli elektronik imza, mobil imza ya da ilgili kişi tarafından Platformumuza daha önce bildirilen ve Platformumuzun sisteminde kayıtlı bulunan elektronik posta adresini kullanmak suretiyle veya başvuru amacına yönelik geliştirilmiş bir yazılım ya da uygulama vasıtasıyla Platformumuza iletebilir.

İlgili kişinin başvurusunda;
- Ad, soyad ve başvuru yazılı ise imza,
- Türkiye Cumhuriyeti vatandaşları için T.C. kimlik numarası, yabancılar için uyruğu, pasaport numarası veya varsa kimlik numarası,
- Tebligata esas yerleşim yeri veya iş yeri adresi,
- Varsa bildirime esas elektronik posta adresi, telefon ve faks numarası,
- Talep konusu,
bulunması zorunludur.

Platformumuz, başvuruda yer alan talepleri, talebin niteliğine göre en kısa sürede ve en geç otuz gün içinde ücretsiz olarak sonuçlandırır. Ancak, işlemin ayrıca bir maliyet gerektirmesi hâlinde, Kurulca belirlenen tarifedeki ücret alınabilir.

### 11. Politika'nın Yürürlüğü ve Değişiklikler

Bu Politika, Platformumuz tarafından yayınlandığı tarihte yürürlüğe girer. Platformumuz, bu Politika'yı gerektiğinde güncelleme ve değiştirme hakkını saklı tutar. Politika'nın güncel versiyonu Platformumuzun web sitesinde yayınlanır.

Son güncelleme tarihi: 01.04.2025
"""
    
    with open(KVKK_DIR / "veri_isleme_politikasi.md", "w", encoding="utf-8") as f:
        f.write(content)

# Çerez politikası
def create_cerez_politikasi():
    content = """# ÇEREZ POLİTİKASI

## Türkiye Hukuk AI Platformu Çerez Politikası

### 1. Çerez Nedir?

Çerezler, ziyaret ettiğiniz internet siteleri tarafından tarayıcılar aracılığıyla bilgisayarınıza veya mobil cihazınıza kaydedilen küçük metin dosyalarıdır. Bu dosyalarda IP adresiniz, oturum bilgileriniz, eriştiğiniz sayfalar, kullandığınız hizmetler gibi bilgiler saklanır. Bu bilgilerin ne kadar süre tutulacağına ilgili çerez türüne bağlı olarak değişir.

### 2. Çerez Türleri

#### a. Zorunlu Çerezler
Bu çerezler, web sitesinin düzgün bir şekilde çalışabilmesi için gerekli olan çerezlerdir. Bu çerezler olmadan, web sitesi veya web sitesinin bazı bölümleri düzgün çalışmayabilir. Bu çerezler, oturum açma bilgilerinizi hatırlama, site içerisindeki hareketlerinizi güvence altına alma gibi amaçlarla kullanılır.

#### b. Performans Çerezleri
Bu çerezler, web sitesinin performansını ölçmek ve iyileştirmek için kullanılır. Ziyaretçilerin web sitesini nasıl kullandığı, hangi sayfaların en çok ziyaret edildiği gibi bilgileri toplar. Bu çerezler, ziyaretçilerin kimliklerini tanımlamaz, toplanan tüm bilgiler anonim olarak saklanır.

#### c. İşlevsellik Çerezleri
Bu çerezler, web sitesinin daha işlevsel ve kişiselleştirilmiş bir deneyim sunmasını sağlar. Bu çerezler, dil tercihinizi veya giriş bilgilerinizi hatırlama gibi işlevler için kullanılabilir.

#### d. Hedefleme/Reklam Çerezleri
Bu çerezler, size ve ilgi alanlarınıza yakın olan içerikleri sunmak amacıyla kullanılır. Bu çerezler, reklam kampanyalarının etkinliğini ölçmek veya bir reklamın kaç kere görüntülendiğini belirlemek için de kullanılabilir.

### 3. Platformumuzda Kullanılan Çerezler

| Çerez Adı | Çerez Türü | Amacı | Saklama Süresi |
|-----------|------------|-------|----------------|
| session_id | Zorunlu | Kullanıcı oturumunu yönetmek için | Oturum süresi |
| auth_token | Zorunlu | Kullanıcı kimlik doğrulaması için | 30 gün |
| language | İşlevsellik | Kullanıcının dil tercihini hatırlamak için | 1 yıl |
| theme | İşlevsellik | Kullanıcının tema tercihini hatırlamak için | 1 yıl |
| _ga | Performans | Google Analytics tarafından kullanıcı ziyaretlerini analiz etmek için | 2 yıl |
| _gid | Performans | Google Analytics tarafından kullanıcı ziyaretlerini analiz etmek için | 24 saat |

### 4. Çerezlerin Kontrolü

Tarayıcınızın ayarlarını değiştirerek çerezlere ilişkin tercihlerinizi kişiselleştirme imkanına sahipsiniz. Tarayıcı ayarlarınızı nasıl değiştireceğinize ilişkin detaylı bilgi için aşağıdaki linklerden yararlanabilirsiniz:

- [Google Chrome](https://support.google.com/chrome/answer/95647)
- [Mozilla Firefox](https://support.mozilla.org/tr/kb/cerezleri-silme-web-sitelerinin-bilgilerini-kaldirma)
- [Safari](https://support.apple.com/tr-tr/guide/safari/sfri11471/mac)
- [Internet Explorer](https://support.microsoft.com/tr-tr/help/17442/windows-internet-explorer-delete-manage-cookies)
- [Microsoft Edge](https://support.microsoft.com/tr-tr/microsoft-edge/microsoft-edge-de-%C3%A7erezleri-silme-63947406-40ac-c3b8-57b9-2a946a29ae09)

### 5. Çerezlerin Kullanımını Reddetme

Çerezlerin kullanımını reddetme hakkınıza sahipsiniz. Ancak, çerezleri reddetmeniz halinde, web sitesinin tüm işlevlerinden yararlanamayabilirsiniz.

### 6. Değişiklikler

Platformumuz, Çerez Politikası'nı periyodik olarak güncelleyebilir. Yapılan değişiklikler, Platformumuzun web sitesinde yayınlanacaktır. Çerez Politikası'nın en güncel halini görmek için lütfen web sitemizi düzenli olarak ziyaret ediniz.

### 7. İletişim

Çerez Politikası ile ilgili sorularınız için kvkk@hukukaiplatformu.com adresine e-posta gönderebilirsiniz.

Son güncelleme tarihi: 01.04.2025
"""
    
    with open(KVKK_DIR / "cerez_politikasi.md", "w", encoding="utf-8") as f:
        f.write(content)

# Ana fonksiyon
def main():
    print("KVKK uyumluluk metinleri oluşturuluyor...")
    create_aydinlatma_metni()
    create_gizlilik_politikasi()
    create_kvkk_basvuru_formu()
    create_veri_isleme_politikasi()
    create_cerez_politikasi()
    print("KVKK uyumluluk metinleri başarıyla oluşturuldu.")

if __name__ == "__main__":
    main()
