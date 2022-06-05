import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://data.gov/")
soup = BeautifulSoup(r.text, "lxml")
print(soup.find_all(class_="entry-title")[0].get_text())
