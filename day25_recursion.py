# Day 25 - Recursion Basics & Core Problems

# 1. Print numbers from 1 to N
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

print("Print 1 to N:")
print_1_to_n(5)


# 2. Print numbers from N to 1
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

print("\nPrint N to 1:")
print_n_to_1(5)


# 3. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))


# 4. Sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print("\nSum of digits of 1234:", sum_of_digits(1234))


# 5. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci of 6:", fibonacci(6))


# 6. Check Palindrome
def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)

word = "madam"
print("\nIs Palindrome:", is_palindrome(word, 0, len(word) - 1))
