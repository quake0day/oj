class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ii = []
        jj = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    ii.append(i)
                    jj.append(j)
        jj = sorted(jj)
        c = len(ii)
        s = 0
        io = ii[c/2]
        jo = jj[c/2]
        for i in ii:
            s += abs(i - io)
        for j in jj:
            s += abs(j - jo)
        return s



