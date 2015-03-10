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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return None
        slow = head.next
        fast = head.next.next

        while (fast != None and fast != slow):
            slow = slow.next
            try:
                fast = fast.next.next
            except:
                fast = fast.next
        if fast == None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

