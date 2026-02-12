# Day 27 - Time & Space Complexity in Recursion


# 1. Linear Recursion (Factorial)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Time Complexity: O(n)
# Space Complexity: O(n)  (due to recursive call stack)



# 2. Fibonacci (Naive Recursion)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Time Complexity: O(2^n)
# Space Complexity: O(n)



# 3. Binary Recursion (Power Set Count)
def count_subsets(n):
    if n == 0:
        return 1
    return 2 * count_subsets(n - 1)


# Time Complexity: O(2^n)
# Space Complexity: O(n)



# 4. Tail Recursion (Optimizable)
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


# Time Complexity: O(n)
# Space Complexity: O(n)



# ---------- Test ----------
print("Factorial(5):", factorial(5))
print("Fibonacci(6):", fibonacci(6))
print("Subsets of 3 elements:", count_subsets(3))
print("Print numbers:")
print_numbers(5)
