# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        # return first index
        # and last index which is:
        # the length - 1, minus the index of the target in a reversed subarray
        # the subarray is all the numbers after the first instance
        return [nums.index(target), len(nums) - 1 - nums[nums.index(target):][::-1].index(target)]

# fast, but hard to read
# Runtime: 76 ms, faster than 99.50% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.