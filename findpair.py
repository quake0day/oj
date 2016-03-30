s = [1,5, 10, 100]
p = [6, 11, 101, 15, 105, 110]
def myPair(p, m):
    s = [0] * m 
    s[0] = (p[0] + p[1] - p[m-1]) / 2
    for i in xrange(m-1):
        s[i+1] = p[i] - s[0]
    return s

print myPair(p, 4)