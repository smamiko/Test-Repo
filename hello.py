import requests


r = requests.get("https://asahi.com")
print(r.status_code)
