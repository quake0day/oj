class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        len_S = len(S)
        len_T = len(T)
        f = [[0] * (len_S + 1) for row in xrange(len_T + 1)]
        f[0][0] = 1
        for i in xrange(1,len_T,1):
            f[i][0] = 0

        for j in xrange(1, len_S):
            f[0][j] = 1

        for i in xrange(1, len_T+1):
            for j in xrange(1, len_S+1):
                f[i][j] = f[i][j-1]
                if T[i-1] == S[j-1]:
                    f[i][j] += f[i-1][j-1]
        return f[len_T][len_S]



a = Solution()
print a.numDistinct("rabbbit", "rabbit")  