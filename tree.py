pairs = [[1, 2], [1, 5], [2, 4], [2, 3], [5,7], [5,6], [4,10], [4,9], [7, 11], [7, 12]]
import collections

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 



def findRoot(pairs):
    parents, child = zip(*pairs)
    root = list(set(parents)-set(child))[0]
    return root

parents, child = zip(*pairs)
uniq = set(parents).union(set(child))
n = len(uniq)
print n
print uniq
def validTree(edges, n):
    if len(edges) != n -1:
        return False
    max_num = max(map(max, edges))
    neighbors = {i:[] for i in range(max_num+1)}
    for v, w in edges:
        neighbors[v].append(w)
        neighbors[w].append(v)
    
    queue = []
    queue.append(findRoot(edges))
    while queue:
        queue.extend(neighbors.pop(queue.pop(0), []))

    for key, val in neighbors.items():
        if key not in edges and val == []:
            continue
        else:
            return False
    return True

def buildTree(edges):
    rootval = findRoot(edges)
    dummy = TreeNode(-1)
    root = TreeNode(str(rootval))
    dummy = root
    queue = collections.deque([root])

    while queue:
        root = queue.popleft()
        childVal = []
        for i in xrange(len(edges)):
            if str(edges[i][0]) == root.val:
                childVal.append(str(edges[i][1]))
        if len(childVal) == 2:
            for c in childVal:
                queue.append(TreeNode(c))
            root.right = queue[-1]
            root.left = queue[-2]
        elif len(childVal) == 1:
            queue.append(TreeNode(c) for c in childVal)
            root.right = queue[-1]
            root.left = None 
    return dummy 
root = buildTree(pairs)
print root.val
print root.left.val
print root.right.val

def printTree(root):

    level = 0
    queuea = collections.deque([root])

    while queuea:
        node = queuea.popleft()
        nodeVal = node.val if node else "None"
        print " " * level + nodeVal
        if node.right:
            queuea.append(node.right)
        if node.left:
            queuea.append(node.left)
        level += 1

printTree(root)
    
# def printTree(edges):
#     level = 0
#     while edges:
#         root = findRoot(edges)
#         print " " * level + str(root)
#         edges.remove(root)
#         level += 1
# printTree(pairs)

    # if len(edges) != set(edges)
# def findRoot2(pairs):
#     for i in pairs:
#         root1 = self.find(root, i[0])
#         root2 = self.find(root, i[1])
#         if root1 == root2:
#             return False
#def isValidTree(pairs):
