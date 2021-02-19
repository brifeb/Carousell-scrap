from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/populer')
def populer():

    titles = ['aku','dua','tigsa', 'emprat']
    return render_template('index.html', yoyos=titles)




if __name__ == '__main__':
    app.run(debug=True)