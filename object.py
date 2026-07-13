class person:
    def __init__(self, name, age, gender): #  defining the constructor method for the class, def__init__ is a special method in Python classes that is automatically called when a new instance of the class is created. It is used to initialize the attributes of the class with the values passed as arguments.
        # self is a reference to the current instance of the class. It allows you to access the attributes and methods of the class within its own methods. # dunder methods are special methods in Python that have double underscores before and after their names. They are also known as magic methods or special methods. Dunder methods allow you to define the behavior of your objects in certain situations, such as when they are created, compared, or represented as strings.
        self.name = name
        self.age = age
        self.gender = gender

person1 = person("John", 30, "Male") # creating an instance of the person class and passing values for name, age, and gender. The constructor method
person2 = person("Alice", 25, "Female") # creating another instance of the person class with different values for name, age
print(person1.name, person1.age, person1.gender) # accessing the attributes of the person1 instance and printing them to the console
print(person2.name, person2.age, person2.gender) # accessing the attributes of the person2 instance and printing them to the console

print(person1)
print(person2) # printing the instances of the person class. By default, this will print the memory address of the object, but you can override the __str__ method to provide a more meaningful representation of the object when printed.

print(type(person1))