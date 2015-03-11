class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if a == 0:
        	return 0
        if n == 0:
        	return 1 % b

        ret = long(0)
        ret = self.fastPower(a, b, n / 2)
        ret *= ret

        ret %= b

        if (n % 2 == 1):
        	ret *= (a % b)
        ret = ret % b
        return ret




