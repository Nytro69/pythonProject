from bs4 import BeautifulSoup
import requests

html_ = requests.get("https://www.youtube.com/watch?v=XVv6mJpFOb0").text
soup = BeautifulSoup(html_, 'lxml')
soup.find_all('div', class_ = ' style-scope ytd-item-section-renderer style-scope ytd-item-section-renderer')
print(soup)