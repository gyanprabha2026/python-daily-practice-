# Day 38 - String Practice Problems


# 1️ Reverse String
def reverse_string(s):
    return s[::-1]


# 2️ Count Vowels and Consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count


# 3️ Check Anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# 4️ First Non-Repeating Character
def first_non_repeating(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return None


# -------- Testing --------

print("Reverse:", reverse_string("hello"))

v, c = count_vowels_consonants("Hello World")
print("Vowels:", v, "Consonants:", c)

print("Are 'listen' and 'silent' anagrams?:", is_anagram("listen", "silent"))

print("First non-repeating in 'aabbcdd':", first_non_repeating("aabbcdd"))
