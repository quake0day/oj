class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right, temp, final_res):

            if left > right:
                return

            if left == 0 and right == 0:
                final_res.append(temp)
                return


            if left > 0:
                dfs(left-1, right, temp+"(", final_res)
            if right > 0:
                dfs(left, right-1, temp+")", final_res)

        if n == 0:
            return []
        final_res = []
        dfs(n, n, "", final_res)
        return final_res

a = Solution()
print a.generateParenthesis(3)
