import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://mof.gov.ua/uk")
soup = BeautifulSoup(r.text, "lxml")
print(soup.currentTag)
