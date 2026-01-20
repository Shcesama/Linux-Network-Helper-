# QLineSec 
Linux Network Helper

 Bu proje, Linux terminali üzerinden sık kullanılan ağ işlemlerini otomatize ederek kullanıcıya hız kazandırmayı amaçlar.

 Özellikler
Bu araç aşağıdaki işlevleri yerine getirir:
- Ping Testi: Google sunucularına paket göndererek internet bağlantı durumunu kontrol eder.
- IP Sorgulama: Sistemin mevcut IP ve ağ arayüzü bilgilerini listeler.
- DNS Yapılandırması: Sistem DNS ayarlarını otomatik olarak Google DNS (8.8.8.8) sunucularına yönlendirir.
- Kullanıcı Arayüzü: Basit ve anlaşılır menü yapısı ile kolay kullanım sağlar.

 Gereksinimler
- Ubuntu (veya Debian tabanlı Linux dağıtımları)
- Python 3.x
- Network Manager (`nmcli`)
- Yönetici yetkileri (`sudo` - DNS değişimi için gereklidir)

 Kurulum ve Kullanım
Projeyi çalıştırmak için terminali açın ve kaynak kodun olduğu dizine giderek şu komutu yazın:

```bash
python3 src/Network_Helper.py

Bu proje MIT lisansı ile lisanslanmıştır.

