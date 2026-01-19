# Day 05 - Functions in Python
# Reusable logic using functions



# 1. Check EVEN or ODD

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(f"{n} is {check_even_odd(n)}")
print()



# 2. Sum of first N numbers

def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print(f"Sum of first {n} numbers is {sum_of_numbers(n)}")
print()



# 3. Voting Eligibility

def check_voting(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

age = int(input("Enter your age: "))
print(check_voting(age))
print()



# 4. Sum of Digits

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
