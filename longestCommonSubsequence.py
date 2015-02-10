class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        len_A = len(A)
        len_B = len(B)
        f = [[0 for col in range(len_A+2)] for row in range(len_B+2)]
        for i in xrange(len_A):
        	for j in xrange(len_B):
        		f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
        		if A[i] == B[j]:
        			f[i+1][j+1] = f[i][j] + 1
        return f[len_A][len_B]

a = Solution()
print a.longestCommonSubsequence("bedaacbade", "dccaeedbeb")

