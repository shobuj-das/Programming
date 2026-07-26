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

def is_duplicate_found(sub_string):
    for x in range(len(sub_string)-1):
        for y in range((x+1),len(sub_string)):
            if sub_string[x] == sub_string[y]:
                return False
    return True

def longest_sub_string(text):
    sub_string_len = []
    x = 0
    y = len(text)-1
    for i in range(len(text)):
        for j in range(len(text),0,-1):
            k = j*-1
            sub = text[i,k]
            print(f"{sub} == {is_duplicate_found(sub)}")


longest_sub_string("assfbcdefadf")


# abcdd