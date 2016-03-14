# 0 1 2
# 3 4 5
# 6 7 8


board = [[0,1,2],[3,4,5],[6,7,8]]
def unlockPattern(board):
    not_reachable = {0:[2,6,8], 1:[7], 2:[0, 6,8], 3:[5], 5:[3], 6:[2,0,8], 7:[1], 8:[0,6,2]}
    def dfs(currentVal, board, temp, final_res):
        if len(temp) == 9:
            if temp not in final_res:
                final_res.append(temp)
            return  
        if len(temp) >= 4:
            if sorted(temp) not in final_res:
                final_res.append(sorted(temp))
            return 

        if currentVal != 'X':
            for c in xrange(9):
                if c == currentVal:
                    continue 
                if board[c/3][c%3] == 'X':
                    continue
                if currentVal == 4:
                        tmp = board[currentVal/3][currentVal%3]
                        board[currentVal/3][currentVal%3] = 'X'
                        dfs(c, board, temp+[currentVal], final_res)
                        board[currentVal/3][currentVal%3] = tmp 
                else:
                    if c in not_reachable[currentVal]:
                        continue
                    else:
                        tmp = board[currentVal/3][currentVal%3]
                        board[currentVal/3][currentVal%3] = 'X'
                        dfs(c, board, temp+[currentVal], final_res)
                        board[currentVal/3][currentVal%3] = tmp                       

    
    final_res = []
    for i in xrange(9):
            dfs(i, board, [], final_res)
    return final_res


print len(unlockPattern(board))