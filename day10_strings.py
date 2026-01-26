# Day 10 - Strings in Python
# Topic: String operations and practice



# 1. String basics

text = "Python Programming"
print("Original:", text)
print("Length:", len(text))
print()



# 2. Indexing & slicing

print("First char:", text[0])
print("Last char:", text[-1])
print("Slice (0:6):", text[0:6])
print()



# 3. Common string methods

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print()



# 4. Substring check

if "Python" in text:
    print("Substring found")
print()



# 5. Word count

sentence = "python is easy and python is powerful"
words = sentence.split()
print("Words:", words)
print("Word count:", len(words))
print()



# 6. Reverse a string

name = "developer"
print("Original:", name)
print("Reversed:", name[::-1])
