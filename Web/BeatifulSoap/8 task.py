import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://python.org/")
soup = BeautifulSoup(r.text, "lxml")
for li in soup.find_all("li"):
    print(li.find_next("a")["href"])
