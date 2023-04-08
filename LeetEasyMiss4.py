# Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initialize the result with the first row
        result = [[1]]
        
        # loop through each row and compute the elements
        for i in range(1, numRows):
            row = [1] * (i+1) # initialize the row with 1s
            
            # compute the elements using the previous row
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            
            result.append(row)
        
        return result

# The Pascal's triangle is a triangular array of the binomial coefficients. 
# The first and the second row of the triangle are 1's. To generate the next row, 
# we add the adjacent elements from the previous row.
# This solution has a time complexity of O(numRows^2), since we need to compute each element of 
# the triangle. However, the space complexity is O(numRows^2) as well, since we need to store 
# the entire triangle in memory.
