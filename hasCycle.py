"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        h1 = head
        h2 = head
        while h1 != None:
        	h1 = h1.next
        	if h1 != None:
        		h1 = h1.next 
        		h2 = h2.next 
        		if h1 == h2:
        			return True
        return False