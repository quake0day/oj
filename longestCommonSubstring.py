class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here]
        if A == None or B == None:
        	return 0

        len_A = len(A)
        len_B = len(B)


        f = [[0] * (len_B+1) for row in xrange(len_A+1)]
        max_ = 0


        for i in xrange(len_A+1):
        	for j in xrange(len_B+1):
        		if i == 0 or j == 0:
        			f[i][j] = 0
        		else:
	        		if A[i-1] == B[j-1]:
	        			f[i][j] = f[i-1][j-1] + 1
	        		else:
	        			f[i][j] == 0

	        	max_ = max(max_, f[i][j])

        return max_

a = Solution()
print a.longestCommonSubstring("ABCD","CBCE")
print a.longestCommonSubstring("www.lintcode.com code", "www.ninechapter.com code")

