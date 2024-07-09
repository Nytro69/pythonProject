import requests

domain = ("openai.com")

response = requests.get(f"https://www.{domain}/status/418")

if response.status_code != 418:
    print("Not Found")
else:
    print(response.text)