import auth
from bs4 import BeautifulSoup

# Call the login function from auth.py
if auth.login():
    url = "https://www.badmintonportalen.no/NBF/Klub/Turnering/Tilmeld/?clubid=67#23806"
    r = auth.s.get(url, headers=auth.headers)
    soup = BeautifulSoup(r.content, 'html.parser')
# Print error message if login was not successful
else:
    print("Login was not successful. Skipping the request.")