# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        vals.pop(-n)
        
        if len(vals) == 0:
            return head
        
        head = ListNode(vals[0])
        temp = head
        
        for i in range(1, len(vals)):
            temp.next = ListNode(vals[i])
            temp = temp.next
            
        return head

# Runtime: 60 ms, faster than 7.72% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.

class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        if len(vals) == 1:
            return head
            
        vals.pop(-n)
        
        head = ListNode(vals[0])
        temp = head
        
        for num in vals[1:]:
            temp.next = ListNode(num)
            temp = temp.next
            
        return head

# Runtime: 36 ms, faster than 11.60% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.

class Solution3:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for i in range(n + 1):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next

# Runtime: 40 ms, faster than 7.72% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.