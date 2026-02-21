# Day 35 - Heap (Priority Queue)

import heapq


# 1. Create Min Heap
nums = [10, 4, 15, 20, 0]

heapq.heapify(nums)   # Convert list into heap
print("Min Heap:", nums)


# 2. Insert Element
heapq.heappush(nums, 2)
print("After inserting 2:", nums)


# 3. Remove Smallest Element
smallest = heapq.heappop(nums)
print("Removed smallest:", smallest)
print("Heap after pop:", nums)


# 4. Find K Largest Elements
arr = [5, 12, 3, 17, 8, 34, 1]
k = 3

largest = heapq.nlargest(k, arr)
print(f"{k} largest elements:", largest)


# 5. Find K Smallest Elements
smallest_k = heapq.nsmallest(k, arr)
print(f"{k} smallest elements:", smallest_k)
