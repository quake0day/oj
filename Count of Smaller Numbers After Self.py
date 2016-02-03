class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        bst = BST()
        for i in xrange(len(nums), -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans 


class TreeNode(object):
    def __init__(self, val):
        # left count
        self.leftCnt = 0
        self.val = val

        # self count
        self.cnt = 1
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return 0

        root = self.root
        cnt = 0 
        while root:
            if val < root.val:
                root.leftCnt += 1
                if root.left == None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftCnt + root.cnt 
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right 
            else:
                cnt += root.leftCnt
                root.cnt += 1
                break
        return cnt 
                     
