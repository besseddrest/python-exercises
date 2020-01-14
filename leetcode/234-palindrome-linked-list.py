# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next == None:
            return True
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        rev = nums[::-1]
        
        for i in range(0, len(nums)):
            if nums[i] != rev[i]:
                return False
            
        return True

# Runtime: 68 ms, faster than 73.18% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 23.1 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.

class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next == None:
            return True
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        return nums == nums[::-1]

# why slower?
# Runtime: 72 ms, faster than 50.80% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 23 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.