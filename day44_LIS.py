# Day 44 - Longest Increasing Subsequence


# 1️⃣ Brute Force Recursion (Understanding Only)
def lis_recursive(nums, prev_index, curr_index):
    if curr_index == len(nums):
        return 0

    take = 0
    if prev_index < 0 or nums[curr_index] > nums[prev_index]:
        take = 1 + lis_recursive(nums, curr_index, curr_index + 1)

    not_take = lis_recursive(nums, prev_index, curr_index + 1)

    return max(take, not_take)


# 2️⃣ DP O(n^2) Solution (Most Important)
def lis_dp(nums):
    n = len(nums)
    dp = [1] * n   # each element alone is LIS of length 1

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# 3️⃣ Optimized O(n log n) Solution (Advanced)
import bisect

def lis_binary_search(nums):
    sub = []

    for num in nums:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num

    return len(sub)


# -------- Testing --------

nums = [10,9,2,5,3,7,101,18]

print("Recursive:", lis_recursive(nums, -1, 0))
print("DP O(n^2):", lis_dp(nums))
print("Binary Search O(n log n):", lis_binary_search(nums))
