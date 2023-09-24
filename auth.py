import requests
from bs4 import BeautifulSoup
import json

# Set headers to avoid 406 error
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# Create a session
with requests.Session() as s:
    url = "https://www.badmintonportalen.no/"

# Get the username and password from auth.json
with open("auth.json") as auth_file:
    auth = json.load(auth_file)

# Set the username and password
username = auth["email"]
password = auth["password"]

auth_file.close()

# Login function
def login():
    # Get the login page
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Get the view state and view state generator from the login page
    view_state = soup.find('input', {'id': '__VIEWSTATE'})['value']
    view_state_generator = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']

    # Set the login data
    login_data = {
        'ctl00_ToolkitScriptManager1_HiddenField': '',
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        'ctl00$TextBoxLoginEmail': username,
        'ctl00$TextBoxLoginPassword': password,
        'ctl00$ButtonLogin': 'Logg inn'
    }

    # Post the login data and get the response
    r = s.post(url, data=login_data, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Check if the login was successful
    if "Logg ut" in soup.text:
        return True
    else:
        return False