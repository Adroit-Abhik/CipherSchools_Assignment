def spiraltraversal(arr, row, column):
    l = 0
    m = 0
    # l starting row indx
    # row ending row idx
    # m starting col idx
    # column starting idx

    while l < row and m < column:
        # --->
        for i in range(m, column):
            print(arr[l][i], end=" ")
        l += 1
        # |
        for i in range(l, row):
            print(arr[i][column-1], end=" ")
        column -= 1

        if l < row:
            for i in range(column-1, m-1, -1):
                print(arr[row-1][i], end=" ")
            m-=1
        if m < column:
            for i in range(row-1, l-1, -1):
                print(arr[i][m], end=" ")
            m += 1


a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

R = 3
C = 6

# Function Call
spiraltraversal(a, R, C)
