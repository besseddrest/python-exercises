# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == "" and B == "":
            return True
        
        for i in range(0, len(A)):
            A = A[1:] + A[0]    
            
            if A == B:
                return True
            
        return False

# Runtime: 24 ms, faster than 84.59% of Python3 online submissions for Rotate String.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate String.