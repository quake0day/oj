# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        if root.right == None and root.left == None:
            return [[root.val]]
        level = 0
        q = collections.deque()
        q.append([root, level])
        while q:
            root, level = q.popleft()
            if root == None:
                continue
            if len(res) < level - 1:
                res.append([])
            res[level].append(root.val)
            q.append([root.left, level+1])
            q.append([root.right, level+1])
        return res 
