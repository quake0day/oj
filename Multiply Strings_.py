class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'
        m = len(num1)
        n = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (m + n + 1)
        for i in xrange(m):
            for j in xrange(n):
                res[i+j] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in xrange(len(res)):
            rem = (res[i] + carry) % 10
            carry = (res[i] + carry) / 10
            res[i] = rem

        return "".join(map(str,res))[::-1].lstrip('0')
            

a = Solution()
print a.multiply("0","0")
print a.multiply("98","9")
print a.multiply("100","9")
print a.multiply("9","100")