#Delete Node in a Linked List
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # copy the value of the next node into the given node
        node.val = node.next.val
        
        # skip over the next node by updating the next pointer of the given node
        node.next = node.next.next

#To delete a node in a singly-linked list, we need to modify the next pointer of 
# the previous node to skip over the node we want to delete. 
# However, in this case, we do not have access to the previous node, 
# only the node to be deleted.
#One way to delete the given node is to copy the value of the next node into the given node, 
# and then skip over the next node by updating the next pointer of the given node to point 
# to the node after the next node.