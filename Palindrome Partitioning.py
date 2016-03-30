class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        self.final_res = []
        lenS = len(s)

        def dfs(start, L):
            if start == lenS:
                self.final_res.append(L)
                return 
            for end in xrange(start, lenS):
                if self.isValid(s[start:end]) == True:
                    self.dfs(end+1, L[:] + [self.s[start : end + 1]])
            

    def isValid(self, s):
        return s == s[::-1]

a = Solution()
print a.partition("aab")