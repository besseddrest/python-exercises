# Source: https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
#

"""
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # placeholder list that we build
    temp_node = ListNode(-1)
    # points to the 'head' of the list we are building 
    head = temp_node
    
    # while there are still nodes in both lists
    while l1 and l2:
        # if l1 value is smaller, make it our next node, and advance l1
        if l1.val < l2.val:
            temp_node.next = l1
            l1 = l1.next
        # else the l2 value is smaller, make it next and advance l2
        else:
            temp_node.next = l2
            l2 = l2.next
            
        # advance to next empty slot
        temp_node = temp_node.next
                        
    # when the while loop completes, we are left with a single list, 
    # which contains all values larger than our last node in temp_node
    # we can just assign the temp_node.next with the remaining list,
    # since we know that list is sorted already
    if l1:
        temp_node.next = l1
    else:
        temp_node.next = l2
        
    # we return the next ListNode from head, because head is -1
    return head.next

# Runtime: 
# 32 ms, faster than 80.81% of Python3 online submissions for Merge Two Sorted Lists.
# 
# Memory Usage: 
# 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
