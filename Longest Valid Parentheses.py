class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        index = 0 
        for i in xrange(len(s)):
            print stack
            if s[i] == ")" and len(stack) != 1:
                length, last = stack.pop(), stack.pop()
                total_length = length + last + 2
                stack.append(total_length)
                longest = max(total_length, longest)
            elif s[i] == "(":
                stack.append(0)
            else:
                stack = [0]
        return longest

a = Solution()
print a.longestValidParentheses(")()())")