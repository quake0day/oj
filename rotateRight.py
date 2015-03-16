# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if (head == None or k == 0):
        	return head
        p = head
        length = 1
        while p.next != None:
        	length += 1
        	p = p.next

        p.next = head
        k = k % length
        for i in xrange(length - k):
        	p = p.next

        head = p.next
        p.next = None
        return head
