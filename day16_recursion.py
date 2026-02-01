# Day 16 - Recursion Problems

# 1. Print numbers from 1 to N
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print("Numbers from 1 to 5:")
print_numbers(5)
print()


# 2. Sum of first N numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum of first 5 numbers:", sum_n(5))
print()


# 3. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print()


# 4. Fibonacci series (nth term)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci 6th term:", fibonacci(6))
print()


# 5. Count digits using recursion
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("Count digits in 1234:", count_digits(1234))
print()


# 6. Reverse a number using recursion
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print("Reverse of 1234:", reverse_number(1234))
print()


# 7. Check Palindrome using recursion
def is_palindrome(n):
    return n == reverse_number(n)

print("Is 121 palindrome?", is_palindrome(121))
