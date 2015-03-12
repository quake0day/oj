"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        cur = root
        if not root:
            root = node
            return root

        while cur:
            if cur.val == node.val:
                return root
            elif cur.val > node.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    return root

