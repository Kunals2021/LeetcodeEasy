#Given two strings needle and haystack, 
#return the index of the first occurrence of needle in haystack, 
#or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1

#In this implementation, we first check if the needle string is empty. 
# If it is, then we can simply return 0 because an empty string is always present in any 
# other string at index 0.
#Next, we check if the needle string is present in the haystack string using the in operator. 
# If it is present, then we return the index of the first occurrence of the needle string in the 
# haystack string using the index method.]
#If the needle string is not present in the haystack string, then we simply return -1 to 
# indicate that the needle string is not part of the haystack string.