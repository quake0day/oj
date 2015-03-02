class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        if len(str) <= 0:
        	return False
        
        str_len = len(str)
        for i in xrange(str_len):
        	c = str[i]
        	for j in xrange(i+1, str_len):
        		d = str[j]
        		if c == d:
        			return False
        return True
