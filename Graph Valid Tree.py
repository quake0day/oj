class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {}
        indegree = {key:0 for key in xrange(n)}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
                indegree[edge[0]] += 1
            else:
                graph[edge[0]].append(edge[1])
                indegree[edge[0]] += 1
        q = []
        for key, val in indegree.iteritems():
            if val == 0:
                q.append(key)
        while q:
            node = q.pop()
            count = 0
            for key, val in graph.iteritems():
                if node in val:
                    count += 1
                    indegree[key] -= 1
                    if indegree[key] == 0:
                        q.append(key)
                    val.remove(node)

            if count > 1:
                return False 
        print graph
        return True






a = Solution()
print a.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print a.validTree(2, [[0,1]])
print a.validTree(4, [[0,1], [2,3]])

print a.validTree(2, [[1,0]])
print a.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
