class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        def dfs(i, j, word, board):
            if len(word) == 0:
                return True
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[0]:
                tmp = board[i][j]
                board[i][j] = '#'
                if dfs(i+1, j, word[1:], board) or dfs(i-1, j, word[1:], board) or dfs(i, j+1, word[1:], board) or dfs(i, j-1, word[1:], board):
                    return True
                board[i][j] = tmp
            
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, board):
                        return True
                        
        return False


a = Solution()
print a.exist([['A','B','C',"E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
print a.exist([['C','A','A'],['A','A','A'],['B','C','D']], "AAB")