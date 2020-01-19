# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if length == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        # find the pivot point
        while left < right:
            mid = (left + right) // 2

            # if the number at the midpoint is greater than our number on the right
            # then we can start from the number after the midpoint
            if nums[mid] > nums[right]:
                left = mid + 1
            # if the number at the midpoint is less than our number on the right
            # then we can shorten the list  
            if nums[mid] < nums[right]:
                right = mid
            
        # the left value after the above logic will be our pivot point
        start = left
        # reset our vars
        left = 0
        right = length - 1
        
        # if the number is within the pivot point and our right bounds
        if target >= nums[start] and target <= nums[right]:
            # move our left index to the pivot point
            left = start
        # else, the number is in the first helf
        else:
            # move our right index at the pivot point
            right = start
            
        # this is a normal binary check
        while left <= right:
            # but our mid point is shifted up (left +) the midpoint between our new left and right bounds
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
            
        return -1

# Runtime: 40 ms, faster than 64.93% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if length == 0:
            return -1
        
        left = 0
        right = length - 1
        
        while left < right:
            mid = (left + right) // 2
            val = nums[mid]
            rval = nums[right]
            
            if val > rval:
                left = mid + 1
            if val < rval:
                right = mid
            
        start = left
        left = 0
        right = length - 1
        
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
            
        while left <= right:
            mid = left + (right - left) // 2
            val = nums[mid]
            
            if val == target:
                return mid
            if val < target:
                left = mid + 1
            if val > target:
                right = mid - 1
            
        return -1

# memoize
# Runtime: 36 ms, faster than 87.39% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        
        if ln == 0:
            return -1
        
        l = 0
        r = ln - 1
        
        while l < r:
            m = (l + r) // 2
            v = nums[m]
            rv = nums[r]
            
            if v > rv:
                l = m + 1
            if v < rv:
                r = m
            
        st = l
        l = 0
        r = ln - 1
        
        if target >= nums[st] and target <= nums[r]:
            l = st
        else:
            r = st
            
        while l <= r:
            m = l + (r - l) // 2
            v = nums[m]
            
            if v == target:
                return m
            if v < target:
                l = m + 1
            if v > target:
                r = m - 1
            
        return -1