from flask import Flask 
from jinja2 import Template
app = Flask(__name__)



@app.route('/')
def home():
    title = 'Home page'
    content = 'Home page'

    link = '''
    <a href='/about'>about</a>
    <a href='/product'>product</a>
    <a href='/contact'>contact</a>
    <a href='/help'>help</a>
    '''
    html_tmp = f'''
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
       <h1> {content}</h1>
        {link}
    </body>
    </html>
    '''

    return html_tmp

@app.route('/about')
def about():
    title = 'about page'
    content = 'about page'

    link = '''
    <a href='/about'>about</a>
    <a href='/product'>product</a>
    <a href='/contact'>contact</a>
    <a href='/help'>help</a>
    '''
    html_tmp = f'''
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
       <h1> {content}</h1>
        {link}
    </body>
    </html>
    '''

    return html_tmp


@app.route('/product')
def product():
    return html_home

@app.route('/contact')
def contact():
    return html_home

@app.route('/help')
def help():
    return html_home

app.run(debug=True)