class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        res = []
        A = sorted(A)
        n = len(A)

        while i 

# # just loop
#     def countOfSmallerNumber(self, A, queries):
#         # write your code here
#         res = []
#         for item in queries:
#         	i = 0
#         	for que in A:
#         		if que < item:
#         			i += 1
#         	res.append(i)
#         return res

a = Solution()
print a.countOfSmallerNumber([1,2,7,8,5], [1,8,5])

