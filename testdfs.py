a = [1,2,3,4,5]

def helper(a):
    print a[0]
    helper(a[1:])
    helper(a[-1:])

helper(a)
