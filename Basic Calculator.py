class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        now = 0
        sign = 1
        stack = []
        ans = 0
        for i in xrange(len(s)):
            if s[i].isdigit():
                now = now * 10 + int(s[i])
                continue 
            stack.append(sign * now)
            now = 0
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                if sign == 1:
                    stack.append('+')
                else:
                    stack.append("-")
                sign = 1
            elif s[i] == ')':
                tmp = 0 
                while stack[-1] != '+' and stack[-1] != '-':
                    tmp += stack.pop()
                if stack[-1] == '-':
                    tmp = -tmp
                stack.pop() 
                stack.append(tmp)
        if now != 0:
            stack.append(sign * now)
        while stack:
            ans += stack.pop() 

        return ans

a = Solution()
print a.calculate(" 1 + 1")