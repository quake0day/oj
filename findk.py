a = "leetcode"
b = "codyabs"
k = 3
def findK(a,b, k):
    m = len(a)
    n = len(b)
    h = {}
    for i in xrange(m-k):
        h[a[i:i+k]] = True
    #dp = [[False] * n for _ in range(m)]
    #dp[0][0] = True 
    for j in xrange(n-k):
        if b[j:j+k] in h:
            return True

def findKDP(a,b,k):
    m = len(a)
    n = len(b)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in xrange(1, m):
        for j in xrange(1, n):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 
            if dp[i][j] >= k:
                return True
    #print dp
    return False 



print findK(a,b,k)
print findKDP(a,b,k)