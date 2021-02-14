'''
The cost of a stock on each day is given in an array,
find the max profit that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0,
selling on day 3. Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order,
then profit cannot be earned at all.

'''

'''
fidn local minima and locla maxima in an iteraction 
profit += arr[local_maxima] - arr[local_minima]

'''

def stockProfit(arr, n):
    if n <= 1:
        return
    profit = 0

    i = 0
    while i < n:
        # find local minima, can not be the last element as cant buy stock at last day
        while i < n-1 and arr[i] >= arr[i+1]:
            i += 1
        local_minima = i
        if local_minima == n-1:
            break

        # find local maxima
        i += 1
        # cant be same index
        while i < n and arr[i-1] <= arr[i]:
            i += 1
        loal_maxima = i -1

        profit += arr[loal_maxima] - arr[local_minima]

        print("Buy: ", local_minima, "  ", "Sell: ", loal_maxima)

    return profit


arr = [100, 180, 260, 310, 40, 535, 695]
print(stockProfit(arr, len(arr)))










