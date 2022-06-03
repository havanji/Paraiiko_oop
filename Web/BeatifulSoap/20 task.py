import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://python.org/")
soup = BeautifulSoup(r.text, "lxml")
print(soup.find_all(href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"))
