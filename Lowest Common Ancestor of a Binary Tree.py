# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack_p = []
        stack_q = []
        def dfs(stack, node, target):
            if node.val == target:
                return
            lastVisit = None
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left 
                else:
                    peek = stack[-1]
                    if peek.right and lastVisit != peek.right:
                        node = peek.right 
                    else:
                        if peek == target:
                            return stack 
                        lastVisit = stack.pop()
                        root = None 
            return stack 



        pathP = dfs(stack_p, root, p)
        pathQ = dfs(stack_q, root, q)
        min_len = min(len(pathP), len(pathQ))
        x = 0
        ans = None 
        while x < min_len and pathP[x] == pathQ[x]:
            ans, x = pathP[x], x + 1
        return ans 