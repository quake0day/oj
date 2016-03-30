def MinuOne(x):
    m = 1
    while not (x & m):
        x = x ^ m
        m <<= 1
    x = x ^ m 
    return x 

print MinuOne(12)