a = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9,0]

def pushzerotolast(a):
    r = len(a) - 1
    idx = 0 
    while idx < r:
        if a[idx] == 0:
            a[idx], a[r] = a[r], a[idx]
            r -= 1 
        if a[idx] != 0:
            idx += 1
    return a 

print pushzerotolast(a)