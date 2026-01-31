# Day 15 - Pattern Problems (Stars, Numbers, Alphabets)

n = 5

# 1. Square Star Pattern
print("Square Pattern:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print()


# 2. Right Triangle Star Pattern
print("Right Triangle Pattern:")
for i in range(1, n + 1):
    print("* " * i)
print()


# 3. Inverted Star Pattern
print("Inverted Triangle Pattern:")
for i in range(n, 0, -1):
    print("* " * i)
print()


# 4. Pyramid Star Pattern
print("Pyramid Pattern:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
print()


# 5. Number Triangle
print("Number Triangle:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# 6. Reverse Number Triangle
print("Reverse Number Triangle:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# 7. Alphabet Triangle (A, AB, ABC...)
print("Alphabet Triangle:")
for i in range(1, n + 1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print()


# 8. Repeating Alphabet Pattern
print("Repeating Alphabet Pattern:")
for i in range(1, n + 1):
    print(chr(64 + i) * i)
print()


# 9. Continuous Alphabet Pattern
print("Continuous Alphabet Pattern:")
ch = ord('A')
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print()


# 10. Alphabet Pyramid
print("Alphabet Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
