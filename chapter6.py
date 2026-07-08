# '''function'''

'''
"""
================================================================
    PYTHON NOTES: FUNCTIONS
================================================================
"""

# ================================================================
# PART 1: FUNCTION BASICS
# ================================================================

# ---- Function kya hoti hai? ----
# Function ek reusable code block hai jo ek specific task perform
# karta hai. `def` keyword se define hoti hai.

def greet():
    print("Hello, Welcome!")

greet()      # function call


# ---- Function with Parameters ----
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Aman")


# ---- Function with Return Value ----
def add(a, b):
    return a + b

result = add(5, 3)
print(result)      # 8

# NOTE: return function ko turant terminate kar deta hai aur value
# wapas bhejta hai. print() sirf display karta hai, return nahi karta.


# ---- Function with Multiple Return Values ----
def calculate(a, b):
    return a + b, a - b, a * b

sum_val, diff_val, prod_val = calculate(10, 5)
print(sum_val, diff_val, prod_val)     # 15 5 50 (tuple ki tarah return hota hai)


# ================================================================
# PART 2: PARAMETERS - TYPES
# ================================================================

# ---- Default Parameters ----
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()             # Hello, Guest!
greet("Riya")        # Hello, Riya!


# ---- Positional Arguments ----
def student_info(name, age):
    print(name, age)

student_info("Aman", 20)     # order matter karta hai


# ---- Keyword Arguments ----
student_info(age=20, name="Aman")     # order matter nahi karta


# ---- *args (Variable number of positional arguments) ----
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))          # 6
print(add_all(1, 2, 3, 4, 5))    # 15 (kitne bhi arguments de sakte ho)


# ---- **kwargs (Variable number of keyword arguments) ----
def print_info(**details):
    for key, value in details.items():
        print(key, ":", value)

print_info(name="Aman", age=20, city="Delhi")


# ---- *args aur **kwargs dono ek saath ----
def mixed_function(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

mixed_function(1, 2, 3, name="Aman", age=20)


# ================================================================
# PART 3: VARIABLE SCOPE (LOCAL vs GLOBAL)
# ================================================================

x = 10   # global variable

def show_global():
    print(x)     # global variable ko read kar sakte hain

def modify_global():
    global x
    x = 20        # global keyword se global variable modify hota hai

def local_example():
    y = 5         # ye sirf function ke andar accessible hai (local)
    print(y)

# print(y)        # ERROR - y function ke bahar accessible nahi hai


# ================================================================
# PART 4: LAMBDA FUNCTIONS (Anonymous Functions)
# ================================================================

# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(square(5))          # 25

multiply = lambda a, b: a * b
print(multiply(3, 4))     # 12

# Lambda mostly map(), filter(), sorted() ke saath use hoti hai


# ================================================================
# PART 5: map(), filter(), reduce()
# ================================================================

nums = [1, 2, 3, 4, 5]

# ---- map() -> har element pe function apply karta hai ----
squared = list(map(lambda x: x ** 2, nums))
print(squared)              # [1, 4, 9, 16, 25]

# ---- filter() -> condition satisfy karne wale elements filter karta hai ----
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)            # [2, 4]

# ---- reduce() -> saare elements ko ek single value me combine karta hai ----
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
print(product)              # 120 (1*2*3*4*5)


# ================================================================
# PART 6: RECURSION
# ================================================================

# ---- Recursion kya hai? ----
# Jab function khud ko call karta hai, tab use recursion kehte hain.
# Har recursive function me ek "base case" hona zaroori hai, warna
# infinite recursion ho jayega (RecursionError).

# ---- Factorial using Recursion ----
def factorial(n):
    if n == 0 or n == 1:    # base case
        return 1
    return n * factorial(n - 1)    # recursive call

print(factorial(5))    # 120


# ---- Fibonacci using Recursion ----
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))    # 8


# ---- GCD using Recursion ----
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))    # 6


# ---- Sum of Digits using Recursion ----
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))    # 10


# ================================================================
# PART 7: CLOSURES (Advanced - Nested Functions)
# ================================================================

# Closure - jab ek inner function outer function ke variable ko
# "remember" rakhta hai, chahe outer function execution khatam ho jaye

def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    return inner_function

my_func = outer_function("Hello Closure")
my_func()     # Message: Hello Closure


# ---- Counter using Closure ----
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter())    # 1
print(my_counter())    # 2
print(my_counter())    # 3


# ================================================================
# PART 8: DECORATORS (Advanced)
# ================================================================

# Decorator ek function hai jo dusre function ko "wrap" karta hai
# aur uske behavior ko modify/extend karta hai (bina original function
# ko change kiye).

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call


# ---- Decorator to measure execution time ----
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.5f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    print("Function finished")

slow_function()


# ================================================================
# PART 9: GENERATOR FUNCTIONS (Advanced)
# ================================================================

# Generator functions `yield` use karte hain aur values one-by-one
# generate karte hain (memory efficient - pura list store nahi hota)

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(10):
    print(num, end=" ")     # 0 1 1 2 3 5 8 13 21 34


# ================================================================
# PART 10: DOCSTRINGS
# ================================================================

def add_numbers(a, b):
    """
    Ye function do numbers ka sum return karti hai.
    Parameters: a (int), b (int)
    Returns: int
    """
    return a + b

print(add_numbers.__doc__)    # docstring print karta hai


# ================================================================
# QUICK SUMMARY
# ================================================================
# def func():           -> basic function definition
# return                -> value wapas bhejta hai (print() se alag hai)
# default parameters    -> def func(x=5)
# *args                 -> multiple positional arguments (tuple ki tarah)
# **kwargs              -> multiple keyword arguments (dict ki tarah)
# lambda                -> one-line anonymous function
# map/filter/reduce     -> functional programming tools
# recursion             -> function khud ko call karta hai (base case zaroori)
# closure               -> inner function outer variable "remember" karta hai
# decorator             -> function ko wrap karke behavior extend karta hai
# generator (yield)     -> memory-efficient tarike se values generate karta hai
# ================================================================

'''

# Python - Function ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

# Ek function banao jo do numbers ka sum return kare.
# Ek function banao jo ek number input lekar check kare ki wo even hai ya odd.
# Ek function banao jo ek number ka square return kare.
# Ek function banao jo user ko greet kare (name parameter lekar).
# Ek function banao without parameters jo simple message print kare.
# Ek function banao jo do numbers me se bada number return kare.
# Ek function banao jo teen numbers ka average calculate kare.
# Ek function banao jo ek number ka factorial calculate kare.
# Ek function banao jo ek number positive, negative ya zero hai check kare.
# Ek function banao jo Celsius ko Fahrenheit me convert kare.

# 🔹 Intermediate Level (11-20)

# Ek function banao jo default parameter use kare (jaise greet(name="Guest")).
# Ek function banao jo variable number of arguments accept kare (*args use karke).
# Ek function banao jo keyword arguments accept kare (**kwargs use karke).
# Ek function banao jo ek list accept kare aur uska sum return kare.
# Ek function banao jo string reverse kare aur return kare.
# Ek function banao jo check kare ki number prime hai ya nahi.
# Ek function banao jo ek list me se largest number find kare.
# Ek function banao jo recursion use karke factorial calculate kare.
# Ek function banao jo recursion use karke Fibonacci series ka Nth term nikale.
# Ek function banao jo multiple values return kare (tuple ki tarah).

# 🔹 Advanced Level (21-30)

# Ek function banao jo lambda function use karke do numbers multiply kare.
# Ek function banao jo map() aur lambda use karke list ke saare elements square kare.
# Ek function banao jo filter() aur lambda use karke list se sirf even numbers filter kare.
# Ek function banao jo GCD (HCF) calculate kare recursion use karke.
# Ek function banao jo palindrome check kare (string input lekar).
# Ek function banao jo nested function use kare (inner function outer ke variable access kare - closure concept).
# Ek function banao jo *args aur **kwargs dono ek saath use kare.
# Ek function banao jo decorator pattern use kare (simple example - kisi function ka execution time print kare).
# Ek function banao jo global aur local variable scope demonstrate kare.
# Ek function banao jo recursion use karke ek number ke digits ka sum nikale.


# Python - 5 Projects (Functions)
# 1️⃣ Modular Calculator with Function Library
# Har operation (add, subtract, multiply, divide, power, modulus) ke liye alag function banao. Ek main function menu dikhaye jo user ke choice ke basis pe corresponding function call kare:

# Har function proper error handling kare (jaise divide by zero)
# History track karo (list me results store karke) - function ke through
# Ek function banao jo history print kare

# 2️⃣ Recursive Math Toolkit
# Recursion use karke multiple math functions banao ek hi program me:

# Factorial calculator
# Fibonacci series generator (Nth term)
# GCD/HCF calculator
# Sum of digits calculator
# Power calculator (x^n recursion se, bina ** operator use kiye)
# Har function reusable ho aur main program menu se koi bhi function call kar sake.

# 3️⃣ Text Processing Toolkit (Function-Based)
# Multiple functions banao jo ek text processing tool jaisa kaam karein:

# count_vowels(text) - vowels count kare
# count_words(text) - words count kare
# reverse_text(text) - text reverse kare
# is_palindrome(text) - palindrome check kare
# capitalize_words(text) - har word capitalize kare
# Sab functions ko combine karke ek main function banao jo pura analysis report generate kare.

# 4️⃣ Student Grade Management System (Function-Based)
# Functions banao:

# calculate_total(marks_list) - total marks nikale
# calculate_percentage(total, max_marks) - percentage nikale
# assign_grade(percentage) - grade decide kare
# check_pass_fail(percentage) - pass/fail decide kare
# generate_report(name, marks_list) - sab functions combine karke ek complete report print kare
# Multiple students ka data process karo functions reuse karke.

# 5️⃣ Functional Data Processor (map/filter/lambda based)
# Ek list of numbers ya list of dictionaries (student data) input lekar:

# map() + lambda se saare numbers ka square/cube nikalo
# filter() + lambda se sirf even numbers ya passing students filter karo
# Custom function se data ko sort karo (jaise marks ke basis pe)
# Higher-order function banao jo koi bhi operation (add/multiply/square) parameter ke roop me function accept kare aur apply kare


