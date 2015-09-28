"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import sys
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        NewList_small = ListNode(-sys.maxint)
        NewList_large = ListNode(-sys.maxint)
        smaller = NewList_small
        larger = NewList_large
        while head != None:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
            smaller.next = NewList_large.next 
            larger.next = None
        return NewList_small.next


