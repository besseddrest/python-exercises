# https://leetcode.com/problems/binary-search/

"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if length == 0:
            return -1
        
        left = 0
        right = length - 1
        
        while left <= right:
            # the mid index gets updated each time the left or right is updated
            mid = (left + right) // 2
            
            # if the mid index is our target, return it
            if nums[mid] == target:
                return mid
            # if our mid val is less than the target
            # we can set the left point to the next index and skip everything else
            if nums[mid] < target:
                left = mid + 1
            # if our mid val is more than the target
            # we can set our ending bounds to the index before the current
            if nums[mid] > target:
                right = mid - 1
                
        return -1

# Runtime: 252 ms, faster than 95.43% of Python3 online submissions for Binary Search.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Binary Search.