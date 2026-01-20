# Research Result for copilot
Teknik Araştırma Raporu: Linux Network Helper
1. Linux’ta Ağ Yönetimi Neden Terminalden Yapılır? (GUI vs CLI)
CLI (Command Line Interface), Linux sistemlerinde ağ yönetimi için tercih edilen yöntemdir. Bunun başlıca sebepleri:

Esneklik ve Güç: CLI, GUI’nin sunduğu sınırlı seçeneklerin ötesinde, sistemin tüm konfigürasyon parametrelerine erişim sağlar.

Otomasyon: Script yazımı ve otomasyon süreçleri CLI üzerinden kolaylıkla gerçekleştirilebilir. Bu, özellikle sistem yöneticileri ve DevOps mühendisleri için kritik öneme sahiptir.

Kaynak Verimliliği: CLI, grafiksel arayüzlere kıyasla daha az sistem kaynağı tüketir. Sunucu ortamlarında GUI genellikle bulunmaz, bu nedenle terminal üzerinden yönetim standarttır.

Uzaktan Yönetim: SSH gibi protokollerle CLI üzerinden ağ yapılandırması yapılabilir. GUI’nin uzaktan kullanımı daha karmaşık ve güvenlik açısından riskli olabilir.

Sonuç olarak, CLI Linux ekosisteminde standart ve güvenilir ağ yönetim aracı olarak kabul edilmektedir.

2. Python’un os ve subprocess Kütüphaneleri ile Shell Komutlarının Çalıştırılması
os Kütüphanesi:

os.system("komut") fonksiyonu ile doğrudan shell komutları çalıştırılabilir.

Basit komutlar için uygundur, ancak çıktı kontrolü sınırlıdır.

subprocess Kütüphanesi:

Daha gelişmiş bir yöntemdir. subprocess.run(), subprocess.Popen() gibi fonksiyonlarla komutların çıktısı, hata mesajları ve dönüş kodları ayrıntılı şekilde yönetilebilir.

Örnek kullanım:

python
import subprocess
result = subprocess.run(["nmcli", "device", "status"], capture_output=True, text=True)
print(result.stdout)
Bu yöntem, Linux Network Helper gibi otomasyon projelerinde tercih edilir çünkü hata yönetimi ve çıktı analizi yapılabilir.

3. nmcli (Network Manager CLI) Aracı
Tanım: nmcli, NetworkManager servisinin komut satırı arayüzüdür. Ağ bağlantılarını, IP yapılandırmalarını, DNS ayarlarını ve VPN bağlantılarını yönetmek için kullanılır.

Avantajları:

Dinamik Yönetim: Netplan dosyalarını elle düzenlemek yerine, nmcli ile anlık değişiklikler yapılabilir.

Hata Riskini Azaltma: Manuel dosya düzenlemelerinde yapılan yazım hataları ağın çökmesine neden olabilir. nmcli bu riski minimize eder.

Otomasyon Uygunluğu: Python scriptleri ile kolayca entegre edilebilir. Örneğin:

python
subprocess.run(["nmcli", "con", "mod", "Wired connection 1", "ipv4.dns", "8.8.8.8"])
subprocess.run(["nmcli", "con", "up", "Wired connection 1"])
Standartlaştırma: Ubuntu ve diğer Linux dağıtımlarında yaygın olarak desteklenir.

4. Google DNS (8.8.8.8) Nedir ve Neden Tercih Edilir?
Google DNS:

IP adresi: 8.8.8.8 ve 8.8.4.4.

Google tarafından sağlanan ücretsiz ve halka açık DNS servisidir.

Tercih Edilme Sebepleri:

Hız: Çoğu durumda ISS (İnternet Servis Sağlayıcı) DNS sunucularına kıyasla daha hızlı çözümleme sağlar.

Güvenilirlik: Google’ın global altyapısı sayesinde yüksek erişilebilirlik ve düşük kesinti oranı sunar.

Güncel Kayıtlar: DNS kayıtlarının hızlı güncellenmesi, özellikle dinamik web servisleri için avantaj sağlar.

Evrensel Kullanım: Dünya çapında standart bir çözüm olarak kabul edilir, bu nedenle scriptlerde ve otomasyon projelerinde yaygın olarak kullanılır.
