'''

You are given an array of 0s and 1s in random order.
Segregate 0s on left side and 1s on right side of the array.
Traverse array only once.
'''


def sorting01(arr, n):
    if n <= 1:
        return arr
    count = 0
    for i in range(n):
        if arr[i] == 0:
            count += 1
    for i in range(count):
        arr[i] = 0

    for i in range(count, n):
        arr[i] = 1
    return arr

arr = [0, 1, 1, 0, 1]
print(sorting01(arr, len(arr)))
