# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if head is None:
            return True
        
        # find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        
        # reverse second half
        
        p, last = slow.next, None
        
        while p:
            next = p.next 
            p.next = last 
            last, p = p, next
        
        # check palidrome
        p1, p2 = last, head 
        
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next 
        
        # resume linked list
        
        p, last = last, None 
        while p:
            next = p.next 
            p.next = last
            last,p = p, next 
        slow.next = last 
        return p1 is None
