"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        if node == None or node.next == None:
        	return False


        temp = node.next
        node.val = temp.val
        node.next = temp.next
        return True


