from flask import Flask,render_template

#Flask instance
app = Flask(__name__)

# http://127.0.0.1:5000/products
@app.route('/') #decorator function
def home(): #view function
    x=5
    name = "Jane"
    numbers =[1,2,3,4,5,6,7,8,9]
    return render_template('index.html',num = x,name = name,numbers = numbers)


@app.route("/products") 
def products():
    return render_template('products.html')


@app.route('/sales')
def sales():
    return render_template('sales.html')


@app.route('/stock')
def stock():
    return render_template('stock.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


app.run(debug=True)