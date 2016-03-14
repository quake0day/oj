def myPow(x, n):
    if n == 0:
        return  1.0

    half = pow(x, n / 2)
    if n % 2 == 0:
        print "half*half", half
        return half * half 

    elif n > 0:
        print "half*half*x", half, x
        return half * half * x
    else:
        print "half/x*half", half,x
        return half / x * half


def sqrt(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    l = 1
    r = x/2+1

    while l <= r:
        m = (l+r) / 2
        if m <= x/m and x / (m + 1) < (m + 1):
            return m 
        if x / m < m:
            r = m -1
        else:
            l = m + 1
    return 0
def gcd(a,b):
    if a == b:
        return a 
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)
def lcm(a, b):
    return (a*b) / gcd(a, b)
print gcd(8, 3)
print gcd(20, 30)
print myPow(2,9)
print sqrt(100)