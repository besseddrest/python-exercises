# https://leetcode.com/problems/remove-element/

"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

# iterate over nums
# if current value is equal to val
# iterate over rest of list until we find the next diff val
# take that diff val and replace current val
# increment
# return new length, or current index + 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length = len(nums)

        for i in range(0, length):
            if nums[i] != val:
                nums.append(nums[i])
                count += 1
                
        nums.reverse()

        print(nums)
        return count

# Runtime: 
# 20 ms, faster than 99.32% of Python3 online submissions for Remove Element.
# 
# Memory Usage: 
# 12.6 MB, less than 100.00% of Python3 online submissions for Remove Element.