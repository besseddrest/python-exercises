# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
"""

"""
Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""

# TODO: need to modify the original list, not just return the length

# nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicates(nums):  
    current = None
    nums_len = 0

    if len(nums) == 0:
        return 0

    for number in nums:
        if current != number:
            current = number
            nums_len = nums_len + 1

    return nums_len
