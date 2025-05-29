import os
import re
import subprocess
import requests
import art
import colorama
from colorama import Fore, Style
import time
import socket

art = art.text2art("sysPeek", font='Georgi16')

colorama.init(autoreset=True)
def get_time():
    simdi = time.localtime()
    return time.strftime("%H:%M:%S", simdi)
def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json()['ip']
        return ip
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Hata: {e}" + Style.RESET_ALL)
        return None
    

def track():
    ip = get_ip()
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'fail':
            print(Fore.RED + f"[!] Hata: {data['message']}" + Style.RESET_ALL)
            return
    print(Fore.RED + f'[-]  NETWORK BİLGİLERİ: ' + Style.RESET_ALL)
    print(Fore.RED + f'[{get_time()}] [-]  İP Adresiniz:: ' + ip + Style.RESET_ALL)
    print(Fore.YELLOW + f'[{get_time()}] [-] *] İnternet Servis Sağlayıcınız: ' + data['isp'] + Style.RESET_ALL)
    print(Fore.YELLOW + f'[{get_time()}] [-] *] Ülke: ' + data['country'] + Style.RESET_ALL)
    print(Fore.YELLOW + f'[{get_time()}] [-] *] Şehir: ' + data['city'] + Style.RESET_ALL)
    print(Fore.YELLOW + f'[{get_time()}] [-] *] Bölge: ' + data['regionName'] + Style.RESET_ALL)
    print(Fore.YELLOW + f'[{get_time()}] [-] *] Zaman Dilimi: ' + data['timezone'] + Style.RESET_ALL)
    print(Fore.RED + f'[{get_time()}] [-] *] WHO İS' + data['isp'] + Style.RESET_ALL)
    print(Fore.RED + f'[-]  WHOIS: ' + Style.RESET_ALL)
    os.system(f'whois {ip}')
def system_info():
    print(Fore.RED + f'[-]  SİSTEM BİLGİLERİ: ' + Style.RESET_ALL)
    os.system('systeminfo')
    os.system("ipconfig /all")
def dns_info():
    print(Fore.RED + f'[-]  DNS BİLGİLERİ: ' + Style.RESET_ALL)
    os.system('nslookup')
def wifi_info():
    print(Fore.RED + f'[-]  WIFI BİLGİLERİ: ' + Style.RESET_ALL)
    os.system('netsh wlan show profile')
def port_scan():
    print(Fore.RED + f'[-]  PORT SCAN: ' + Style.RESET_ALL)
    ip = input(Fore.YELLOW + '[*] Sorgulanıyor..: ' + Style.RESET_ALL)
    os.system(f'nmap {ip}')
def ping_test():
    target = input("Ping atılacak IP veya site: ")
    command = f"ping -n 4 {target}"
    os.system(command)
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
def show_macs():
    print(Fore.RED + f'[-]  MAC ADRESLERİ: ' + Style.RESET_ALL)
    os.system('getmac')
def start():
    while True:
        print(Fore.CYAN + art + Style.RESET_ALL)
        print(Fore.GREEN + "[*] @shenzhe tarafından geliştirilmiştir." + Style.RESET_ALL)
        print(Fore.GREEN + "[*] SB HUB" + Style.RESET_ALL)
        print(Fore.GREEN + "[*] V1.0" + Style.RESET_ALL)
        print(Fore.RED + "[*] MENÜ" + Style.RESET_ALL)
        print(Fore.YELLOW + "[1] İP Adresi Takibi" + Style.RESET_ALL)
        print(Fore.YELLOW + "[2] Sistem Bilgileri" + Style.RESET_ALL)
        print(Fore.YELLOW + "[3] DNS Bilgileri" + Style.RESET_ALL)
        print(Fore.YELLOW + "[4] Wifi Bilgileri" + Style.RESET_ALL)
        print(Fore.YELLOW + "[5] Port Tarayıcı" + Style.RESET_ALL)
        print(Fore.YELLOW + "[6] Ping Testi" + Style.RESET_ALL)
        print(Fore.YELLOW + "[7] İnternet Kontrolü" + Style.RESET_ALL)
        print(Fore.YELLOW + "[8] MAC Adresleri" + Style.RESET_ALL)
        print(Fore.YELLOW + "[9] Çıkış" + Style.RESET_ALL)
        choice = input(Fore.YELLOW + '[*] Seçiminizi yapınız: ' + Style.RESET_ALL)
        if choice == '1':
            track()
        elif choice == '2':
            system_info()
        elif choice == '3':
            dns_info()
        elif choice == '4':
            wifi_info()
        elif choice == '5':
            port_scan()
        elif choice == '6':
            ping_test()
        elif choice == '7':
            if check_internet():
                print(Fore.GREEN + "[*] İnternet bağlantınız var." + Style.RESET_ALL)
            else:
                print(Fore.RED + "[!] İnternet bağlantınız yok." + Style.RESET_ALL)
        elif choice == '8':
            show_macs()
        elif choice == '9':
            print(Fore.RED + '[*] Çıkılıyor...' + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + '[!] Geçersiz seçim. Lütfen tekrar deneyin.' + Style.RESET_ALL)
        input(Fore.YELLOW + "\nDevam etmek için Enter'a basınız..." + Style.RESET_ALL)
start()