class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]; num2 = num2[::-1]
        arr = [0 for i in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
        	for j in xrange(len(num2)):
        		arr[i+j] += int(num1[i]) * int(num2[j])
        ans = []
        for i in xrange(len(arr)):
        	digit = arr[i] % 10
        	carry = arr[i] / 10
        	if i < len(arr) - 1:
        		arr[i+1] += carry
        	ans.insert(0, str(digit))
        while ans[0] == '0' and len(ans) > 1:
        	del ans[0]
        return "".join(ans)