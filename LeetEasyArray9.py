#Given an array of integers nums and an integer target, return indices of the two numbers such that they #add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element #twice.
#You can return the answer in any order.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to store the complement of each number and its index
        complement_dict = {}

        # iterate through nums
        for i in range(len(nums)):
            # calculate the complement of the current number
            complement = target - nums[i]
            # if the complement is in the dictionary, we found a pair that adds up to target
            if complement in complement_dict:
                return [complement_dict[complement], i]
            # add the current number and its index to the dictionary
            complement_dict[nums[i]] = i
#The idea is to use a dictionary to store the complement of each number and its index. 
# We iterate through the array and for each number, 
# we calculate its complement and check if it is in the dictionary. 
# If it is, we found a pair that adds up to the target and return their indices. 
# If it is not, we add the current number and its index to the dictionary. 
# This ensures that we don't use the same element twice in the solution