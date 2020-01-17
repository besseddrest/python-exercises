# https://leetcode.com/problems/swap-nodes-in-pairs/

def swapPairs1(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    new_list = ListNode(-1)
    temp_node = new_list
    
    while head:
        if head.next is None:
            temp_node.next = ListNode(head.val)
            temp_node.next.next = None
            break
        else:
            temp_node.next = ListNode(head.next.val)
            temp_node.next.next = ListNode(head.val)
        
        if head.next == None:
            temp_node.next = None
            head = head.next
        else:
            temp_node = temp_node.next.next
            head = head.next.next
        
    return new_list.next
    

# Runtime: 32 ms, faster than 31.26% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.

def swapPairs2(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    new = ListNode(-1)
    temp = new
    
    while head:
        if head.next is None:
            temp.next = ListNode(head.val)
            temp.next.next = None
            break
        else:
            temp.next = ListNode(head.next.val)
            temp.next.next = ListNode(head.val)
        
        temp = temp.next.next
        head = head.next.next
        
    return new.next

# i guess shorter var names helps speed significantly
# removed second conditional check
# Runtime: 24 ms, faster than 89.87% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.

def swapPairs3(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    new = ListNode(-1)
    temp = new

    while head:
        if head.next is None:
            temp.next = ListNode(head.val)
            temp.next.next = None
            break
    
        temp.next = ListNode(head.next.val)
        temp.next.next = ListNode(head.val)
        temp = temp.next.next
        head = head.next.next

    return new.next

# removing the 'else' runs slower, why?
# Runtime: 28 ms, faster than 70.20% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.