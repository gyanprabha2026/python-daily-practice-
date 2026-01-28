# Day 12 - Advanced Dictionary Practice (Real World Problems)

# 1. Word Frequency Counter (Text Analysis)
sentence = "python is easy and python is powerful"
words = sentence.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequency:", word_freq)
print()


# 2. Student Result Management System
students = {
    "Amit": {"maths": 78, "science": 85, "english": 74},
    "Neha": {"maths": 88, "science": 90, "english": 82},
    "Ravi": {"maths": 65, "science": 70, "english": 60}
}

for name, marks in students.items():
    total = sum(marks.values())
    avg = total / len(marks)
    print(f"{name} -> Total: {total}, Average: {avg}")
print()


# 3. Find Topper
topper = ""
highest_avg = 0

for name, marks in students.items():
    avg = sum(marks.values()) / len(marks)
    if avg > highest_avg:
        highest_avg = avg
        topper = name

print("Topper:", topper)
print()


# 4. Inventory Management (Real Shop Example)
inventory = {
    "apple": {"price": 100, "quantity": 10},
    "banana": {"price": 40, "quantity": 25},
    "milk": {"price": 60, "quantity": 8}
}

# Update stock after purchase
inventory["apple"]["quantity"] -= 2
inventory["milk"]["quantity"] -= 1

for item, details in inventory.items():
    print(item, "->", details)
print()


# 5. Filter Data (Products below threshold)
low_stock = {}

for item, details in inventory.items():
    if details["quantity"] < 10:
        low_stock[item] = details

print("Low stock items:", low_stock)
print()


# 6. Merge Two Dictionaries (User Data Update)
user_profile = {"name": "Gyan", "email": "gyan@email.com"}
update_data = {"email": "gyan123@email.com", "city": "Ahmedabad"}

user_profile.update(update_data)
print("Updated Profile:", user_profile)
