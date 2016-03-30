import collections
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        m = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '1':[], '0':[]}
        q = collections.deque()
        for c in m[digits[0]]:
            q.append((c,digits[1:]))
        final_res = []
        while q:
            tmp, candidate = q.popleft()
            if len(candidate) == 0:
                final_res.append(tmp)
                continue
            for c in m[candidate[0]]:
                q.append((tmp+c, candidate[1:]))
        return final_res
            
a = Solution()
print a.letterCombinations("22")