# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left == None and root.right == None:
            return True 
        elif root.left == None or root.right == None:
            return False 
        ql = collections.deque()
        qr = collections.deque()
        ql.append(root.left)
        qr.append(root.right)
        while ql and qr:
            l = ql.popleft()
            r = qr.popleft()

            if not l and not r:
                continue 
            if l.val != r.val:
                return False 
            if (l.left and r.right) or (l.left == None and r.right == None):
                ql.append(l.left)
                qr.append(r.right)
            else:
                return False 
            if (l.right and r.left) or (l.right == None and r.left == None):
                ql.append(l.right)
                qr.append(r.left)
            else:
                return False 
        
        return True