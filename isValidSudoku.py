class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
    	for i in xrange(9):
    		for j in xrange(9):
    			if board[i][j] != '.':
    				for k in xrange(9):
    					if j != k:
	    					if board[i][j] == board[i][k]:
	    						return False
	    				if i != k:
	    					if board[i][j] == board[k][j]:
	    						return False
        return True



a = Solution()
print a.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])