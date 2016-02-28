# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum, path):
            if root == None:
                return 
            if sum == root.val and root.left == None and root.right == None:
                path.append(root.val)
                self.final_res.append(path)
                print self.final_res, root.val
                return
            dfs(root.left, sum-root.val, path+[root])
            dfs(root.right, sum-root.val, path+[root])
        
        self.final_res = []
        dfs(root, sum, [])
        return self.final_res

a = Solution()
root = TreeNode(1)
print a.pathSum(root,1)