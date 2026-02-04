# Day 19 - Space Complexity Examples

# O(1) Space - Constant Space
def sum_two_numbers(a, b):
    return a + b


# O(n) Space - Linear Space
def create_list(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr


# O(n) Space - Using Extra Array
def copy_array(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item)
    return new_arr


# O(n) Space - Recursive Call Stack
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# O(1) Space - In-place modification
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# ---------- Testing ----------
print("O(1) space example:", sum_two_numbers(5, 7))

print("O(n) space example:", create_list(5))

arr = [1, 2, 3, 4]
print("Copied array:", copy_array(arr))

print("Factorial using recursion:", factorial(5))

print("In-place reverse:", reverse_array([10, 20, 30, 40]))
