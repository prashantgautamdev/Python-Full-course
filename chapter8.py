'''oops'''

'''

"""
================================================================
    PYTHON NOTES: OOP (OBJECT-ORIENTED PROGRAMMING)
================================================================
"""

# ================================================================
# PART 1: OOP BASICS - CLASS & OBJECT
# ================================================================

# ---- Class kya hai? ----
# Class ek blueprint/template hai jisse objects banaye jaate hain.
# Object class ka ek real instance hota hai.

class Person:
    def __init__(self, name, age):    # constructor
        self.name = name               # instance attribute
        self.age = age

    def greet(self):                    # instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


# ---- Object create karna ----
p1 = Person("Aman", 20)
p2 = Person("Riya", 22)

p1.greet()      # Hello, my name is Aman and I am 20 years old
p2.greet()      # Hello, my name is Riya and I am 22 years old


# ---- self keyword ----
# `self` current object ko represent karta hai. Ye har instance
# method ka pehla parameter hota hai (automatically pass hota hai).


# ================================================================
# PART 2: __init__ CONSTRUCTOR
# ================================================================

# __init__ method object create hote hi automatically call hota hai.
# Isse hum object ke initial attributes set karte hain.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Fortuner", 2023)
car1.display_info()


# ================================================================
# PART 3: CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ================================================================

class Student:
    school_name = "ABC School"      # class attribute (sabhi objects ke liye common)

    def __init__(self, name):
        self.name = name             # instance attribute (har object ka alag)

s1 = Student("Aman")
s2 = Student("Riya")

print(s1.school_name)    # ABC School
print(s2.school_name)    # ABC School (same for all objects)
print(s1.name, s2.name)  # Aman Riya (different for each object)


# ================================================================
# PART 4: INHERITANCE
# ================================================================

# Inheritance ek class (child) ko dusri class (parent) ke properties
# aur methods inherit karne deta hai.

class Animal:                       # Parent class
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):                  # Child class - Animal se inherit
    def make_sound(self):           # method overriding
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

d = Dog("Buddy")
c = Cat("Whiskers")
d.make_sound()      # Buddy says Woof!
c.make_sound()       # Whiskers says Meow!


# ---- super() function ----
# super() se child class parent class ke methods/constructor ko
# call kar sakti hai

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)    # parent constructor call
        self.department = department

    def display(self):
        print(f"{self.name} manages {self.department}, earns {self.salary}")

m = Manager("Aman", 80000, "Engineering")
m.display()


# ---- Multiple Inheritance ----
class Father:
    def skills(self):
        print("Father: Coding, Cooking")

class Mother:
    def talents(self):
        print("Mother: Painting, Singing")

class Child(Father, Mother):
    pass

kid = Child()
kid.skills()      # Father ki class se
kid.talents()     # Mother ki class se


# ================================================================
# PART 5: ENCAPSULATION (Data Hiding)
# ================================================================

# Encapsulation - data ko class ke andar "protect" karna, directly
# access na hone dena. Private variables `__` (double underscore) se banate hain.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):            # getter method
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())     # 1300

# print(account.__balance)        # ERROR - directly access nahi kar sakte


# ---- @property decorator (Getter/Setter - Pythonic way) ----
class Employee2:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):                 # getter
        return self.__salary

    @salary.setter
    def salary(self, value):          # setter
        if value > 0:
            self.__salary = value
        else:
            print("Invalid salary")

emp = Employee2(50000)
print(emp.salary)        # getter call (bina parentheses ke!)
emp.salary = 60000        # setter call
print(emp.salary)         # 60000


# ================================================================
# PART 6: POLYMORPHISM
# ================================================================

# Polymorphism - same method name, different classes me alag
# implementation (behavior class ke hisaab se change hota hai)

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(4), Circle(3)]
for shape in shapes:
    print(shape.area())     # same method call, different result


# ================================================================
# PART 7: MAGIC / DUNDER METHODS
# ================================================================

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):              # object ko readable string me print karta hai
        return f"Book: {self.title}, Price: {self.price}"

    def __add__(self, other):        # operator overloading (+)
        return self.price + other.price

    def __eq__(self, other):          # == operator overload
        return self.price == other.price

b1 = Book("Python Basics", 300)
b2 = Book("Advanced Python", 500)

print(b1)               # __str__ call hota hai -> Book: Python Basics, Price: 300
print(b1 + b2)           # __add__ call hota hai -> 800
print(b1 == b2)          # __eq__ call hota hai -> False


# ================================================================
# PART 8: CLASS METHOD vs STATIC METHOD
# ================================================================

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):              # class ke saath kaam karta hai (cls parameter)
        return cls.count

    @staticmethod
    def add(a, b):                    # na self na cls - independent utility function
        return a + b

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())     # 2
print(MyClass.add(5, 3))        # 8


# ================================================================
# PART 9: ABSTRACT CLASSES (using abc module)
# ================================================================

from abc import ABC, abstractmethod

class Shape2(ABC):                     # abstract class - directly object nahi bana sakte
    @abstractmethod
    def area(self):
        pass                            # child class me implement karna zaroori hai

class Rectangle(Shape2):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

r = Rectangle(5, 4)
print(r.area())         # 20

# s = Shape2()           # ERROR - abstract class ka object nahi ban sakta


# ================================================================
# PART 10: COMPOSITION (has-a relationship)
# ================================================================

# Composition - ek class dusri class ka object as attribute rakhti hai

class Engine:
    def start(self):
        print("Engine started")

class Car2:
    def __init__(self):
        self.engine = Engine()          # Car "has-a" Engine

    def start_car(self):
        self.engine.start()
        print("Car is ready to go")

car = Car2()
car.start_car()


# ================================================================
# PART 11: PRACTICE - STACK CLASS (Data Structure using OOP)
# ================================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())      # 3
print(s.peek())      # 2


# ================================================================
# QUICK SUMMARY
# ================================================================
# class / object          -> blueprint aur uska real instance
# __init__                -> constructor, object banate hi run hota hai
# self                    -> current object ko refer karta hai
# Inheritance              -> child class parent ki properties leti hai
# super()                 -> parent class ka constructor/method call karta hai
# Encapsulation            -> __private variables se data hide karna
# @property                -> Pythonic getter/setter
# Polymorphism             -> same method name, different behavior
# __str__, __add__, __eq__ -> dunder/magic methods (operator overloading)
# @classmethod / @staticmethod -> cls-based vs independent methods
# Abstract class (ABC)     -> incomplete blueprint, child ko implement karna padta hai
# Composition              -> ek class dusri class ka object use karti hai (has-a)
# ================================================================

'''


# Python - OOP ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

# Ek Person class banao jisme name aur age attributes ho, aur ek method jo dono print kare.
# __init__ constructor kya hota hai? Example se samjhao.
# Ek Car class banao jisme brand, model, year attributes ho.
# Ek class banao jisme ek method ho jo class ke kisi attribute ko update kare.
# self keyword ka use kya hota hai Python classes me?
# Ek Rectangle class banao jisme length aur width ho, aur area calculate karne wala method ho.
# Ek Circle class banao jisme radius input lekar area aur circumference calculate ho.
# Class attribute aur instance attribute me kya difference hai? Example do.
# Ek BankAccount class banao jisme balance store ho aur deposit/withdraw methods ho.
# Multiple objects ek hi class se banao aur unke attributes alag-alag print karo.

# 🔹 Intermediate Level (11-20)

# Inheritance kya hota hai? Ek Animal parent class aur Dog child class banao.
# super() function ka use kya hai? Example se samjhao.
# Method overriding kya hota hai? Parent aur child class me same method banake demonstrate karo.
# Multiple inheritance ka example banao (do parent classes se ek child class).
# Encapsulation kya hota hai? Private variables (__variable) use karke example do.
# Ek Employee class banao jisme salary private ho aur getter/setter methods se access ho.
# Polymorphism kya hota hai? Different classes me same method name use karke example do.
# __str__ method ka use kya hai? Ek class me implement karke dikhao.
# Class method aur static method me kya difference hai? Example se samjhao.
# Ek Student class banao jisme marks ke basis pe grade calculate karne wala method ho.

# 🔹 Advanced Level (21-30)

# Ek Shape abstract class banao jisme Circle aur Square uska use karke area calculate karein.
# Operator overloading demonstrate karo (__add__ method use karke do objects add karna).
# Ek Library class banao jisme books add/remove/search karne ke methods ho.
# isinstance() aur issubclass() functions ka use karke check karo object/class ka relationship.
# Ek Stack class banao (push, pop, peek, is_empty methods ke saath) - Data Structure implement karo OOP se.
# Ek Queue class banao (enqueue, dequeue methods ke saath).
# Composition demonstrate karo - ek class dusri class ka object as attribute use kare (jaise Car class me Engine object ho).
# __eq__ method overload karo jisse do objects ko compare kiya ja sake (jaise obj1 == obj2).
# Method Resolution Order (MRO) kya hota hai? Multiple inheritance example se samjhao.
# Ek Inventory Management System banao classes use karke (Product class + Inventory class combine karke add/update/remove/search operations).




# Python - 5 Projects (OOP)
# 1️⃣ Bank Management System
# Classes banao: Account (base class) aur SavingsAccount, CurrentAccount (child classes - inheritance use karke):

# Deposit, withdraw, check balance methods
# Encapsulation use karo (balance ko private rakho, getter/setter se access)
# Interest calculation alag method se (SavingsAccount ke liye)
# Multiple accounts (objects) create karke transactions simulate karo
# __str__ method se account details neat format me print karo

# 2️⃣ Library Management System
# Classes banao: Book aur Library:

# Book class me title, author, ISBN, availability status ho
# Library class me books add/remove/search/issue/return karne ke methods ho
# Composition use karo (Library class ke andar Book objects ki list ho)
# Ek member kitni books issue kar sakta hai limit set karo
# Overdue books ke liye fine calculate karne wala method banao

# 3️⃣ E-Commerce Shopping Cart System
# Classes banao: Product, Cart, aur Customer:

# Product class me name, price, quantity ho
# Cart class me products add/remove karo aur total bill calculate karo (composition se)
# Discount apply karne ka method banao (membership type ke basis pe - polymorphism use karke different customer types ke liye)
# Operator overloading use karo (__add__) taki do carts merge ho sake
# Final invoice generate karne wala method banao

# 4️⃣ Vehicle Rental System (Inheritance-Based)
# Base class Vehicle banao aur usse Car, Bike, Truck child classes inherit karein:

# Har vehicle type ka alag rental rate (per day) ho - method overriding use karke
# Rental class banao jo vehicle ko customer ko rent pe de (composition)
# Total rental cost calculate karo (days × rate + late fees agar ho)
# Abstract method use karo (calculate_rate()) jo har child class me alag implement ho

# 5️⃣ School Management System (Multi-Class Combined)
# Classes banao: Person (base class) → Student aur Teacher (inherited classes):

# Student class me marks, attendance, grade calculation ho
# Teacher class me subject, salary, experience ho
# School class banao jo students aur teachers ki lists manage kare (composition)
# Polymorphism use karo - display_info() method har class me alag tarike se implement ho
# Search functionality banao (roll number se student ya name se teacher search karna)

