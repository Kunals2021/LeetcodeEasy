# Shuffle an Array
# Given an integer array nums, design an algorithm to randomly shuffle the array. 
# All permutations of the array should be equally likely as a result of the shuffling.

import random

class Solution:
    def __init__(self, nums: List[int]):
        # Store the input array in a member variable called "nums"
        self.nums = nums
        # Make a copy of the input array and store it in another member variable called "original_nums"
        self.original_nums = nums.copy()

    def reset(self) -> List[int]:
        # Reset the "nums" array to its original configuration by copying the values from "original_nums" back to "nums"
        self.nums = self.original_nums.copy()
        # Return the "nums" array
        return self.nums

    def shuffle(self) -> List[int]:
        # Use the "random.shuffle" function to shuffle the "nums" array in place
        random.shuffle(self.nums)
        # Return the shuffled "nums" array
        return self.nums

#We import the random module to use the random.shuffle() function, which shuffles the elements of a 
# list in place.
#In the __init__() method, we initialize two member variables nums and original_nums. nums is 
# assigned the input array nums, and original_nums is assigned a copy of nums using the copy() method. 
# The reason for this is that when we call the reset() method, we want to be able to restore the 
# original array, so we need to make a copy of it before modifying it.
#The reset() method simply resets the nums array to its original state by copying the values from 
# original_nums back to nums.
#The shuffle() method shuffles the nums array using the random.shuffle() function and returns 
# the shuffled array. Note that random.shuffle() shuffles the list in place, so there is no need 
# to return the list explicitly.

