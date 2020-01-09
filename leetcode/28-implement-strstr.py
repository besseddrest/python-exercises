# https://leetcode.com/problems/implement-strstr/

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        try:
            return haystack.index(needle)
        except ValueError:
            return -1

# Runtime:
# 36 ms, faster than 33.96% of Python3 online submissions for Implement strStr().
# 
# Memory Usage: 
# 12.9 MB, less than 100.00% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle) if needle != '' else 0
        except ValueError:
            return -1

# Runtime: 
# 20 ms, faster than 98.05% of Python3 online submissions for Implement strStr().
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Implement strStr().