class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = "".join(num).lstrip('0')
        return ans or '0'


    def compare(self, a, b):
    	return [1, -1][a + b > b + a]



a = Solution()
print a.largestNumber([3, 30, 34, 5, 9])