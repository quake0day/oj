class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code here
        q = [1]
        i3 = i5 = i7 = 0
        while len(q)-1 < k:
        	m3, m5, m7 = q[i3] * 3, q[i5] * 5, q[i7] * 7
        	m = min(m3, m5, m7)
        	if m == m3:
        		i3 += 1
        	if m == m5:
        		i5 += 1
        	if m == m7:
        		i7 += 1
        	q.append(m)
        return q[-1]


a = Solution()
print a.kthPrimeNumber(5)