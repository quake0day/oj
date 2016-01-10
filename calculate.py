class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        stack = []
        res = 0
        sign = 1
        i = 0
        while i < xrange(len(s)-1) :
            try:
                c = s[i]
            except:
                break
            if c.isdigit():
                cur = c
                while(i+1<len(s) and s[i+1].isdigit()):
                    cur += s[i+1]
                    i += 1
                print cur
                res += sign * int(cur)
                print "RES", res
            elif c == '-':
                sign = -1
            elif c == '+':
                sign = 1
            elif c == '(':
                stack.append(res)
                res = 0
                stack.append(sign)
                sign = 1
            elif c == ')':
                res = stack.pop() * res + stack.pop()
                sign = 1
            i += 1
        return res


a = Solution()
print a.calculate("2147483647")
