class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def get_maxLength(self, dicts):
		max_length = 0
		for item in dicts:
			max_length = max(max_length, len(item))
		return max_length

    def wordSegmentation(self, s, dict):
        # write your code here
        if len(s) == 0 and len(dict) == 0:
        	return True
        if s == None or len(s) == 0:
        	return False

        f = [False] * (len(s) + 1)
        f[0] = True
        max_length = self.get_maxLength(dict)
        #max_length = self.get_maxLength(dict)
        for i in xrange(1,len(s)+1):
        	f[i] = False
        	for j in xrange(1, max_length+1):
        		if (j <= i):
        			if (not f[i-j]):
        				continue
        			word = s[i-j:i]
        			if word in dict:
        				f[i] = True
        				break
        return f[-1]

	



a = Solution()
print a.wordSegmentation("lintcode", ["lint","code"])