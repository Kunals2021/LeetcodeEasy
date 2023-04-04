#Given an integer array nums, return true if any value appears at least twice in the array, 
#and return false if every element is distinct.
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if any value appears at least twice in the array nums, False otherwise.
        """
        return len(nums) != len(set(nums))
