class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }

        def dfs(temp, index, final_res):
            if index == len(digits):
                final_res.append(temp)
                return
            for c in dict[digits[index]]:
                dfs(temp+c, index+1, final_res)

        final_res = []
        dfs("", 0, final_res)
        return final_res


a = Solution()
print a.letterCombinations("23")