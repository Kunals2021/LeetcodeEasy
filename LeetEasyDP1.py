# Climbing stairs - Dynamic programming 
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top

# To count the number of distinct ways to climb to the top of a staircase with n steps, we can use 
# dynamic programming. We start by defining an array dp of size n+1, where dp[i] represents the number 
# of distinct ways to reach step i. Since we can only climb 1 or 2 steps at a time, we can reach 
# step i from either step i-1 (by climbing 1 step) or step i-2 (by climbing 2 steps). 
# Therefore, we can compute dp[i] as the sum of dp[i-1] and dp[i-2].
# We can initialize dp[0] = 1 and dp[1] = 1, since there is only one way to reach the first two steps. 
# Then, we can use a for loop to compute dp[i] for i = 2 to n, using the recurrence 
# relation dp[i] = dp[i-1] + dp[i-2]. Finally, we return dp[n], which represents the number of distinct 
# ways to reach the top.

class Solution:
    def climbStairs(self, n: int) -> int:
        # If there is only one step, we can reach the top in one way
        if n == 1:
            return 1
        
        # Initialize dp[0] and dp[1] to the base cases
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        # Use dynamic programming to compute dp[i] for i = 2 to n
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        # Return dp[n], which represents the number of distinct ways to reach the top
        return dp[n]
# We first check if n is equal to 1, in which case there is only one step and we can reach the
#  top in one way. If n is greater than 1, we initialize an array dp of size n+1 to store the 
# dynamic programming values. We also initialize dp[0] and dp[1] to 1, since there is only one 
# way to reach the first two steps.
# We then use a for loop to compute dp[i] for i = 2 to n, using the recurrence 
# relation dp[i] = dp[i-1] + dp[i-2]. At each step, we add the number of ways to reach step i-1 and 
# the number of ways to reach step i-2, since we can only climb 1 or 2 steps at a time.
# Finally, we return dp[n], which represents the number of distinct ways to reach the top. 
# This is because dp[n] represents the number of ways to reach the nth step, and once we reach 
# the nth step, we have reached the top.