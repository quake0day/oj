class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 1:
        	return True 
        if n <= 0:
            return False
        appera = 0
        for item in bin(n)[2:]:
        	if item == '1' and appera == 0:
        		appera = 1
        	elif item == '1' and appera == 1:
        		return False
        return True


a = Solution()
print a.checkPowerOf2(72)
        
