def numIslands(self, grid):
	if grid == None or len(grid) == 0 or len(grid[0]) == 0:
		return 0
	count = 0



	for i in xrange(len(grid)):
		for j in xrange(len(grid[0]):
			if grid[i][j] == 1:
				count += 1
				self.remove(grid, i , j)
	return count



def remove(self, grid, row, col):
	if row < 0 or row >= len(grid) or col < 0 or col >= len(grid) or grid[row][col] == 0:
		return 


	grid[row][col] = 0

	self.remove(grid, row+1, col)
	self.remove(grid, row-1, col)
	self.remove(grid, row, col-1)
	self.remove(grid, row, col+1)
