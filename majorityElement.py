'''
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”.
A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).
'''

# Naive approach

def find_majority_element(arr, n):
    if n == 0:
        return -1
    maxCount = 0
    resIndex = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count  > maxCount:
            maxCount = count
            resIndex = i

    if maxCount > n//2:
        return arr[resIndex]
    else:
        return -1


def find_majority_faster(arr, n):

    res = 0
    count = 1
    # find element with highest count
    for i in range(1, n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            count = 1
            res = i
    count = 0
    # check if majority
    for i in range(n):
        if arr[res] == arr[i]:
            count += 1
    if count > n//2:
        return res
    else:
        return -1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(find_majority_element(arr, n))
