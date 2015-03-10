class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if board == None or len(board) == 0:
        	return False
        if len(word) == 0:
        	return True


        for i in xrange(len(board)):
        	for j in xrange(len(board[i])):
        		if (board[i][j] == word[0]):
        			rst = self.find(board, i, j, word, 0)
        			if (rst):
        				return True
        return False


    def find(self, board, i, j, word, start):
    	if (start == len(word)):
    		return True

    	if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[start]):
    		return False

    	board[i][j] = '#'
    	rst = self.find(board, i-1, j, word, start+1) or \
    	self.find(board, i+1, j, word, start+1) or \
    	self.find(board, i, j-1, word, start+1) or \
    	self.find(board, i, j+1, word, start+1)
    	board[i][j] = word[start]
    	return rst