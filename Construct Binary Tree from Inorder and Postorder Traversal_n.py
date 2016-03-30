# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None 
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index+1:-1])
        return root
        # def findRoot(postorder):
        #     if len(postorder) == 0 or postorder == None:
        #         return None
        #     return postorder[-1]

        # def findSubTree(root, inorder, postorder):
        #     if len(inorder) != len(postorder):
        #         raise "ERROR"

        #     subTrees = inorder.split(root.val)
        #     POrderedLeftTree = []
        #     POrderedRightTree = []
        #     if len(subTrees) == 2:
        #         ILeftTree = subTrees[0]
        #         IRightTree = subTrees[1]
        #         for item in postorder:
        #             if item in ILeftTree:
        #                 POrderedLeftTree.append(item)
        #             elif item in IRightTree:
        #                 POrderedRightTree.append(item)
        #     elif len(subTrees) < 2:
        #         print "FUCK"

        #     return POrderedLeftTree, POrderedRightTree, ILeftTree, IRightTree
       
        # def buildTree(root, rootleft, rootright):


        # while root:
        #     root = findRoot(postorder)
        #     newTRoot = TreeNode(root.a)
        #     POrderedLeftTree, POrderedRightTree, inorderLeftTree, inorderRightTree = findSubTree(root, inorder, postorder)
