"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.balanceHelper(root) != -1


    def balanceHelper(self, node):
    	if node == None:
    		return 0

    	left = self.balanceHelper(node.left)
    	if left == -1:
    		return -1
    	right = self.balanceHelper(node.right)
    	if right == -1:
    		return -1
    	diff = abs(left-right)
    	if (diff > 1):
    		return -1

    	if left > right:
    		return left + 1
    	else:
    		return right + 1

