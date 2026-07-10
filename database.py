import psycopg2
conn = psycopg2.connect(host="localhost", port=5432, database="flask_myduka", user="postgres", password="Swtheart@2026")

#creating a cursor object to perform db operations
cur = conn.cursor()


def get_products():
    cur.execute("select * from products") # execute the query in sql query
    products = cur.fetchall() # fetchall() method fetches all the rows from the result of the query and returns them as a list of tuples
    return products


def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('shoes',2000,2500)")
    conn.commit() # commit your changes permanently in the database

insert_products()

products = get_products()
print(products)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = get_sales()
print(sales)

def insert_sales():
    cur.execute("insert into sales(pid,quantity)values(2,5000)")
    conn.commit()

insert_sales()
sales = get_sales()
print(sales)

def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

def insert_stock():
    cur.execute("insert into stock(pid,stock_quantity)values(1,10)")
    conn.commit()

insert_stock()
stock = get_stock()
print(stock)

def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)", product_values)
    conn.commit() # commit your changes permanently in the database

product1 = ("laptop", 2000, 2500)
product2 = ("shirts", 1500, 2000)
insert_products(product1)
insert_products(product2)
products = get_products()
print(products)


def insert_sales(sale_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)", sale_values)
    conn.commit()

sale1 = (1, 5)
sale2 = (2, 10)
insert_sales(sale1)
insert_sales(sale2)
sales = get_sales()
print(sales)

def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)", stock_values)
    conn.commit()

stock1 = (1, 10)
stock2 = (2, 20)
insert_stock(stock1)
insert_stock(stock2)
stock = get_stock()
print(stock)


def sales_per_product():
    cur.execute("""
           select products.name, sum(sales.quantity) as total_sales from sales join products on sales.pid = products.id group by products.name
""")
    sales_per_product = cur.fetchall()
    return sales_per_product
sales_per_product = sales_per_product()
print(sales_per_product)