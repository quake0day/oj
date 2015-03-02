class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        list_s = list(s)
        list_t = list(t)
        for item in list_s:
        	try:
        		list_t.remove(item)
        	except:
        		return False
        if len(list_t) == 0:
        	return True
