import requests, pprint
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/photography-6/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
kamera_populer = soup.find(attrs={'class':'D_jr M_fT D_W'})
# print(kamera_populer)
titles = kamera_populer.find_all(attrs={'class':'D_lQ M_ij D_lL D_jn'})

for title in titles:
    user = title.find_all('p')
    print(user[2].text)
