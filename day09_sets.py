# Day 10 - Sets in Python
# Topic: Unique elements and set operations



# 1. Create a set

numbers = {1, 2, 3, 4, 4, 5}
print("Set (unique values):", numbers)
print()



# 2. Add and remove elements

numbers.add(6)
numbers.remove(2)
print("After add & remove:", numbers)
print()



# 3. Set methods (safe remove)

numbers.discard(10)   # no error if element not found
print("After discard:", numbers)
print()



# 4. Set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Union:", a.union(b))
print("Intersection:", a & b)
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a - b)
print("Difference (a - b):", a.difference(b))
print()



# 5. Remove duplicates from list

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_with_duplicates))
print("Unique list:", unique_list)
