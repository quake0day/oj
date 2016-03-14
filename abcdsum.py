arr = [3,4,7,1,2,9,8]


h = {}
for i in xrange(len(arr)):
    for j in xrange(i+1, len(arr)):
        h[i, j] = arr[i] + arr[j]

f = {}
for k, v in h.iteritems():
    if v not in f:
        f[v] = [k]
    else:
        f[v].append(k)


print f

for key, v in f.iteritems():
    if len(v) > 1:
        for i in range(len(v)):
            for k in range(i+1, len(v)):
                print v[i] + v[k], key