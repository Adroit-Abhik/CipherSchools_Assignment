'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:

Input: arr[]   = {2, 0, 2}
Output: 2

'''


def trapWater(arr, n):
    if n <= 1:
        return 0

    res = 0
    for i in range(1, n-1):
        # find left tallest
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        # find right tallest
        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])
        res += (min(left, right) - arr[i])

    return res


def trapwaterFaster(arr, n):
    if n <= 1:
        return 0
    left = [0]*(n)
    right = [0]*(n)

    res = 0

    # find left tallest for each element
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    # find right tallest for each element from the end
    right[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    # find total water
    for i in range(n):
        res += min(left[i], right[i]) - arr[i]

    return res

arr = [2, 0, 2]
print(trapwaterFaster(arr, len(arr)))


