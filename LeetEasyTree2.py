#  Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # We use the inorder traversal of the binary tree to check if it is a valid BST.
        # In inorder traversal, we visit the left subtree, then the current node, and then the right subtree.
        # In a valid BST, the inorder traversal should produce a sorted sequence.
        # We keep track of the last visited node in the inorder traversal and check if each node is greater than the last.
        # If any node violates this property, the binary tree is not a valid BST.
        stack = []
        last_value = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= last_value:
                return False
            last_value = root.val
            root = root.right
        return True
# In this code, we have defined the Solution class with the isValidBST method that takes a root 
# node of a binary tree and returns a boolean indicating whether the binary tree is a valid binary 
# search tree (BST) or not.
# We use the inorder traversal of the binary tree to check if it is a valid BST. In inorder traversal,
#  we visit the left subtree, then the current node, and then the right subtree. In a valid BST, the inorder traversal should produce a sorted sequence.
# We use a stack to simulate the recursive function call stack for inorder traversal. 
# We keep track of the last visited node in the inorder traversal and check if each node is greater 
# than the last. If any node violates this property, the binary tree is not a valid BST and we return 
# False. Otherwise, we continue with the traversal. If we reach the end of the traversal without any 
# violation, the binary tree is a valid BST and we return True.
