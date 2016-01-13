class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i] == s[i+1] == '+'and not self.canWin(s[0:i]+"--"+s[i+2:]):
                return True
        return False
        


a = Solution()
print a.canWin("++++")
