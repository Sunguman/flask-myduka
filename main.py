from flask import Flask, render_template, request, redirect, url_for
from database import get_products, get_sales, get_stock, insert_products, insert_sales, insert_stock

# Flask instance
app = Flask(__name__)


# http://127.0.0.1:5000/products
@app.route('/')
def home():
    x = 5
    name = "Jane"
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render_template('index.html', num=x, name=name, numbers=numbers)


@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html', products_data=products_data)

@app.route('/add_product',methods=['GET','POST'])   # route for adding products
def add_products():
    if request.method=='POST':
        product_name=request.form['p_name']
        buying_price=request.form['b_price']
        selling_price=request.form['s_price']

        new_product=(product_name,buying_price,selling_price)
        insert_products(new_product)
        print("Product added successfully")
    return redirect(url_for('products'))



@app.route('/sales')
def sales():
    sales_data = get_sales()
    products_data = get_products()
    return render_template('sales.html', sales_data=sales_data,products_data=products_data)

@app.route('/add_sales',methods=['GET','POST'])   # route for adding Sales
def make_sale():
    if request.method=='POST':
        pid = request.form['pid']
        quantity = request.form['quantity']
       

        new_sale = (pid, quantity)
        insert_sales(new_sale)
        print("Sale made successfully")
    return redirect(url_for('sales'))



@app.route('/stock')
def stock():
    stock_data = get_stock()
    products_data = get_products()
    return render_template('stock.html', stock_data=stock_data,products_data=products_data)

@app.route('/add_stock',methods=['GET','POST'])   # route for adding Stock
def add_stock():
    if request.method=='POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']
     

        new_stock = (pid, stock_quantity,)
        insert_stock(new_stock)
        print("Stock added successfully")
    return redirect(url_for('stock'))



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
