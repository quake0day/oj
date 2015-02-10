class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        res = 0
        for i in A:
            res ^= i
        print res


a = Solution()
a.singleNumber([1,2,2,1,3,4,3])