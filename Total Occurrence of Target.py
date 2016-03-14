class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if len(A) == 0 or A == None:
            return 0
        start = 0
        end = len(A)
        find_mid = None
        total = 0
        while start+1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                find_mid = mid
                break
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
        if find_mid != None:
            for i in xrange(find_mid, len(A)):
                if A[i] == target:
                    total += 1
                else:
                    break
            for i in xrange(find_mid-1, -1, -1):
                if A[i] == target:
                    total += 1
                else:
                    break
        return total

a = Solution()
print a.totalOccurrence([1,3,4,4], 4)