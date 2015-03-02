"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        head = dummy
        while l1 != None or l2 != None:
        	if l1 != None and l2 != None:
        		if l1.val < l2.val:
	        		new_node = ListNode(l1.val)
	        		head.next = new_node
	        		head = head.next
	        		l1 = l1.next
	        	elif l1.val >= l2.val:
	        		new_node = ListNode(l2.val)
	        		head.next = new_node
	        		head = head.next
	        		l2 = l2.next
        	elif l1 != None and l2 == None:
        		new_node = ListNode(l1.val)
        		head.next = new_node
        		head = head.next
        		l1 = l1.next
        	elif l1 == None and l2 != None:
        		new_node = ListNode(l2.val)
        		head.next = new_node
        		head = head.next
        		l2 = l2.next
        return dummy.next





