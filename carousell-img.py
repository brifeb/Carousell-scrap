import requests
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/photography-6/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
posts = soup.find_all(attrs={'class':'D_hc M_jV D_gZ D_fw'})
for post in posts:
    produk = post.find_all('p')[2].text   # produk
    # print(produk)
    # print(produk.replace(' ','_').replace('/','')[:20])
    img_url = post.find_all('img')[0]['src']

    with open('hasil/' + produk.replace(' ','_').replace('/','')[:20] + '.jpg', 'wb') as f:
        img = requests.get(img_url)
        f.write(img.content)




