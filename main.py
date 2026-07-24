from flask import Flask, render_template, request, redirect, url_for,flash
from database import get_products, get_sales, get_stock, insert_products, insert_sales, insert_stock,check_available_stock,sales_per_product,sales_per_day,profit_per_product,profit_per_day

# Flask instance
app = Flask(__name__)

app.secret_key= 'vfbfscsfg5677ghn'


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
        flash("Product added successfully",'success')
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

        available_stock=check_available_stock(pid)

        if float(quantity)>available_stock:
            flash("Insufficient stock",'danger')
            return redirect(url_for('sales'))
       

        new_sale = (pid, quantity)
        insert_sales(new_sale)
        flash("Sale made successfully",'success')
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
        flash("Stock added successfully",'success')
    return redirect(url_for('stock'))



@app.route('/dashboard')
def dashboard():
    sales_product = sales_per_product()
    sales_day = sales_per_day()

    profit_product = profit_per_product()
    profit_day = profit_per_day()

    product_names = [i[0] for i in sales_product]
    s_product = [i[1] for i in sales_product]
    p_profit = [i[1] for i in profit_product]

    dates = [i[0] for i in sales_day]
    dates_sales = [i[1] for i in sales_day]
    dates_profit = [i[1] for i in profit_day]

    return render_template('dashboard.html',
                           product_names=product_names,
                           s_product=s_product,
                           p_profit=p_profit,
                           dates=dates,
                           dates_sales=dates_sales,
                           dates_profit=dates_profit
                           )


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
