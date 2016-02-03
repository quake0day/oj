class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        firstRowHasZero = False
        firstColHasZero = False
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return 
        for col in xrange(0, len(matrix[0])):
        	if matrix[0][col] == 0:
        		firstRowHasZero = True
        		break

        for row in xrange(0, len(matrix)):
        	if matrix[row][0] == 0:
        		firstColHasZero = True
        		break

        for row in xrange(1, len(matrix)):
        	for col in xrange(1, len(matrix[0])):
        		if matrix[row][col] == 0:
        			matrix[0][col] = 0
        			matrix[row][0] = 0

        for row in xrange(1, len(matrix)):
        	for col in xrange(1, len(matrix[0])):
        		if matrix[row][0] == 0 or matrix[0][col] == 0:
        			matrix[row][col] = 0

        if firstRowHasZero:
        	for col in xrange(0, len(matrix[0])):
        		matrix[0][col] = 0

       	if firstColHasZero:
       		for row in xrange(0, len(matrix)):
       			matrix[row][0] = 0
       	return firstRowHasZero, firstColHasZero, matrix
        # rownum = len(matrix)
        # colnum = len(matrix[0])
        # row = [False for _ in xrange(rownum)]
        # colnum = [False for _ in xrange(colnum)]

        # for i in xrange(rownum):
        # 	for j in xrange(colnum):
        # 		if matrix[i][j] == 0:
        # 			row[i] = True
        # 			col[j] = True

        # for i in xrange(rownum):
        # 	for j in xrange(colnum):
        # 		if row[i] or col[j]:
        # 			matrix[i][j] = 0 
a = Solution()
print a.setZeroes([[1,0,3]])