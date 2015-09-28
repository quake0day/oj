class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        oldNum = -1
        j = 0
        while num != 0:
        	oldNum = num
        	num = num / 2
        	if oldNum == num * 2 + 1:
        		j += 1
        return j


a = Solution()
print a.countOnes(32)


