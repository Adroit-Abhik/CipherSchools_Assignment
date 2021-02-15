


def validPair(res, val, open, idx, n):
    if idx >= n*2:
        res.append(val)
        return
    if open < n:
        validPair(res, val+'(', open+1, idx+1, n)
        if open * 2 > idx:
            validPair(res, val+')', open, idx+1, n)
    elif open == n:
        validPair(res, val+')', open, idx+1, n)

def gen(n):
    open = 0
    close = 0
    res = []
    validPair(res, "", open, close, n)
    return res


print(gen(3))



