class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        rows = len(matrix)
        if rows == 0:
        	return 
        cols = len(matrix[0])
        if cols == 0:
        	return 
        zerorow0 = False
        zerocol0 = False
        for ci in xrange(cols):
        	if matrix[0][ci] == 0:
        		zerorow0 = True
        		break
        for ri in xrange(rows):
        	if matrix[ri][0] == 0:
        		zerocol0 = True
        		break


        for ri in xrange(rows):
        	for ci in xrange(cols):
        		if matrix[ri][ci] == 0:
        			matrix[0][ci] = 0
        			matrix[ri][0] = 0


        for ri in xrange(1, rows):
        	for ci in xrange(1, cols):
        		if matrix[0][ci] == 0 or matrix[ri][0] == 0:
        			matrix[ri][ci] = 0


        if zerorow0:
        	for ci in xrange(cols):
        		matrix[0][ci] = 0

        if zerocol0:
        	for ri in xrange(rows):
        		matrix[ri][0] = 0
        return matrix
