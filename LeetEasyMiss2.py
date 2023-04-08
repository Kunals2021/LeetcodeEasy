#   Hamming Distance
# The Hamming distance between two integers is the number of positions at which the 
# corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two integers to get a binary number where the bits are 1 where the corresponding bits were different
        xor_num = x ^ y
        # Initialize a count to keep track of the number of 1's in the binary number
        count = 0
        # Iterate through each bit in the binary number
        while xor_num:
            # If the current bit is 1, increment the count
            count += xor_num & 1
            # Shift the binary number one bit to the right to move on to the next bit
            xor_num >>= 1
        # Return the count of 1's, which is the Hamming distance between x and y
        return count

# In this code, we first compute z as x ^ y which gives us a number where the bits are set wherever 
# there is a difference between x and y. We then initialize a variable count to 0, and use a loop to 
# iterate over the bits in z. In each iteration, we check if the least significant bit of z is set
# by performing z & 1. If it is set, we increment count. We then shift z one bit to the right by 
# performing z >>= 1, so that we can check the next bit. We continue this until all the bits in z
# have been checked. Finally, we return count which gives us the Hamming distance between x and y.