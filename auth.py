import requests
from bs4 import BeautifulSoup
import json

with open("auth.json") as auth_file:
    auth = json.load(auth_file)

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

username = auth["email"]
password = auth["password"]

with requests.Session() as s:
    url = "https://www.badmintonportalen.no/"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    view_state = soup.find('input', {'id': '__VIEWSTATE'})['value']
    view_state_generator = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']

    login_data = {
        'ctl00_ToolkitScriptManager1_HiddenField': '',
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        'ctl00$TextBoxLoginEmail': username,
        'ctl00$TextBoxLoginPassword': password,
        'ctl00$ButtonLogin': 'Logg inn'
    }

    r = s.post(url, data=login_data, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

if "Logg ut" in soup.text:
    print("Login successful.")
else:
    print("Login failed.")