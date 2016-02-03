class Solution(object):

    def dfs(self, v, visit, gr, ans):
        if visit[v] == -1:
            return False

        elif visit[v] == 1:
            return True

        visit[v] = -1
        for i in gr[v]:
            if visit[i] == -1 or not self.dfs(i, visit, gr, ans):
                return False
        ans.append(v)
        visit[v] = 1
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for x in range(numCourses)]
        visited = [0] * numCourses
        ans = []

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        for i in xrange(numCourses):
            if not self.dfs(i, visited, graph, ans):
                return []
        return ans
