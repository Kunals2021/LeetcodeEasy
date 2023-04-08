# Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that 
# tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We use the two-pointer technique to check for cycle in the linked list.
        # We start with two pointers: slow and fast.
        # Slow moves one step at a time while fast moves two steps at a time.
        # If there is a cycle, then at some point, fast will catch up with slow.
        # If there is no cycle, then fast will reach the end of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#In this code, we have defined the Solution class with the hasCycle method that takes a head
#  node of a singly-linked list and returns a boolean indicating whether the linked list has 
# a cycle or not.
# We use the two-pointer technique to check for cycle in the linked list. We start with two pointers:
# slow and fast. Slow moves one step at a time while fast moves two steps at a time. 
# If there is a cycle, then at some point, fast will catch up with slow. 
# If there is no cycle, then fast will reach the end of the linked list. 
# If fast ever becomes None, we know that there is no cycle and we return False.
