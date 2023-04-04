#Merge Two Sorted Lists
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the head node of the merged list
        merged_head = ListNode(-1)
        # Keep a pointer to the current node of the merged list
        current_node = merged_head
        
        # Traverse both the lists till one of them becomes empty
        while list1 and list2:
            if list1.val <= list2.val:
                # Append the smaller value to the merged list
                current_node.next = list1
                # Move the pointer of the merged list to the next node
                current_node = current_node.next
                # Move the pointer of list1 to the next node
                list1 = list1.next
            else:
                current_node.next = list2
                current_node = current_node.next
                list2 = list2.next
        
        # Append the remaining nodes of the non-empty list to the merged list
        if list1:
            current_node.next = list1
        if list2:
            current_node.next = list2
        
        # Return the head of the merged list (excluding the initial dummy node)
        return merged_head.next

#The mergeTwoLists function takes two linked lists list1 and list2 as input and returns 
# the head of the merged linked list.
#The implementation initializes the head node of the merged list with a dummy node (-1) and 
# keeps a pointer to the current node of the merged list. It then traverses both the input 
# lists and appends the smaller value of the current nodes to the merged list, while moving the 
# pointers of both the current input list and the merged list to their next nodes. 
# Once one of the input lists becomes empty, the remaining nodes of the non-empty list are 
# appended to the merged list. Finally, the head of the merged list (excluding the initial 
# dummy node) is returned.