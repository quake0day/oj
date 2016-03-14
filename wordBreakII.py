class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s, start, cur, res, dict):
            n = len(s)
            if start >= n:
                res.append(cur[:])
                return
            for i in xrange(start, n+1):
                sub = s[start:i]
                if sub in dict:
                    oldLen = len(cur)
                    if oldLen != 0:
                        cur += " "
                    cur += sub
                    dfs(s, i, cur, res, dict)
                    cur = cur[0:oldLen]
        ret = []
        if s == None or len(s) == 0: return ret
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in xrange(1, n+1):
            if s[:i] in wordDict:
                dp[i] = True
                continue
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        if (dp[n] == False):
            return ret
        dfs(s, 0, "", ret, wordDict)
        return ret

a = Solution()
print a.wordBreak("catsanddog",
["cat","cats","and","sand","dog"])