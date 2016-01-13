# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        if root != None:
            st.append([root, False])
            while len(st) != 0:
                tmp  = st[-1]
                if tmp[1] == True:
                    res.append(st.pop()[0].val)
                elif tmp[0].left == None and tmp[0].right == None:
                    res.append(st.pop()[0].val)
                else:
                    if tmp[0].right != None:
                        st.append([tmp[0].right, False])
                    if tmp[0].left != None:
                        st.append([tmp[0].left, False])
        
