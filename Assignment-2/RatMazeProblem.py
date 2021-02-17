def setup():
    global v
    v = [[0 for i in range(100)] for j in range(100)]
    global ans
    ans = []


def path(arr, x, y, pth, n):
    if x == n - 1 and y == n - 1:
        global ans
        ans.append(pth)

        return
    global v
    if arr[x][y] == 0 or v[x][y] == 1:
        return
    v[x][y] = 1
    if x > 0:
        path(arr, x - 1, y, pth + 'U', n)
    if y > 0:
        path(arr, x, y - 1, pth + 'L', n)
    if x < n - 1:
        path(arr, x + 1, y, pth + 'D', n)
    if y < n - 1:
        path(arr, x, y + 1, pth + 'R', n)
    v[x][y] = 0


def findPath(arr, n):
    global ans
    ans = []

    if arr[0][0] == 0 or arr[n - 1][n - 1] == 0:
        return ans

    setup()
    path(arr, 0, 0, "", n)
    ans.sort()
    return ans