import requests
from bs4 import BeautifulSoup
r = requests.get(url="https://data.gov/")
soup = BeautifulSoup(r.text, "lxml")
print("".join([x for x in soup.find_all("a", {"href":"metrics.html"})[0].get_text() if x.isdigit()]))
