from flask import Flask 
app = Flask(__name__)
html_home = '<h1>Home page</h1>'

@app.route('/')
def home():
    return html_home

@app.route('/product')
def product():
    return html_home

@app.route('/contact')
def contact():
    return html_home

@app.route('/about')
def about():
    return html_home

@app.route('/help')
def help():
    return html_home

app.run(debug=True)