'''
Given an n x n matrix, where every row and column is sorted in non-decreasing order.
Find the kth smallest element in the given 2D array.

'''

# Naive approach


def findKth(arr, row, col, k):
    if k == 0:
        return arr[0][0]
    if k >= row * col:
        return arr[row-1][col-1]
    temp = []
    for i in range(row):
        for j in range(col):
            temp.append(arr[i][j])
    temp.sort()
    return temp[k-1]


# better approach using binary search

def findKthFaster(arr, row, col, k):
    pass



mat = [[10, 20, 30, 40],
    [15, 25, 35, 45],
    [25, 29, 37, 48],
    [32, 33, 39, 50]]
print(findKth(mat, 4, 4, 7))

