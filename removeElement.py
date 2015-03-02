class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        status = True
        k = 0
        init_length = len(A)
        while status:
        	try:
        		A.remove(elem)
        	except:
        		pass
        	if k == init_length:
        		status = False
        	k += 1
        return len(A)

a = Solution()
print a.removeElement([0,4,4,0,0,2,4,4],4)
