a = ['1','a','c']
print map(len, a)
print reduce(lambda x, y: x+y, map(len, a))