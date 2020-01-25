# https://leetcode.com/problems/house-robber/

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        amounts = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            amounts.append(max(nums[i] + amounts[i - 2], amounts[i - 1]))
            
        return amounts[len(nums) - 1]

# "Dynamic Programming" Bottom up approach
# much like stair/steps problem
# calculate easiest cases and then for each next iteration add it to previous results
# Runtime: 28 ms, faster than 74.32% of Python3 online submissions for House Robber.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.

class Solution2:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0:
            return 0
        
        if length <= 2:
            return max(nums)
        
        amounts = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, length):
            amounts.append(max(nums[i] + amounts[i - 2], amounts[i - 1]))
            
        return amounts[length - 1]

# Runtime: 24 ms, faster than 92.82% of Python3 online submissions for House Robber.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.