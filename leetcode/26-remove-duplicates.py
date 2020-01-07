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

# nums = [1, 1, 2]
nums = [0,0,1,1,2,2,3,3,4]

def remove_duplicates(nums):  
    # we use this as a pointer to the current array index that we want to edit 
    # it conveniently doubles as a counter
    index = 1
    num_length = len(nums)

    for i in range(0, num_length - 1):
        # if the current value and the next value are different
        if nums[i] != nums[i + 1]:
            # update our pointer index value to the next unique value
            nums[index] = nums[i + 1]
            # move our pointer to the next slot to update
            index += 1

    # our index has conveniently doubled as a counter
    # since technically the index now points at the slot AFTER our last unique number
    return index

print(remove_duplicates(nums))

# Runtime: 
# 84 ms, faster than 76.78% of Python3 online submissions for Remove Duplicates from Sorted Array.
# 
# Memory Usage: 
# 14.4 MB, less than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.