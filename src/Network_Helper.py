import os
import subprocess

def menu():
    print("-" * 30)
    print("NETWORK HELPER )
    print("-" * 30)
    print("1. Ping Testi Yap")
    print("2. IP Adresini Göster")
    print("3. DNS Ayarlarını Değiştir (Google DNS)")
    print("4. Çıkış")
    
    secim = input("Seçiminiz (1-4): ")
    return secim

def ping_test():
    hedef = input("Ping atılacak adres (örn: google.com): ")
    os.system(f"ping -c 4 {hedef}")

def ip_goster():
    print("\n--- IP BİLGİLERİ ---")
    os.system("ip a")

def dns_degistir():
    print("DNS değiştiriliyor... (Yönetici şifresi gerekebilir)")
    
    os.system('sudo nmcli connection modify "netplan-enp0s3" ipv4.dns "8.8.8.8 8.8.4.4"')
    
    os.system('sudo nmcli connection up "netplan-enp0s3"')
    print("DNS Google DNS (8.8.8.8) olarak ayarlandı!")

while True:
    kullanici_secimi = menu()
    
    if kullanici_secimi == '1':
        ping_test()
    elif kullanici_secimi == '2':
        ip_goster()
    elif kullanici_secimi == '3':
        dns_degistir()
    elif kullanici_secimi == '4':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")
    
    input("\nDevam etmek için Enter'a bas...")
