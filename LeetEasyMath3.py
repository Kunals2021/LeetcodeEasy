# Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^^x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # If n is negative or 0, it cannot be a power of 3, so return False
        if n <= 0:
            return False
        
        # Keep dividing n by 3 until it becomes less than or equal to 1
        while n > 1:
            if n % 3 != 0: # If n is not divisible by 3, it cannot be a power of 3, so return False
                return False
            n //= 3 # Divide n by 3
        
        return True # If n reaches 1, it means it was a power of 3, so return True

# The code checks if the input number is negative or 0. If so, it cannot be a power of 3, so the f
# unction returns False.
# If the input is positive, the function keeps dividing it by 3 until it becomes less than 
# or equal to 1. If the number is not divisible by 3 at any point during this process, it cannot be 
# a power of 3, so the function returns False.
# If the number eventually becomes 1, it means it was a power of 3, so the function returns True.