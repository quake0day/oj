class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        result = []
        if (n <= 0):
            return result
        cols = []
        self.search(n, cols, result)
        return result

    def search(self, n, cols, result):
        if (len(cols) == n):
            result.append(self.drawRes(cols))
            return
        for col in xrange(n):
            if (self.isValid(cols, col)) != True:
                pass
            else:
                cols.append(col)
                self.search(n, cols, result)
                cols.pop()

    def isValid(self, cols, col):
        row = len(cols)
        for i in xrange(row):                     
            # same column
            if (cols[i] == col):
                return False
            # left - top to right-bottom 
            if (i - cols[i]) == (row - col):
                return False
            if (i + cols[i]) == (row + col):
                return False
        return True



    def drawRes(self, cols):
        chessboard = [""] * len(cols)
        for i in xrange(len(cols)):
            chessboard[i] = ""
            for j in xrange(len(cols)):
                if j == cols[i]:
                    chessboard[i] += "Q"
                else:
                    chessboard[i] += "."
        return chessboard



a = Solution()
print a.solveNQueens(5)

