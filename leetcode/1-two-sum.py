# https://leetcode.com/problems/two-sum/
#
# 1. Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # indices to return
    indices = []
    # keep track of values we've checked
    checked = {}
    
    for i in range(0, len(nums)):
        # get the 'partner' value of our current number
        diff = target - nums[i]
        
        # if the partner exists in the values we've already checked
        if diff in checked.keys():
            # add those two values to the indices
            indices.append(i)
            indices.append(checked[diff])
            return indices
            
        # add this value and index to our checked values
        checked[nums[i]] = i
        
    # return the result
    return indices
    

# 1st pass:
#    
# Runtime: 
# 56 ms, faster than 39.96% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 14.7 MB, less than 16.51% of Python3 online submissions for Two Sum.


# 2nd pass:
# added line 32:
# once we have these values, we don't have to continue checking, since there is only one solution
#
# Runtime: 
# 52 ms, faster than 54.13% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 14 MB, less than 65.58% of Python3 online submissions for Two Sum.


# ideas for 3rd pass:
# 
# maybe faster and less memory if we use a non-dictionary solution

