import os
from pystyle import Colorate, Colors, Center, Write

os.system("clear")

password = Write.Input("[+] Введите пароль -> ", Colors.white_to_black, interval=0.005)

if password != "@FELIXSOFTOOL":
    print("Неверный пароль. Выход из программы.")
    exit()

banner = '''
  ██████╗ ███████╗ ██████╗ ██████╗ ██╗     ███████╗
  ██╔══██╗██╔════╝██╔═══██╗██╔══██╗██║     ██╔════╝
  ██████╔╝█████╗  ██║   ██║██████╔╝██║     █████╗  
  ██╔═══╝ ██╔══╝  ██║   ██║██╔═══╝ ██║     ██╔══╝  
  ██║     ███████╗╚██████╔╝██║     ███████╗███████╗
  ╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝
                                                                                     
╭────────────────────────────────────────────────────────────╮
│                 ░▒▓ МЕНЮ ПОИСКА ДАННЫХ ▓▒░                 │
├────────────────────────────────────────────────────────────┤
│  [1] ➤ Поиск по FullName       |  [8] ➤ Поиск по Database  │
│  [2] ➤ Поиск по Number         |  [9] ➤ Поиск по Getcontact│
│  [3] ➤ Поиск по PROXY          | [10] ➤ Поиск по Снилсу    │
│  [4] ➤ Поиск по EMAIL          | [11] ➤ Поиск по Инн       │
│  [5] ➤ Поиск по IP адресу      | [12] ➤ Поиск по Авто      │
│  [6] ➤ Поиск по Домену         | [13] ➤ Поиск по Соц.сетям │
│  [7] ➤ Поиск по Никнейму       | [14] ➤ Информация о софте │
╰────────────────────────────────────────────────────────────╯
'''

print(Colorate.Vertical(Colors.white_to_black, banner, 2))

choice = Write.Input("[+] Введите номер -> ", Colors.white_to_black, interval=0.005)

if choice == '':
    print("Вынужденная остановка программы.")
    exit()  

elif choice == '1':
    from search import searchbd
    searchbd()

elif choice == '2':
    from search import searchbd
    searchbd()

elif choice == '3':
    from search import searchPR
    searchPR()

elif choice == '4':
    from search import searchbd
    searchbd()

elif choice == '5':
    from search import searchIp
    searchIp()

elif choice == '6':
    from search import searchDomen
    searchDomen()

elif choice == '7':
    from search import searchNICK
    searchNICK()

elif choice == '8':
    from search import searchbd
    searchbd()

elif choice == '9':
    from search import searchbd
    searchbd()

elif choice == '10':
    from search import searchbd
    searchbd()

elif choice == '11':
    from search import searchbd
    searchbd()

elif choice == '12':
    from search import searchbd
    searchbd()

elif choice == '13':
    from search import searchF
    searchF()

elif choice == '14':
    from search import searchinfo
    searchinfo()

elif choice == '90':
    print("Выход из программы.")
    exit()
else:
    print("Неверный выбор.")
