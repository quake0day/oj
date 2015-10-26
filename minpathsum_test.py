def minPathsum(self, grid):
	n = len(grid)
	m = len(grid[0])

	path_sum = [[0] * m for row in xrange(n)]

	path_sum[0][0] = grid[0][0]

	for i in xrange(n):
		for j in xrange(m):
			if i >= 0 and j >= 0:
				if i >= 1 and j >= 1:
					path_sum[i][j] = min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]
				elif i >=1 and j < 1:
					path_sum[i][j] = path_sum[i-1][j] + grid[i][j]
				else:
					path_sum[i][j] = path_sum[i][j-1] + grid[i][j]

	return path_sum[-1][-1]