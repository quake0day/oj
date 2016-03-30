
def Sieve_of_Eratosthenes(n):
    st = [True] * n
    res = []
    for i in xrange(2, n):
        if st[i] != False:
            res.append(i)
            for k in xrange(i, n, i):
                st[k] = False
    return res

print Sieve_of_Eratosthenes(100)
