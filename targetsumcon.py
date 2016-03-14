a = [1,3,5,7,9]
t = 15
t=8
t=1
t = 25
def findSub(a, t):
    l, r = 0, 0
    tmp = a[0]
    while l <= r:
        if tmp == t:
            return True, a[l:r+1]
        elif tmp < t:
            r += 1 
            tmp += a[r]
        elif tmp > t:
            tmp -= a[l]
            l += 1
    return False,[]

print findSub(a, t)
            
