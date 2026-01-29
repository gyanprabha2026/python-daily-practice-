# Day 13 - Digit Based Problems

# 1. Count number of digits
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# 2. Sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


# 3. Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


# 4. Check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)


# 5. Check Armstrong number
def is_armstrong(num):
    temp = num
    power = count_digits(num)
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num


# 6. Find product of digits
def product_of_digits(num):
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product


# 7. Find maximum digit
def max_digit(num):
    maximum = 0
    while num > 0:
        digit = num % 10
        if digit > maximum:
            maximum = digit
        num //= 10
    return maximum


# -------- Testing --------
number = 153

print("Number:", number)
print("Count of digits:", count_digits(number))
print("Sum of digits:", sum_of_digits(number))
print("Reverse:", reverse_number(number))
print("Is Palindrome:", is_palindrome(number))
print("Is Armstrong:", is_armstrong(number))
print("Product of digits:", product_of_digits(number))
print("Max digit:", max_digit(number))
