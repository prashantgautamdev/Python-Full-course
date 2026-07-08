#Variables, Input/Output, Operators

'''
"""
================================================================
    PYTHON NOTES: VARIABLES, INPUT/OUTPUT & OPERATORS
================================================================
"""

# ================================================================
# PART 1: VARIABLES
# ================================================================

# ---- Variable kya hota hai? ----
# Variable ek naam hota hai jo memory me value store karta hai.
# Python me declare karne ke liye koi keyword (int, var) nahi chahiye.

x = 10
name = "Aman"
price = 99.5


# ---- Naming Rules ----
# 1. Sirf letters, digits, underscore (_) allowed
# 2. Number se start nahi ho sakta
# 3. Case-sensitive hota hai (Name != name)
# 4. Reserved keywords use nahi kar sakte (if, for, class, etc.)
# 5. Space allowed nahi

valid_name = 10      # correct
_temp = 20            # correct
# 2value = 30         # ERROR - number se start
# my var = 40         # ERROR - space nahi chalega


# ---- Dynamic Typing ----
# Data type value ke basis pe automatically decide hota hai

x = 10          # int
x = "Hello"     # ab string
x = 3.14        # ab float


# ---- Multiple Assignment ----
a, b, c = 1, 2, 3          # alag-alag values
x = y = z = 100             # same value sabko

# Swapping without third variable
a, b = 5, 10
a, b = b, a                 # ab a=10, b=5


# ---- Variable Scope ----
# Local     -> function ke andar defined, sirf usi me accessible
# Global    -> function ke bahar defined, pure program me accessible
# Nonlocal  -> nested function me outer variable modify karne ke liye

g_var = 10   # global variable

def show():
    global g_var
    g_var = 20   # global variable modify kiya
    print(g_var)


# ---- Mutable vs Immutable ----
# Immutable (change NAHI ho sakte): int, float, str, tuple, bool
# Mutable   (change ho sakte hain): list, dict, set

my_name = "Aman"
# my_name[0] = "B"     # ERROR - string immutable hai

my_list = [1, 2, 3]
my_list[0] = 99         # OK - list mutable hai


# ---- id() aur Memory (Advanced) ----
p = 10
q = 10
print(id(p) == id(q))   # True -> small integers cached (Integer Interning)


# ---- Type Hinting (Advanced) ----
age: int = 25
uname: str = "Aman"
amount: float = 99.9
# Ye Python ko force nahi karta, sirf documentation/readability ke liye


# ================================================================
# PART 2: INPUT / OUTPUT
# ================================================================

# ---- Output: print() ----
print("Hello World")
print("A", "B", "C")               # A B C
print("A", "B", sep="-")           # A-B
print("Hello", end=" ")            # next print same line pe aayega

# Parameters:
#   sep -> values ke beech separator (default = space)
#   end -> line ke end me kya aayega (default = \n)


# ---- Input: input() ----
# name = input("Enter your name: ")
# NOTE: input() HAMESHA STRING return karta hai

# age = input("Enter age: ")         # string milega
# age = int(input("Enter age: "))    # ab integer milega


# ---- Type Casting with Input ----
# a = int(input("Enter a number: "))
# b = float(input("Enter decimal: "))

# Multiple values ek line me:
# a, b = input().split()               # space se split, string me
# a, b = map(int, input().split())     # dono ko int me convert bhi


# ---- String Formatting ----

uname2 = "Aman"
age2 = 20

# 1. f-string (Recommended)
print(f"My name is {uname2} and I am {age2} years old")

# 2. .format() method
print("My name is {} and I am {} years old".format(uname2, age2))

# 3. % operator (old style)
print("My name is %s and I am %d years old" % (uname2, age2))

# Decimal precision control
pi = 3.14159265
print(f"{pi:.2f}")     # 3.14


# ---- Advanced Output ----

# Multiline string
print("""Line 1
Line 2
Line 3""")

# Escape sequences
print("Hello\nWorld")    # \n = new line
print("Name\tAge")       # \t = tab space

# eval() -> input ko expression ki tarah evaluate karta hai
# result = eval(input("Enter expression: "))   # "5+3" input pe 8 milega


# ================================================================
# PART 3: OPERATORS
# ================================================================

# ---- 1. Arithmetic Operators ----
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division (float result)
# //  Floor Division (integer result)
# %   Modulus (remainder)
# **  Exponent (power)

print(10 / 3)     # 3.333...
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 5)     # 32

# Advanced: negative numbers ke saath // floor towards -infinity
print(-7 // 2)    # -4 (na ki -3)


# ---- 2. Comparison (Relational) Operators ----
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal
# <=   Less than or equal

print(5 == 5)     # True
print(5 != 3)     # True


# ---- 3. Logical Operators ----
# and   Dono conditions true honi chahiye
# or    Koi ek condition true ho
# not   Condition reverse karta hai

val = 5
print(val > 2 and val < 10)   # True
print(val > 2 or val > 100)   # True
print(not (val > 2))          # False


# ---- 4. Assignment Operators ----
# =    x = 5
# +=   x = x + 3
# -=   x = x - 3
# *=   x = x * 3
# /=   x = x / 3
# //=  x = x // 3
# %=   x = x % 3
# **=  x = x ** 3


# ---- 5. Bitwise Operators (Advanced) ----
# &   AND
# |   OR
# ^   XOR
# ~   NOT (complement)
# <<  Left shift
# >>  Right shift

bit_a = 5   # binary: 101
bit_b = 3   # binary: 011

print(bit_a & bit_b)    # 1  (001)
print(bit_a | bit_b)    # 7  (111)
print(bit_a ^ bit_b)    # 6  (110)
print(bit_a << 1)       # 10 (left shift = multiply by 2)
print(bit_a >> 1)       # 2  (right shift = divide by 2)


# ---- 6. Identity Operators ----
# is       Same object hai ya nahi (memory reference check)
# is not   Different object hai

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True  (values same)
print(list1 is list2)   # False (different memory location)


# ---- 7. Membership Operators ----
# in       Element present hai ya nahi
# not in   Element present nahi hai

lst = [1, 2, 3]
print(2 in lst)         # True
print(5 not in lst)     # True


# ---- Operator Precedence (Advanced) ----
# Order High -> Low:
# 1.  ()                     Parentheses
# 2.  **                     Exponent
# 3.  +x, -x, ~x             Unary operators
# 4.  *, /, //, %            Multiplicative
# 5.  +, -                   Additive
# 6.  <<, >>                 Bitwise Shift
# 7.  &                      Bitwise AND
# 8.  ^                      Bitwise XOR
# 9.  |                      Bitwise OR
# 10. ==, !=, >, <, >=, <=   Comparison
# 11. not                    Logical NOT
# 12. and                    Logical AND
# 13. or                     Logical OR
# 14. =, +=, -=, etc.        Assignment

result = 10 + 2 * 3 ** 2    # ** pehle, fir *, fir +
print(result)               # 10 + 2*9 = 10+18 = 28


# ---- Walrus Operator := (Python 3.8+) (Advanced) ----
# Assignment aur expression evaluation ek saath karta hai

# Normal way:
# n = int(input())
# if n > 10:
#     print("Big")

# Walrus operator way:
# if (n := int(input())) > 10:
#     print("Big")


# ---- Chained Comparison ----
cx = 5
print(1 < cx < 10)    # True (1<5 and 5<10 dono check hote hain)


# ================================================================
# QUICK SUMMARY
# ================================================================
# Variables       -> Dynamic typing, no declaration needed
# Mutable/Immutable-> list/dict mutable, str/tuple/int immutable
# Input            -> Always returns string, type cast as needed
# Output           -> f-strings best hain formatting ke liye
# Operators        -> Precedence yaad rakho, / vs // ka difference
# Bitwise          -> Advanced topic, binary logic samjhna zaroori
# is vs ==         -> is memory check karta hai, == value check karta hai
# ================================================================

'''


# Section A: Variables (Q1–25)


''' Ek variable banao jisme apna naam store ho, aur usse print karo.'''


'''Ek variable age banao jisme aap apni age store karo aur print karo.'''


'''Do variables a aur b banao jisme 10 aur 20 store karo, dono ko ek hi print statement me print karo.'''


'''Ek program likho jo teen variables x, y, z ko ek line me assign kare (x, y, z = 1, 2, 3).'''


'''Ek variable city banao, uski value change karo aur dono values print karo.'''


'''Variable ka data type check karo type() function use karke (int, str, float ke liye).'''


'''Integer, float, string, aur boolean — chaaron type ke variables banao aur print karo.'''


'''Ek variable me integer store karo, phir usi variable me string assign karo — kya hota hai check karo.'''


# ye to ek set ban ja rah ahai

'''id() function use karke kisi variable ka memory address print karo.'''


'''Multiple variables ko same value assign karo (a = b = c = 100) aur print karo'''


'''Global variable aur local variable ka example likho.'''


# yeha a,b ye dono globle variabale hai and d ek local varsariabale hai 

    
# '''global keyword ka use karke ek function ke andar global variable modify karo.'''


'''Ek variable banao jiska naam invalid ho (jaise 1name) aur error dekho, phir sahi naam use karo.'''


'''Constant variable (convention se, jaise PI = 3.14) banao aur use karo.'''


'''Swap two variables without using a third variable.'''


'''Swap two variables using a third (temporary) variable.'''


'''Variable naming rules explain karte hue 5 valid aur 5 invalid variable names likho.'''


'''del statement use karke ek variable delete karo aur usse access karne ki koshish karo.'''


'''Ek variable me list store karo aur uske elements print karo.'''


# '''Dynamic typing dikhane ke liye ek variable ko baar-baar different data types assign karo.'''


'''Two numbers ko variables me store karke unka sum ek third variable me store karo.'''


'''String variable banao aur usko number ke sath concatenate karne ki koshish karo (error dekho).'''


'''type() aur isinstance() dono se variable ka type check karo.'''


'''Underscore variable naming (_temp, my_var) ka example likho.'''


'''Ek variable me apna pura naam, age, aur city ek dictionary ke form me store karo.'''


# Section B: Input / Output (Q26–55)


'''input() se user ka naam lo aur "Hello, <naam>" print karo.'''


'''User se do numbers lo aur unka sum print karo.'''


'''input() se li gayi value ka default type kya hota hai — check karo.'''


'''String input ko int() me convert karke ek number ke sath add karo.'''


'''User se apni age lo aur "Aapki age X saal hai" print karo.'''


'''print() me multiple arguments comma se separate karke print karo.'''


'''print() function me sep parameter use karke output format karo.'''


'''print() function me end parameter use karke line break avoid karo.'''


'''Formatted string (f-string) use karke naam aur age ek sath print karo.'''


'''.format() method use karke output print karo.'''


'''% operator (old style formatting) use karke output print karo.'''


'''User se 3 numbers lo (ek hi line me space se separated) aur unka average print karo.'''


'''split() function use karke ek line se multiple inputs lo'''


'''User se float value lo aur usko 2 decimal places tak print karo.'''


'''Multi-line string print karo triple quotes use karke.'''


# i miss u
# '''


'''Ek program likho jo user se 5 numbers lekar unka sum aur average print kare'''


'''print() me tab space (\t) aur newline (\n) ka use karo.'''


'''User se ek sentence lo aur usme total characters count karo.'''


'''
print() statement me variable, string aur expression ek sath use karo.'''


'''User se input lekar usko reverse karke print karo (string reverse).'''


'''Escape sequences (\n, \t, \\, \") ka use karke output print karo.'''


'''User se 3 subjects ke marks lo aur total, percentage print karo.'''


'''input() se list ke elements lo (comma separated) aur unko list me store karo.'''


'''
Program likho jo user ka naam, age, aur email lekar ek profile card print kare'''


'''f-string me expression directly use karo (jaise f"Sum = {a+b}").'''


'''User se temperature Celsius me lo aur usko Fahrenheit me convert karke print karo'''


# Section C: Arithmetic Operators (Q56–70)


'''Do numbers lo aur unka sum, difference, product, quotient print karo.'''


'''Modulus operator (%) use karke ek number even ya odd check karo.'''


'''Exponent operator (**) use karke kisi number ka square aur cube nikaalo.'''


'''Floor division (//) aur normal division (/) ka difference dikhane wala program likho.'''


'''Ek number ke digits ka sum nikaalo arithmetic operators use karke'''

# User se number lo


'''Simple interest calculate karo formula SI = (P*R*T)/100 use karke.'''


'''Area of rectangle nikaalo user se length aur width lekar.'''


# # Area calculate karo


'''Circle ka area aur circumference nikaalo radius lekar.'''


'''Ek number ka reverse nikaalo (jaise 123 → 321) using arithmetic operators.'''


'''Percentage calculate karo do numbers ke beech.'''


'''BMI (Body Mass Index) calculate karo weight aur height lekar'''


'''Compound expression evaluate karo: result = (a + b) * c - d / e.'''


'''Two numbers ke LCM aur HCF nikaalne ka basic arithmetic approach likho.'''


'''Simple discount calculator banao (price aur discount % lekar final price nikaalo).'''


# # Discount amount

# # Final price


# Section D: Comparison & Logical Operators (Q71–85)

'''Do numbers compare karo (==, !=, >, <, >=, <=) aur result print karo.'''


'''or operator use karke check karo ki number even hai ya negative hai.'''


'''not operator use karke boolean value ko invert karo.'''


'''Ek number positive, negative, ya zero hai — comparison operators se check karo.'''


'''Teen numbers me sabse bada number nikaalo comparison operators use karke.'''


'''Age input lekar check karo ki person voting ke liye eligible hai (age >= 18) ya nahi.'''


'''Do strings compare karo == operator se (case-sensitive check).'''


'''Logical operators combine karke complex condition likho (jaise a > 5 and b < 10 or c == 0).'''


# # Complex condition

'''Leap year check karne ka logical condition likho (year % 4 == 0 and year % 100 != 0 or year % 400 == 0).'''


'''Character ek vowel hai ya nahi check karo or operator use karke.'''


'''Number ek range (10 se 50) ke beech hai ya nahi check karo.'''


'''Do boolean variables banao aur unpar and, or, not apply karo.'''


'''Password aur confirm password match karte hain ya nahi check karo (== operator).'''


'''Comparison chaining ka example likho (jaise 1 < 2 < 3).'''


# Section E: Assignment, Bitwise & Identity/Membership Operators (Q86–100)


'''Assignment operators (+=, -=, *=, /=, %=) ka use karke ek variable update karo.'''


'''**= aur //= operators ka use karke examples likho.'''


'''Bitwise AND (&) operator use karke do numbers ka result nikaalo.'''


'''Bitwise OR (|) operator use karke do numbers ka result nikaalo.'''


'''Bitwise XOR (^) operator ka example likho.'''


'''Bitwise NOT (~) operator use karke ek number ka result nikaalo.'''


'''Left shift (<<) aur right shift (>>) operators ka example likho.'''


'''is operator use karke check karo ki do variables same object ko refer karte hain ya nahi.'''


'''is not operator ka example likho.'''


'''in operator use karke check karo ki ek character kisi string me maujood hai ya nahi.'''


'''not in operator use karke check karo ki ek element kisi list me nahi hai.'''


'''Ek program likho jisme sabhi operator types (arithmetic, comparison, logical, assignment, bitwise, identity, membership) ek sath use ho.'''


'''Operator precedence dikhane wala expression likho (jaise 2 + 3 * 4 ** 2 % 5) aur result predict karke verify karo.'''


'''+= operator use karke ek string ko baar-baar concatenate karo (loop ke bina, sirf repeat karke).'''


'''Ek mini-program banao: user se 2 numbers aur operation choice (1-Add, 2-Sub, 3-Mul, 4-Div) lekar result print karo using if-elif aur arithmetic operators'''


'''Project'''


# 1️⃣ Real-Time Currency & Unit Converter Suite
# Ek program jo user se do inputs le - amount aur conversion type ka number (1, 2, 3...) - aur multiple conversions ek saath calculate kare using arithmetic operators: currency (INR→USD, USD→EUR), temperature (C→F→K), aur distance (km→miles→meters) - sab ek hi output me formatted print ho.
# Advanced twist: f-strings se multi-line formatted receipt-style output banao, decimal precision (.2f) control karo.


# 2️⃣ Loan EMI & Amortization Calculator
# User se principal amount, interest rate, aur tenure (months) input lekar EMI formula apply karo:


# 3️⃣ Student Result & Percentage Analyzer
# 5 subjects ke marks input lekar total, percentage, average, aur grade points (GPA style) calculate karo bitwise/arithmetic operators combine karke - jaise highest/lowest marks nikalna comparison operators se (bina if-else, sirf max()/min() built-in ya arithmetic tricks se).
# Advanced twist: Weighted percentage (kuch subjects ka weightage zyada) calculate karna multiplication operators se.


# 4️⃣ Cryptography - Simple Caesar Cipher (Encoder)
# User se ek message (string) aur shift number input lekar, ASCII values (ord(), chr()) aur arithmetic operators (+, %) use karke encrypted message generate karo.
# Formula: new_char = chr((ord(char) - 65 + shift) % 26 + 65)
# Advanced twist: Modulo operator ka real-world encryption logic me use, ASCII manipulation.


# 5️⃣ Bank Account Interest & Tax Simulator
# User se principal, rate of interest, number of years, aur tax bracket % input lekar:

# Simple Interest aur Compound Interest dono calculate karo
# Compound interest par tax deduct karo
# Net amount in-hand vs gross amount ka comparison formatted output me dikhao
# Advanced twist: Multiple formulas ek saath, nested arithmetic expressions, precise decimal formatting (round(), f-strings).
