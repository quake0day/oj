def addValue(A, value):
    for i in xrange(len(A)-1, -1, -1):
        value += A[i]
        A[i] = value % 10
        value /= 10 

    if value > 0:
        A = [value] + A  
    return A 

print addValue([0,0,5],19)