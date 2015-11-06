class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        stack = []
        i = 0
        res = ""
        while i < len(path):
        	end = i + 1
        	while end < len(path) and path[end] != "/":
        		end += 1
        	sub = path[i+1 : end]
        	if len(sub) > 0:
        		if sub == "..":
        			if stack != []:
        				stack.pop()
        		elif sub != ".":
        			stack.append(sub)

        	i = end 
        if stack == []: 
        	return "/"

        for i in stack:
        	res += "/"+i 
        return res


a = Solution()

print a.simplifyPath("/..")