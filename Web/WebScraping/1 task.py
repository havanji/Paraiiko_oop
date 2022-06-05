import requests
r = requests.get(url="https://python.org/")
print(r.status_code)
