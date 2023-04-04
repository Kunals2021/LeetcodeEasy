#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
#non-zero elements.
#Note that you must do this in-place without making a copy of the array.
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialize a pointer to keep track of the next index to place a non-zero element
        next_non_zero_idx = 0

        # iterate through nums
        for i in range(len(nums)):
            # if the current element is non-zero, move it to the next available index
            if nums[i] != 0:
                nums[next_non_zero_idx] = nums[i]
                next_non_zero_idx += 1

        # fill the remaining elements with zeros
        for i in range(next_non_zero_idx, len(nums)):
            nums[i] = 0
#The idea is to use a pointer to keep track of the next index to place a non-zero element. 
# We iterate through the array and if the current element is non-zero, 
# we move it to the next available index and increment the pointer. 
# After iterating through the array, we fill the remaining elements with zeros starting 
# from the pointer index. 
# This ensures that we move all zeros to the end of the array while maintaining 
# the relative order of the non-zero elements.
