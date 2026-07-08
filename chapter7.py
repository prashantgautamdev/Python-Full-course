'''file input and outpu'''
'''

"""
================================================================
    PYTHON NOTES: FILE HANDLING (INPUT/OUTPUT)
================================================================
"""

# ================================================================
# PART 1: FILE HANDLING BASICS
# ================================================================

# ---- File Handling kya hai? ----
# Python me files ko read/write/append karne ke liye built-in
# `open()` function use hota hai.

# Syntax: open(filename, mode)


# ---- File Modes ----
# 'r'   -> Read (default) - file exist karni chahiye
# 'w'   -> Write - naya file banata hai ya existing ko overwrite karta hai
# 'a'   -> Append - end me content add karta hai (file na ho to bana deta hai)
# 'r+'  -> Read + Write
# 'w+'  -> Write + Read (overwrite karta hai)
# 'a+'  -> Append + Read
# 'rb'  -> Read Binary (images, pdf, etc.)
# 'wb'  -> Write Binary


# ================================================================
# PART 2: OPENING & CLOSING FILES
# ================================================================

# ---- Basic way (manual close zaroori hai) ----
# f = open("sample.txt", "w")
# f.write("Hello World")
# f.close()          # close karna zaroori hai warna data properly save nahi hoga

# ---- Recommended way: with statement (Context Manager) ----
# `with` automatically file close kar deta hai, chahe error aaye ya na aaye

with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is Python file handling")

# File yahan automatically close ho jaati hai (with block khatam hote hi)


# ================================================================
# PART 3: WRITING TO A FILE
# ================================================================

# ---- write() -> single string likhta hai ----
with open("sample.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# ---- writelines() -> list of strings likhta hai ----
lines = ["Python\n", "is\n", "fun\n"]
with open("sample.txt", "w") as f:
    f.writelines(lines)

# ---- Append mode -> purane content ke baad naya add hota hai ----
with open("sample.txt", "a") as f:
    f.write("New line added at the end\n")


# ================================================================
# PART 4: READING FROM A FILE
# ================================================================

# ---- read() -> pura content ek string ki tarah ----
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# ---- read(n) -> sirf n characters read karta hai ----
with open("sample.txt", "r") as f:
    partial = f.read(10)
    print(partial)

# ---- readline() -> ek line at a time read karta hai ----
with open("sample.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, line2)

# ---- readlines() -> saari lines ek list me ----
with open("sample.txt", "r") as f:
    all_lines = f.readlines()
    print(all_lines)      # ['Python\n', 'is\n', 'fun\n']

# ---- Loop through file directly (memory efficient - best way) ----
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())    # strip() se \n hat jaata hai


# ================================================================
# PART 5: FILE POINTER / CURSOR POSITION (Advanced)
# ================================================================

with open("sample.txt", "r") as f:
    print(f.tell())        # current cursor position (0 se start)
    f.read(5)
    print(f.tell())         # 5 characters read karne ke baad position
    f.seek(0)                # cursor ko wapas start pe le jaata hai
    print(f.read())


# ================================================================
# PART 6: CHECKING FILE EXISTENCE
# ================================================================

import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist")

# Other useful os functions
print(os.path.getsize("sample.txt"))    # file size in bytes
# os.remove("sample.txt")                # file delete karna


# ================================================================
# PART 7: EXCEPTION HANDLING WITH FILES
# ================================================================

try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")


# ================================================================
# PART 8: WORKING WITH CSV FILES
# ================================================================

import csv

# ---- Writing to CSV ----
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])         # header row
    writer.writerow(["Aman", 20, "Delhi"])
    writer.writerow(["Riya", 22, "Mumbai"])

# ---- Reading from CSV ----
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)          # each row is a list

# ---- Using DictReader/DictWriter (data as dictionary) ----
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])


# ================================================================
# PART 9: WORKING WITH JSON FILES
# ================================================================

import json

data = {
    "name": "Aman",
    "age": 20,
    "skills": ["Python", "SQL"]
}

# ---- Writing JSON to file ----
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)      # indent -> pretty formatting

# ---- Reading JSON from file ----
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
    print(loaded_data["name"])

# ---- Convert Python object <-> JSON string (without file) ----
json_string = json.dumps(data)         # dict -> JSON string
print(json_string)

python_obj = json.loads(json_string)   # JSON string -> dict
print(python_obj)


# ================================================================
# PART 10: COMMON PRACTICE LOGIC
# ================================================================

# ---- Count words in a file ----
def count_words(filename):
    with open(filename, "r") as f:
        content = f.read()
    words = content.split()
    return len(words)

# print(count_words("sample.txt"))


# ---- Count lines in a file ----
def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())

# print(count_lines("sample.txt"))


# ---- Find frequency of a specific word in a file ----
def word_count_in_file(filename, target_word):
    with open(filename, "r") as f:
        content = f.read()
    return content.lower().split().count(target_word.lower())


# ---- Copy content from one file to another ----
def copy_file(source, destination):
    with open(source, "r") as f_src:
        content = f_src.read()
    with open(destination, "w") as f_dest:
        f_dest.write(content)


# ---- Remove blank lines from a file ----
def remove_blank_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    non_blank_lines = [line for line in lines if line.strip() != ""]
    with open(filename, "w") as f:
        f.writelines(non_blank_lines)


# ---- Find and Replace a word in a file ----
def find_and_replace(filename, old_word, new_word):
    with open(filename, "r") as f:
        content = f.read()
    content = content.replace(old_word, new_word)
    with open(filename, "w") as f:
        f.write(content)


# ---- Simple Logging System with Timestamp ----
from datetime import datetime

def log_message(filename, message):
    with open(filename, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

# log_message("app.log", "Application started")


# ================================================================
# QUICK SUMMARY
# ================================================================
# open(file, mode)      -> file open karne ka basic syntax
# with statement         -> automatic file close (best practice)
# 'r','w','a','r+'       -> common file modes
# read()/readline()/readlines() -> file read karne ke tarike
# write()/writelines()   -> file me likhne ke tarike
# csv module             -> CSV files ke liye reader/writer, DictReader/DictWriter
# json module            -> dump/load (file ke saath), dumps/loads (string ke saath)
# try-except             -> FileNotFoundError jaisi exceptions handle karne ke liye
# os.path.exists()       -> file check karne ke liye zaroori
# ================================================================

'''

# Python - File Input/Output ke 30 Coding Practice Questions
# 🔹 Basic Level (1-10)

# Ek naya text file create karo aur usme kuch text likho (write() use karke).
# Ek existing text file ka pura content read karo aur print karo.
# File me text append karo (naya content purane ke end me add karo).
# Ek file ko line by line read karo (readline() use karke).
# Ek file ki saari lines ko list me store karo (readlines() use karke).
# with open() statement kya hota hai? Ek example likho file read karne ka.
# File open karne ke different modes kya hain (r, w, a, r+) - each ka example do.
# Check karo ki ek file exist karti hai ya nahi (os.path.exists() use karke).
# Ek file ki total lines count karo.
# Ek file ke content ko uppercase me convert karke naye file me likho.

# 🔹 Intermediate Level (11-20)

# Ek file me se specific word search karo aur count karo ki wo kitni baar aaya hai.
# User se multiple lines input lekar unhe ek file me save karo (loop se).
# Ek file ke saare words count karo.
# Ek file ka content copy karke doosri file me paste karo.
# File me se ek particular line delete karo (content read karke, filter karke, dobara likhna).
# Ek CSV file create karo aur usme data likho (csv module use karke).
# Ek CSV file read karo aur uska data print karo.
# File me se blank lines remove karo aur clean content naye file me save karo.
# Ek file ke words ko alphabetically sort karke naye file me likho.
# Ek file ka size (bytes me) check karo.

# 🔹 Advanced Level (21-30)

# Ek text file ke words ki frequency count karo (dictionary use karke) aur result file me save karo.
# Multiple files ka content ek single file me merge karo.
# Ek file ko read karke uska content reverse order me (last line first) naye file me likho.
# JSON file create karo aur usme dictionary data likho (json module use karke).
# JSON file read karo aur data ko Python dictionary me convert karo.
# Exception handling use karke file operations me error handle karo (jaise file not found).
# Ek log file banao jisme timestamp ke saath messages append hote rahein.
# Binary file read/write karo (rb, wb mode use karke - jaise image file copy karna).
# Ek file ke content me specific word ko doosre word se replace karo (find and replace).
# Ek program banao jo file ke content ko encrypt/decrypt kare (Caesar cipher + file I/O combine karke).



# Python - 5 Projects (File Input/Output)
# 1️⃣ Personal Diary/Journal App
# Ek program banao jisme user:

# Har entry likh sake jo automatically timestamp ke saath file me save ho (append mode)
# Purani entries read kar sake (pura diary dikhana)
# Specific date ki entry search kar sake
# Total entries count kar sake
# Menu-driven system ho jo while loop + file handling combine kare.

# 2️⃣ Student Records Management (CSV-Based)
# CSV file use karke student database banao:

# Naya student record add karo (name, roll no, marks) - CSV me row add karke
# Saare records read karke table format me print karo
# Kisi specific student ka record search karo
# Marks ke basis pe records update karo
# Average marks calculate karke report file me save karo

# 3️⃣ Word Frequency Analyzer & Report Generator
# User se ek text file input lekar (ya khud content likhkar):

# Saare words ki frequency count karo (dictionary se)
# Top 5 most frequent words find karo
# Total unique words, total words, aur file size calculate karo
# Pura analysis ek naye "report.txt" file me formatted way me save karo

# 4️⃣ Contact Book with JSON Storage
# JSON file use karke persistent contact book banao:

# Naya contact add karo (name, phone, email) - JSON me save ho
# Saare contacts JSON file se load karke dikhao
# Contact search karo (name se)
# Contact delete/update karo aur JSON file update karo
# Program band karne ke baad bhi data file me save rahega (persistence demonstrate hoga).

# 5️⃣ Simple Log Monitoring System
# Ek program banao jo events/errors ko continuously log file me likhe:

# Har action (login attempt, error, warning) timestamp ke saath append ho
# Log file se saare "ERROR" type entries filter karke alag file me save karo
# Log file me total entries, errors count, warnings count nikalo
# Purane logs (jaise 7 din se purane - simulate karke) delete/archive karne ka logic banao
# Exception handling bhi use karo (file not found, permission errors handle karna).

