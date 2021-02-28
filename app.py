from flask import Flask , render_template
from jinja2 import Template
import json
app = Flask(__name__)

country = json.loads(open('country.json').read())
print(country[0]['abbreviation'])
@app.route('/home')
@app.route('/')
def home():
    title = 'Home page'
    content = 'Home page'
    data = {'name':'Zarif','age':33}
    img_url = 'uz.png'


    return render_template('home.html',title=title,content=content,data=data,img_url=img_url)

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