import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://analytics.usa.gov/data/live/realtime.json")
soup = BeautifulSoup(r.text, "lxml")
print(soup.find_all("active_visitors")[0].get_text())
