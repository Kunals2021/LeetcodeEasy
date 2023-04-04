#You are given a large integer represented as an integer array digits, where each digits[i] is the ith #digit of the integer. 
#The digits are ordered from most significant to least significant in left-to-right order. 
#The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate through digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            # add one to the current digit
            digits[i] += 1
            # if the digit is less than 10, we don't need to carry over
            if digits[i] < 10:
                return digits
            # if the digit is 10, set it to 0 and carry over to the next digit
            digits[i] = 0

        # if we reach here, it means all digits were 9 and we need to add an extra digit 1
        digits.insert(0, 1)
        return digits
    
#The idea is to start iterating through the digits from right to left. 
#We add one to the current digit and check if it is less than 10. 
#If it is less than 10, we don't need to carry over and can return the digits array. 
#If it is 10, we set the digit to 0 and carry over to the next digit. 
#If we reach the leftmost digit and it is 10, 
#it means all digits were 9 and we need to add an extra digit 1 at the beginning of the array.

