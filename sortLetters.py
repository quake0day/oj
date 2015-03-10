class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        n = len(chars)
        small = 0
        for i in xrange(n):
        	if chars[i].islower():
        		tmp = chars[small]
        		chars[small] = chars[i]
        		chars[i] = tmp
        		small += 1
        return chars




    	


a = Solution()
print a.sortLetters("abAcD")