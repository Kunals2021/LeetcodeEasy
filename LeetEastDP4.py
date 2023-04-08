#  House Robber
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum amount of money that can be robbed at the current house and the previous house
        curr_max = 0
        prev_max = 0
        
        # Iterate through the nums array
        for num in nums:
            # Calculate the maximum amount of money that can be robbed at the current house
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        
        # Return the maximum amount of money that can be robbed
        return curr_max

# We first initialize variables to keep track of the maximum amount of money that can be robbed at 
# the current house and the previous house. We then iterate through the nums array and for each house,
#  we calculate the maximum amount of money that can be robbed at that house. We do this by taking 
# the maximum of two possibilities: either rob the current house and add the maximum amount of money 
# that could be robbed at the previous house (which cannot be robbed because of the adjacent house 
# constraint), or skip the current house and take the maximum amount of money that could be robbed 
# at the previous house.
# To keep track of these possibilities, we use two variables: curr_max to keep track of the maximum 
# amount of money that can be robbed at the current house, and prev_max to keep track of the maximum 
# amount of money that could be robbed at the previous house. At each house, we update these variables 
# accordingly.
# Finally, we return the maximum amount of money that can be robbed, which is stored in curr_max.