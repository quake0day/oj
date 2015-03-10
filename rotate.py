class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix) / 2
        row_num = len(matrix)
        for i in xrange(n):
        	for j in xrange(row_num-1):
        		tmp = matrix[i][i+j]
        		matrix[i][i+j] = matrix[i+row_num-1-j][i]
        		matrix[i+row_num-1-j][i] = matrix[i+row_num-1][i+row_num-1-j]
        		matrix[i+row_num-1][i+row_num-1-j] = matrix[i+j][i+row_num-1]
        		matrix[i+j][i+row_num-1] = tmp
        	row_num -= 2
