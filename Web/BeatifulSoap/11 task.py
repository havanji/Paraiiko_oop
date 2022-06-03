import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://python.org/")
soup = BeautifulSoup(r.text, "lxml")
h1 = soup.find_all("h1")
h2 = soup.find_all("h2")
h3 = soup.find_all("h3")
print(list(h1 + h2 + h3))
