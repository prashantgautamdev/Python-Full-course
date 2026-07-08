'''loop'''


'''

"""
================================================================
    PYTHON NOTES: LOOPS
================================================================
"""

# ================================================================
# PART 1: LOOPS KYA HOTE HAIN?
# ================================================================

# Loop ek code block ko baar-baar execute karne ke liye use hota hai
# jab tak koi condition True rehti hai ya ek fixed range tak.
#
# Python me do main types ke loops hote hain:
#   1. for loop
#   2. while loop


# ================================================================
# PART 2: for LOOP
# ================================================================

# for loop tab use hota hai jab humein pata ho kitni baar iterate
# karna hai (jaise ek list, string, ya range ke through).

# ---- range() function ----
# range(stop)              -> 0 se stop-1 tak
# range(start, stop)       -> start se stop-1 tak
# range(start, stop, step) -> step ke hisaab se increment/decrement

for i in range(5):
    print(i)              # 0 1 2 3 4

for i in range(1, 6):
    print(i)              # 1 2 3 4 5

for i in range(10, 0, -2):
    print(i)              # 10 8 6 4 2 (reverse counting)


# ---- for loop with list ----
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)


# ---- for loop with string ----
for ch in "Python":
    print(ch)              # P y t h o n (character by character)


# ---- enumerate() with for loop ----
# index ke saath value bhi milta hai
for index, fruit in enumerate(fruits):
    print(index, fruit)     # 0 apple, 1 banana, 2 mango


# ================================================================
# PART 3: while LOOP
# ================================================================

# while loop tab use hota hai jab humein exact iterations pata nahi
# hote - condition True hone tak chalta rehta hai.

n = 1
while n <= 5:
    print(n)
    n += 1                  # increment zaroori hai, warna infinite loop

# ---- Infinite Loop (careful!) ----
# while True:
#     print("This runs forever unless break is used")


# ================================================================
# PART 4: break, continue, else (with loops)
# ================================================================

# ---- break ----
# Loop ko turant rok deta hai (chahe condition abhi True ho)
for i in range(10):
    if i == 5:
        break
    print(i)                # 0 1 2 3 4 (5 pe ruk gaya)


# ---- continue ----
# Current iteration skip karke next iteration pe chala jata hai
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)                # 1 3 5 7 9 (even numbers skip ho gaye)


# ---- else with loop ----
# Loop ke saath else block bhi likh sakte hain - ye tab run hota hai
# jab loop bina break hue completely khatam ho jaye

for i in range(5):
    print(i)
else:
    print("Loop completed without break")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because break was used")


# ================================================================
# PART 5: NESTED LOOPS (loop ke andar loop)
# ================================================================

# Outer loop ek baar chalta hai, uske andar inner loop pura chalta hai

for i in range(3):
    for j in range(3):
        print(i, j)

# Nested loop ka common use: patterns, matrix, tables


# ================================================================
# PART 6: LOOP CONTROL PATTERNS (Common Logic)
# ================================================================

# ---- Multiplication Table ----
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


# ---- Sum of numbers using loop ----
total = 0
for i in range(1, 11):
    total += i
print(total)          # 55


# ---- Factorial using loop ----
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)            # 120


# ---- Reverse a number using while loop ----
num = 1234
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(reversed_num)     # 4321


# ---- Fibonacci Series ----
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b       # 0 1 1 2 3 5 8 13 21 34


# ---- Star Pyramid Pattern ----
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****


# ---- Inverted Pyramid Pattern ----
for i in range(rows, 0, -1):
    print("*" * i)


# ---- Number Pattern (1, 12, 123...) ----
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Output:
# 1
# 12
# 123
# 1234
# 12345


# ---- Prime Numbers in a Range ----
def print_primes(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

print_primes(1, 50)


# ================================================================
# QUICK SUMMARY
# ================================================================
# for loop        -> jab iterations ki known count ho (list, range, string)
# while loop       -> jab condition-based repetition ho (unknown count)
# break            -> loop ko turant terminate karta hai
# continue         -> current iteration skip karta hai
# else with loop   -> tab run hota hai jab loop bina break ke complete ho
# nested loop      -> loop ke andar loop, patterns/matrix ke liye useful
# range(start, stop, step) -> loop control ka core function
# ================================================================


'''
 

#  Basic Level (1-10)

'''1 se 10 tak numbers print karo for loop se.'''


# 1 se N tak numbers print karo while loop se.


# 10 se 1 tak reverse counting print karo.


# 1 se 100 tak saare even numbers print karo.


# 1 se 100 tak saare odd numbers print karo.


# Ek number input lekar uski table (multiplication table) print karo.


# 1 se N tak numbers ka sum nikalo loop se.


# Ek word ko loop se character by character print karo.


# 5 baar "Hello World" print karo loop use karke.


# 1 se 10 tak numbers print karo but sirf multiples of 3 skip karke.


# 🔹 Intermediate Level (11-20)

# Ek number input lekar uski factorial calculate karo.


# Ek number input lekar check karo ki wo prime hai ya nahi (loop se).


# Fibonacci series print karo N terms tak.


'''Ek number ke saare factors print karo.'''


# 1 se N tak numbers me se sirf prime numbers print karo.


'''Ek number input lekar uske digits ka sum nikalo.'''


# Ek number reverse karo loop se (jaise 123 → 321).


# Ek number input lekar check karo ki wo Armstrong number hai ya nahi.
# Sum of squares of first N natural numbers nikalo.
# Ek list ke elements ka sum aur average nikalo loop se.

# 🔹 Advanced Level (21-30)

# Star pattern print karo (simple pyramid - jaise 5 rows ka triangle).
# Number pattern print karo (jaise 1, 12, 123, 1234...).
# Inverted pyramid pattern print karo stars se.
# Multiplication table 1 se 10 tak print karo (nested loop se).
# GCD (HCF) of two numbers nikalo loop se.
# LCM of two numbers nikalo loop se.
# Ek number input lekar check karo ki wo perfect number hai ya nahi.
# Diamond pattern print karo stars se (nested loops).
# Ek string ke saare palindrome substrings find karo (nested loop se).
# Simple guessing game banao - computer ek random number soche, user guess kare jab tak correct na ho (attempts count kare).


# Python - 5 Projects (Loops)
# 1️⃣ Number Guessing Game with Hints
# Computer ek random number (1-100) generate kare. User loop me tab tak guess kare jab tak correct answer na mile:

# Har wrong guess pe "Too High" ya "Too Low" hint do
# Total attempts count karo
# Agar 10 attempts ke andar guess na ho to "Game Over" print karo

# 2️⃣ Multiplication Table Generator (Custom Range)
# User se number, start range, aur end range input lekar us number ki table sirf given range ke beech print karo (jaise sirf 5 se 10 tak table dikhao).
# Extra feature: Multiple numbers ki tables ek saath print karna (nested loop se), formatted grid style output ke saath.
# 3️⃣ Pattern Printing Menu System
# User ko menu dikhao (loop se):

# Pyramid pattern
# Inverted pyramid
# Diamond pattern
# Number pattern
# Pascal's triangle (basic)
# User apna choice input kare aur rows input kare, program corresponding pattern print kare. Program tab tak chalta rahe jab tak user "Exit" na choose kare (loop + menu combine).

# 4️⃣ Prime Numbers & Factors Explorer
# User se ek range input lekar (start, end):

# Us range me saare prime numbers print karo
# Har number ke factors bhi dikhao
# Total prime numbers ki count aur unka sum bhi calculate karo
# Nested loops ka heavy use - outer loop range ke liye, inner loop primality check ke liye.

# 5️⃣ ATM Simulation with Retry Loop
# ATM system banao jisme:

# User PIN enter kare, agar 3 baar tak wrong PIN dale to account block ho jaye (loop + counter)
# Correct PIN ke baad menu loop chale (Balance Check, Deposit, Withdraw, Exit) jab tak user "Exit" na choose kare
# Withdraw karte time agar balance insufficient ho to error dikhakar dobara try karne do
