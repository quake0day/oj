class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        for i in xrange(len(A)):
            if A[i] == 0:
                res = self.check(A[0:i])
                if res == False:
                    return False
        return True

    def check(self, subA):
        compare = [n for n in xrange(len(subA))]
        subA = subA[::-1]
        for i in xrange(len(subA)):
            if subA[i] - 1 > compare[i]:
                return True
        return False

a = Solution()
print a.canJump([2,3,1,1,4])
