# https://leetcode.com/problems/longest-common-prefix/
#
# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

"""
Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""

"""
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Note:
# All given inputs are in lowercase letters a-z.

strs = ["flower", "flow", "flight"]
# strs = ["dog","racecar","car"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        if len(strs) == 0:
            return common

        index = 0

        for x in strs[0]:
            for y in range(1, len(strs)):
                if (index >= len(strs[y]) or strs[y][index] != x):
                    return common

            common += x
            index += 1

        return common
                
# Runtime: 
# 28 ms, faster than 86.97% of Python3 online submissions for Longest Common Prefix.
# 
# Memory Usage: 
# 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.