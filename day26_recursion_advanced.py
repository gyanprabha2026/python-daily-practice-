# Day 26 - Recursion Advanced & Backtracking Basics


# 1. Print all subsets of a string (Power Set)
def print_subsets(s, current="", index=0):
    if index == len(s):
        print(current)
        return

    # Include character
    print_subsets(s, current + s[index], index + 1)

    # Exclude character
    print_subsets(s, current, index + 1)


print("Subsets of 'abc':")
print_subsets("abc")


# 2. Generate all permutations of a string
def permutations(s, l, r):
    if l == r:
        print("".join(s))
        return

    for i in range(l, r + 1):
        s[l], s[i] = s[i], s[l]   # swap
        permutations(s, l + 1, r)
        s[l], s[i] = s[i], s[l]   # backtrack


print("\nPermutations of 'abc':")
permutations(list("abc"), 0, 2)


# 3. Count ways to climb stairs (1 or 2 steps)
def count_ways(n):
    if n == 0 or n == 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)


print("\nWays to climb 4 stairs:", count_ways(4))


# 4. Binary strings of length n
def generate_binary(n, current=""):
    if len(current) == n:
        print(current)
        return

    generate_binary(n, current + "0")
    generate_binary(n, current + "1")


print("\nBinary strings of length 3:")
generate_binary(3)
