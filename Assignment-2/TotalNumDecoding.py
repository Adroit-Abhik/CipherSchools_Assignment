def totalDecoding(str, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if int(code[n-1]) > 0:
        count += totalDecoding(str, n-1)
    if int(code[n-2] + code[n-1]) <= 26:
        count += totalDecoding(str, n-2)
    return count


def numDecoding(code, n):
    if n == 0 or (n==1 and code[0] == '0'):
        return 0
    res = totalDecoding(code, n)
    return res


if __name__ == "__main__":
    n = int(input())
    code = input()
    print(numDecoding(code, n))
