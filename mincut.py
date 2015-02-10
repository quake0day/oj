import sys
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        n = len(s)
        f = [0] * (n+1)
        isPalindrome = self.getIsPalndrome(s)
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 0

        if len(s) == 2:
            if s[0] != s[1]:
                return 1
            else:
                return 0

        for i in xrange(1, n+1):
            f[i] = sys.maxint
            for j in xrange(1, i+1):
                if isPalindrome[i - j][i - 1] and f[i-j] != sys.maxint:
                    f[i] = min(f[i], f[i-j]+1)
        return f[-1] -1 

    def getIsPalndrome(self,s):
        n = len(s)
        isPalindrome = [[False for col in range(n)] for row in range(n)]
        for i in xrange(n):
            isPalindrome[i][i] = True
        for i in xrange(n-1):
            isPalindrome[i][i + 1] = (s[i] == s[i+1])
        for length in xrange(2, n):
            for start in xrange(n):
                if start + length < n:
                    isPalindrome[start][start + length] = isPalindrome[start + 1][start + length - 1] and (s[start] == s[start + length])
        return isPalindrome


    def isPalindrome(self, s):
        return str(s) == str(s)[::-1]



a = Solution()
print a.minCut("cdd")
#a.getIsPalndrome("aabbs")