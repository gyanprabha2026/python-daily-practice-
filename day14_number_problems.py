# Day 14 - Number Problems (Math Logic)

# 1. Check Prime Number
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 2. Find GCD (Euclidean Algorithm)
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 3. Find LCM
def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)


# 4. Generate Prime Numbers up to N
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# 5. Check Perfect Number
def is_perfect(num):
    if num <= 1:
        return False

    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


# 6. Check Strong Number
def is_strong(num):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == num


# -------- Testing --------
a, b = 12, 18

print("Is 29 prime?", is_prime(29))
print("GCD of", a, "and", b, ":", find_gcd(a, b))
print("LCM of", a, "and", b, ":", find_lcm(a, b))
print("Primes up to 20:", generate_primes(20))
print("Is 28 perfect?", is_perfect(28))
print("Is 145 strong?", is_strong(145))
