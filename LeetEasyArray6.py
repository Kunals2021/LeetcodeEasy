#Given two integer arrays nums1 and nums2, return an array of their intersection. 
#Each element in the result must appear as many times as it shows in both arrays and 
#you may return the result in any order.
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create empty dictionary to store frequency of each number in nums1
        freq_map = {}

        # iterate through nums1 and update frequency count in freq_map
        for num in nums1:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # create empty list to store intersection of nums1 and nums2
        intersection = []

        # iterate through nums2 and check if the number is in freq_map
        # if the frequency of the number in freq_map is greater than 0,
        # add the number to intersection and decrement the frequency count
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                intersection.append(num)
                freq_map[num] -= 1

        return intersection
