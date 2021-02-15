'''
Given an n x n matrix and a number x,
find the position of x in the matrix if it is present in it.
Otherwise, print “Not Found”. In the given matrix,
every row and column is sorted in increasing order.
The designed algorithm should have linear time complexity.

'''

def search(mat, n, x):
    row = 0
    col = n-1
    while (row < n) and (col >= 0):
        if mat[row][col] == x:
            return "Found"
        if mat[row][col] > x:
            col -= 1
        else:
            # mat[row][col] < x:
            row += 1
    return "Not Found"

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
print(search(mat, 4, 29))
