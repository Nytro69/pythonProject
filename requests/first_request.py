import os

import requests
import dotenv
r = requests.post(f'https://www.youtube.com')

v = r.json()
print(v)
dotenv.load_dotenv(override=True)

x = os.getenv('SOME_KEY')

