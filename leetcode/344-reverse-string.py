# https://leetcode.com/problems/reverse-string/

"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s) == 0:
            return []

        i = 0
        j = len(s) - 1
        
        while i < j:
            first = s[i]
            last = s[j]
            s[i] = last
            s[j] = first
            
            i += 1
            j -= 1

# Runtime: 204 ms, faster than 93.67% of Python3 online submissions for Reverse String.
# Memory Usage: 17.2 MB, less than 98.84% of Python3 online submissions for Reverse String.