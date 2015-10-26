class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if not matrix:
            return 0


        board = [[0 for x in row] for row in matrix]

        max_square_size = 0

        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                if i == 0 or j == 0:
                    board[i][j] = 1 if matrix[i][j] == 1 else 0
                else:
                    board[i][j] = 0 if matrix[i][j] == 0 else min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

                if board[i][j] > max_square_size:
                    max_square_size = board[i][j]
        return max_square_size ** 2



a = Solution()
print a.maxSquare([[0,1,0,1,1,0],[1,0,1,0,1,1],[1,1,1,1,1,0],[1,1,1,1,1,1],[0,0,1,1,1,0],[1,1,1,0,1,1]])
