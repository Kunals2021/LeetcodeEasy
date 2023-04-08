# Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the 
# root node down to the farthest leaf node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the root is None, the maximum depth is 0.
        if root is None:
            return 0
        
        # Otherwise, we compute the maximum depth of the left and right subtrees.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth of the tree is 1 + the maximum depth of the deeper subtree.
        return 1 + max(left_depth, right_depth)
# In this code, we have defined the Solution class with the maxDepth method that takes a root 
# node of a binary tree and returns the maximum depth of the tree as an integer.
# We use recursion to compute the maximum depth of the left and right subtrees. 
# If the root node is None, we return 0. Otherwise, the maximum depth of the tree 
# is 1 + the maximum depth of the deeper subtree. We use the max function to determine which 
# subtree is deeper.
