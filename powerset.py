a = ['a','b','c']
def powerset(a):
    size = 2 ** len(a)
    for counter in xrange(size):
        res = []
        for j in xrange(size):      
            if counter & (1 << j):
                res.append(a[j])
        if len(res) > 0:
            print "".join(res)

powerset(a)