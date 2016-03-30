class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = {key:[] for key in xrange(numCourses)}
        indegree = [0] * numCourses
        for p in prerequisites:
            a,b = p
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
        q = []
        for i in xrange(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            val = q.pop()
            for item in graph[val]:
                graph[item].remove(val)
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
            del graph[val]
        return True if len(graph) == 0 else False
a = Solution()
# print a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
# print a.findOrder(2, [[1,0]])
# print a.findOrder(2, [[1,0],[0,1]])

# print a.findOrder(1, [])
# print a.findOrder(2, [])