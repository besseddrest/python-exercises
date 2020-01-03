# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.
#
#
# Example 1:
#
# Input: 121
# Output: true
#
#
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

my_num = 10

def is_palindrome(num):
    string_num = str(num)
    reverse_num = str(num)[::-1]

    return "true" if string_num == reverse_num else "false"

print(is_palindrome(my_num))