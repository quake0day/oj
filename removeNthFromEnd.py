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
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if head == None:
            return 0

        dummy = ListNode(0)
        dummy.next = head
        h1 = dummy 
        h2 = dummy
        h2_head = h2
        while n > 0:
            h1 = h1.next
            n -= 1
        while h1.next != None:
            h1 = h1.next
            h2 = h2.next
        h2.next = h2.next.next
        return h2_head.next

