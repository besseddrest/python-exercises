# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1 or s == s[::-1]:
            return True
        
        x = 0
        y = len(s) - 1
        
        while (x < y):
            if s[x] != s[y]:
                return self.isPalindrome(s, x + 1, y) or self.isPalindrome(s, x, y - 1)
            
            x += 1
            y -= 1
            
        return True
    
    def isPalindrome(self, s: str, x: int, y: int) -> bool:
        while (x < y):
            if s[x] != s[y]:
                return False
            
            x += 1
            y -= 1
        
        return True

# Runtime: 144 ms, faster than 59.69% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 13.2 MB, less than 75.00% of Python3 online submissions for Valid Palindrome II.