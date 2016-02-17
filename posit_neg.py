def rightRotate(a, curr, lastNeg):
    tmp = a[curr]
    for i in xrange(curr, lastNeg+1):
        a[i] = a[i-1]
        i -= 1
    a[lastNeg+1] = tmp 
    return a



a = [1, 7, -5, 9, -12, 15]
rightRotate(a, 2, -1)
print a