array = [9,6,2,14,5,7,4]
print len(array) == len(set(array))


def findlocalMin(arr, start, end):
    mid = (start + end ) / 2
    if mid - 2 < 0 and mid + 1 > len(array:
        return -1 
    if arr[mid-2] > arr[mid-1] and arr[mid-1] < arr[mid]:
        return arr[mid-1]
    if arr[mid-1] > arr[mid-2]:
        
