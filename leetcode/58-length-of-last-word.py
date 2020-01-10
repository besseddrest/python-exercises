# https://leetcode.com/problems/length-of-last-word/

"""
58. Length of Last World

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return 0 if len(words) == 0 else len(words[len(words) - 1])

# Runtime: 24 ms, faster than 84.86% of Python3 online submissions for Length of Last Word.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Length of Last Word.