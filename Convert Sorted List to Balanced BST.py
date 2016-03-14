"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def getLength(self, head):
        if head == None:
            return 0
        i = 0
        while head:
            head = head.next
            i += 1
        return i 

    def sortedListToBST(self, head):
        # write your code here
        if head == None:
            return None
        current = head 
        size = self.getLength(head)
        if size == 1:
            return head
        return self.sortedListToBSTHelper(size, current)
    
    def sortedListToBSTHelper(self, size, head):
        if size ==0:
            return None
        root = TreeNode(0)
        root.left = self.sortedListToBSTHelper(head, size / 2)
        root.val = head.val
        head = head.next 
        root.right = self.sortedListToBSTHelper(head, size - size/2 -1)
        return root
