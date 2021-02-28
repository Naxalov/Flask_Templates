from flask import Flask , render_template
from jinja2 import Template
import json
app = Flask(__name__)

country_data = json.loads(open('country.json').read())
@app.route('/home')
@app.route('/')
def home():
    content = 'Home page'


    return render_template('home.html',content=content)

@app.route('/country')
def country():
    title = 'Country'
    content = 'Country page'
    img_url = country_data[230:240]
    # print(img_url)
    return render_template('country.html',title=title,content=content,img_url=img_url)

@app.route('/about')
def about():
    title = 'about page'
    content = 'about page'

    return render_template('home.html',title=title,content=content)



@app.route('/product')
def product():
    title = 'product page'
    content = 'product page'

    return render_template('home.html',title=title,content=content)


@app.route('/contact')
def contact():
    title = 'contact page'
    content = 'contact page'

    return render_template('home.html',title=title,content=content)

@app.route('/help')
def help():
    title = 'help page'
    content = 'help page'

    return render_template('home.html',title=title,content=content)

app.run(debug=True)