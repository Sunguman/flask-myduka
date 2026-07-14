**introduction to psycopg2**
psycopg2 is a driver or adapter that is used to connect python to a prostgres database
to establish this connection we use a function called *psycopg2.connect()* which takes some arguments
1 . host> where is my database located>>>in your local device(localhost)
2. Port where exactly in my device is the postgres service is running
3 . user default postgres username
4 . password password attached to the user for login
5 . dbname name of the database you want to connect to

*localhost domain 


import psycopg2
conn = psycopg2.connect(host="localhost", port=5432, database="flask_myduka", user="postgres", password="Swtheart@2026")

INTRODUCTION TO GITHUB Git -> A version control system that keeps track of changes you make to your project over time Github -> a cloud hosting / storage platform that hosts / stores git repositories

repository -> folder in Github

Github allows you to do the following: 1.store your projects securely online 2.back up your code 3.Collaborate with other developers 4.share your work with employers / clients 5.contribute to open source projects

git config --global user.name " Your Name" git config --global user.email " your email address"

Pushing new code to Github 1.Initializing git to track my files git init

2.Connect local folder to my github repository git remote add origin https://github.com/l-tting/flask-project.git"

3.Add files from local folder to my github repo git add .

4.Commit before final push -> commit: a saved snapshot of your project git commit -m "My first commit"

5.git push origin main or git push origin master

master / main -> branches ->

U -> untracked A -> added M -> modified

Updating existing code / repos in Github 1.git add . 2.git commit -m"added a p-tag in index" 3.git push origin master

Run the following commands in your terminal:

pip install flask 2.pip install psycopg2-binary
create database flask_myduka; \c flask_myduka

CREATE TABLE products ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0), selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0) );

CREATE TABLE stock ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

CREATE TABLE sales ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, quantity INTEGER NOT NULL CHECK (quantity > 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

CREATE TABLE users ( id SERIAL PRIMARY KEY, full_name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, phone_number VARCHAR(100) NOT NULL, password VARCHAR(255) NOT NULL );

insert into products(name,buying_price,selling_price)values('eggs',50,60);

INTRODUCTION TO PSYCOPG2 Psycopg2 is a driver that connects Python to a Postgres database conn -> a avriable that represents our connection to Postgres psycopg2.connect() -> a function that is used to establish a connection to the db

1.host -> where is my Postgres located? on what server is it located -> localhost 2.port -> where in my server is the Postgres service running 3.user -> default postgres user 4.password -> password attached to the user to allow login 5.dbname -> the name of the database you want to connect to

ip addresses and domain names IP address -> a number used to uniquely identify a device on a network types -> ipv4 and ipv6 ipv4 -> 192.181.102.255 google builds an app -> make it available to end users (deploy) -> server(ip address)

Domain name -> a human friendly name for an ip address 192.181.102.255 -> www.google.com

your local device has a default ip address of 127.0.0.1 127.0.0.1 -> ip address for your local device localhost -> domain name for 127.0.0.1

performing db operations using psycopg2 -> to perform db operations in psycopg2 we use an object called cursor cur -> object responsible for db operations; select , insert, update, delete cur.execute() -> a function meant to execute sql queries cur.fetchall() -> a function responsible for fetching data from Postgres to Python conn.commit() -> permanently save your changes to the database

task using functions write code that does the following: 1.fetches sales data 2.inserts sales data


data format of fetched data
data fetched using cur.fetchall()
list represent the entire dataset
tuple represent a single row of data

*function*


# List to store sales records
sales_database = []

# Function to fetch sales data
def fetch_sales_data():
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per item: "))

    sales = {
        "Product": product,
        "Quantity": quantity,
        "Price": price,
        "Total": quantity * price
    }

    return sales

# Function to insert sales data
def insert_sales_data(sales):
    sales_database.append(sales)
    print("Sales data inserted successfully!")

# Function to display sales data
def display_sales_data():
    print("\nSales Records")
    print("-" * 40)

    if len(sales_database) == 0:
        print("No sales records found.")
    else:
        for i, sale in enumerate(sales_database, start=1):
            print(f"Record {i}")
            print(f"Product : {sale['Product']}")
            print(f"Quantity: {sale['Quantity']}")
            print(f"Price   : {sale['Price']}")
            print(f"Total   : {sale['Total']}")
            print("-" * 40)

# Main program
sales = fetch_sales_data()
insert_sales_data(sales)
display_sales_data()

using functions write code that does the following:
fetches sales data

sales per product
sales per day
profit per product
profit per day

*sales per product*   sales & product table
sales is derived column selling_price*quantity per product(name)

select product.name,sum(product.selling_price*sales.quantity) as total_sales from products join sales on products.id=sales.pid group by p_name;

multiline string is astring that traverses more than 

using functions fetch the following data
sales per day
profit per product
profit per day


 pushing code to GitHub
# initialize a new git repository
git init
# add all files to the staging area # remote origin connects your local repository to the remote repository on GitHub
git remote add origin <repository-url>
git add .
# commit the changes
git commit -m "Initial commit"
# push the changes to the remote repositoryi
git push origin main

# updating code on GitHub
# check the status of your repository
git status
# add the modified files to the staging area
git add .
# commit the changes with a message
git commit -m "Updated code"
# push the changes to the remote repository
git push origin main



*Object oriented programming*

OOP -> Object Oriented Programming : a paradigm / concept where programs are built around classes and objects -> We have 2 broad classifications of data types in Python 
1.Inbuilt data types : come with the programming language 
2.user defined / custom data types: -> built using classes and objects

class - a blueprint / template for creating objects object - an instance of a class

class -> sketch of the building object -> real building created from the sketch

-> Any class has the following 3 things: 1.Identity - the unique name of a class 2.State - defined by attributes of a class -> answers the question: what does a class have? attribute - a variable inside a class 3.Behaviour -> defined by methods of a class -> answers the question: what can a class do? method - a function inside a class

class Car: identity -> Car state -> make, model, yom, is_imported,colour,no_of_doors behaviour -> move, stop , carry goods,

Define the following classes with their identity, state and behavior: -> class Student identity -> Student state -> name,age , course behaviour -> study, eat ,sleep, walk

-> class Phone -> class Dog

def init() -> a constructor Constructor -> a special method that is automatically called when creating objects used to initialize these objects with some data self - references an object itself dunder method -> double underscore methods

task OOP Task 1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 3.Create two BankAccount objects that can deposit, withdraw and display_info


This solution demonstrates:

Class: BankAccount
Attributes: account_number, balance, owner_name, date_opened
Methods: deposit(), withdraw(), and display_info()
Objects: account1 and account2, each performing deposits, withdrawals, and displaying account information.


class student
1. Student
Identity: Student ID = STU001
State: Name = John, Age = 21, Course = Computer Science
Behavior: Registers for courses, submits assignments, attends classes.
2. Laptop
Identity: Serial Number = HP123456
State: Brand = HP, RAM = 16GB, Storage = 512GB SSD
Behavior: Boots up, connects to the internet, runs applications.
3. Table
Identity: Table Number = TBL100
State: Material = Wood, Color = Brown, Height = 75 cm
Behavior: Holds items, can be moved, can be cleaned.

*oops concepts*
inheritance methods of overriding
polymorphism method and operator overloading
Abtraction
Encapsulation


## Flask

A Python framework used to build web applications.

## Framework vs Library
