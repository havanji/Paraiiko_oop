import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://python.org/")
soup = BeautifulSoup(r.text, "lxml")
print(soup.findAll("h1"))
print(soup.findAll("h2"))
print(soup.findAll("h3"))
