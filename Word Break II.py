class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def helper(s, start, wordDict, currentRes, res):
            if start >= len(s):
                res.append(" ".join(currentRes))
                currentRes = []
                return
            str_ = ""
            for i in xrange(start, len(s)):
                str_ += s[i]
                if str_ in wordDict:
             
                    currentRes.append(str_)
                   
                    #currentRes.append(str_)
                    helper(s, i+1, wordDict, currentRes, res)
                #if len(currentRes) > 0:
                    #currentRes.pop()
        res = []
        helper(s, 0, wordDict, [], res)
        return res

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: List[str]
#         """
#         def dfs(s, start, res, cur, wordDict):
#             n = len(s)
#             for i in xrange(start, n):
#                 curWord = s[start:i]
#                 if curWord in wordDict:
#                     cur.append(curWord)
#                     if i == n:
#                         str_ = " ".join(cur)

#                     res.append(curWord)
#                 else:
#                     dfs(s, i, res, cur, wordDict)
#                 cur.pop() 
        
#         if s == None or len(s) == 0:
#             return res
            
#         res = []
#         dfs(s, 0, res, [], wordDict)
#         return res


a = Solution()
print a.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])