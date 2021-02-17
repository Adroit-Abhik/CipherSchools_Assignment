'''
The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down

'''


def countPath(row, col):
    if row == 1 or col == 1:
        return 1
    return countPath(row-1, col) + countPath(row, col-1)


if __name__ == '__main__':
    row = int(input())
    col = int(input())
    print(countPath(row, col))
