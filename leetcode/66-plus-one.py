"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

# convert the list to a number that we can incrememnt by 1
# add 1
# create a new list from the new number

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        
        for i in range(0, len(digits)):
            number = (number * 10) + digits[i]

        # cast the full number as a string
        # iterate over each number in the string and re-cast the digit as int before placing into our new list
        return [int(i) for i in str(number + 1)]

# Runtime: 
# 24 ms, faster than 94.58% of Python3 online submissions for Plus One.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Plus One.