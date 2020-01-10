# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_list = ListNode('x')
        temp_node = new_list
        
        while head:
            if temp_node.val != head.val:
                temp_node.next = ListNode(head.val)
                temp_node = temp_node.next
            
            head = head.next
            
        return new_list.next

# Runtime: 
# 44 ms, faster than 20.56% of Python3 online submissions for Remove Duplicates from Sorted List.
# 
# Memory Usage: 
# 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.

"""
Fastest accepted solution:
Note: I almost had this but was not checking for node.next in the while condition

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
"""