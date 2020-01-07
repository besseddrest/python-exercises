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

def twoSum2(self, nums: List[int], target: int) -> List[int]:
    indices = []
    checked = {}
    
    for i in range(0, len(nums)):
        diff = target - nums[i]
        
        if diff in checked.keys():
            indices.append(i)
            indices.append(checked[diff])
            return indices
            
        checked[nums[i]] = i
        
    return indices
    
# 2nd pass:
# added line 59:
# once we have these values, we don't have to continue checking, since there is only one solution
#
# Runtime: 
# 52 ms, faster than 54.08% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 13.9 MB, less than 68.14% of Python3 online submissions for Two Sum.


# ideas for 3rd pass:
# 
# maybe faster and less memory if we use a non-dictionary solution
# how about don't create dicionary and just re-check the input array for value?

def twoSum3(self, nums: List[int], target: int) -> List[int]:
    indices = []
        length = len(nums)

        for i in range(0, length):
            diff = target - nums[i]

            if diff in nums[i + 1:]:
                indices.extend((i, length - 1 - nums[::-1].index(diff)))
                return indices

        return indices


# Runtime: 
# 776 ms, faster than 30.55% of Python3 online submissions for Two Sum.
#
# Memory Usage:
# 13.9 MB, less than 68.37% of Python3 online submissions for Two Sum.

# Runtime: 
# 792 ms, faster than 29.76% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 13.8 MB, less than 69.77% of Python3 online submissions for Two Sum.

# Runtime: 
# 852 ms, faster than 26.42% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 13.8 MB, less than 73.72% of Python3 online submissions for Two Sum.

# 4th pass:
# dicionary method but use extend instead of append twice

def twoSum4(self, nums: List[int], target: int) -> List[int]:
    indices = []
    checked = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]

        if diff in checked.keys():
            indices.extend((i, checked[diff]))
            return indices

        checked[nums[i]] = i

    return indices

# Runtime: 
# 48 ms, faster than 77.99% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 13.9 MB, less than 66.05% of Python3 online submissions for Two Sum.

# 5th pass - fastest!

def twoSum5(self, nums: List[int], target: int) -> List[int]:
    checked = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]

        if diff in checked.keys():
            return [i, checked[diff]]

        checked[nums[i]] = i

    return []

# Runtime: 
# 44 ms, faster than 91.98% of Python3 online submissions for Two Sum.
# 
# Memory Usage: 
# 14.1 MB, less than 64.65% of Python3 online submissions for Two Sum.