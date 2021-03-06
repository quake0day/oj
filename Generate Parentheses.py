class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
        	return []
        res = []
        self.helper(n , n, res, "")
        return res

    def helper(self, l, r, res, line):
    	if r < l:
    		return 
    	if l == 0 and r == 0:
    		res.append(line)
    		return 

    	if l > 0:
    		self.helper(l-1, r, res, line+"(")
    	if r > 0:
    		self.helper(l, r-1, res, line+")")
   