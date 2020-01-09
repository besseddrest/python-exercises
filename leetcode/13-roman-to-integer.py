# https://leetcode.com/problems/roman-to-integer/

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution1:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        length = len(s)

        if length == 1:
            return romans[s]

        i = 0
        total = 0

        while i < length:
            curr = s[i]
            total += romans[s[i]]

            if i > 0:
                if curr in 'VX' and s[i - 1] == 'I':
                    total += -2

                if curr in 'LC' and s[i - 1] == 'X':
                    total += -20

                if curr in 'DM' and s[i - 1] == 'C':
                    total += -200

            i += 1

        return total 

# Runtime: 
# 52 ms, faster than 28.82% of Python3 online submissions for Roman to Integer.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution2:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        length = len(s)

        if length == 1:
            return romans[s]

        i = 0
        total = 0

        while i < length:
            less = 0
            curr = s[i]

            if i > 0:
                if curr in 'VX' and s[i - 1] == 'I':
                    less = -2
                    pass

                if curr in 'LC' and s[i - 1] == 'X':
                    less = -20
                    pass

                if curr in 'DM' and s[i - 1] == 'C':
                    less = -200

            total += romans[s[i]] + less

            i += 1

        return total 

# Runtime: 
# 48 ms, faster than 49.67% of Python3 online submissions for Roman to Integer.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution3:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return romans[s]

        i = 0
        total = 0

        while i < len(s):
            less = 0
            curr = s[i]

            if i > 0:
                if curr in 'VX' and s[i - 1] == 'I':
                    less = -2
                    pass

                if curr in 'LC' and s[i - 1] == 'X':
                    less = -20
                    pass

                if curr in 'DM' and s[i - 1] == 'C':
                    less = -200

            total += romans[s[i]] + less

            i += 1

        return total 

# Runtime: 
# 36 ms, faster than 95.02% of Python3 online submissions for Roman to Integer.
# 
# Memory Usage: 
# 12.9 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution4:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return romans[s]

        total = 0

        for i in range(0, len(s)):
            less = 0
            curr = s[i]

            if i > 0:
                if curr in 'VX' and s[i - 1] == 'I':
                    less = -2
                    pass

                if curr in 'LC' and s[i - 1] == 'X':
                    less = -20
                    pass

                if curr in 'DM' and s[i - 1] == 'C':
                    less = -200

            total += romans[s[i]] + less

        return total 

# Runtime: 
# 44 ms, faster than 71.35% of Python3 online submissions for Roman to Integer.
# 
# Memory Usage: 
# 12.9 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        # value map
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # return if just one value
        if len(s) == 1:
            return romans[s]

        total = 0

        for i in range(0, len(s)):
            less = 0
            curr = s[i]

            # if we're past the first item, we can now check the previous value
            if i > 0:
                # `less` value is doubled because we've already added it to the total in the previous iteration
                if curr in 'VX' and s[i - 1] == 'I':
                    less = -2
                    pass
                elif curr in 'LC' and s[i - 1] == 'X':
                    less = -20
                    pass
                elif curr in 'DM' and s[i - 1] == 'C':
                    less = -200
            
            # add total plus current value plus the less value
            total += romans[s[i]] + less

        return total 

# Runtime: 
# 32 ms, faster than 98.64% of Python3 online submissions for Roman to Integer.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.