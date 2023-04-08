# Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
#In this code, we have defined the Solution class with the isSymmetric method that takes a root node of 
# a binary tree and returns a boolean indicating whether the binary tree is symmetric (i.e., a mirror of
#  itself) or not.
# We use a helper method isMirror to recursively check if two subtrees are mirrors of each other. 
# If both nodes are None, they are mirrors of each other, so we return True. If only one node is None, 
# they are not mirrors of each other, so we return False. If the values of the nodes are not equal, 
# they are not mirrors of each other, so we return False. Otherwise, we recursively check if the left 
# subtree of the first node is a mirror of the right subtree of the second node and if the right subtree 
# of the first node is a mirror of the left subtree of the second node.
# In the isSymmetric method, we check if the root node is None. If it is None, it is symmetric, 
# so we return True. Otherwise, we call the isMirror method with the left subtree of the root node 
# and the right subtree of the root node. If both subtrees are mirrors of each other, the binary 
# tree is symmetric and we return True. Otherwise, it is not symmetric and we return False.

