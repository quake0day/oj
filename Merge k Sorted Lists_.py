# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if not lists or n == 0:
        	return None
        elif n == 1:
        	return lists[0]
        elif n == 2:
        	return self.mergeTwoLists(lists[0], lists[1])
        else:
        	mid = n / 2
        	return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])

    def mergeTwoLists(self, list1, list2):
    	if list1 == None:
    		return list2
    	if list2 == None:
    		return list1

    	dummy = ListNode(-1)
    	p = dummy
    	while list1 != None and list2 != None:
    		if list1.val > list2.val:
    			p.next = list2
    			list2 = list2.next 
    		else:
    			p.next = list1
    			list1 = list1.next
    		p = p.next
    	if list1 != None:
    		p.next = list1 
    	else:
    		p.next = list2
    	return dummy.next