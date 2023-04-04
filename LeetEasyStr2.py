# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
#then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        # check if the integer is negative or positive
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        
        # reverse the integer
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10
        
        # check if the result is within the signed 32-bit integer range
        if rev > (2 ** 31 - 1):
            return 0
        
        # return the result with the appropriate sign
        return sign * rev
#This implementation first checks if the given integer is negative or positive, 
#then reverses the digits of the integer by repeatedly taking the last digit of the integer and 
# adding it to the result variable while removing the last digit from the integer. 
# Finally, it checks if the result is within the signed 32-bit integer range and returns it 
# with the appropriate sign.