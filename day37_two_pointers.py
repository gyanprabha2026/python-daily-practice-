# Day 37 - Two Pointer Technique


# 1️ Reverse Array using Two Pointers
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# 2️ Check Palindrome (String)
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# 3️ Pair with Given Sum (Sorted Array)
def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


# -------- Testing --------

print("Reverse:", reverse_array([1, 2, 3, 4, 5]))

print("Is 'madam' palindrome?:", is_palindrome("madam"))
print("Is 'hello' palindrome?:", is_palindrome("hello"))

print("Pair with sum 9:", pair_sum([1, 2, 3, 4, 5, 6, 7], 9))
