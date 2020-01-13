# https://leetcode.com/problems/sort-array-by-parity/

"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        
        for num in A:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        
        even.extend(odd)
                
        return even

# Runtime: 
# 68 ms, faster than 99.78% of Python3 online submissions for Sort Array By Parity.
# 
# Memory Usage: 
# 13.4 MB, less than 98.70% of Python3 online submissions for Sort Array By Parity.