# Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the 
# array # # nums1. To accommodate this, nums1 has a length of m + n, where the first m 
# elements denote the elements # that should be merged, and the last n elements are set to 0 and 
# should be ignored. nums2 has a length of n.
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize three pointers: i points to the last element of nums1,
        # j points to the last element of nums2, and k points to the last empty slot in nums1
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        # Merge nums1 and nums2 from right to left, putting the larger element at the end of nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Put the larger element from nums1 at the end of nums1
                i -= 1  # Decrement the pointer of nums1
            else:
                nums1[k] = nums2[j]  # Put the larger element from nums2 at the end of nums1
                j -= 1  # Decrement the pointer of nums2
            k -= 1  # Decrement the pointer of nums1 (where the next largest element will go)
        
        # Merge any remaining elements of nums2 into nums1, if there are any left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# To merge two sorted arrays in non-decreasing order, we can use a two-pointer approach. 
# We start with two pointers, one pointing to the last element of nums1 (at index m-1) and another 
# pointing to the last element of nums2 (at index n-1). We compare the elements at these pointers 
# and put the larger element at the end of nums1 (at index m+n-1). We continue this process, moving 
# the pointer of the larger element one step to the left, until all elements of nums2 are merged 
# into nums1.

# We start with three pointers i, j, and k. Pointer i points to the last element of nums1, pointer j points
#  to the last element of nums2, and pointer k points to the last empty slot in nums1. We use a while 
# loop to compare the elements at these pointers and put the larger element at the end of nums1. 
# We decrement the pointers as we merge elements, until all elements of nums2 are merged into nums1.
# Note that we also need a separate while loop to merge any remaining elements of nums2 into nums1,
#  in case there are any left after the first loop.
# The time complexity of this algorithm is O(m + n), and the space complexity is O(1), 
# as we are modifying the input array nums1 in place without using any extra space.