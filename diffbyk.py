
a = [1,2,3,5,6,8,9,11,12,13]
k = 3

def diffbyk(a, k):
    d = {}
    res = []
    for item in reversed(a):
        target = item - k 
        d[target] = item
        if item in d:
            print d[item], item 

        
    return res 

diffbyk(a, k)