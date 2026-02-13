# Day 28 - Memoization & DP Intro


# -----------------------------------
# 1. Normal Fibonacci (Very Slow)
# -----------------------------------

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Time Complexity: O(2^n)
# Space Complexity: O(n)



# -----------------------------------
# 2. Fibonacci with Memoization
# -----------------------------------

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# Time Complexity: O(n)
# Space Complexity: O(n)



# -----------------------------------
# 3. DP (Bottom-Up Approach)
# -----------------------------------

def fib_dp(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Time Complexity: O(n)
# Space Complexity: O(n)



# -----------------------------------
# 4. Space Optimized DP
# -----------------------------------

def fib_optimized(n):
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Time Complexity: O(n)
# Space Complexity: O(1)



# --------- Testing ---------

print("Recursive:", fib_recursive(6))
print("Memoization:", fib_memo(6))
print("DP:", fib_dp(6))
print("Optimized DP:", fib_optimized(6))
