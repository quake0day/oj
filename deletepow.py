array = [2,4,6,7]
array2 = [2,3,5,9,14]


for i in range(len(array)):
    for j in range(i):
        if i != j:
            if array[i] != '#' and array[j] != '#':
                if array[i] % array[j] == 0:
                    if array[i] > array[j]:
                        array[i] = '#'
                    else:
                        array[j] = '#'
array = [x for x in array if x != '#']
print len(array)