def birthday(s, d, m):
    i = 0
    count = 0 
    while i < len(s):
        if sum(s[i:(i+m)]) == d:
            count = count + 1
        i = i + 1
    return(count)

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums)-1:
            j=i+1
            while j < len(nums):
                if (nums[i]+nums[(j)]) == target:
                    return([i, j])
                j=j+1
            i = i + 1