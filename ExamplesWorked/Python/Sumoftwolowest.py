# Test.describe("Basic tests")
# Test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
# Test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
# Test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

#Array
numbers = [7, 15, 12, 18, 22]
#String
#numbers = '2,4,5,6,12,13'

def sum_two_smallest_numbers(num_list):
    #num_list = num_list.split(",") ### For string input
    num_list.sort()
    #print(int(num_list[0]) + int(num_list[1]))  ### For string input
    print(num_list[0] + num_list[1])
    return num_list[0] + num_list[1]
sum_two_smallest_numbers(numbers)