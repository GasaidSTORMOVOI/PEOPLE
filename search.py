import requests
import random
import re
from bs4 import BeautifulSoup
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
from googlesearch import search
import sys
import socket
import urllib.request
import urllib.error
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import fake_useragent
from fake_useragent import UserAgent
from pystyle import Colors, Colorate
import requests
import sys
import subprocess
import requests
from colorama import init, Fore
import time
import whois
from urllib.parse import quote_plus
import phonenumbers
import time
from colorama import init, Fore
import os
from colorama import Fore, Style

def searchbd():
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]

    def get_random_user_agent():
        return random.choice(USER_AGENTS)

    def is_valid_value(value):
        return not re.match(r'^[a-f0-9]{32,}$', value.strip())

    def extract_emails(text):
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        emails = [email for email in emails if "email protected" not in email.lower()]
        return list(set(emails))

    def search_info(query):
        query_encoded = quote_plus(query)
        headers = {'User-Agent': get_random_user_agent()}
        reveng_url = f'https://reveng.ee/search?q={query_encoded}&per_page=100'
        results = []

        reveng_response = requests.get(reveng_url, headers=headers)
        if reveng_response.status_code == 200:
            soup = BeautifulSoup(reveng_response.text, 'html.parser')
            for link in set(a['href'] for a in soup.find_all('a', href=True) if 'entity' in a['href']):
                page_response = requests.get(f'https://reveng.ee{link}', headers=headers)
                if page_response.status_code == 200:
                    soup = BeautifulSoup(page_response.text, 'html.parser')
                    entity = soup.find('div', class_='bg-body rounded shadow-sm p-3 mb-2 entity-info')
                    if entity:
                        result = {'База данных': 'FELIXSOFTOOL'}
                        name = entity.find('span', class_='entity-prop-value')
                        if name:
                            result['Имя'] = name.get_text(strip=True)
                        emails = extract_emails(page_response.text)
                        if emails:
                            result['E-mail'] = ", ".join(emails)
                        for row in entity.find_all('tr', class_='property-row'):
                            prop_name = row.find('td', class_='property-name').get_text(strip=True)
                            prop_value = row.find('td', class_='property-values').get_text(strip=True)
                            if is_valid_value(prop_value):
                                result[prop_name] = prop_value
                        results.append(result)

        return results

    def format_results(results, duration):
        if not results:
            return f"➤ Информация не найдена\nПоиск занял: {duration:.2f} секунд"
        
        formatted_text = f"➤ Информация найдена\nПоиск занял: {duration:.2f} секунд\n\n"
        for result in results:
            formatted_text += f"➤ База данных: {result['База данных']}\n"
            for key, value in result.items():
                if key != 'База данных':
                    formatted_text += f"   ➤ {key}: {value}\n"
            formatted_text += "\n"
        return formatted_text

    query = input("➤ Введите данные для поиска: ")
    if not query.strip():
        print("➤ Пожалуйста, введите корректные данные.")
    else:
        print("➤ Поиск... Пожалуйста, подождите.")
        start_time = time.time()
        results = search_info(query)
        duration = time.time() - start_time
        print(format_results(results, duration))

    input("\n➤ Нажмите Enter для продолжения...")
    exit()

def main():
    searchbd()

if __name__ == "__main__":
    main()
                   
init(autoreset=True)

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data


def get_ip_type(ip_address):
    url = f"https://ipwho.is/{ip_address}"
    response = requests.get(url)
    ip_info = response.json()
    return ip_info


def color_text(text, color=Fore.WHITE):
    return f"{color}{text}{Fore.WHITE}"


def ipsearch(ip_address):
    ip_info = get_ip_info(ip_address)
    print(color_text("╔" + "─" * 65 + "╗"))
    print(color_text("◆ ОБЩАЯ ИНФОРМАЦИЯ:"))

    if 'ip' in ip_info:
        print(color_text(f"◆ [+] IP-адрес: {ip_info['ip']}"))
        ip_type_info = get_ip_type(ip_address)
    else:
        print(color_text("◆ [-] IP-адрес недоступен"))

    print(color_text(f"◆ [+] Город: {ip_info.get('city', 'недоступен')}"))
    print(color_text(f"◆ [+] Регион: {ip_info.get('region', 'недоступен')}"))

    print(color_text(f"◆ [+] Континент: {ip_type_info['continent']} {ip_type_info['continent_code']}"))
    print(color_text(f"◆ [+] Страна: {ip_type_info['country']} {ip_type_info['country_code']}"))
    print(color_text(f"◆ [+] Почтовый Индекс: {ip_type_info.get('postal', 'недоступен')}"))
    print(color_text(f"◆ [+] Код Телефона: {ip_type_info.get('calling_code', 'недоступен')}"))
    print(color_text(f"◆ [+] Языки: {ip_type_info.get('borders', 'недоступны')}"))
    print(color_text(f"◆ [+] Часовой пояс: {ip_info.get('timezone', 'недоступен')}"))

    print(color_text("◆ ГЕОЛОКАЦИЯ:"))
    if 'loc' in ip_info:
        latitude, longitude = ip_info['loc'].split(',')
        print(color_text(f"◆ [+] Координаты: {ip_info['loc']}"))
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        yandex_maps_url = f"https://yandex.ru/maps/?ll={longitude},{latitude}&z=10"
        print(color_text(f"◆ [+] Ссылка на Google Maps: {google_maps_url}"))
        print(color_text(f"◆ [+] Ссылка на Yandex Maps: {yandex_maps_url}"))
    else:
        print(color_text("◆ [-] Координаты недоступны"))

    print(color_text("◆ ТЕХНИЧЕСКАЯ ИНФОРМАЦИЯ:"))
    print(color_text(f"◆ [+] Тип IP-адреса: {ip_type_info.get('type', 'недоступен')}"))
    print(color_text(f"◆ [+] Hostname: {ip_info.get('hostname', 'недоступен')}"))
    print(color_text(f"◆ [+] Организация: {ip_info.get('org', 'недоступна')}"))

    print(color_text("◆ ПОИСК IP В IoT:"))
    shodan_url = f"https://www.shodan.io/search?query={ip_address}"
    censys_url = f"https://censys.io/ipv4/{ip_address}"
    zoomeye_url = f"https://www.zoomeye.org/searchResult?q={ip_address}"
    criminalip_url = f"https://www.criminalip.io/asset/report/{ip_address}"
    virustotal_url = f"https://www.virustotal.com/gui/ip-address/{ip_address}"

    print(color_text(f"◆ [+] Shodan: {shodan_url}"))
    print(color_text(f"◆ [+] Censys: {censys_url}"))
    print(color_text(f"◆ [+] Zoomeye: {zoomeye_url}"))
    print(color_text(f"◆ [+] CriminalIP: {criminalip_url}"))
    print(color_text(f"◆ [+] VirusTotal: {virustotal_url}"))
    print(color_text("╚" + "─" * 65 + "╝"))


def searchIp():
    ip_address = input(color_text("Введите айпи адрес: "))
    ipsearch(ip_address)


def main():
    searchIp()


if __name__ == "__main__":
    main()


init(autoreset=True)

def searchDomen():
    domain = input(Fore.WHITE + "\n[?] Введите сайт (например, example.com): ")  

    return domain

def get_website_info(domain):
    try:
        print(Fore.WHITE + "[*] Получаем информацию о домене...")
        domain_info = whois.whois(domain)
        
        # Проверка, есть ли информация о домене
        if not domain_info.domain_name:
            print(Fore.RED + "[!] Не удалось найти информацию о домене.")
            return
        
       
        print_string = f"""
{Fore.WHITE}[+] Домен: {Fore.WHITE}{domain_info.domain_name}
{Fore.WHITE}[+] Зарегистрирован: {Fore.WHITE}{domain_info.creation_date}
{Fore.WHITE}[+] Истекает: {Fore.WHITE}{domain_info.expiration_date}  
{Fore.WHITE}[+] Владелец: {Fore.WHITE}{domain_info.registrant_name}
{Fore.WHITE}[+] Организация: {Fore.WHITE}{domain_info.registrant_organization}
{Fore.WHITE}[+] Адрес: {Fore.WHITE}{domain_info.registrant_address}
{Fore.WHITE}[+] Город: {Fore.WHITE}{domain_info.registrant_city}
{Fore.WHITE}[+] Штат: {Fore.WHITE}{domain_info.registrant_state}
{Fore.WHITE}[+] Почтовый индекс: {Fore.WHITE}{domain_info.registrant_postal_code}
{Fore.WHITE}[+] Страна: {Fore.WHITE}{domain_info.registrant_country}
{Fore.WHITE}[+] IP-адрес: {Fore.WHITE}{domain_info.name_servers}
        """
        print(print_string)
    except Exception as e:
        print(Fore.RED + f"[!] Ошибка при получении информации о домене: {str(e)}")

def main():
    domain = search_domain()  
    get_website_info(domain)  

def searchDomen():
    domain = input(Fore.WHITE + "\n[?] Введите сайт (например, example.com): ")  #
    get_website_info(domain) 
    return domain

if __name__ == "__main__":
    main()

init(autoreset=True)

def searchNICK():
    nick = input(f"\n{Fore.WHITE}[?] Введите никнейм -> {Fore.WHITE}")
    urls = [
        f"https://www.instagram.com/{nick}",
        f"https://www.tiktok.com/@{nick}",
        f"https://twitter.com/{nick}",
        f"https://www.facebook.com/{nick}",
        f"https://www.youtube.com/@{nick}",
        f"https://t.me/{nick}",
        f"https://www.roblox.com/user.aspx?username={nick}",
        f"https://www.twitch.tv/{nick}",
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{Fore.WHITE}> {url} - аккаунт найден{Fore.WHITE}")
            elif response.status_code == 404:
                print(f"{Fore.WHITE}> {url} - аккаунт не найден{Fore.WHITE}")
            else:
                print(f"{Fore.WHITE}> {url} - ошибка {response.status_code}{Fore.WHITE}")
        except:
            print(f"{Fore.WHITE}> {url} - ошибка при проверке{Fore.WHITE}")
    print()

def main():
    searchNICK()

if __name__ == "__main__":
    main()

init(autoreset=True)

def searchinfo():
    message = [
        "Данный софт создан для развлекательных целей",
        "Автор софта : @Felix_335",
        "Канал : @FELIXSOFTOOL"
    ]
    
    for line in message:
        print(f"{Fore.WHITE}{line}")
        time.sleep(0.05)

    print(f"{Fore.LIGHTGREEN_EX}\nНажмите Enter для продолжения...")
    input()
    os.system("python PEOPLE.py")

def main():
    searchinfo()

if __name__ == "__main__":
    main()

def user_agents():
    ua = UserAgent()
    return ua.random

def searchPR():
    timeout, url, url2 = '300', 'https://api.proxyscrape.com/v3/free-proxy-list/get', 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'
    ip_api_url = 'http://ip-api.com/json/'
    headers = {'accept': 'text/plain, */*; q=0.01', 'accept-language': 'en-US,en;q=0.8', 'user-agent': user_agents()}
    socket.setdefaulttimeout(3)

    def fetch_proxies():
        proxies = []
        try:
            response = requests.get(url, headers=headers)
            proxies.extend(response.text.split('\n'))
            response2 = requests.get(url2, headers=headers)
            proxies.extend(response2.text.split('\n'))
        except requests.RequestException:
            pass
        return proxies

    def is_bad_proxy(pip):
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': pip})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlopen('https://www.example.com', timeout=5)
            return False
        except Exception:
            return True

    def get_country(ip):
        try:
            response = requests.get(ip_api_url + ip)
            return response.json().get('country', 'Unknown')
        except requests.RequestException:
            return 'Unknown'

    proxies = fetch_proxies()
    working_proxies, working_count, limit = [], 0, int(input('[+] Введите количество нужных вам прокси: '))

    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda proxy: (proxy if not is_bad_proxy(proxy) else None, get_country(proxy.split(':')[0])) if proxy else (None, None), proxies)
        for result, country in results:
            if result:
                ip_port = result.strip()
                print(f'➤ Рабочий прокси: {ip_port}, Страна: {country}\n')
                working_proxies.append(ip_port + '\n')
                working_count += 1
                if working_count >= limit:
                    print(f'[+] Найдено {working_count} прокси. Программа завершена.')
                    break  # Завершаем цикл, так как нужное количество прокси найдено

    exit(0)  # Программа завершится после этого вызова

def main():
    if input('[+] Желаете начать поиск прокси? - Да / Нет: ') == 'Да':
        searchPR()
    else:
        print('Закрываем программу')
        exit(1)

if __name__ == '__main__':
    main()

def searchF():
    def search_social_media(query):
        social_networks = {
            'Facebook': f'site:facebook.com {query}',
            'VK': f'site:vk.com {query}',
            'Instagram': f'site:instagram.com {query}',
            'Twitter': f'site:twitter.com {query}'
        }

        for network, query_str in social_networks.items():
            print(f"\nПоиск в {network} для {query}...")
            links = list(search(query_str, num_results=5))
            if links:
                print(f'Найдено {len(links)} ссылок для {network}:\n')
                for link in links:
                    print(f'➤ {link}')
            else:
                print(f'Не удалось найти профиль в {network} для {query}.')

    query = input('Введите имя пользователя для поиска по соц.сетям: ')
    search_social_media(query)

def main():
    searchF()

if __name__ == '__main__':
    main()
