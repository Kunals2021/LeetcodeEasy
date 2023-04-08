# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., 
# from left to right, level by level).
from typing import List
from typing import List, Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Initialize the result list and the queue for BFS
        result = []
        queue = [root]
        
        while queue:
            level = []
            level_size = len(queue)
            
            # Traverse all the nodes in the current level
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                # Add the left and right child of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Add the values of the nodes in the current level to the result list
            result.append(level)
            
        return result
# We first check if the root is null. If it is, we return an empty list. Otherwise, we initialize 
# two variables: result, which will store the level order traversal of the binary tree, and queue, 
# which is a list that will be used to perform BFS on the binary tree.
# In the while loop, we keep traversing the binary tree level by level until the queue becomes empty. 
# For each level, we first initialize an empty list level and determine the number of nodes in the 
# current level, which is the size of the queue.
# We then traverse all the nodes in the current level, which are the first level_size nodes in the queue.
#  For each node, we append its value to the level list, and we add its left and right 
# child (if they exist) to the queue.
# After we have traversed all the nodes in the current level, we append the level list to the result 
# list. Once we have traversed all the levels in the binary tree, we return the result list.