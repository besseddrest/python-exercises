# https://leetcode.com/problems/first-unique-character-in-a-string/

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == '':
            return -1
        
        counts = {}
        
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
                
        for key, val in counts.items():
            if val == 1:
                return s.index(key)
                
        return -1

# Runtime: 96 ms, faster than 77.17% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
