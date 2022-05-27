import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://emm.cv.ua")
soup = BeautifulSoup(r.text, "lxml")
print(len(soup.findAll("lt")))
print(len(soup.findAll("p")))
print(len(soup.findAll("gt")))