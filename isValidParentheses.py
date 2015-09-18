class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        symbol0 = ['(',')']
        symbol1 = ['{','}']
        symbol2 = ['[',']']
        temp = []
        for i in xrange(len(s)):
        	if len(temp) == 0:
        		temp.append(s[i])
        	else:
        		if temp[-1] in symbol0 and s[i] in symbol0 and temp[-1] != s[i]:
        			temp.pop()
        		elif temp[-1] in symbol1 and s[i] in symbol1 and temp[-1] != s[i]:
        			temp.pop()
        		elif temp[-1] in symbol2 and s[i] in symbol2 and temp[-1] != s[i]:
        			temp.pop()
        		else:
        			temp.append(s[i])
        return len(temp) == 0


a = Solution()
print a.isValidParentheses(['(',')','[','{','}',']','{'])

