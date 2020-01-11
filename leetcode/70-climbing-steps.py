# https://leetcode.com/problems/climbing-stairs/submissions/
"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution1:
    def climbStairs(self, n: int) -> int:
        # handle the first two ways (0 steps - don't step, 1 step: move 1 step)
        ways = [1, 1]
        
        # to get to 2 steps, u start from either step 0 or step 1
        # so add all the ways you get to step 0 plus all the ways to get to step 1
        for i in range(2, n + 1):
            ways.append(ways[i - 1] + ways[i - 2])
            
        return ways[n]
        
# Runtime: 
# 28 ms, faster than 55.88% of Python3 online submissions for Climbing Stairs.
# 
# Memory Usage: 
# 12.6 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

class Solution2:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1]
        
        i = 2

        while i <= n:
            ways.append(ways[i - 1] + ways[i - 2])
            i += 1
            
        return ways[n]

# Runtime: 
# 24 ms, faster than 83.39% of Python3 online submissions for Climbing Stairs.
# 
# Memory Usage: 
# 12.6 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1]
        
        i = 2

        while i <= n:
            ways[i] = ways[i - 1] + ways[i - 2]
            i += 1
            
        return ways[n]