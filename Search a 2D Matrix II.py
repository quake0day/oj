class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = (0,0)
        m = len(matrix)
        n = len(matrix[0])
        # 1st round
        curRow = 0
        curCol = 0
        i = 0
        j = 0
        while j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                j -= 1
                break
        if j == n: 
            j -= 1

        while i < m:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                i -= 1
                break
        i = 0
        j = 0 
        while i < m:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                i -= 1
                break
        if i == m:
            i -= 1
        while j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                j -= 1
                i -= 1 
        return False 

a = Solution()
print a.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 12)
        