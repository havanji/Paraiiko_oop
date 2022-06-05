import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://en.wikipedia.org/robots.txt")
soup = BeautifulSoup(r.text, "lxml")
print(soup.get_text())

