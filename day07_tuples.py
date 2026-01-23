# Day 07 - Tuples in Python
# Topic: Immutability, packing/unpacking, and practical usage



# 1. Tuple immutability

numbers = (10, 20, 30)
print("Original tuple:", numbers)

# numbers[0] = 100   # Uncommenting this will raise TypeError
print("Tuples are immutable")
print()



# 2. Tuple packing & unpacking

data = 1, "Python", 3.14   # packing
a, b, c = data             # unpacking
print("Packed tuple:", data)
print("Unpacked values:", a, b, c)
print()



# 3. Swapping values using tuple

x = 5
y = 10
x, y = y, x
print("After swapping: x =", x, "y =", y)
print()



# 4. Nested tuples

students = (
    ("Amit", 85),
    ("Neha", 92),
    ("Rahul", 78)
)

for name, marks in students:
    print(name, "scored", marks)
print()



# 5. Tuple with functions

def get_min_max(numbers):
    return min(numbers), max(numbers)

values = (4, 8, 1, 9, 2)
minimum, maximum = get_min_max(values)
print("Minimum:", minimum)
print("Maximum:", maximum)
