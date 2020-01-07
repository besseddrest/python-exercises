# https://leetcode.com/problems/reverse-integer/
#
# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(self, x: int) -> int:
    # keeps track if input value is negative
    neg = False

    # temporarily change our input value to positive
    if (x < 0):
        neg = True
        x *= -1

    # placeholder for our new number
    reversed = 0

    # takes the input value and converts the numbers in each position by multiplying and dividing by 10
    # for example:
    # 123 is 100 + 20 + 3
    # our result must be 300 + 20 + 1
    while (x > 0):
        # first pass, 123 here will return 3
        reversed = (reversed * 10) + (x % 10)
        # our new value will be 12
        x //= 10

        # 12 yields 2, so our next pass will be (3 * 10) + (12 % 10) = 32
        # new value becomes 1
        # 1 % 10 yields 1, final pass becomes (32 * 10) + 1 = 321

    # if this value exeeds max int limit, return 0
    if (abs(reversed) > (2 ** 31 - 1)):
        return 0

    # return our number, but make sure to make it negative if the input value was negative
    return reversed if neg == False else reversed * -1

# Runtime: 
# 28 ms, faster than 76.59% of Python3 online submissions for Reverse Integer.
# 
# Memory Usage:
# 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.