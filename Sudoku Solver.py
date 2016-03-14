class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #9x9
        def isValid(x, y):
            temp = board[x][y]
            board[x][y] = 'D'
            for i in xrange(9):
                if board[x][i] == temp:
                    return False
            for j in xrange(9):
                if board[j][y] == temp:
                    return False 

            for i in xrange(3):
                for j in xrange(3):
                    if board[(x/3)*3+i][(y/3)*3+j] == temp:
                        return False 
            board[x][y] = temp 
            return True

        def dfs(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == ".":
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False 
            return True
        dfs(board)

