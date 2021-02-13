'''
find k smallest element in an array according to their index order.
'''


def find(arr, n, k):
    if k >= n:
        return arr

    # making window of k size
    for i in range(k, n):
        max = arr[k - 1]
        max_pos = k - 1
        # find max of the window for every iteration
        for j in range(k-1, -1, -1):
            if arr[j] > max:
                max = arr[j]
                max_pos = j
        print(max)
        curr = arr[i]
        # if curr < max start shifting leftwards from k-1 to max_pos
        if curr < max:
            temp = max_pos
            while temp < k-1:
                arr[temp] = arr[temp+1]
                temp += 1
            # put current smaller element at the window in order
            arr[k-1] = curr

    return arr[:k]

arr = [4,2,6,1,5]
print(find(arr, len(arr), 3))



