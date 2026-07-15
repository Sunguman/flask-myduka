from flask import Flask,render_template
#Flask instance
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    return "This is products"

@app.route('/sales')
def sales():
    return "This is sales"


@app.route('/stock')
def stock():
    return "This is stock"



@app.route('/dashboard')
def dashboard():
    return "This is dashboard"



@app.route('/register')
def register():
    return "This is register"


@app.route('/login')
def login():
    return "This is login"




app.run()