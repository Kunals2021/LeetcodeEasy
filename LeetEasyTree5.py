# Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case: if the nums list is empty, return None
        if not nums:
            return None
        
        # find the middle index of the nums list
        mid = len(nums) // 2
        
        # create a new TreeNode with the value at the middle index
        node = TreeNode(nums[mid])
        
        # recursively call sortedArrayToBST with the left half of the nums list
        # and set the result as the left child of the current node
        node.left = self.sortedArrayToBST(nums[:mid])
        
        # recursively call sortedArrayToBST with the right half of the nums list
        # and set the result as the right child of the current node
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        # return the current node
        return node
#The sortedArrayToBST function takes a sorted array of integers nums as input and returns the 
# root node of a height-balanced binary search tree that has nums as its inorder traversal.
# The function first checks if the input nums is empty or not. If it is empty, then there is no 
# node to create a binary search tree, so it returns None. If nums is not empty, then it calculates 
# the middle index of nums by (len(nums) - 1) // 2. This middle element will be used as the 
# root of the binary search tree.
# Then, the function recursively constructs the left and right subtrees of the root node by calling 
# sortedArrayToBST with the left and right halves of the nums array, respectively. These left and 
# right halves are obtained by slicing nums using the middle index.
# Finally, the root node is returned with its left and right subtrees attached to it.