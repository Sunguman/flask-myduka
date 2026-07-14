class person:
    def __init__(self, name, age, gender): #  defining the constructor method for the class, def__init__ is a special method in Python classes that is automatically called when a new instance of the class is created. It is used to initialize the attributes of the class with the values passed as arguments.
        # self is a reference to the current instance of the class. It allows you to access the attributes and methods of the class within its own methods. # dunder methods are special methods in Python that have double underscores before and after their names. They are also known as magic methods or special methods. Dunder methods allow you to define the behavior of your objects in certain situations, such as when they are created, compared, or represented as strings.
        self.name = name
        self.age = age
        self.gender = gender
    def talks(self,words): # defining a method called talks that takes an additional parameter called words. This method will allow the person instance to "talk" by printing the words passed to it.
        print(f"{self.name} talks and says: {words}") # printing the words passed to the talks method to the console



person1 = person("John", 30, "Male") # creating an instance of the person class and passing values for name, age, and gender. The constructor method
person2 = person("Alice", 25, "Female") # creating another instance of the person class with different values for name, age
print(person1.name, person1.age, person1.gender) # accessing the attributes of the person1 instance and printing them to the console
print(person2.name, person2.age, person2.gender) # accessing the attributes of the person2 instance and printing them to the console

print(person1)
print(person2) # printing the instances of the person class. By default, this will print the memory address of the object, but you can override the __str__ method to provide a more meaningful representation of the object when printed.

print(type(person1))


# Define the BankAccount class
class BankAccount:

    # Constructor
    def __init__(self, account_number, owner_name, balance, date_opened):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

        from datetime import datetime
        today= datetime.now().date()
    

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Ksh {amount} deposited successfully.")
        else:
            print("Deposit unsuccessful.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Ksh {amount} withdrawn successfully.")
        else:
            print("Withdrawal unsuccessful. Insufficient balance.")

    # Display account information
    def display_info(self):
        print("\n----- Account Information -----")
        print("Account Number:", self.account_number)
        print("Owner Name:", self.owner_name)
        print("Balance: Ksh", self.balance)
        print("Date Opened:", self.date_opened)


# Create two BankAccount objects
account1 = BankAccount("1001", "John Doe", 5000, "01-01-2026")
account2 = BankAccount("1002", "Jane Smith", 10000, "15-02-2026")


# Perform transactions on account1
account1.deposit(2000)
account1.withdraw(1500)
account1.display_info()


# Perform transactions on account2
account2.deposit(5000)
account2.withdraw(3000)
account2.display_info()