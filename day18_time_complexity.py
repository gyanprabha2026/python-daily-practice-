# Day 18 - Time Complexity (Big O Examples)

# O(1) - Constant Time
def get_first_element(arr):
    return arr[0]


# O(n) - Linear Time
def print_elements(arr):
    for element in arr:
        print(element)


# O(n^2) - Quadratic Time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# O(log n) - Logarithmic Time
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# O(n log n) - Linearithmic Time
def sort_array(arr):
    return sorted(arr)


# ---------- Testing ----------
arr = [10, 20, 30, 40, 50]

print("O(1) example:", get_first_element(arr))
print()

print("O(n) example:")
print_elements(arr)
print()

print("O(n^2) example:")
print_pairs([1, 2, 3])
print()

print("O(log n) example (binary search):", binary_search(arr, 30))
print()

print("O(n log n) example (sorting):", sort_array([5, 2, 9, 1]))
