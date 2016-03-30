a = ["GGGG",
"GGBC",
"BBBD",
"ECED"]
c = []
for i in a:
    i = list(i)
    c.append(i)

class Solution(object):

    def __init__(self):
        self.max_area = 0

    def findcolor(self, c):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i, j, c, area):
            color = c[i][j]
            c[i][j] = '#'
            self.max_area = max(self.max_area, area)
            for d in directions:
                x = i + d[0]
                y = j + d[1]
                if 0 <= x < len(c) and 0 <= y < len(c[0]) and c[x][y] == color:
                    dfs(x, y, c, area+1)
            c[i][j] = color 
        for i in xrange(len(c)):
            for j in xrange(len(c[0])):
                    dfs(i, j, c, 1)
        return self.max_area
    


a = Solution()
print a.findcolor(c)
#print findcolor(c)