# https://leetcode.com/problems/single-number/

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        
        while i < length:
            val = nums[i]
            if val in nums[i + 1:]:
                nums.remove(val)
                nums.remove(val)
                length -= 2
            else:
                return val

# Runtime: 2880 ms, faster than 5.12% of Python3 online submissions for Single Number.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Single Number.

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for i in range(len(nums)):
            xor ^= nums[i]
            
        return xor

# Runtime: 100 ms, faster than 17.46% of Python3 online submissions for Single Number.
# Memory Usage: 15 MB, less than 26.23% of Python3 online submissions for Single Number.

class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for num in nums:
            xor ^= num
            
        return xor

# Runtime: 88 ms, faster than 64.56% of Python3 online submissions for Single Number.
# Memory Usage: 15 MB, less than 21.31% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

# get the sum as if all numbers were doubled, and subtract it from the sum of all numbers
# the answer is the value that is missing a double in the original list
# Runtime: 152 ms, faster than 9.48% of Python3 online submissions for Single Number.
# Memory Usage: 15 MB, less than 21.31% of Python3 online submissions for Single Number.