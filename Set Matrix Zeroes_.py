class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        FC = False
        FR = False
        m = len(matrix)
        n = len(matrix[0])
        for i in xrange(m):
            if matrix[i][0] == 0:
                FC = True
        for j in xrange(n):
            if matrix[0][j] == 0:
                FR = True
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0
        for j in xrange(n):
            if matrix[0][j] == 0:
                for i in xrange(1,m):
                    matrix[i][j] = 0
        if FC:
            for i in xrange(m):
                matrix[i][0] = 0
        if FR:
            for i in xrange(n):
                matrix[0][i] = 0