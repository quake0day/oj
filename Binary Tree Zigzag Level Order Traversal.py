# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     # def helper(root, stack, level):
    #     #     if root == None:
    #     #         return 
    #     #     if level + 1 > len(stack):
    #     #         stack.append([])
    #     #     stack[level].append(root)
    #     #     if level % 2 == 0:

    #     #         helper(root.right, stack, level+1)
    #     #         helper(root.left, stack, level+1)

    #     #     else:
    #     #         helper(root.left, stack, level+1)
    #     #         helper(root.right, stack, level+1)

    #     # stack = []
    #     # helper(root, stack, 0)
    #     # return stack
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        stack = []
        level = 1
        item = []
        item.append(root.val)
        res.append(item)
        stack.push(root)
        while stack:
            newStack = []
            item = []
            while stack:
                node = stack.pop()
                if level % 2 == 0:
                    if node.left != None:
                        newStack.append(node.left)
                        item.append(node.left.val)
                    if node.right != None:
                        newStack.append(node.right)
                        item.append(node.right.val)
                else:
                    if node.right != None:
                        newStack.append(node.right)
                        item.append(node.right.val)
                    if node.left != None:
                        newStack.append(node.left)
                        item.append(node.left.val)    
            level += 1
            if (len(item) > 0):
                res.append(item)
            stack = newStack

        return res