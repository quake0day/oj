class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        if (m == 0 or n == 0):
        	return 0
        path_sum = [[0 for col in range(n)] for row in range(m)]
        i = 0
        while i < m:
        	path_sum[i][0] = 1
        	i += 1
        path_sum[0] = [1] * (n)
        i,j = 1,1
        while i < m:
        	while j < n:
        		path_sum[i][j] = path_sum[i-1][j] + path_sum[i][j-1]
        		j += 1
        	j = 1
        	i += 1
        
       	return path_sum[m-1][n-1]
