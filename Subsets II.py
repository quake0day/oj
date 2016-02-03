class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        def dfs(depth, start, currlist):
        	if currlist not in res: 
        		res.append(currlist)
        	if depth == len(S):
        		return
        	for i in xrange(start, len(S)):
        		dfs(depth+1, i+1, currlist.append(S[i]))
        res = []
        S = sorted(S)
        dfs(0, 0,[])
        return res