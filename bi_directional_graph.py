A = [(1,2), (2,1), (3,4), (4,3),(3,4)]

A = map(sorted, A)
print A[0] == A[1]

cnt = 0
for i in xrange(1, len(A)):
    if A[i-1] == A[i]:
        cnt += 1
print cnt
