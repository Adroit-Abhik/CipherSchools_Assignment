'''

Given an array A[] consisting 0s, 1s and 2s.
The task is to write a function that sorts the given array.
The functions should put all 0s first, then all 1s and all 2s in last

'''


def sorting012(arr, n):
    left = 0
    right = n-1
    mid = 0

    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr


arr = [0, 1, 2, 1, 0, 1, 2]
print(sorting012(arr, len(arr)))
