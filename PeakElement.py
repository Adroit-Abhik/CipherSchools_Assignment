'''
Given an array of integers. Find a peak element in it.
An array element is a peak if it is NOT smaller than its neighbours.
For corner elements, we need to consider only one neighbour.
'''


def find_peak(arr, n):
    if n == 0:
        return -1
    if n == 1:
        return 0

    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1

    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i

# arr = [1, 5, 10, 7, 6]
# print(find_peak(arr, len(arr)))


def find_peak_optimized(arr, n):
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1

    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
            return mid
        elif mid > 0 and arr[mid-1] > arr[mid]:
            high = mid
        else:
            low = mid + 1


arr = [1, 5, 10, 7, 6]
print(find_peak_optimized(arr, len(arr)))


