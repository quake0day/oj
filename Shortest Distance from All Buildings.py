class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        def bfs(grid, i, j, dist, nums):
        	directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        	m = len(grid)
        	n = len(grid[0])
        	pre_level = [(i,j)]
        	dist = 0
        	visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        	visited[i][j] = True
        	while pre_level:
        		dist += 1
        		cur_level = []
        		for i , j in pre_level:
        			for dir_ in directions:
        				I, J = i + dir_[0], j + dir_[1]
        				if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
        					nums[I][J] += 1
        					dists[I][J] += dist 
        					cur_level.append((I, J))
        					visited[I][J] = True
        		pre_level = cur_level




        m, n, dist = len(grid), len(grid[0]), 0
        # record the distants sum
        dists = [[0 for _ in xrange(n)] for _ in xrange(m)]

        # records the buildings that can be reached
        nums = [[0 for _ in xrange(n)] for _ in xrange(m)]
        buildingsNUM = 0 
        for i in xrange(m):
        	for j in xrange(n):
        		if grid[i][j] == 1:
        			buildingsNUM += 1
        			bfs(grid, i, j, dists, nums)

        shortest = float('inf')

        for i in xrange(m):
        	for j in xrange(n):
        		if dists[i][j] < shortest and nums[i][j] == buildingsNUM:
        			shortest = dists[i][j]
        return shortest if shortest != float('inf') else -1

a = Solution()
print a.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])