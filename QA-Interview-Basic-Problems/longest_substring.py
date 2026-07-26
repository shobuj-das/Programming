# ============================================================
# Day 21 - Longest Substring Without Repeating Characters
#
# Difficulty:
# Medium
#
# Concepts:
# - String
# - Sliding Window
# - Dictionary / Set
# - Two Pointers
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Given a string, find the length of the longest substring
# without repeating characters.
#
# A substring consists of consecutive characters.
#
# Return ONLY the maximum length.
#
# ------------------------------------------------------------
#
# Examples
#
# Input:
# "abcabcbb"
#
# Output:
# 3
#
# Explanation:
# "abc"
#
# ------------------------------------------------------------
#
# Input:
# "bbbbb"
#
# Output:
# 1
#
# Explanation:
# "b"
#
# ------------------------------------------------------------
#
# Input:
# "pwwkew"
#
# Output:
# 3
#
# Explanation:
# "wke"
#
# ------------------------------------------------------------
#
# Input:
# ""
#
# Output:
# 0
#
# ------------------------------------------------------------
#
# Input:
# "dvdf"
#
# Output:
# 3
#
# Explanation:
# "vdf"
#
# ------------------------------------------------------------
#
# Constraints
#
# - String may contain:
#   - lowercase letters
#   - uppercase letters
#   - digits
#   - symbols
#   - spaces
#
# ------------------------------------------------------------
#
# Follow-up
#
# 1. Solve using a brute-force approach.
#
# 2. Then optimize it using Sliding Window.
#
# 3. Compare the time complexity of both approaches.
#
# ============================================================

def has_duplicate(sub_string):
    for x in range(len(sub_string)-1):
        for y in range((x+1),len(sub_string)):
            if sub_string[x] == sub_string[y]:
                return True
    return False

def longest_substring(text):
    max_len = 0
    for i in range(len(text)):
        for j in range(i+1,len(text)+1):
            sub = text[i:j]
            if not has_duplicate(sub_string=sub):
                max_len = max(max_len, len(sub))

    return max_len



if __name__=="__main__":
    print(longest_substring("abcabcbb"))       # 3
    print(longest_substring("bbbbb"))          # 1
    print(longest_substring("pwwkew"))         # 3
    print(longest_substring(""))               # 0
    print(longest_substring("a"))              # 1
    print(longest_substring("au"))             # 2
    print(longest_substring("dvdf"))           # 3
    print(longest_substring("abba"))           # 2
    print(longest_substring("abcdef"))         # 6
    print(longest_substring("aab"))            # 2
    print(longest_substring("abcadef"))        # 6
    print(longest_substring("123451234"))      # 5
    print(longest_substring("!@#!$"))          # 3
    print(longest_substring(" "))              # 1
    print(longest_substring("abc def"))        # 7


# abcdd