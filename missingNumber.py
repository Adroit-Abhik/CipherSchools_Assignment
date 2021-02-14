'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

'''

def findMissing(arr):
    n = len(arr)
    missing_num = ((n+1)*(n+2) / 2) - sum(arr)
    return int(missing_num)

a = [1,2,4,5,6]
print(findMissing(a))


