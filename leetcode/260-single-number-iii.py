# https://leetcode.com/problems/single-number-iii/

class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        return [num for num in count if count[num] == 1]

# Runtime: 60 ms, faster than 67.18% of Python3 online submissions for Single Number III.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Single Number III.

class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        
        for i in range(0, len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
                
        return [num for num in count if count[num] == 1]

# range(x, y) is faster
# Runtime: 56 ms, faster than 86.74% of Python3 online submissions for Single Number III.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Single Number III.