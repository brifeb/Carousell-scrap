from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/populer')
def populer():
    res = requests.get('https://id.carousell.com/categories/photography-6/')
    soup = BeautifulSoup(res.text, 'html.parser')
    posts = soup.find_all(attrs={'class': 'D_hc M_jV D_gZ D_fw'})

    return render_template('index.html', posts=posts)






if __name__ == '__main__':
    app.run(debug=True)