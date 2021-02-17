
def allPermutations(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            allPermutations(s, l+1, r)
            s[l], s[i] = s[i], s[l]


if __name__ == "__main__":
    s = input()
    n = len(s)
    print(allPermutations(list(s), 0, n-1))
