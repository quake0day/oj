"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 == None:
        	return True
        elif T1 == None:
        	return False
        return self.isSameTree(T1, T2) or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)



    def isSameTree(self, T1, T2):
    	if (T1 == None and T2 == None):
    		return True
    	if (T1 == None or T2 == None):
    		return False
    	if (T1.val != T2.val):
    		return False
    	return self.isSameTree(T1.left, T2.left) and self.isSameTree(T1.right, T2.right)
