"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        return self.gen(1, n)



    def gen(self, start, end):
    	if start > end:
    		return [None]
    	res = []
    	for rootVal in xrange(start, end + 1):
    		leftList = self.gen(start, rootVal - 1)
    		rightList = self.gen(rootVal + 1, end)
    		for i in leftList:
    			for j in rightList:
    				root = TreeNode(rootVal)
    				root.left = i
    				root.left = j
    				res.append(root)
    	return res

