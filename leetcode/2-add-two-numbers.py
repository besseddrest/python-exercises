# https://leetcode.com/problems/add-two-numbers/

"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        
        # concatenate each number to a string
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        # reverse each number, recast as string, add together
        total = int(num1[::-1]) + int(num2[::-1])
        # reverse the total and cast as string
        total = str(total)[::-1]

        # start a new list with a placeholder
        new_list = ListNode(-1)
        # head allows us to advance to next item
        head = new_list
        
        # for each character in the total
        for i in total:
            # create a linked list by recasting the char as an int
            head.next = ListNode(int(i))
            head = head.next

        # return the next ListNode after our placeholder 
        return new_list.next
        
# Success on first submit!!
#
# Runtime: 
# 72 ms, faster than 34.38% of Python3 online submissions for Add Two Numbers.
# 
# Memory Usage: 
# 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        
        # preprend the string with each number so we don't have to reverse before adding
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
            
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        # add the numbers, cast as string, and reverse   
        total = str(int(num1) + int(num2))[::-1]

        new_list = ListNode(-1)
        head = new_list
        
        for i in total:
            head.next = ListNode(int(i))
            head = head.next
            
        return new_list.next

# Runtime: 
# 68 ms, faster than 60.01% of Python3 online submissions for Add Two Numbers.
# 
# Memory Usage: 
# 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []
        
        while l1:
            arr1.insert(0, l1.val)
            l1 = l1.next
            
        while l2:
            arr2.insert(0, l2.val)
            l2 = l2.next
            
        num1 = 0
        num2 = 0
        
        for num in arr1:
            num1 = (num1 * 10) + num
            
        for num in arr2:
            num2 = (num2 * 10) + num
            
        total = str(num1 + num2)[::-1]

        l1 = ListNode(-1)
        head = l1
        
        for i in total:
            head.next = ListNode(int(i))
            head = head.next
            
        return l1.next

# Runtime: 
# 64 ms, faster than 80.76% of Python3 online submissions for Add Two Numbers.
# 
# Memory Usage: 
# 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.