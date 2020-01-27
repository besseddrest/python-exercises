# https://leetcode.com/problems/odd-even-linked-list/

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        nums = []
        i = 1
        isEven = True
        
        temp = head.next
        
        while temp and temp.next:
            even = temp.next.val
            odd = temp.val
            
            temp.val = even
            temp.next.val = odd
            
            
            # if isEven:
            #     nums.insert(i, temp.val)
            #     i += 1
            #     isEven = False
            # else:
            #     nums.append(temp.val)
            #     isEven = True

            temp = temp.next
            
        temp = head
        
        for i in range(len(nums)):
            temp.val = nums[i]
            temp = temp.next
            
        return head
            
# Runtime: 44 ms, faster than 45.89% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.