'''
[10,20,40,5,6,7,8]
original sorted array = [5,6,7,8,10,20,40]
pivot element = 40
'''

def binarySearch(arr, low, high, target):
    if high < low:
        return -1
    mid = low + (high - low)//2
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binarySearch(arr, (mid+1), high, target)
    return binarySearch(arr, low, mid-1, target)

def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = low + (high-low)//2
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if arr[mid] > arr[low]:
        return findPivot(arr, mid+1, high)
    else:
        return findPivot(arr, low, mid-1)


def findEl(arr, n, target):
    pivot_idx = findPivot(arr, 0, n-1)
    # if array is not rotated or fully rotated the pivotidx = -1
    if pivot_idx == -1:
        return binarySearch(arr, 0, n-1, target)
    if arr[pivot_idx] == target:
        return pivot_idx
    if target >= arr[0]:
        # between 0 and pivotIdx
        return binarySearch(arr, 0, pivot_idx-1, target)
    return binarySearch(arr, pivot_idx+1, n-1, target)


arr = [10,20,40,5,6,7,8]
print(findEl(arr, len(arr), 6))
