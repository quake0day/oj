def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumfactorial(n):
    res = 0
    for i in xrange(1, n+1):
        res += factorial(i)
    return res

print sumfactorial(4)