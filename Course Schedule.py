class Solution(object):

    def dfs(self, v, visit, gr):
        if visit[v] == 1:
            return True

        visit[v] = -1
        for i in gr[v]:
            if visit[i] == -1 or not self.dfs(i, visit, gr):
                return False
        visit[v] = 1
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        gr = [[] for x in range(numCourses)]
        visit = [0 for x in range(numCourses)]

        for p in prerequisites:
            if p[0] not in gr[p[1]]:
                gr[p[1]].append(p[0])

        for v in range(numCourses):
            if visit[v] != 1:
                if not self.dfs(v, visit, gr):
                    return False
        return True
