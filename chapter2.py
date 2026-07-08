'''Strings''' 

'''

"""
================================================================
    PYTHON NOTES: STRINGS
================================================================
"""

# ================================================================
# PART 1: STRING BASICS
# ================================================================

# ---- String kya hoti hai? ----
# String characters ka sequence hoti hai, single ('') ya double ("")
# quotes ke andar likhi jaati hai.

s1 = 'Hello'
s2 = "World"
s3 = """Multiline
string"""


# ---- String Immutable hoti hai ----
# Ek baar create hone ke baad string ko modify nahi kar sakte

name = "Aman"
# name[0] = "B"     # ERROR - string immutable hai

# Naya string banega, purana change nahi hoga
name = "B" + name[1:]   # "Bman"


# ---- Indexing ----
# Positive indexing: 0 se start (left se right)
# Negative indexing: -1 se start (right se left)

word = "Python"
print(word[0])     # P
print(word[-1])    # n
print(word[2])     # t


# ---- Slicing ----
# syntax: string[start:stop:step]

word = "Python"
print(word[0:3])    # Pyt
print(word[:3])      # Pyt   (start default 0)
print(word[3:])      # hon   (stop default end)
print(word[::-1])    # nohtyP  (reverse)
print(word[::2])     # Pto   (every 2nd char)


# ---- Concatenation & Repetition ----
a = "Hello"
b = "World"
print(a + " " + b)    # Hello World
print(a * 3)          # HelloHelloHello


# ---- len() function ----
print(len("Python"))    # 6


# ================================================================
# PART 2: STRING METHODS
# ================================================================

# ---- Case Conversion ----
text = "Hello World"
print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.title())         # Hello World (har word capital)
print(text.capitalize())    # Hello world (sirf pehla letter)
print(text.swapcase())      # hELLO wORLD


# ---- Whitespace Handling ----
padded = "   Hello   "
print(padded.strip())       # "Hello" (dono taraf se space hatao)
print(padded.lstrip())      # "Hello   " (left se)
print(padded.rstrip())      # "   Hello" (right se)


# ---- Searching ----
sentence = "Python is fun and Python is powerful"
print(sentence.find("Python"))     # 0 (first occurrence index)
print(sentence.rfind("Python"))    # 18 (last occurrence index)
print(sentence.index("is"))        # 7 (find jaisa hi but error deta hai agar na mile)
print(sentence.count("Python"))    # 2 (kitni baar aaya)


# ---- Checking Content ----
print("hello".startswith("he"))    # True
print("hello".endswith("lo"))      # True
print("123".isdigit())              # True
print("abc".isalpha())              # True
print("abc123".isalnum())           # True
print("   ".isspace())              # True
print("Hello".isupper())            # False
print("HELLO".isupper())            # True


# ---- Replace ----
msg = "I like cats"
print(msg.replace("cats", "dogs"))    # I like dogs


# ---- Split & Join ----
sentence = "Python is a great language"
words = sentence.split()            # ['Python', 'is', 'a', 'great', 'language']
print(words)

csv_line = "a,b,c,d"
print(csv_line.split(","))          # ['a', 'b', 'c', 'd']

word_list = ["Python", "is", "fun"]
print(" ".join(word_list))          # Python is fun
print("-".join(word_list))          # Python-is-fun


# ---- Alignment ----
print("hi".center(10, "*"))    # ****hi****
print("hi".ljust(10, "-"))     # hi--------
print("hi".rjust(10, "-"))     # --------hi
print("7".zfill(3))            # 007


# ================================================================
# PART 3: STRING FORMATTING
# ================================================================

name = "Aman"
age = 20

# 1. f-string (Recommended - fastest & most readable)
print(f"My name is {name} and I am {age} years old")
print(f"{age:.2f}")            # decimal precision

# 2. .format() method
print("My name is {} and I am {}".format(name, age))
print("{0} is {1}, {0} is happy".format(name, age))    # positional index reuse

# 3. % operator (old style)
print("My name is %s and I am %d years old" % (name, age))


# ---- Escape Sequences ----
print("Hello\nWorld")     # \n -> new line
print("Name\tAge")        # \t -> tab
print("She said \"Hi\"")  # \" -> double quote inside string
print('It\'s okay')       # \' -> single quote inside string
print("Path: C:\\Users")  # \\ -> backslash


# ---- Raw Strings ----
# Escape sequences ko ignore karta hai
path = r"C:\\Users\\new_folder"
print(path)     # C:\\Users\\new_folder (as-is print hoga)


# ================================================================
# PART 4: STRING & ASCII / UNICODE
# ================================================================

print(ord('A'))     # 65  (character -> ASCII number)
print(chr(65))       # A   (ASCII number -> character)

# Caesar Cipher basic logic (shift by 1)
char = 'A'
shifted = chr((ord(char) - 65 + 1) % 26 + 65)
print(shifted)       # B


# ================================================================
# PART 5: COMMON STRING ALGORITHMS (Practice Logic)
# ================================================================

# ---- Reverse a string ----
s = "hello"
print(s[::-1])                  # slicing method

reversed_str = ""
for ch in s:
    reversed_str = ch + reversed_str
print(reversed_str)             # loop method


# ---- Palindrome Check ----
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("madam"))          # True
print(is_palindrome("A man a plan a canal Panama"))   # True


# ---- Count Vowels ----
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))     # 3


# ---- Anagram Check ----
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))   # True


# ---- Character Frequency Count ----
def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("hello"))    # {'h':1,'e':1,'l':2,'o':1}


# ---- Longest Word in a Sentence ----
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("I love programming in Python"))   # programming


# ---- String Compression ----
def compress(text):
    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1
    result += text[-1] + str(count)
    return result

print(compress("aaabbbcc"))    # a3b3c2


# ---- Word-by-word Reverse ----
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("Hello World Python"))   # Python World Hello


# ================================================================
# QUICK SUMMARY
# ================================================================
# String is Immutable       -> hamesha naya string banta hai modify pe
# Indexing                  -> positive (0,1,2..) & negative (-1,-2..)
# Slicing                   -> str[start:stop:step]
# f-string                  -> best formatting method (fastest, readable)
# split() / join()          -> string <-> list conversion
# ord() / chr()             -> character <-> ASCII conversion
# raw string r""            -> escape sequences ignore karta hai
# Common patterns            -> palindrome, anagram, frequency count,
#                               reverse, compression - sab practice zaroor karo
# ================================================================

'''


# 🔹 Basic Level (1-10)

'''Ek string input lekar uski length print karo (bina len() use kiye, loop se count karo).'''


'''Ek string ko reverse karo (slicing use karke).'''


'''Check karo ki given string palindrome hai ya nahi.'''


'''String ke saare vowels count karo.'''


'''String ke saare consonants count karo.'''


'''Ek string me spaces ki total count nikalo.'''


'''String ko uppercase aur lowercase me convert karke print karo.'''


'''Ek sentence ke words ki total count nikalo (bina split() use kiye).'''


'''String ke first aur last character print karo.'''


'''Do strings ko concatenate karo aur beech me space add karo.'''


# 🔹 Intermediate Level (11-20)

'''Ek string me se saare vowels remove karo.'''


'''String me har word ka first letter capital karo (Title Case - bina .title() use kiye).'''


'''Check karo ki two strings anagram hain ya nahi.'''


# # Spaces remove karo

# # Characters sort karke compare karo


'''Ek string ke characters ki frequency count karo (dictionary use karke).'''


'''String me se duplicate characters remove karo.'''

   
'''Ek string ko word-by-word reverse karo (jaise "Hello World" → "World Hello").'''


'''Ek given character string me kitni baar aaya hai count karo.'''


# # Character count karo


'''String me numbers, alphabets, aur special characters ki alag-alag count karo.'''


'''Ek string ko without using slicing reverse karo (loop se).'''


'''Check karo ki given string sirf digits contain karti hai ya nahi.'''


# 🔹 Advanced Level (21-30)

'''Longest word ek sentence me se find karo.'''


'''String me se saare repeated words remove karo (order maintain karte hue).'''


'''Ek string ko compress karo jaise "aaabbbcc" → "a3b3c2".'''


'''Check karo ki given string valid palindrome hai (spaces aur special characters ignore karke).'''


'''Ek paragraph me sabse zyada frequently aane wala word find karo.'''


'''String rotation check karo - ki ek string doosri string ka rotation hai ya nahi (jaise "abcd" aur "cdab").'''


'''Ek string me sabse pehla non-repeating character find karo.'''


'''Two strings ko merge karo alternately (jaise "abc" + "xyz" → "axbycz").'''


'''Ek sentence ke har word ko reverse karo but word order same rakho (jaise "Hello World" → "olleH dlroW").'''


'''Caesar Cipher implement karo (string ko given shift value se encrypt/decrypt karo).'''


# 1️⃣ Text Analyzer Tool
# User se ek paragraph input lekar uska complete analysis karo:

# Total words, sentences, characters (with/without spaces)
# Vowels, consonants, digits, aur special characters ki count
# Longest aur shortest word
# Most frequently used word
# Output ko ek neat formatted report ki tarah print karo.


# 2️⃣ Password Strength Checker
# User se password input lekar check karo ki wo strong hai ya weak based on:

# Minimum length (8+ characters)
# Uppercase aur lowercase letters dono hain ya nahi
# Digits present hain ya nahi
# Special characters (@, #, $, etc.) present hain ya nahi
# Har condition ke basis pe strength score do (Weak/Medium/Strong) aur missing requirements bhi bata do.


# 3️⃣ Caesar Cipher - Encryption/Decryption Tool
# Ek complete tool banao jisme user:

# Message input kare
# Shift value input kare
# Choose kare Encrypt ya Decrypt karna hai
# Program ord(), chr() aur modulo operator use karke encrypted/decrypted message generate kare. Spaces aur punctuation ko unchanged rakho, sirf letters shift karo.


# 4️⃣ Palindrome & Anagram Checker Suite
# Ek menu-based (simple) tool jo:

# Check kare ki ek string palindrome hai ya nahi (numbers, sentences, special characters sab handle kare)
# Do strings input lekar check kare ki wo anagram hain ya nahi
# Case-insensitive aur space-ignore logic bhi include karo
# Real-world example: "A man a plan a canal Panama" jaisi sentences bhi correctly check ho.


# 5️⃣ Simple Text-Based Word Game (Hangman Lite)
# Ek fixed word ya user-input word ko hidden format me dikhao (jaise "_ _ _ _ _"). User character guess kare:

# Agar correct hai to us position pe letter reveal ho
# Wrong guesses count track ho
# Given attempts ke andar puri word guess karni ho
# String indexing, slicing, aur comparison operators ka heavy use hoga is project me.

 
'''conditional statements'''


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


'''🔹 Basic Level (1-10)'''

'''Ek number input lekar check karo ki wo positive, negative ya zero hai.'''


'''Ek number input lekar check karo ki wo even hai ya odd.'''


'''Do numbers input lekar unme se bada number print karo.'''


'''Teen numbers input lekar unme se sabse bada number find karo.'''


'''Ek number input lekar check karo ki wo 10 se bada hai ya chota.'''


'''User ki age input lekar check karo ki wo voting ke liye eligible hai ya nahi (18+).'''


'''Ek number input lekar check karo ki wo 5 se divisible hai ya nahi.'''


'''Ek number input lekar check karo ki wo single digit hai ya multi-digit.'''


'''Ek year input lekar check karo ki wo leap year hai ya nahi.'''


'''🔹 Intermediate Level (11-20)'''

'''Student ke marks input lekar grade decide karo (A, B, C, D, F).'''


'''Teen sides input lekar check karo ki triangle valid hai ya nahi.'''


'''Triangle ke teen sides input lekar check karo ki wo equilateral, isosceles ya scalene hai.'''


'''Ek number input lekar check karo ki wo prime hai ya nahi'''


'''Simple calculator banao jo operator (+, -, *, /) input lekar operation perform kare.'''


'''Ek number input lekar check karo ki wo 100 se 999 ke beech ka 3-digit number hai ya nahi.'''


'''BMI calculator banao jo weight/height input lekar category (Underweight, Normal, Overweight, Obese) decide kare.'''


'''Electricity bill calculator banao jo units ke basis pe different rate slabs apply kare.'''


'''Ek number input lekar check karo ki wo Armstrong number hai ya nahi.'''


'''Login system simulate karo - username aur password input lekar check karo ki wo match karta hai ya nahi (fixed credentials se compare).'''


'''🔹 Advanced Level (21-30)'''

'''Ek number input lekar check karo ki wo perfect square hai ya nahi.'''


'''Quadratic equation ke coefficients (a, b, c) input lekar check karo ki roots real hain, equal hain, ya imaginary hain (discriminant use karke).'''


'''Ek date (day, month, year) input lekar check karo ki wo valid date hai ya nahi'''  


'''Ticket price calculator banao jo age aur day (weekday/weekend) ke basis pe discount apply kare.'''


'''Ek number input lekar check karo ki wo palindrome number hai ya nahi.'''


'''Traffic light simulator banao - color input lekar (red/yellow/green) action print karo (Stop/Wait/Go).'''


'''Employee ke salary aur experience input lekar bonus percentage decide karo (nested conditions se).'''


'''Ek number input lekar uska sign (+/-) aur wo even/odd bhi hai check karo ek hi program me (nested if-else).'''


'''Season predictor banao - month number input lekar season (Summer, Winter, Monsoon, Spring) print karo.'''


'''Simple grading system with multiple criteria - marks aur attendance dono input lekar final result decide karo (Pass/Fail with conditions combine karke).'''


# Python - 5 Projects (Conditional Statements)
# 1️⃣ Smart ATM Simulator
# User se PIN input lekar (fixed PIN se compare karo). Agar correct hai to menu dikhao:

# Balance check
# Withdraw amount (check karo ki balance sufficient hai ya nahi, aur withdrawal limit bhi check karo jaise ek time me max ₹50,000)
# Agar 3 baar wrong PIN dala to "Card Blocked" message do
# Nested conditions ka use karke sab edge cases handle karo.


# 2️⃣ Movie Ticket Booking System
# User se age, day (weekday/weekend), aur show timing (morning/evening) input lekar:

# Age ke basis pe ticket category decide karo (Child/Adult/Senior Citizen)
# Weekend pe extra charge apply karo
# Evening show pe premium pricing
# Senior citizens aur children ko discount do
# Final ticket price multiple conditions combine karke calculate karo.


# 3️⃣ Loan Eligibility Checker
# User se age, monthly income, credit score, aur employment status input lekar check karo ki wo loan ke liye eligible hai ya nahi:

# Age 21-60 ke beech honi chahiye
# Minimum income requirement
# Credit score 650+ hona chahiye
# Employment status (employed/self-employed/unemployed) ke basis pe alag rules
# Sab conditions ek saath check karke final eligibility aur reason (agar reject hua to kyu) print karo.


# 4️⃣ Restaurant Bill & Discount System
# User se total bill amount, membership type (None/Silver/Gold/Platinum), aur payment method (Cash/Card/UPI) input lekar:

# Membership ke basis pe discount % apply karo
# Payment method ke basis pe extra cashback/offer
# Bill amount 1000+ hone par extra flat discount
# Final bill nested conditions se calculate karke detailed breakdown print karo.


# 5️⃣ Traffic Fine Calculator
# User se violation type (No helmet/Overspeeding/Red light jump/No license), vehicle type (Bike/Car/Truck), aur repeat offender status (Yes/No) input lekar:

# Violation type ke basis pe base fine decide karo
# Vehicle type ke basis pe fine multiply/adjust karo
# Repeat offenders ke liye double fine
# Multiple nested if-elif conditions se final fine amount calculate karo.

