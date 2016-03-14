import collections
import itertools
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """
    def __init__(self):
        self.res = []
        self.pairs = []
        self.compare = []

    def isTweakedIdentical(self, a, b):
        # Write your code here
        if ( a == None and b == None):
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
            
        if (a != None and b != None):
            if self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left):
                return True
            if self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right):
                return True
        return False

    def getAll(self, root):
        final_res = []
        res = []
        queue = collections.deque()
        queue.append([root,0])
        level = 0
        while queue:
            root,level = queue.popleft()
            if len(res) < level + 1:
                res.append([])
            res[level].append(root)
            [queue.append([c, level+1]) for c in (root.left, root.right) if c ]

        for level in res:

            for i in xrange(len(level)):
                for j in xrange(i):
                    if i != j:
                        if level[i].val != None and level[j].val != None:
                            if self.isTweakedIdentical(level[i], level[j]):
                                final_res.append([level[i].val, level[j].val])
        return final_res





    def preorder(self, root):
        
        if not root:
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.res




    def getAllPairs(self, preorderlist):
        queue = collections.deque(preorderlist)
        if queue:
            root = queue.popleft()
            n = len(queue)
            half = int(n/2)
            if sorted(queue) not in self.compare:
                self.compare.append(sorted(queue))
            else:
                self.pairs.append(queue)
            print self.compare
            #print queue, collections.deque(itertools.islice(queue, 0, half)), collections.deque(itertools.islice(queue, half, n))
            self.getAllPairs(itertools.islice(queue, 0, half))
            self.getAllPairs(itertools.islice(queue, half, n))
        return self.pairs

    def deserialize(self, data):
        queue = collections.deque()
        i = 0

        while i < len(data):
            if not queue:
                root = TreeNode(data[i])
                queue.append(root)
                i += 1
                continue

            for _ in xrange(len(queue)):
                node = queue.popleft()
                node.left, node.right = [TreeNode(data[i+j]) for j in xrange(2)]
                [queue.append(c) for c in (node.left, node.right) if c]
                i += 2
        return root


    def recoverTree(self, data):

        def rec(data, pos):
            pos += 1
            if pos >= len(data) or data[pos] == None:
                return None, pos
            root = TreeNode(data[pos])
            print data[pos]
            root.left, pos = rec(data, pos)
            root.right, pos = rec(data, pos)
            return root, pos
        #root = TreeNode(data.popleft())
        pos = -1
        root, count = rec(data, pos)
        return root

    def serialize(self, root):
        queue = [root]
        [map(queue.append, (node.left, node.right)) for node in queue if node]
        data = []
        for item in queue:
            if item == None:
                data.append('x')
            else:
                data.append(str(item.val))
        return ":".join(data)
        #return ":".join(map(lambda n: n and str(n.val) or 'x', queue))
    
    def buildTreeNode(self, val):
        return TreeNode(int(val)) if val != 'x' else None

    def deserialize2(self, data):
        queue = collections.deque()
        data = data.split(":")
        i = 0
        while  i < len(data):
            if not queue:
                root = self.buildTreeNode(data[i])
                queue.append(root)
                i += 1
                continue

            for _ in xrange(len(queue)):
                node = queue.popleft()
                node.left, node.right = [self.buildTreeNode(data[i+j]) for j in xrange(2)]
                [queue.append(c) for c in (node.left, node.right) if c]
                i += 2
    
    def printTree(self, root, level):
        if not root:
            print "  "

        if root:
            print " "*level+str(root.val)
            if root.left:
                self.printTree(root.left, level+1)
            if root.right:
                self.printTree(root.right, level+1)



data = [1,2,5,4,3,4,6,2,1,None,None,1,2,None,None]
tt = Solution()
root = tt.deserialize(data)
tt.printTree(root, 0)

#list__ =  tt.preorder(root)
print tt.getAll(root)
#print tt.getAllPairs(list__)
#tt.printTree(newroot,0)
# print root.val
# print root.left.val
# print root.right.val

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# a.left = b
# a.right = c 
# b.left = d 
# new_data = tt.serialize(a)
# print new_data
# newroot = tt.deserialize2(new_data)
# tt.printTree(newroot, 0)
# e = TreeNode(1)
# f = TreeNode(2)
# g = TreeNode(3)
# h = TreeNode(4)
# e.left = g
# e.right = f
# f.right = h
# tt.printTree(e, 0)
# t = Solution()
# print t.isTweakedIdentical(a, e)
