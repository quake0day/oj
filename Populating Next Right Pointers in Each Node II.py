class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        p = root.next
        while p:
            if p.left != None:
                p = p.left
                break
            elif p.right != None:
                p = p.right
                break
            p = p.next
        if (root.right != None):
            root.right.next = p
        if(root.left != None):
            if root.right != None:
                root.left.next = root.right
            else:
                root.left.next = p
        self.connect(root.right)

        self.connect(root.left)
