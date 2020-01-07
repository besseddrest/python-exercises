# https://leetcode.com/problems/remove-element/

"""
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keeps track of non-matched values
        count = 0
        # store original length
        length = len(nums)

        # we use a range because we want to iterate over the original length
        for i in range(0, length):
            # if we find a non-match
            if nums[i] != val:
                # add it to the end of our list
                nums.append(nums[i])
                # increment count
                count += 1
                
        # reverse the list so that all the unique values will be at the front of the list
        nums.reverse()

        return count

# Runtime: 
# 20 ms, faster than 99.32% of Python3 online submissions for Remove Element.
# 
# Memory Usage: 
# 12.6 MB, less than 100.00% of Python3 online submissions for Remove Element.