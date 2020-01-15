# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:

"""
iterate over numbers
square each number, store it
when we get to a squared value that is more than target
subtract largest number
count++
if negative
  subtract next smallest number
  count++
if 0
  count++ then return count