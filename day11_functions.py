# Day 11 - Functions (Advanced Basics)


# 1. Greeting Function
def greet(name):
    return f"Hello, {name}! Welcome to Python."


# 2. Return vs Print
def add(a, b):
    return a + b


# 3. Default Arguments
def calculate_bill(amount, tax=5):
    return amount + (amount * tax / 100)


# 4. Even or Odd
def is_even(num):
    return num % 2 == 0


# 5. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 6. Sum of Digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


# 7. Grade Calculator
def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 45:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "Fail"


# ---------- Function Calls (Testing) ----------
print(greet("Gyan"))

print("Sum:", add(10, 20))

print("Bill with default tax:", calculate_bill(1000))
print("Bill with custom tax:", calculate_bill(1000, 18))

print("Is 10 even?", is_even(10))

print("Factorial of 5:", factorial(5))

print("Sum of digits of 123:", sum_of_digits(123))

print("Grade:", calculate_grade(72))
