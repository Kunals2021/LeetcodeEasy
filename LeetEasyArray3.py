#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # calculate the actual number of steps to rotate, accounting for cases where k > len(nums)
        k %= len(nums)

        # reverse the entire array
        nums.reverse()

        # reverse the first k elements of the array
        nums[:k] = reversed(nums[:k])

        # reverse the remaining elements of the array
        nums[k:] = reversed(nums[k:])
