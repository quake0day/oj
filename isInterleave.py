class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)

        if len_s1 + len_s2 != len_s3:
        	return False

        interleaved = [[False] * (len_s2+1) for row in xrange(len_s1+1)]
        interleaved[0][0] = True
        for i in xrange(1,len_s1+1):
        	if s3[i-1] == s1[i-1] and interleaved[i-1][0]:
        		interleaved[i][0] = True
        for j in xrange(1, len_s2+1):
        	if s3[j-1] == s2[j-1] and interleaved[0][j-1]:
        		interleaved[0][j] = True
        for i in xrange(1, len_s1+1):
        	for j in xrange(1, len_s2+1):
        		if (s3[i+j-1] == s1[i-1] and interleaved[i-1][j]) or \
        		(s3[i+j-1] == s2[j-1] and interleaved[i][j-1]):
        			interleaved[i][j] = True
        return interleaved[-1][-1]

        

a = Solution()
print a.isInterleave("a","","a")
