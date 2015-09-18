"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        if root != None:
            self.invert(root)
        
        return root





    def invert(self, node):
        temp = node.left
        node.left = node.right
        node.right = temp

        if (node.left != None):
            self.invert(node.left)

        if (node.right != None):
            self.invert(node.right)

        return
