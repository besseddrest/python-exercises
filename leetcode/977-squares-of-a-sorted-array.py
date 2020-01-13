# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
977. Squares of a Sorted Array
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

class Solution1:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = [num * num for num in A]
        
        return sorted(squares)

# Runtime: 
# 224 ms, faster than 87.33% of Python3 online submissions for Squares of a Sorted Array.
# 
# Memory Usage: 
# 14.6 MB, less than 97.62% of Python3 online submissions for Squares of a Sorted Array.

class Solution2:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = []
        
        for num in A:
            squares.append(num * num)
        
        return sorted(squares)

# Runtime: 
# 220 ms, faster than 92.80% of Python3 online submissions for Squares of a Sorted Array.
# 
# Memory Usage: 
# 14.6 MB, less than 97.62% of Python3 online submissions for Squares of a Sorted Array.