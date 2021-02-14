
def maxSumSub(arr, n):
    if n == 0:
        return
    res = - 9999999
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        if curr_sum > res:
            res = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return res

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSumSub(a, len(a)))

