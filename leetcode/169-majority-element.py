# https://leetcode.com/problems/majority-element/

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        for num in num_set:
            if nums.count(num) > len(nums) / 2:
                return num

# Runtime: 180 ms, faster than 56.65% of Python3 online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 97.62% of Python3 online submissions for Majority Element.

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)
        half = len(nums) / 2
        
        return [num for num in num_set if nums.count(num) > half][0]

# Runtime: 172 ms, faster than 84.57% of Python3 online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 97.62% of Python3 online submissions for Majority Element.

class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        
        for num in set(nums):
            if nums.count(num) > half:
                return num

# Runtime: 168 ms, faster than 93.58% of Python3 online submissions for Majority Element.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Majority Element.