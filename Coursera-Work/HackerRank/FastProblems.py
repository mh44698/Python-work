# Find max of the top 4 and min of the bottom 4
def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[1:])
    print(min, max)
miniMaxSum([1,2,3,4,5])

# Find the Number of Maximum
def birthdayCakeCandles(ar):
    maxi = max(ar)
    count = ar.count(maxi)
    print(count)
birthdayCakeCandles([3, 2, 1, 3,])

