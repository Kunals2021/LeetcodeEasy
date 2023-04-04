# Given a string s, find the first non-repeating character in it and return its index. 
#If it does not exist, return -1.
from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        # count the frequency of each character
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        
        # find the index of the first non-repeating character
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        return -1
# In the first loop, we count the frequency of each character in the string using a dictionary. 
# In the second loop, we find the index of the first non-repeating character by 
# iterating over the string and checking if the frequency of the current character is 1. 
# If we find such a character, we return its index. 
# If we don't find any non-repeating characters, we return -1.
