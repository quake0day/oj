"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        output = []
        if root == None:
            return output
        self.searchRangeHelper(root, k1, k2, output)
        output = sorted(output)
        return output

    def searchRangeHelper(self, root, k1, k2, output):
        #output = copy.deepcopy(output)
        if root == None:
            return 
        if root.val >= k1 and root.val <= k2:
            output.append(root.val) 
        if root.val > k1:
            self.searchRangeHelper(root.left, k1, k2, output)
        if root.val < k2:
            self.searchRangeHelper(root.right, k1, k2, output)
