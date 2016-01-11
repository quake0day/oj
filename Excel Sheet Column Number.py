class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        k = 0
        if s == None: return res
        for i in range(len(s)):
            res = 26 * res 
            res += (ord(s[i])  - 64)
        return res 

a = Solution()
print a.titleToNumber('AB')
print a.titleToNumber('BA')
print a.titleToNumber('AAA')
