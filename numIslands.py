class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
        	return 0
        count = 0

        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		if grid[i][j] == 1:
        			count += 1
        			self.remove(grid, i, j)
        return count


    def remove(self, grid, row, col):
    	if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
    		return

    	grid[row][col] = 0

    	self.remove(grid, row+1, col)
    	self.remove(grid, row-1, col)
    	self.remove(grid, row, col-1)
    	self.remove(grid, row, col+1)



a = Solution()
print a.numIslands([
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
])
