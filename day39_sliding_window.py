# Day 39 - Sliding Window Technique


# 1️ Maximum Sum Subarray of Size K
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# 2️ Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# -------- Testing --------

print("Max Sum Subarray (k=3):", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))

print("Longest Unique Substring Length:", longest_unique_substring("abcabcbb"))
