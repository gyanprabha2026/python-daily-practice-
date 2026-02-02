# Day 17 - Searching and Sorting Algorithms

# ---------- Searching ----------

# 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. Binary Search (array must be sorted)
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


# ---------- Sorting ----------

# 3. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 4. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 5. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# ---------- Testing ----------
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

print("Linear search for 25:", linear_search(arr, 25))

sorted_arr = bubble_sort(arr.copy())
print("Bubble sort:", sorted_arr)

print("Binary search for 25:", binary_search(sorted_arr, 25))

print("Selection sort:", selection_sort(arr.copy()))

print("Insertion sort:", insertion_sort(arr.copy()))
