'''
Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

'''


def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()

    platform = 1
    res = 1
    depidx = 0
    arridx = 1

    while depidx < n and arridx < n:
        if dep[depidx] >= arr[arridx]:
            platform += 1
            arridx += 1
        elif dep[depidx] < arr[arridx]:
            platform -= 1
            depidx += 1
        res = max(res, platform)
    return res

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(findPlatform(arr, dep, len(arr)))
