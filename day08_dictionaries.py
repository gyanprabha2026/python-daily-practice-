# Day 08 - Dictionaries in Python
# Topic: Key-Value pairs and common dictionary operations



# 1. Create and access dictionary

student = {
    "name": "Amit",
    "age": 21,
    "marks": 88
}

print("Student name:", student["name"])
print("Student marks:", student["marks"])
print()



# 2. Add and update values

student["grade"] = "A"
student["marks"] = 90
print("Updated dictionary:", student)
print()



# 3. Loop through dictionary

for key, value in student.items():
    print(key, ":", value)
print()



# 4. Check key existence

if "age" in student:
    print("Age key exists")
print()



# 5. Dictionary methods

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print()



# 6. Practical example: Word count

sentence = "python is easy and python is powerful"
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count:", word_count)
