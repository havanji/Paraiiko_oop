import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://emm.cv.ua")
soup = BeautifulSoup(r.text, "lxml")
# print(soup.select("lt")[0].get_text())
print(soup.select("p")[0].get_text())
# print(soup.select("gt")[0].get_text())
