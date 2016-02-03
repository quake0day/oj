class Solution(object):
    def generateParenthesis(self, n):
    	if n == 0:
    		return []
    	res = []
    	self.helper(n , n , res, "", n)
    	return res

    def helper(self, l, r, res, line, space):
    	if r < l:
    		return 

    	if l == 0 and r == 0:
    		res.append(line)
    		return 
    	space_str = space * " "
    	if l > 0:
    		self.helper(l-1, r, res, line+space_str+"(", space)

    	if r > 0:
    		
    		self.helper(l, r-1, res, line+space_str+")", space)


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [('', 0, n)]
        maxn = n
        while maxn > 0:
        	maxn = 0
        	l = len(res)
        	for i in xrange(l):
        		s, b, k = res[i]
        		if k > maxn: maxn = k
        		if k > 0:
        			res[i] = (s+"(", b+1, k -1)
        			if b > 0:
        				res.append((s+")", b-1, k))
        		elif b > 0:
        			res[i] = (s+")", b-1, k)
        return [s[0] for s in res]

a = Solution2()
print a.generateParenthesis(5)

print float(13*16**3+10*16**2+13*16+10)

def isMirror(a, b):
	if a == None and b == None:
		return True
	if a == None or b == None:
		return False
	if a.value == b.value:
		return isMirror(a.left, b.right) and isMirror(a.right, b.left)
	else:
		return False

def isMirrorIteself(root):
	if root == None:
		return True

	return isMirror(root.left, root.right)