import requests
import re
from bs4 import BeautifulSoup
r = requests.get(url="https://python.org/")
soup = BeautifulSoup(r.text, "lxml")
for i in soup.find_all(string=re.compile("Python")):
    print("".join(i.split()))
