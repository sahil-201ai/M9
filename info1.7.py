import telebot
from user_agent import generate_user_agent
import requests;import webbrowser;import hashlib;import pyfiglet;import hmac;import time
from datetime import datetime
script_version = '1.0.0'
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"\x1b[38;5;190m     \t           Script Version: {script_version}")
print(f"\x1b[38;5;174m             Date and Time: {current_datetime}")
print("\x1b[38;5;150m               Script programmed by Raven")
text = "      Raven"
fig = pyfiglet.Figlet(font='slant')
formatted_text = fig.renderText(text)
print("\x1b[38;5;99m" + formatted_text + "\x1b[0m")
print("\x1b[38;5;228m")
webbrowser.open('https://t.me/ZZKGZ')
API_TOKEN = input('Token : ')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أرسل يوزر المستخدم للحصول على المعلومات.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.text.strip()
    cookies = {
        'csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
        'ig_did': '394458D6-565A-48F0-BFBB-CB75FD177F49',
        'ig_nrcb': '1',
        'dpr': '2.25',
        'mid': 'ZsqbPgABAAFrLhyT_amwiK59BNv4',
        'datr': 'PpvKZjhMQN858xPWY13-suQ2',
        'wd': '480x919',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://www.instagram.com/shbs/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"RMX3511"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"13.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'x-asbd-id': '129477',
        'x-csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': '0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'username': user,
    }

    try:
        response = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            cookies=cookies,
            headers=headers
        ).json()

        name = response['data']['user']['full_name']
        bio = response['data']['user']['biography']
        fols = response['data']['user']['edge_followed_by']['count']
        flog = response['data']['user']['edge_follow']['count']
        id = response['data']['user']['id']
        pr = response['data']['user']['is_private']
        op = response['data']['user']['edge_owner_to_timeline_media']['count']

        try:
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
            ree = re.json()
            data = ree['date']
        except:
            data = "Not Data"
          
        ff = f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @F_M_D | @ZZKGZ 
═══════════════════
𝖓𝖆𝖒𝖊 : {name}
𝖚𝖘𝖊𝖗 : {user}
𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fols}
𝖋𝖔𝖗𝖗𝖔𝒘𝖎𝖓𝖌 : {flog}
𝖉𝖆𝖙𝖆 : {data} 
𝖕𝖔𝖘𝖙 : {op} 
𝖎𝖉 : {id}
𝖗𝖎𝖓𝖐 : https://www.instagram.com/{user}
═══════════════════
	'''
        bot.reply_to(message, ff)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ. يرجى التحقق من اليوزر وإعادة المحاولة.")
bot.polling()
