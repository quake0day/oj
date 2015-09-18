class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome

    def genAlphabet(self):     
		str = ""
		str_ = ""
		str__ = ""
		for i in range(97,123):
		    str = str + chr(i)
		for i in range(65,91):
		    str_ = str_ + chr(i)
		for i in range(48,58):
		    str__ = str__ + chr(i)
		alphabet = str_+str+str__
		return alphabet

    def isPalindrome(self, s):
        # Write your code here
        len_s = len(s)
        if len_s == 0:
        	return True
        i = 0
        j = len(s) - 1

        alpha = self.genAlphabet()

        if i == j:
        	return True

        while i < j:
	        while s[i] not in alpha and i < j:
	        	i += 1
	        while s[j] not in alpha and i < j:
	        	j -= 1
	        alpha1 = s[i].upper()
	        alpha2 = s[j].upper()
        	if alpha1 != alpha2:
        		return False
        	else:
        		i += 1
        		j -= 1
        return True

a = Solution()

print a.isPalindrome("aba")

print a.isPalindrome(".,")
print a.isPalindrome("1a2")

print a.isPalindrome("A man, a plan, a canal: Panama")

