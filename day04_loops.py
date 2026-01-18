# Day 04 - Loops Practice


# 1. Print Numbers from 1 to N

n = int(input("Enter a number : "))
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")



# 2. Sum of numbers from 1 to N

n = int(input("Enter a number : "))
sum_of_numbers = 0

for i in range(1, n + 1):
    sum_of_numbers += i

print("Sum:", sum_of_numbers)
print()



# 3. Multiplication Table

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
print()



# 4. Sum of Digits

num = int(input("Enter a number : "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("Sum of digits:", sum_of_digits)
