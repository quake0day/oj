a = [[1,2,3,4],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

b = [[1,2,3,4] for _ in xrange(4)]

result = [[0] * len(a[0]) for _ in xrange(len(a))]
print result

for i in xrange(len(a)):
    for j in xrange(len(a[0])):
        if i == 0:
            result[i][j] = a[i][j]
        elif j == 0:
            result[i][j] = a[i][j]
        elif i != 0 and j != 0:
            if i - 1 >= 0 and j - 1 >=0:
                result[i][j] = result[i-1][j-1] + a[i][j]
print result 
print b
