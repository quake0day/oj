# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(1)
        runner = dummy
        carry = 0
        cur = 0

        while l1 != None or l2 != None:
        	if l1 == None:
        		cur = carry + l2.val
        		carry = cur / 10
        		cur %= 10
        		l2 = l2.next
        	elif l2 == None:
        		cur = carry + l1.val
        		carry = cur / 10
        		cur %= 10
        		l1 = l1.next
        	else:
        		cur = carry + l1.val + l2.val
        		carry = cur / 10
        		cur %= 10
        		l1 = l1.next
        		l2 = l2.next


        	runner.next = ListNode(cur)
        	runner = runner.next
        if (carry != 0):
        	runner.next = ListNode(carry)
        return dummy.next
