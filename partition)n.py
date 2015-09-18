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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        NewList_small = ListNode(None)
        NewList_large = ListNode(None)
        while head.next != None:
            if head.val < x:
                newNode = ListNode(head.val, None)
                NewList_small.next = newNode
            else:
                ListNode.n


