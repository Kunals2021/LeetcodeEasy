# Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Initialize a variable to keep track of the count
        count = 0
        
        # Loop through each integer in the array
        for num in nums:
            # Convert the integer to a string and check its length
            if len(str(num)) % 2 == 0:
                # If the length is even, increment the count
                count += 1
        
        # Return the count of integers with an even number of digits
        return count
    
# This code initializes a count variable to 0, loops through each integer in the input array,
# checks if the integer has an even number of digits by converting it to a string and checking 
# the length of the string, and increments the count if the integer has an even number of digits. 
# Finally, the function returns the count of integers with an even number of digits.