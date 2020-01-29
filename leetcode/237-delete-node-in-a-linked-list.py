# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next != None:
            node.val = node.next.val
            node.next = node.next.next

# Runtime: 28 ms, faster than 97.87% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Delete Node in a Linked List.