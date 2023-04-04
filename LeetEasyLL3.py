#Reverse Linked List
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers to None and head
        prev = None
        curr = head
        
        # Loop through the linked list and reverse the pointers
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Return the new head
        return prev

#The basic idea of the solution is to reverse the pointers of the linked list. 
#We initialize two pointers, prev and curr, to None and head respectively. 
# We loop through the linked list and for each node, we store the next node in a 
# temporary variable next_node, we reverse the pointer of the curr node to point to 
# the prev node, and we move prev and curr one node ahead. After looping through 
# the entire list, prev will point to the last node of the original list, which will 
# be the new head of the reversed list.