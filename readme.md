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
anology building a house
scenerio 1:
Thomas intends to build a house. he recognizes that he is not an expert in this field and decides to seek the help of professionals *(engineers)* to make it more easier but becomes very rigid because i have to be advised.
very easy and fast but very strict.
--framwork--

Scenario 2
decides to build it by myself. process becomes much harder but fairly flexible.
process is harder but flexible
--Library--

*framework* a prebuilt structure of code and tools that help developers build applications easily but not haveing to build everything on their own and from scratch . it makes the development process easier but has very strict guidelines on usage.

Examples of framework

1. python --Flask, Django, FastAPI
2. Javascript--React, Vue, Angular, svelte
3. Laravel
4. Spring
5. c# .net
6. Go Chi,gin
7. Ruby on rails

Mobile native --android kotlin,java
              --ios swift

React native can build apps for both android and ios(apps are slow)

*FLASK*
*Routing* : is the mechanisms that maps or connects urls to python
*URL* uniform resource locator; the full address that is used to access an application e.g <https://meet.google.com/dsh-idtb-oqb>

Part of a url

1. Protocol; tells the browser the mode of communication, http and https, http hypertext transfer protocol( transfer data as raw text), https hypertext transfer protocol secure(Transfer data in encrypted format) to convert use ssl /tls certificate which is free
2. Domain Name; human friendly name for an ip address.
3. path/rule; specific resource or sections to be access on an application, <https://meet.google.com/*dsh-idtb-oqb>*
4. port(optional)



To enable routing in Flask we use a decorator function called @app.route('/)


https://www.google.com/
/ index route / default route/location a user lands in when they first open an application

@app.route('/')  decorator function
def home():   view function
    return "Hello world"   data to be returned.

View function  is responsible for returning some data


To render/ return html pages in Flask we must have the following

Static data/ all static files of your project:
css files, images, videos, favicons,icons
templates/contain all html pages/files
index.html
sales.html
single html file is called a template
database.py
main.py

to return a html pages we use a function called *render_template* which is imported from flask

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

Data format of data fetched using psycopg2 -> Our data from cur.fetchall() is returned in a list of tuples list-> contains all rows returned from the database tuple -> represents a single row of record

function - reusable block of code meant to perform a specific task To make functions reusable we use parameters parameters & arguments parameter - a placeholder variable meant to make a function reusable argument - a real value passed in place of a parameter when calling the function

fetching data from two tables

1.sales per product

sales per product -> sales & product name sales (products & sales) -> selling_price * quantity -> product name

select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales from products join sales on sales.pid = products.id group by p_name;

multiline strings -> allow us to have strings that traverse more than one line by using tripple openinng and closing quotations

task Using functions write code that fetches the following data: 2.sales per day 3.profit per product 4.profit per day

must know 1.SQL - basic queries ,pk & fk , joins , aggregate functions, filter clauses , group by 2.Python - data types , data structures(lists and tuples), conditional statements , loops, functions(emphasis)

OOP -> Object Oriented Programming : a paradigm / concept where programs are built around classes and objects -> We have 2 broad classifications of data types in Python 1.Inbuilt data types : come with the programming language 2.user defined / custom data types: -> built using classes and objects

class - a blueprint / template for creating objects object - an instance of a class

class -> sketch of the building object -> real building created from the sketch

-> Any class has the following 3 things: 1.Identity - the unique name of a class 2.State - defined by attributes of a class -> answers the question: what does a class have? attribute - a variable inside a class 3.Behaviour -> defined by methods of a class -> answers the question: what can a class do? method - a function inside a class

class Car: identity -> Car state -> make, model, yom, is_imported,colour,no_of_doors behaviour -> move, stop , carry goods,

Define the following classes with their identity, state and behavior: -> class Student identity -> Student state -> name,age , course behaviour -> study, eat ,sleep, walk

-> class Phone -> class Dog

def init() -> a constructor Constructor -> a special method that is automatically called when creating objects used to initialize these objects with some data self - references an object itself dunder method -> double underscore methods

task OOP Task 1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 3.Create two BankAccount objects that can deposit, withdraw and display_info

OOP Concepts -> Inheritance -> method overriding -> Polymorphism -> method overloading -> Abstraction -> Encapsulation

FLASK -> A python framework used to build robust web applications

framework vs library Analogy: Building a house

Scenario 1: David intends to build a house.he recognizes that he is not an expert in this field and decides to seek the help of professionals(architrect,engineers,construction workers). The process ends up becoming simpler since these experts have domain knowledge and experience in this field but David has to do everything exactly as advised by these experts. Conclusion: Process is simpler and faster but very strict guidelines must be followed ----> Framework

Scenario 2: Jerry also intends to build a house. He decides not to seek the help of any professional but rather he does everything by himself. The process is much harder but very flexible because he gets to decide what to do at every stage. Conclusion: process is much harder but flexible -----> Library

framework - a prebuilt structure of code and tools used to help developers build applications by making the development process much easier where they dont have to build the application from scratch but it enforces very strict guidelines that must be followed.

Examples of frameworks 1.Python -> Flask, Django, FastAPI 2.JavaScript -> React , Angular , Vue, Svelte 3.Java -> Spring 4.C# -> .NET 5.PHP -> Laravel 6.Go -> Chi, Gin 7.Ruby -> Ruby on Rails

Flask Routing in Flask -> Routing is a mechanism that maps or connects urls to Python functions url -> uniform resource locator -> the full address used to access and application e.g. https://meet.google.com/dsh-idtb-oqb

Parts of a url 1.protocol -> tells the browser how to communicate (http or https) http -> hypertext transfer protocol (transfers data as raw text) https -> hypertext transfer protocol secure (transfers data in encrypted format) http -> https -> ssl / tls certificate(free) 2.domain name -> human friendly name used in place of an ip address 3.Path/Rule -> specific resource to be accessed in an appliation 4.Port(optional)

-> Routing in Flask is enabled through the use of a decorator function called @app.route() decorator function -> a function that determines /modifies the behaviour of another function -> decorator functions in Python are usually preceded by the '@' prefix -> our decorator function takes some arguments: 1.rule / path -> e.g . /, /login ,/profie 2.methods --->

https://www.google.com/

/ -> index route -> default landing location / page when a user opens an application

@app.route("/products") -> decorator function def products(): -> view function return "This is products"

view function -> a function meant to execute a specific task in our application and give back some response or data

app.run() -> a function meant to start your server and run your application

N/B: -> View functions cannot share the same name

Instead of returning single pieces of data , we can return full html pages which can the render as much content as we want

To return html pages we must have the following structure

static : contains all statiic files : css files, images , videos , icons , favicons templates : contains all html files : a single html file is called a template main.py database.py

To display these html files we use a function called render_template() which is imported from flask -> render means return

TEMPLATE INHERITANCE -> This is a feature thta enables us reduce redundancy in development by having one parent template (base) that has all common features of all pages , then every other html page inherits from the parent template automatically inheriting these common features(navbar and footer) -> template inheritance is supported by a Flask feature called jinja

{% block title %} --- a page's title goes here ----{% endblock %}

{% block content %} --- a page's unique content goes here-----

{% endblock %}

block title -> defines a block in which we can pass the unique title of each page block content -> defines a block in which we can pass the unique content of each page

-> to apply template inheritance we use ---> extends base.html in jinja

JINJA -> A templating engine integrated with Flask to render dynamic html pages. -> It is simply syntax used depending on whether a control structure is used or not

control structures -> building blocks of a language: 1.Sequence -> a program executes from top to bottom , left to right 2.Selection -> decision making -> conditional statements 3.Repitition -> iteration -> loops

how to use Jinja 1.Variables -> use double curly braces ====> {{ }} 2.Control structures e.g if statements , for loops, while loops etc -> when using Jinja with control structures , it must have the following parts: => initialization (where does the control structure start) => termination( terminating the control structure) -> we use modulus signs embedded inside curly braces ==> {% %}

e.g. 
 
 {% if x== 5 %}  -> initialization
    .............
 {% endif %} - termination


 {% for i in numbers %}
     ......
 {% endfor %}


 *DISPLAY DATA IN HTML*
==> Database -> Psycopg2 -> Python -> Jinja -> HTML
==> data format : list of tuples 
==> display data in user friendly tables 


[(1, 'eggs', Decimal('50.00'), Decimal('60.00')), (2, 'bread', Decimal('55.00'), Decimal('65.00')), (3, 'shoes', Decimal('2000.00'), Decimal('2500.00')), (4, 'samsung phone', Decimal('20000.00'), Decimal('25000.00')), (5, 'juice', Decimal('80.00'), Decimal('120.00')), (6, 'juice', Decimal('80.00'), Decimal('120.00')), (7, 'juice', Decimal('80.00'), Decimal('120.00')), (8, 'charger', Decimal('1500.00'), Decimal('2000.00'))]

list => the entire dataset
tuple => a single record of data 


*Task*
Display your sales and stock data using a datatable

https://datatables.net/examples/styling/bootstrap5.html

==> Display your sales and stock data using a datatable. 


*POSTING DATA IN FLASK*

*Posting data workflow*
1.User is provided with a form to fill
2.User will fill and submit the form
3.The form is submitted to a route in Flask for processing
4.Flask extracts form data using a request object
    -> data comes in form of key value pairs
    -> data is extracted using the key 
    -> key is specified in the name attribute of an input
    -> request object uses the key to access and extract form data
    -> request object has 2 methods:
          > request.method -> used to determine what method has been specified in a form
          > request.form -> accesses and extracts form data using the key
5.Data is processed and stored
6.User is notified and redirected



*Form Checklist to Post Data*
1.action attribute 
    => specifies the route in which the form data is to be submitted
2.method attribute 
   => specifies what the server should do with the resource / data
3.name attribute 
   => form data sent to the server is sent in form of key-value pairs
   => name attribute specifies the key used to access the value
4.input type 
5.button of type submit


*What can a server do with data?*
1.GET -> moving data from the server to the client
      -> e.g. viewing products
2.POST -> moving data from client to server
       -> e.g. posting pictures on instagram, adding a product 
3.PUT -> updating an existing resource
      -> e.g. changing username / password, changing product name / prices
4.DELETE -> getting rid of data / resource



"eggs" -> product name
17 -> buying price
20 - selling price

p_name : "eggs"
b_price: 17
s_price : 20

*redirecting*
-> taking a user from one section to another
-> here we use the redirect and url_for functions which are imported from flask
redirect(url_for('   '))-> pass the name of the view function

*Task*
-> apply the same procedure to post sales and stock data 
