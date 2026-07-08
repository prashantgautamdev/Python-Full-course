# '''list & tuple'''


'''

"""
================================================================
    PYTHON NOTES: LIST & TUPLE
================================================================
"""

# ================================================================
# PART 1: LIST BASICS
# ================================================================

# ---- List kya hoti hai? ----
# List ek ordered, mutable (changeable) collection hai jisme
# different data types ek saath store ho sakte hain.

fruits = ["apple", "banana", "mango"]
mixed = [1, "hello", 3.14, True]

print(fruits)


# ---- Indexing & Slicing (String jaisa hi) ----
print(fruits[0])       # apple
print(fruits[-1])      # mango (negative indexing)
print(fruits[0:2])     # ['apple', 'banana']
print(fruits[::-1])    # reverse list


# ---- List is Mutable ----
fruits[0] = "orange"
print(fruits)           # ['orange', 'banana', 'mango']


# ================================================================
# PART 2: LIST METHODS
# ================================================================

nums = [3, 1, 4, 1, 5, 9]

# ---- Adding elements ----
nums.append(6)          # end me single element add
nums.insert(0, 100)     # specific index pe insert
nums.extend([7, 8])     # multiple elements add (list merge)
print(nums)

# ---- Removing elements ----
nums.remove(1)          # value ke basis pe (pehla match remove hota hai)
popped = nums.pop()     # last element remove karta hai aur return karta hai
popped_index = nums.pop(0)   # specific index se remove
# del nums[0]            # index ke basis pe delete (return nahi karta)
# nums.clear()           # pura list khali kar deta hai

# ---- Sorting & Reversing ----
nums = [3, 1, 4, 1, 5, 9]
nums.sort()              # ascending order me sort (original list modify hoti hai)
print(nums)              # [1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)  # descending order
print(nums)              # [9, 5, 4, 3, 1, 1]

nums.reverse()           # list ko reverse kar deta hai (sort nahi karta)

# sorted() -> naya sorted list banata hai, original change nahi hota
original = [3, 1, 2]
new_list = sorted(original)
print(original, new_list)


# ---- Other Useful Methods ----
nums = [1, 2, 3, 2, 4]
print(nums.count(2))     # 2 (kitni baar aaya)
print(nums.index(3))     # 2 (first occurrence ka index)
copy_list = nums.copy()  # shallow copy banata hai


# ================================================================
# PART 3: LIST COMPREHENSION
# ================================================================

# Syntax: [expression for item in iterable if condition]

squares = [x**2 for x in range(1, 6)]
print(squares)             # [1, 4, 9, 16, 25]

even_nums = [x for x in range(20) if x % 2 == 0]
print(even_nums)

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)


# ================================================================
# PART 4: NESTED LISTS (2D LIST / MATRIX)
# ================================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])        # [1, 2, 3]  -> first row
print(matrix[1][2])     # 6          -> row 1, column 2

# Traverse entire matrix
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()


# ================================================================
# PART 5: LIST COPY - SHALLOW vs DEEP COPY (Advanced)
# ================================================================

# ---- Direct assignment (NOT a copy - same reference) ----
list1 = [1, 2, 3]
list2 = list1              # list2 same memory ko point karta hai
list2[0] = 99
print(list1)                # [99, 2, 3] -> original bhi change ho gaya!

# ---- Shallow Copy ----
list3 = list1.copy()        # ya list1[:]
list3[0] = 500
print(list1)                 # original change NAHI hoga

# ---- Deep Copy (nested lists ke liye zaroori) ----
import copy
nested = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(nested)
deep_copied[0][0] = 999
print(nested)                 # original safe rahega


# ================================================================
# PART 6: TUPLE BASICS
# ================================================================

# ---- Tuple kya hoti hai? ----
# Tuple bhi list jaisi hoti hai lekin IMMUTABLE hoti hai
# (ek baar create hone ke baad change nahi ho sakti)

my_tuple = (1, 2, 3, "hello")
single_tuple = (5,)         # comma zaroori hai single element tuple ke liye

print(my_tuple[0])           # 1
print(my_tuple[-1])          # hello
print(my_tuple[0:2])         # (1, 2) slicing kaam karti hai

# my_tuple[0] = 100          # ERROR - tuple immutable hai


# ---- Tuple kyu use karte hain? ----
# 1. Immutable hone se data safe rehta hai (accidental change nahi hoga)
# 2. List se thoda fast hota hai
# 3. Dictionary keys ke roop me use ho sakta hai (list nahi ho sakti)


# ---- Tuple Methods (limited hote hain, kyunki immutable hai) ----
t = (1, 2, 3, 2, 4)
print(t.count(2))            # 2
print(t.index(3))            # 2


# ---- Tuple Unpacking ----
person = ("Aman", 25, "Delhi")
name, age, city = person
print(name, age, city)

# Swapping using tuple unpacking
a, b = 5, 10
a, b = b, a                  # tuple unpacking se swap
print(a, b)                  # 10 5

# Extended unpacking
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print(first, middle, last)   # 1 [2, 3, 4] 5


# ---- Convert between List and Tuple ----
list_data = [1, 2, 3]
tuple_data = tuple(list_data)     # list -> tuple
back_to_list = list(tuple_data)   # tuple -> list


# ================================================================
# PART 7: LIST vs TUPLE - KEY DIFFERENCES
# ================================================================

# | Feature       | List              | Tuple             |
# |---------------|-------------------|-------------------|
# | Mutability    | Mutable            | Immutable          |
# | Syntax        | [1, 2, 3]          | (1, 2, 3)          |
# | Speed         | Slower             | Faster             |
# | Methods       | Many (append etc.) | Few (count,index)  |
# | Use case      | Data changes often | Data fixed/constant|
# | Dict key      | Cannot be used     | Can be used        |


# ================================================================
# PART 8: COMMON PRACTICE LOGIC (List & Tuple)
# ================================================================

# ---- Find largest & smallest (without max/min) ----
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 7, 2, 9, 4]))    # 9


# ---- Remove duplicates from list ----
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))   # [1, 2, 3, 4]


# ---- Second largest number ----
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1]

print(second_largest([10, 20, 4, 45, 99]))    # 45


# ---- Common elements between two lists (Intersection) ----
def common_elements(list1, list2):
    return [x for x in list1 if x in list2]

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))   # [3, 4]


# ---- Rotate a list by k positions ----
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_list([1, 2, 3, 4, 5], 2))    # [3, 4, 5, 1, 2]


# ---- Sum and Average of a list ----
def list_sum_avg(lst):
    total = sum(lst)
    avg = total / len(lst)
    return total, avg

total, avg = list_sum_avg([10, 20, 30])
print(total, avg)    # 60 20.0


# ---- Flatten a nested list ----
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, [5, 6]]]))    # [1, 2, 3, 4, 5, 6]


# ================================================================
# QUICK SUMMARY
# ================================================================
# List             -> Mutable, ordered, [] syntax, methods bahut hain
# Tuple            -> Immutable, ordered, () syntax, methods kam hain
# List Comprehension -> [expr for item in iterable if condition]
# Shallow vs Deep Copy -> nested lists ke liye deepcopy() zaroori
# Tuple Unpacking   -> a, b, c = tuple  (swap ke liye bhi useful)
# List vs Tuple     -> data change hoga to List, fixed data ho to Tuple
# ================================================================

'''

# Python - List & Tuple ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

# Ek list banao aur uske saare elements print karo loop se.  




# List me naya element add karo (append() use karke).
# List se ek element remove karo (remove() use karke).
# List ki length nikalo (bina len() use kiye, loop se count karo).
# Ek list ke saare elements ka sum nikalo.
# List me sabse bada aur sabse chota number find karo (bina max()/min() use kiye).
# Ek list ko reverse karo (bina reverse() method use kiye).
# List me ek particular element search karo aur uska index print karo.
# Ek tuple banao aur uske elements print karo.
# List ko tuple me convert karo aur tuple ko list me convert karo.

# 🔹 Intermediate Level (11-20)

# List me se saare even numbers alag list me store karo.
# List me se duplicate elements remove karo.
# Do lists ko merge/concatenate karo.
# List ke elements ko ascending order me sort karo (bina sort() use kiye - bubble sort logic se).
# List ke elements ko descending order me sort karo.
# List me se saare negative numbers count karo.
# Ek list ke elements ka average nikalo.
# List slicing use karke first 3 aur last 3 elements print karo.
# Ek tuple ke elements ka sum aur average nikalo.
# Check karo ki ek element list me present hai ya nahi (in operator use karke).

# 🔹 Advanced Level (21-30)

# List me se second largest number find karo (bina sort/max use kiye).
# Two lists common elements find karo (intersection).
# Two lists ke unique elements find karo (jo dono me na ho ek saath).
# Ek list ko rotate karo (jaise [1,2,3,4,5] → [5,1,2,3,4]).
# List of tuples ko ek particular index ke basis pe sort karo.
# Nested list (2D list/matrix) banao aur uske saare elements print karo.
# Matrix transpose karo (nested list use karke).
# List me consecutive duplicate elements remove karo (jaise [1,1,2,2,3] → [1,2,3]).
# Tuple unpacking use karke multiple variables ek saath assign karo aur swap karo.
# List comprehension use karke 1 se 50 tak saare perfect squares ki list banao.

# Python - 5 Projects (List & Tuple)
# 1️⃣ Student Marks Management System
# List of tuples use karke multiple students ka data store karo (name, marks) format me:

# Sabse zyada aur sabse kam marks wale student find karo
# Class ka average marks nikalo
# Marks ke basis pe students ko sort karo (highest to lowest)
# Pass/Fail students ki separate lists banao (list comprehension se)

# 2️⃣ Shopping Cart System
# List of tuples/lists use karke cart items store karo (item_name, price, quantity):

# User items add/remove kar sake (loop + menu se)
# Total bill calculate karo (sab items ka sum)
# Sabse expensive aur sabse cheap item find karo
# Final formatted bill receipt print karo

# 3️⃣ Matrix Operations Tool
# Nested lists (2D lists) use karke:

# Do matrices ka addition aur subtraction
# Matrix transpose karna
# Matrix ke saare elements ka sum, row-wise sum, column-wise sum
# Identity matrix generate karna (given size ki)

# 4️⃣ Contact Book (Mini Address Book)
# List of tuples use karke contacts store karo (name, phone_number, email):

# Naya contact add karo
# Name se search karke contact details dikhao
# Saare contacts alphabetically sort karo (name ke basis pe)
# Duplicate phone numbers check karo aur remove karo

# 5️⃣ Exam Result Analyzer (Multi-Subject)
# List of tuples ya nested list use karke multiple students ke multiple subjects ka data store karo (name, [marks1, marks2, marks3...]):

# Har student ka total aur percentage calculate karo
# Topper student find karo
# Subject-wise class average nikalo
# Grade assign karo (list comprehension + conditional logic combine karke)

