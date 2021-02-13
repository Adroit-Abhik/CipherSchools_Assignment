'''
Given an array of integers,
print the array in such a way that the first element is first maximum and second element is first minimum and so on.
'''


def alternateSorting(arr, n):
    if n <= 1:
        return arr
    arr.sort()
    res = []

    left = 0
    right = n-1

    while left <= right:
        if left == right:
            res.append(arr[left])
            break
        res.append(arr[right])
        right -= 1
        res.append(arr[left])
        left += 1

    return res

arr = [4, 1, 2, 5, 3]
print(alternateSorting(arr, len(arr)))


