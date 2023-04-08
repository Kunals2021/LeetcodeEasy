# Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum sum seen so far and the current sum
        max_sum = float('-inf')
        curr_sum = 0
        
        # Iterate through the nums array
        for num in nums:
            # If the current sum is negative, reset it to 0
            if curr_sum < 0:
                curr_sum = 0
            # Add the current number to the current sum
            curr_sum += num
            # If the current sum is greater than the maximum sum seen so far, update the maximum sum
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        # Return the maximum sum seen
        return max_sum

# We first initialize variables to keep track of the maximum sum seen so far and the current sum. 
# We set the maximum sum to negative infinity to handle the case where all the numbers in the nums 
# array are negative. Then, we iterate through the nums array and for each number, we add it to the 
# current sum. If the current sum is negative, we reset it to 0 because a negative sum can only 
# decrease the total sum. If the current sum is greater than the maximum sum seen so far, 
# we update the maximum sum.
# This approach works because we are essentially trying to find the subarray with the largest sum. 
# By keeping track of the current sum and resetting it to 0 if it becomes negative, we effectively 
# start looking for a new subarray from the current index. By updating the maximum sum whenever we 
# find a new subarray with a larger sum, we keep track of the largest sum seen so far.