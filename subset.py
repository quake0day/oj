class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        result = []
        if (S == None or len(S) == 0):
            return result
        res_list = []
        S = sorted(S)
        self.subsetsHelper(result, res_list, S, 0)
        return result

    def subsetsHelper(self, result, res_list, S, pos):
        res_list_new = list(res_list)
        result.append(res_list_new)
        for i in xrange(pos, len(S)):
            res_list.append(S[i])
            self.subsetsHelper(result, res_list, S, i+1)
            res_list.pop()





        # # write your code here
        # if len(S) == 0:
        #     return []
        # if len(S) == 1:
        #     return [S]
        # total = 2 ** len(S)
        # res = []

        # for i in xrange(total):
        #     pick = S
        #     print pick
        #     bina = bin(i)
        #     item = []
        #     for bit in bina:
        #         if bit == '1':
        #             item.append(pick.pop())
        #         elif bit == '0':
        #             pick.pop()
        #     res.append(item)







a = Solution()
print a.subsets([1,2,3])