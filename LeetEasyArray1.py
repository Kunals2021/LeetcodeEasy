#Given an integer array nums sorted in non-decreasing order, 
#remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same. 
#Then return the number of unique elements in nums.
#Remove Duplicates from Sorted Array
class Solution:
   def removeDuplicates(self, nums):
       # Check if the array is empty
       if not nums:
          return 0

       # Initialize two pointers i and j, where i points to the last non-duplicate element
       i = 0

       # Traverse the array with the pointer j
       for j in range(1, len(nums)):

          # If the current element is not a duplicate, update i and update the non-duplicate element at i+1 position
          if nums[j] != nums[i]:
             i += 1
             nums[i] = nums[j]

       # Return the number of unique elements in the array, which is i+1
       return i + 1
