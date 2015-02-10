import sys
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if (len(A) <= 0):
            return 0
        n = len(A)
        start = 0
        end = 0
        count = 0
        if n == 1:
            return 0
        while end < n :
            maxium = 0
            count += 1
            for i in xrange(start,end+1):
                if A[i] + i >= n - 1:
                    return count
                if A[i] + i > maxium:
                    maxium = A[i] + i 
            start = end + 1
            end = maxium
        return count



a = Solution()
print a.jump([2,3,1,1,1,1,1,1,1,4])
