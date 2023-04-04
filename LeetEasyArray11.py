#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
#DO NOT allocate another 2D matrix and do the rotation.
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse the rows of the matrix
        matrix.reverse()
        
        # transpose the matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#The rotate method first reverses the rows of the matrix using the reverse method of the list object.
# Then, it transposes the matrix in-place by swapping the elements at the symmetric positions 
# along the diagonal. 
# The transpose operation swaps the rows and columns of the matrix, 
# effectively rotating it by 90 degrees clockwise.