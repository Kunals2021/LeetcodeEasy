#Palindrome Linked List
#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First, we traverse the linked list and store the values in a list.
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # Then, we compare the values in the list from both ends.
        i, j = 0, len(values) - 1
        while i < j:
            if values[i] != values[j]:
                return False
            i += 1
            j -= 1
        
        return True

# In this code, we have defined the Solution class with the isPalindrome method that takes a 
# head node of a singly-linked list and returns a boolean indicating whether the linked list is 
# a palindrome or not.
# We use the same logic as before: first, we traverse the linked list and store the values in a list. 
# Then, we compare the values in the list from both ends. If we encounter any mismatch, 
# we return False, indicating that the linked list is not a palindrome. Otherwise, we return True.