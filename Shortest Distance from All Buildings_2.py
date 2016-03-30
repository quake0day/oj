import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        buildings = sum(row.count(1) for row in grid)
        hit = [[0] * N for _ in xrange(M)]
        distSum = [[0] * N for _ in xrange(M)]
        def BFS(s_x, s_y):
            visited = [[False] * N for _ in xrange(M)]
            visited[s_x][s_y] = True
            count1 = 1
            queue = collections.deque([(s_x, s_y, 0)])
            directions = [[1,0],[0,1],[0,-1],[-1,0]]
            while queue:
                x, y, dist = queue.popleft()
                for i, j in directions:

                    if  0<= (x + i) < M and 0 <= (y+j) < N and not visited[x+i][y+j]:
                        visited[x+i][y+j] == True

                        if not grid[x+i][y+j] == 0:
                            queue.append((x+i, y+j, dist+1))
                            hit[x+i][y+j] += 1
                            distSum[x+i][y+j] += dist + 1
                        elif grid[x+i][y+j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in xrange(M):
            for y in xrange(N):
                if grid[x][x] == 1:
                    if not BFS(x, y): return -1
        return min([distSum[i][j] for i in xrange(M) for j in xrange(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])




a = Solution()
print a.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])