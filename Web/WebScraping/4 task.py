import requests
from bs4 import BeautifulSoup
r = requests.get(url="http://maps.googleapis.com/maps/api/geocode/json")
soup = BeautifulSoup(r.text, "lxml")
