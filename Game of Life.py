class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # 1 live 3 to live
        # 0 dead 2 to dead
        if not board:
            return board
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = self.readDestiny(i, j, board)
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] = board[i][j] % 2
        print board
                

    def readDestiny(self, x,y,board):
        directions = [(-1,-1), (-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
        live = 0
        dead = 0
        inistatus = board[x][y]
        status = None
        for d in directions:
            nx,ny = x+d[0], y+d[1]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 0 or board[nx][ny] == 3:
                    dead += 1
                elif board[nx][ny] == 1 or board[nx][ny] == 2:
                    live += 1

        if x == 2 and y == 2:
            print board
            print live, dead, board[x][y]
        if inistatus == 1 and (live < 2 or live > 3):

            status = 2

        elif inistatus == 0 and live == 3:
            status = 3
        elif inistatus == 1 and live == 2 or live == 3:
            status = 1
        else:
            status = 0
        if x == 2 and y == 2:
            print status
        return status
a = Solution()
print a.gameOfLife([[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,0,0,0,0,0]])