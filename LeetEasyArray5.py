#Given a non-empty array of integers nums, every element appears twice except for one. 
#Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to zero
        result = 0
        
        # Loop through all the numbers in the array
        for num in nums:
            # Perform XOR operation between the current num and the result
            result ^= num
        
        # Return the result variable which contains the value of the single number that appears only once
        return result
