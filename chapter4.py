'''distionary and set'''


'''

"""
================================================================
    PYTHON NOTES: DICTIONARY & SET
================================================================
"""

# ================================================================
# PART 1: DICTIONARY BASICS
# ================================================================

# ---- Dictionary kya hoti hai? ----
# Key-value pairs ka collection hai. Keys unique hoti hain,
# values duplicate ho sakti hain. Python 3.7+ me insertion
# order maintain hoti hai.

student = {"name": "Aman", "age": 20, "city": "Delhi"}
print(student)


# ---- Accessing Values ----
print(student["name"])            # Aman
print(student.get("age"))         # 20
print(student.get("marks", 0))    # 0 -> default agar key na mile (error nahi aayega)


# ---- Adding / Updating ----
student["marks"] = 85             # naya key add
student["age"] = 21               # existing key update
student.update({"city": "Mumbai", "grade": "A"})   # multiple update
print(student)


# ---- Removing ----
student.pop("grade")              # key remove, value return karta hai
del student["marks"]              # key delete, return nahi karta
# student.clear()                  # pura dictionary khali

print(student)


# ================================================================
# PART 2: DICTIONARY METHODS
# ================================================================

data = {"a": 1, "b": 2, "c": 3}

print(data.keys())        # dict_keys(['a', 'b', 'c'])
print(data.values())      # dict_values([1, 2, 3])
print(data.items())       # dict_items([('a',1), ('b',2), ('c',3)])

# ---- Loop through dictionary ----
for key, value in data.items():
    print(key, value)

# ---- Check key existence ----
print("a" in data)        # True (default me keys check hoti hain)

# ---- Copy dictionary ----
data_copy = data.copy()


# ================================================================
# PART 3: NESTED DICTIONARY
# ================================================================

students = {
    "101": {"name": "Aman", "marks": 85},
    "102": {"name": "Riya", "marks": 90}
}

print(students["101"]["name"])       # Aman

for roll_no, info in students.items():
    print(roll_no, "->", info["name"], info["marks"])


# ================================================================
# PART 4: DICTIONARY COMPREHENSION
# ================================================================

# Syntax: {key_expr: value_expr for item in iterable if condition}

squares = {x: x**2 for x in range(1, 6)}
print(squares)                # {1:1, 2:4, 3:9, 4:16, 5:25}

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)


# ================================================================
# PART 5: MERGING & INVERTING DICTIONARIES
# ================================================================

# ---- Merge two dictionaries ----                  
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}       # dict2 ki values override karti hain common keys
print(merged)          # {'a': 1, 'b': 3, 'c': 4}

# ---- Invert a dictionary (keys <-> values swap) ----
def invert_dict(d):
    return {v: k for k, v in d.items()}

print(invert_dict({"a": 1, "b": 2, "c": 3}))    # {1:'a', 2:'b', 3:'c'}

# ---- Sort dictionary by value ----
scores = {"Aman": 85, "Riya": 92, "Sam": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)      # {'Riya': 92, 'Aman': 85, 'Sam': 78}


# ================================================================
# PART 6: SET BASICS
# ================================================================

# ---- Set kya hoti hai? ----
# Set ek UNORDERED collection hai jisme DUPLICATE elements allowed
# nahi hote. Set mutable hoti hai, lekin uske elements immutable
# (hashable) hone chahiye.

my_set = {1, 2, 3, 4, 4, 5}
print(my_set)              # {1, 2, 3, 4, 5} -> duplicate automatically remove ho gaya

empty_set = set()          # NOTE: {} se empty dictionary banti hai, empty set nahi!


# ---- Set create from list (duplicates remove karne ka common trick) ----
lst = [1, 2, 2, 3, 3, 3, 4]
unique_set = set(lst)
print(unique_set)          # {1, 2, 3, 4}
print(list(unique_set))    # back to list: [1, 2, 3, 4]


# ================================================================
# PART 7: SET METHODS
# ================================================================

s = {1, 2, 3}

# ---- Adding elements ----
s.add(4)                   # single element add
s.update([5, 6, 7])        # multiple elements add
print(s)

# ---- Removing elements ----
s.remove(6)                 # element na ho to ERROR aayega
s.discard(100)              # element na ho to bhi ERROR nahi aayega (safe way)
popped = s.pop()             # random element remove karta hai (order fixed nahi)
# s.clear()                  # pura set khali

print(s)


# ================================================================
# PART 8: SET OPERATIONS (Mathematics wale set jaise)
# ================================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# ---- Union: dono sets ke saare unique elements ----
print(a | b)                # {1, 2, 3, 4, 5, 6}
print(a.union(b))

# ---- Intersection: common elements ----
print(a & b)                # {3, 4}
print(a.intersection(b))

# ---- Difference: a me hai but b me nahi ----
print(a - b)                # {1, 2}
print(a.difference(b))

# ---- Symmetric Difference: dono me se sirf ek me present ----
print(a ^ b)                # {1, 2, 5, 6}
print(a.symmetric_difference(b))


# ================================================================
# PART 9: SET RELATIONSHIPS
# ================================================================

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print(x.issubset(y))          # True -> x, y ka subset hai
print(y.issuperset(x))        # True -> y, x ka superset hai

p = {1, 2}
q = {3, 4}
print(p.isdisjoint(q))        # True -> koi common element nahi hai


# ================================================================
# PART 10: FROZENSET (Immutable Set)
# ================================================================

# frozenset() -> ek immutable set hota hai (add/remove nahi kar sakte)
# Use case: dictionary key ki tarah ya set ke andar set rakhne ke liye

fs = frozenset([1, 2, 3, 4])
print(fs)
# fs.add(5)          # ERROR - frozenset immutable hai


# ================================================================
# PART 11: COMMON PRACTICE LOGIC
# ================================================================

# ---- Remove duplicates from a list using set ----
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 4]))    # [1, 2, 3, 4] (order guarantee nahi)


# ---- Find common elements in two lists (fast approach) ----
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))    # [3, 4]


# ---- Check if two strings are anagrams using character sets ----
def has_same_unique_chars(s1, s2):
    return set(s1) == set(s2)

print(has_same_unique_chars("listen", "silent"))     # True


# ---- Two Sum Problem using Dictionary (O(n) approach) ----
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

print(two_sum([2, 7, 11, 15], 9))    # [0, 1]


# ---- Word Frequency Count using Dictionary ----
def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("apple banana apple mango banana apple"))
# {'apple': 3, 'banana': 2, 'mango': 1}


# ---- Find unique words across multiple sentences using set ----
def unique_words(sentences):
    words = set()
    for sentence in sentences:
        words.update(sentence.split())
    return words

print(unique_words(["I love Python", "Python is fun"]))
# {'I', 'love', 'Python', 'is', 'fun'}


# ---- Check duplicate elements in a list (fast way using set) ----
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 4]))      # False
print(has_duplicates([1, 2, 2, 3]))       # True


# ================================================================
# QUICK SUMMARY
# ================================================================
# Dictionary          -> key-value pairs, keys unique, fast lookup O(1)
# get()               -> safe access with default value
# Dict Comprehension  -> {key: value for item in iterable if condition}
# {**d1, **d2}        -> merge dictionaries shortcut
# Set                 -> unordered, unique elements only, mutable
# set() vs {}         -> {} khali dictionary banati hai, set() khali set
# add()/update()      -> set me elements add karna
# remove() vs discard()-> remove error deta hai, discard safe hai
# Union | Intersection & | Difference - | Symmetric Diff ^  -> set operations
# issubset/issuperset/isdisjoint -> set relationships check karna
# frozenset           -> immutable version of set
# Common use: duplicates remove karna, fast membership check (in operator O(1))
# ================================================================

'''


# 
# Python - Dictionary ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

'''Ek dictionary banao (student data) aur uske keys, values print karo.'''


'''Dictionary me naya key-value pair add karo.'''


# data["mon"] = 3584689476


# Dictionary se ek key-value pair remove karo (pop() use karke).


# Check karo ki ek key dictionary me present hai ya nahi.


# Dictionary ke saare keys ek list me convert karo.


# Dictionary ke saare values ek list me convert karo.


# Dictionary ki length nikalo (len() use karke).


# Dictionary ko loop se iterate karo (keys, values, aur items dono print karo).


# Ek dictionary ka value update karo (existing key ka).


# data["name"] = "kumar"

# get() method ka use karke safely value access karo (default value ke saath).


# 🔹 Intermediate Level (11-20)

# Do dictionaries ko merge karo (update() method use karke).


# Dictionary ke values ka sum nikalo.


# Dictionary me maximum value wali key find karo.
# Dictionary me minimum value wali key find karo.
# Dictionary ko value ke basis pe sort karo.
# Dictionary ko key ke basis pe sort karo.
# Ek list ko dictionary me convert karo (index: value format me).
# Do lists (keys list, values list) ko ek dictionary me convert karo (zip() use karke).
# Dictionary comprehension use karke 1-10 tak numbers ki squares ki dictionary banao.
# Nested dictionary banao aur uske values access/print karo.

# 🔹 Advanced Level (21-30)

# Ek string ke characters ki frequency count karo dictionary use karke.
# Ek sentence ke words ki frequency count karo dictionary use karke.
# Dictionary ko invert karo (keys values ban jayein, values keys ban jayein).
# Do dictionaries me common keys find karo.
# Dictionary se duplicate values wale keys remove karo.
# Counter class use karke ek list ke elements ki frequency count karo.
# defaultdict use karke ek program banao jo grouping kare (jaise words unki length ke basis pe group karna).
# Nested dictionary ko flatten karo (single level dictionary banao).
# Dictionary ke items ko value ke basis pe descending order me sort karke top 3 print karo.
# Ek dictionary of lists banao (jaise {"fruits": ["apple","banana"], "veggies": [...]}) aur total elements count karo sabhi lists milakar.


# Python - 5 Projects (Dictionary)
# 1️⃣ Student Database Management System
# Dictionary of dictionaries use karke student records store karo (jaise {roll_no: {"name": ..., "marks": ..., "age": ...}}):

# Naya student record add karo
# Kisi student ka data update karo (marks update karna)
# Roll number se student search karo
# Saare students ka average marks nikalo
# Topper student find karo (dictionary values compare karke)

# 2️⃣ Word Frequency Counter & Text Analyzer
# User se ek paragraph input lekar:

# Dictionary use karke har word ki frequency count karo
# Most frequent word find karo
# Words ko unki frequency ke basis pe sort karo (descending)
# Unique words count karo
# Counter class bhi use karke same result verify karo aur compare karo dono approach me

# 3️⃣ Simple Inventory Management System
# Dictionary use karke products store karo ({product_name: {"price": ..., "quantity": ...}}):

# Naya product add karo
# Stock update karo (quantity increase/decrease)
# Total inventory value calculate karo (price × quantity sabke liye sum)
# Low stock products find karo (jinki quantity ek threshold se kam hai)
# Product search karo naam se

# 4️⃣ Contact Book Application
# Dictionary use karke contacts store karo ({name: {"phone": ..., "email": ..., "address": ...}}):

# Naya contact add karo
# Existing contact update karo
# Contact delete karo
# Saare contacts alphabetically print karo (dictionary ko sorted karke)
# Phone number se reverse search karo (kis naam ka ye number hai)

# 5️⃣ Employee Payroll & Department Management System
# Dictionary of dictionaries use karke employees store karo ({emp_id: {"name": ..., "department": ..., "salary": ...}}):

# Department-wise employees group karo (defaultdict use karke)
# Department-wise total aur average salary calculate karo
# Highest paid employee find karo (overall aur department-wise dono)
# Salary hike apply karo (percentage ke basis pe - saare employees ya specific department ke liye)
# Complete payroll report generate karo (dictionary comprehension use karke)


# Python - Set ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

# Ek set banao aur uske elements print karo.


# Set me naya element add karo (add() use karke).


# Set se ek element remove karo (remove() aur discard() dono try karo).


# Set ki length nikalo (len() use karke).


# Check karo ki ek element set me present hai ya nahi (in operator).


# Ek list ko set me convert karo (duplicates automatically remove ho jayenge).


# Set ko loop se iterate karo aur elements print karo.


# Do sets banao aur unka union nikalo (union() ya | operator)


# Do sets ka intersection nikalo (intersection() ya & operator).


# clear() method use karke ek set ke saare elements remove karo.


# 🔹 Intermediate Level (11-20)

# Do sets ka difference nikalo (difference() ya - operator).
# Do sets ka symmetric difference nikalo (^ operator).
# Check karo ki ek set doosre set ka subset hai ya nahi (issubset()).
# Check karo ki ek set doosre set ka superset hai ya nahi (issuperset()).
# Check karo ki do sets disjoint hain ya nahi (isdisjoint()).
# update() method use karke ek set me multiple elements add karo.
# pop() method use karke set se random element remove karo.
# Ek list se duplicate elements remove karo set use karke, phir wapas list me convert karo.
# Do lists ke common elements find karo sets use karke (list ke bina loop ke).
# Frozenset kya hota hai? Ek frozenset banao aur uska use demonstrate karo.

# 🔹 Advanced Level (21-30)

# Ek string ke unique characters find karo set use karke.
# Do strings check karo ki unke unique characters same hain ya nahi (set comparison se).
# Set comprehension use karke 1-20 tak ke numbers ka set banao jo 3 se divisible hain.
# Multiple lists ke saare unique elements combine karo ek set me.
# Set use karke check karo ki ek list me saare elements unique hain ya nahi.
# Nested list (list of lists) ke saare unique elements ek set me nikalo.
# Set operations (union, intersection, difference) combine karke ek complex problem solve karo (jaise "students enrolled in both Math and Science" jaise scenario).
# Set use karke anagram check karo (dono strings ke characters set compare karke - basic check).
# Two sets ko compare karo aur unka result (equal/not equal/subset/superset) determine karo.
# Ek program banao jo set operations use karke Venn diagram jaisa logic implement kare (three sets - A, B, C ke saare combinations: only A, only B, A∩B, A∩B∩C, etc.)


# Python - 5 Projects (Set)
# 1️⃣ Student Course Enrollment Analyzer
# Multiple sets banao different courses ke liye (jaise math_students, science_students, english_students):

# Students find karo jo dono Math aur Science me enrolled hain (intersection)
# Students find karo jo sirf ek hi course me hain (symmetric difference)
# Total unique students count karo (union)
# Students find karo jo Math me hain but Science me nahi (difference)
# Ek complete Venn-diagram style report generate karo (only A, only B, both, neither).

# 2️⃣ Duplicate Data Cleaner Tool
# User se multiple lists input lekar (jaise different sources se collected emails/phone numbers):

# Sets use karke saare duplicates remove karo
# Unique entries count karo
# Common entries across multiple lists find karo (jaise same email 2 sources me hai)
# Clean, duplicate-free final list file me save karo (bonus: file handling combine karo)

# 3️⃣ Social Media Friend Recommendation System
# User A aur User B ke friends lists (sets) banao:

# Common friends find karo (mutual friends - intersection)
# "People you may know" suggest karo (User B ke friends jo User A ke friends nahi hain - difference)
# Total unique connections count karo (union)
# Check karo ki dono users completely unrelated hain ya nahi (isdisjoint())

# 4️⃣ Inventory Comparison System (Two Store Branches)
# Do stores ke products sets banao (store_A_products, store_B_products):

# Products find karo jo dono stores me common hain
# Products find karo jo sirf Store A me hain (transfer ke liye suggest karna)
# Products find karo jo sirf Store B me hain
# Total unique products (combined catalog) count karo
# Real-world inventory management scenario simulate karo.

# 5️⃣ Text Plagiarism/Similarity Checker (Basic)
# Do documents/paragraphs input lekar:

# Har document ke unique words ka set banao
# Common words find karo dono documents me (intersection)
# Similarity score calculate karo: (common words / total unique words) × 100 (Jaccard similarity concept)
# Words find karo jo sirf ek document me hain (unique content detect karna)
# Basic plagiarism detection logic set operations se implement karo.


