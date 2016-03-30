class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        def dfs(s, d):
            if s in d:
                return True
            for i in xrange(len(s)):
                if s[:i] in d:
                    return dfs(s[i:], d)
        if dfs(s, wordDict):
            return True 
        return False
        

a = Solution()
print a.wordBreak("leetcode", ["leet", "code"])          