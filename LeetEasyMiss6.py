# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of all numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        # Calculate the actual sum of the given numbers
        actual_sum = sum(nums)
        # The missing number is the difference between the expected and actual sums
        return expected_sum - actual_sum

# In this implementation, we first calculate the expected sum of all numbers from 0 to n using the 
# formula (n * (n + 1)) // 2. We then calculate the actual sum of the given numbers using the sum 
# function. Finally, we subtract the actual sum from the expected sum to get the missing number. 
# This works because the missing number is the only number that's not accounted for in the actual sum.