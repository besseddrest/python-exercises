# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[::-1][k - 1]

# doesn't seem like a medium question
# Runtime: 60 ms, faster than 91.89% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.