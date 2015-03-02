
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderButtom(self, root):
        # write your code here
        res = []
        if root == None: return res
        Solution.L = {}
        self.preOrder(root, 0)
        for i in sorted(Solution.L.keys(), reverse = True):
        	res.append(Solution.L[i])
        return res
    def preOrder(self, root, level):
    	if level not in Solution.L:
    		Solution.L[level] = [root.val]
    	else:
    		Solution.L[level].append(root.val)
    	if root.left:
    		self.preOrder(root.left, level + 1)
    	if root.right:
    		self.preOrder(root.right, level + 1)
        

