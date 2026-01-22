# Day 06 - Lists in Python
# Topic: List operations and practice programs



# 1. Create and print a list

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)
print()



# 2. Add elements to a list

numbers.append(60)
numbers.insert(2, 25)
print("After append & insert:", numbers)
print()



# 3. Remove elements from a list

numbers.remove(30)
last_element = numbers.pop()
print("After remove & pop:", numbers)
print("Popped element:", last_element)
print()



# 4. Find max, min and sum

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print()



# 5. Find Runner-Up Score (Practice)

scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
print("Runner-Up Score:", unique_scores[1])
