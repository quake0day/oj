class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        up = 0; left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        direct = 0 # 0 go right 1 go down 2 go left 3 go up
        res = []
        while True:
            if direct == 0:
                for i in xrange(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in xrange(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in xrange(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in xrange(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right: return res
            direct = (direct + 1) % 4