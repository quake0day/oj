
def NDM(n, faces):
    if n <= 0:
        return 
    dp = [[0] * faces for _ in xrange(n)]

    s = 1
    for i in xrange(faces):
        dp[0][i] = 1

    for i in xrange(1, n):
        for t in 


NDM(1, 6)