#Your task is to find the first element of an array that is not consecutive.

arr = [1,2,3,4,6,7,8]

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            print(arr[i])
            return arr[i]
first_non_consecutive(arr)


# Test.describe("Basic tests")
# Test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
# Test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
# Test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
# Test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)
# Test.assert_equals(first_non_consecutive([31,32]), None)
# Test.assert_equals(first_non_consecutive([-3,-2,0,1]), 0)
# Test.assert_equals(first_non_consecutive([-5,-4,-3,-1]), -1)