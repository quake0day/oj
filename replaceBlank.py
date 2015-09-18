class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if 0 == length:
        	return 0
        num = 0
        for i in xrange(length):
        	if string[i] == ' ':
        		num += 1
        newLen = length + num * 2
        j = 1 
        for i in xrange(length-1, -1, -1):
        	if string[i] != ' ':
        		string[newLen - j] = string[i]
        		j += 1
        	else:
        		string[newLen - j] = '0'
        		j += 1
        		string[newLen - j] = '2'
        		j += 1
        		string[newLen - j] = '%'
        		j += 1
       
        return newLen


a = Solution()
print a.replaceBlank(['M','r',' ',' ',' '], 3)

