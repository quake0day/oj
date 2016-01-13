class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        id_ = [i for i in xrange(n)]
    
        start = 0
        for edge in edges:
            i = self.root(id_, edge[0])
            j = self.root(id_, edge[1])
            id_[i] = j
        count = 0
        for i in xrange(len(id_)):
            if id_[i] == i:
                count += 1
        return count 
    def root(self, id_, i):
        while i != id_[i]:
            id_[i] = id_[id_[i]]
            i = id_[i]
        return i



a = Solution()
print a.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
print a.countComponents(5, [[0,1],[1,2],[0,2],[3,4]])
