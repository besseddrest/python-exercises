# https://leetcode.com/problems/unique-number-of-occurrences/

"""
1207. Unique Number of Occurrences
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        used = []
        
        for num in arr:
            if num not in used:
                used.append(num)
                counts.append(arr.count(num))
            
        for num in counts:
            if counts.count(num) > 1:
                return False
        
        return True
        

# Runtime: 72 ms, faster than 5.54% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.

class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        unique = set(arr)
        
        for num in unique:
            counts.append(arr.count(num))
            
        for num in counts:
            if counts.count(num) > 1:
                return False
        
        return True

# Runtime: 44 ms, faster than 16.72% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.