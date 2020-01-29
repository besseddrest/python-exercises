# https://leetcode.com/problems/fizz-buzz/submissions/

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        words = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                words.append("FizzBuzz")
                continue
            if i % 3 == 0:
                words.append("Fizz")
                continue
            if i % 5 == 0:
                words.append("Buzz")
                continue
            
            words.append(str(i))
            
        return words

# Runtime: 36 ms, faster than 93.73% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.