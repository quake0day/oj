class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(word, index, board, x , y):
            if index == len(word)-1:
                return True

            position = [[0,1],[0,-1],[-1,0],[1,0]]
            ctmp = board[x][y]
            board[x][y] = '#'
            for pos in position:
                newx = x+pos[0]
                newy = y+pos[1]
                print word[index], index
                if 0<=newx<len(board[0]) and 0<=newy<len(board) and board[newy][newx] == word[index]:
                    if dfs(word, index+1, board, newx, newy):
                        return True
            board[x][y] = ctmp
            return False 

        startWord = word[0]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == startWord:
                    if dfs(word, 1, board, i, j):
                        return True
        return False

a = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print a.exist(board, "ABCCED")
print a.exist(board, "SEE")
print a.exist(board, "ABCB")
board = [["a","a"]]
print a.exist(board, 'a')