# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        longest = []
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        for char in s:
            if char not in chars:
                chars.append(char)
                continue
                
            if char in chars:
                if len(chars) > len(longest):
                    longest = chars
                chars = chars[chars.index(char) + 1:]
                chars.append(char)
                
        return max(len(longest), len(chars))

# Runtime: 
# 68 ms, faster than 50.19% of Python3 online submissions for Longest Substring Without Repeating Characters.
# 
# Memory Usage: 
# 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        if len(s) < 2:
            return len(s)

        chars = []
        longest = []
        
        for char in s:                
            if char in chars:
                if len(chars) > len(longest):
                    longest = chars
                chars = chars[chars.index(char) + 1:]

            chars.append(char)
            
        return max(len(longest), len(chars))

# Runtime: 
# 68 ms, faster than 50.19% of Python3 online submissions for Longest Substring Without Repeating Characters.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.