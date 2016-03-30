A = [1,2,3,4, 4,5,8,9]
B = [1,4,5,10]

hashMap = {key:1 for key in A}
print hashMap 

for i in B:
    if i not in hashMap:
        print i