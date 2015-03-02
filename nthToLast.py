"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        if head == None:
            return head
        fast = head
        slow = head
        while n != 0:
            fast = fast.next 
            n -= 1
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow
