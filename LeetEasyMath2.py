#  Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        # Create a boolean array "is_prime[0..n]" and
        # initialize all entries as true. A value in
        # is_prime[i] will finally be false if i is
        # Not a prime, else true.
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False
        
        # Iterate from 2 to sqrt(n) to mark all the multiples of i as not prime
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Count the number of primes less than n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        
        return count

# The basic idea is to use the Sieve of Eratosthenes algorithm to mark all the multiples of each prime 
# number as not prime. Then, we can count the number of prime numbers less than n by simply counting 
# the number of True values in the boolean array is_prime. Note that we only need to iterate up to 
#  the square root of n to mark all the multiples of each prime number.