# is_low(), is_mid(), is_high()
# white, red, blue 
arr = [8,6,5,4,7,2]
pro = {8:'h',6:'m',5:'m',4:'l',7:'h',2:'l'}

def is_low(i):
    return pro[i] == 'l'
def is_mid(i):
    return pro[i] == 'm'
def is_high(i):
    return pro[i] == 'h'
print is_low(2)

def sortArr(nums):
    low, mid, high = 0,0, len(nums)-1
    while mid <= high:
        if is_low(nums[mid]):
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif is_mid(nums[mid]):
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

print sortArr(arr)