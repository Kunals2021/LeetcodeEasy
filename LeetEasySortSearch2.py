# First Bad Version
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left < right:
            # Avoid integer overflow by using (left + right) // 2 instead of left + (right - left) // 2
            mid = (left + right) // 2
            if isBadVersion(mid):
                # The middle version is bad, so search for the first bad version in the left half
                right = mid
            else:
                # The middle version is good, so search for the first bad version in the right half
                left = mid + 1
        
        # At this point, left and right point to the first bad version, since left == right
        return left


#To find the first bad version using the minimum number of API calls, we can use a binary search algorithm.
# We start by checking the middle version (version (n+1)//2) using the isBadVersion() API. 
#If this version is bad, then we know that all versions after it must also be bad, so we need to 
#search for the first bad version in the left half of the range (versions 1 to (n+1)//2 - 1). 
#If the middle version is not bad, then we know that all versions before it are good, so we need 
#to search for the first bad version in the right half of the range (versions (n+1)//2 + 1 to n).
#We repeat this process until we find the first bad version. At each step, we only need to make 
#one API call to determine whether the middle version is bad or not, and we can eliminate half of the 
#remaining versions from consideration.

#We start with two pointers, left and right, pointing to the first and last versions respectively. 
# We use a while loop to repeat the binary search process until we find the first bad version. 
# We use the isBadVersion() API to determine whether the middle version is bad or not,
# and update left or right accordingly to eliminate half of the remaining versions. 
# We keep doing this until left and right point to the same version, which must be the first 
# bad version.
#Note that we use (left + right) // 2 to calculate the middle version to avoid integer overflow, 
# as left + right can exceed the maximum value of an integer if left and right are both close to
#  the maximum value.
#The time complexity of this algorithm is O(log n), since we eliminate half of the remaining 
# versions at each step, and the space complexity is O(1), since we only use a constant amount 
# of extra space for the pointers left, right, and mid.



