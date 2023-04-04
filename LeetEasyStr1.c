#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # initialize pointers to the start and end of the array
        start, end = 0, len(s) - 1
        
        # swap the elements at the corresponding positions of start and end pointers
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
# The reverseString method uses two pointers start and end to traverse the array from opposite ends. 
#It swaps the elements at the corresponding positions of the start and end pointers until 
#they meet at the middle of the array. This effectively reverses the array in-place without 
#using any extra memory.