# Day 40 - Dynamic Programming Intro


# 1️ Fibonacci - Simple Recursion (Inefficient)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2️ Fibonacci - Memoization (Top Down DP)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# 3️ Fibonacci - Tabulation (Bottom Up DP)
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 4️ Climbing Stairs Problem
# You can climb 1 or 2 steps at a time

def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


# -------- Testing --------

print("Fib Recursive (5):", fib_recursive(5))
print("Fib Memo (10):", fib_memo(10))
print("Fib Tab (10):", fib_tab(10))

print("Climbing Stairs (5):", climb_stairs(5))
