# Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result to 0
        result = 0
        
        # Loop through 32 bits
        for i in range(32):
            # Shift the result left by one bit to make space for the next bit
            result <<= 1
            
            # If the last bit of n is 1, set the new last bit of result to 1
            if n & 1:
                result |= 1
            
            # Shift n right by one bit to check the next bit
            n >>= 1
        
        # Return the reversed integer
        return result
    
# This function uses a loop to iterate through each of the 32 bits in the input integer n.
# It shifts the result left by one bit to make space for the next bit, then checks whether the 
# last bit of n is 1. If it is, it sets the new last bit of the result to 1 using the bitwise
# OR operator. Finally, it shifts n right by one bit to check the next bit. After looping through
# all 32 bits, the function returns the reversed integer.