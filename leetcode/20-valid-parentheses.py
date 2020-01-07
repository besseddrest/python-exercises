# https://leetcode.com/problems/valid-parentheses/

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def isValid(self, s: str) -> bool:
    # if blank
    if len(s) == 0:
            return True

    # if odd number of chars or starts with closing bracket
    if len(s) % 2 == 1 or s[0] in ')}]':
        return False
        
    all = []
    # create a dict so we know the correct partner chars
    partners = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        # keep track of opened brackets in order
        if char in '([{':
            all.append(char)
            continue

        # if we passed the above check, its a closing bracket
        # pop the last character and see if it is the partner of this closing bracket
        if all.pop() != partners[char]:
            return False

    # we've gone through the string, all open brackets should have been popped    
    return len(all) == 0

# Runtime: 
# 20 ms, faster than 97.71% of Python3 online submissions for Valid Parentheses.
# 
# Memory Usage: 
# 12.6 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.