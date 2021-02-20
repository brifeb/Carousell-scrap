import requests, pprint
from bs4 import BeautifulSoup
import csv

file = open('produk.csv', 'w', newline="")
writer = csv.writer(file)
header = ["Toko", "Produk", "Harga"]
writer.writerow(header)

url = 'https://id.carousell.com/categories/photography-6/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(attrs={'class':'D_hc M_jV D_gZ D_fw'})
for post in posts:
    toko = post.find_all('p')[0].text   # toko
    produk = post.find_all('p')[2].text   # produk
    harga = post.find_all('p')[3].text   # harga

    file = open('produk.csv', 'a', encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow([toko, produk, harga])
    file.close()



