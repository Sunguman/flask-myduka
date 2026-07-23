import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="flask_myduka",
        user="postgres",
        password="Swtheart@2026",
    )


def get_products():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select * from products")
            return cur.fetchall()


def get_sales():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select * from sales")
            return cur.fetchall()


def get_stock():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select * from stock")
            return cur.fetchall()


def insert_products(product_values=None):
    if product_values is None:
        product_values = ("shoes", 2000, 2500)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "insert into products(name,buying_price,selling_price) values(%s,%s,%s)",
                product_values,
            )
            conn.commit()


def insert_sales(sale_values=None):
    if sale_values is None:
        sale_values = (2, 5000)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("insert into sales(pid,quantity) values(%s,%s)", sale_values)
            conn.commit()


def insert_stock(stock_values=None):
    if stock_values is None:
        stock_values = (1, 10)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("insert into stock(pid,stock_quantity) values(%s,%s)", stock_values)
            conn.commit()


def sales_per_product():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select products.name, sum(sales.quantity) as total_sales
                from sales
                join products on sales.pid = products.id
                group by products.name
                """
            )
            return cur.fetchall()


def profit_per_product():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select products.name,
                       sum(sales.quantity * (products.selling_price - products.buying_price)) as total_profit
                from sales
                join products on sales.pid = products.id
                group by products.name
                order by products.name
                """
            )
            return cur.fetchall()


def profit_per_day():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select date(sales.created_at) as sale_date,
                       sum(sales.quantity * (products.selling_price - products.buying_price)) as total_profit
                from sales
                join products on sales.pid = products.id
                group by date(sales.created_at)
                order by sale_date
                """
            )
            return cur.fetchall()
            


def check_available_stock(pid):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select sum(stock_quantity) from stock where pid = %s",(pid,))  # a comma represent a tuple
            total_stock = cur.fetchone()[0] or 0 # cur.fetchall() returns a list of tuples, cur.fetchone() returns a tuple

            cur.execute("select sum(quantity) from sales where pid = %s",(pid,))
            total_sold = cur.fetchone()[0] or 0

            return total_stock - total_sold