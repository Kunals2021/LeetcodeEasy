#Remove Nth Node From End of List
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Calculate the index of the node to be removed from the beginning of the list
        index = length - n
        
        # If the first node needs to be removed, return the second node
        if index == 0:
            return head.next
        
        # Traverse the list to the node before the node to be removed
        curr = head
        for i in range(index - 1):
            curr = curr.next
        
        # Remove the node at the calculated index
        curr.next = curr.next.next
        
        return head
    


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create two pointers, one for the beginning and another for n nodes ahead
        first_ptr = head
        second_ptr = head
        for i in range(n):
            second_ptr = second_ptr.next
        
        # If the second pointer has reached the end, remove the first node
        if not second_ptr:
            return head.next
        
        # Traverse both pointers until the second pointer reaches the end
        while second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        
        # Remove the nth node from the end
        first_ptr.next = first_ptr.next.next
        
        return head

#To remove the nth node from the end of a linked list, we need to first traverse 
# the list to find the length of the list. Once we have the length of the list, 
# we can calculate the index of the node to be removed from the beginning of the list. 
# Then, we can traverse the list again and remove the node at the calculated index.
#The time complexity of this solution is O(n), where n is the length of the list. 
# We need to traverse the list twice, once to find the length and once to remove the node. 
# The space complexity is O(1), as we only use constant extra space.


#The basic idea is to create two pointers, one for the beginning of the linked list 
# and another n nodes ahead. Then, we traverse both pointers until the second pointer 
# reaches the end of the linked list. At this point, the first pointer will be pointing 
# to the node that precedes the nth node from the end. We can then remove the nth node by 
# updating the next attribute of the (n-1)th node to point to the (n+1)th node.