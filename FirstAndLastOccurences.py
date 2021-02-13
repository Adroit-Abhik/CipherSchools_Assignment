'''
Given a sorted array with possibly duplicate elements,
the task is to find indexes of first and last occurrences of an element x in the given array.
[ 1, 5, 5, 5, 6]
[1, 5, 5]
[1, 5]
[5, 6]
'''


def find_first(arr, n, target):
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high - low) // 2

        if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_last(arr, n, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if (mid == n-1 or arr[mid + 1] > target) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [5, 6]
print("first occurrence: ", find_first(arr, len(arr), 5))
print("first last: ", find_last(arr, len(arr), 5))



