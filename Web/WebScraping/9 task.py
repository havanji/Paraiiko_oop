import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://twitter.com/elonmusk")
soup = BeautifulSoup(r.text, "lxml")
print(soup.find_all("a", {"href":"/elonmusk/followers"})[0].get_text())
