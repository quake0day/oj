def binarysearchwithE(arr, target, first, last):
    mid = (last - first) / 2

    if arr[mid] == "":
        left = mid - 1
        right = mid + 1

        while True:
            if left < first and right > last:
                return -1 
            elif right <= last and arr[right] != "":
                mid = right
                break 
            elif left >= first and arr[left] != "":
                mid = left
                break
            else:
                left -= 1
                right += 1
    if arr[mid] == target:
        return mid 
    elif target < arr[mid]:
        return binarysearchwithE(arr, target, first, mid-1)
    else:
        return binarysearchwithE(arr, target, mid+1, last)





arr = [0, "", 1, 2, 5, "", "","","","","",7, 9, "",10]
print binarysearchwithE(arr, 5, 0, len(arr)-1)