import random

n = 3
k = 3
res = []

x = range(n)
for i in range(k):
    t = random.randint(i, n-1)
    x[i], x[t] = x[t], x[i]
    print t,i
    
    res.append(x[i])
    print res
print res