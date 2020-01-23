# https://leetcode.com/problems/longest-palindromic-substring/

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check for empty or single char case

        # create a start and end
        # these will be the index that are the bounds of the longest substring

        # iterate over letters, expanding from middle
        # needs two values, because there is sometimes a unique middle char in the palindrome
        # get the max of those two lengths, this is our longest length

        # if the length is greater than previous length
        # update the start and end values
        # start is i plus the front half
        # end is i plus the back half

        # return a substring using the new start and end values as indices


    # create a helper function expandFromMiddle
    # while left is greater than 0
    # while right is less than length
    # and while char at left equals char at right
    # increment left
    # decrement right
    # return length: right - left - 1