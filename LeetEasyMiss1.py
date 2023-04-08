# Number of 1 Bits
# Write a function that takes the binary representation of an unsigned integer and 
# returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a count variable to 0
        count = 0
        # Loop through each bit of the input integer
        while n != 0:
            # Increment the count if the current bit is 1
            count += n & 1
            # Right shift the input integer by 1 to check the next bit
            n >>= 1
        # Return the final count
        return count

# This code implements the "bit manipulation" approach to counting the number of 1 bits in the 
# binary representation of an unsigned integer. Here's a breakdown of how it works:\
# The input integer n is passed in as an argument to the hammingWeight method.
# The count variable is initialized to 0.
# The while loop continues as long as n is not equal to 0 (i.e. there are still bits left to check).
# Inside the loop, the current bit is checked using the bitwise AND operator (n & 1). 
# This operation returns 1 if the current bit is 1 and 0 otherwise. If the current bit is 1, 
# the count variable is incremented.
# The input integer is right shifted by 1 to move on to the next bit.
# Once all bits have been checked, the final count is returned.