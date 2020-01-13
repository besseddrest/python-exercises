# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
"""

class Solution1:
    def subtractProductAndSum(self, n: int) -> int:
        if len(str(n)) == 1:
            return 0
        
        n = str(n)
        prod_all = int(n[0])
        sum_all = int(n[0])
        
        for i in range(1, len(n)):
            prod_all *= int(n[i])
            sum_all += int(n[i])
            
        return prod_all - sum_all

# Runtime: 
# 24 ms, faster than 83.24% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# 
# Memory Usage: 
# 12.9 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        
        if len(n_str) == 1:
            return 0
        
        n_int = int(n_str[0])
        
        prod_all = n_int
        sum_all = n_int
        
        for i in range(1, len(n_str)):
            curr = int(n_str[i])
            prod_all *= curr
            sum_all += curr
            
        return prod_all - sum_all

# Runtime: 
# 20 ms, faster than 95.97% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.