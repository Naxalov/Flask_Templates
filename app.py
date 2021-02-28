from flask import Flask , render_template
from jinja2 import Template
app = Flask(__name__)

html_tmp = Template('''
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    <h1> {{content}}</h1>

    <a href='/home'>home</a>
    <a href='/about'>about</a>
    <a href='/product'>product</a>
    <a href='/contact'>contact</a>
    <a href='/help'>help</a>

    </body>
</html>
''')

@app.route('/home')
@app.route('/')
def home():
    title = 'Home page'
    content = 'Home page'


    return render_template('home.html',title='TITLE')

@app.route('/about')
def about():
    title = 'about page'
    content = 'about page'


    return html_tmp.render(title=title,content=content)


@app.route('/product')
def product():
    title = 'product page'
    content = 'product page'

    return html_tmp.render(title=title,content=content)

@app.route('/contact')
def contact():
    title = 'contact page'
    content = 'contact page'

    return html_tmp.render(title=title,content=content)

@app.route('/help')
def help():
    title = 'help page'
    content = 'help page'

    return html_tmp.render(title=title,content=content)

app.run(debug=True)