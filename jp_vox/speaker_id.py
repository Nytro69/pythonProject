import requests

r = requests.get("http://127.0.0.1:50021/speakers")
r = r.json()
print(r)