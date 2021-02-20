import requests, pprint
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/photography-6/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(attrs={'class':'D_hc M_jV D_gZ D_fw'})
for post in posts:
    # user = post.find_all('p')
    # print(user[2].text)
    print(post.find_all('p')[0].text)   # toko
    # print(post.find_all('p')[2].text)   # judul
    # print(post.find_all('p')[3].text)   #harga
    # print(post.find_all('p')[4].text)   #desc
    # print(post.find_all('img')[0]['src'])   #gambar
    # print(post.find_all('a')[1]['href'])   #link
    # pass



