#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # If the input list is empty, return empty string
            return ""
        
        # Find the string with minimum length, since the longest common prefix cannot be longer than that
        min_str = min(strs, key=len)
        
        # Iterate over the characters of the minimum length string
        for i, char in enumerate(min_str):
            # Check if the character matches with the same index character of all other strings
            for other_str in strs:
                if other_str[i] != char:
                    # If not, return the substring up to the previous index
                    return min_str[:i]
        
        # If all characters match, return the minimum length string itself
        return min_str
#The function takes in a list of strings strs as input and returns the longest common prefix string 
# amongst them. If there is no common prefix, it returns an empty string.
#First, the function checks if the input list is empty, in which case it returns an empty string. 
# Then, it finds the string with the minimum length, 
# since the longest common prefix cannot be longer than that. 
# It does this using the min() function with key=len as the sorting key.
#Then, the function iterates over the characters of the minimum length string using enumerate(). 
# For each character, it checks if it matches with the same index character of all other strings using a nested loop. 
# If there is a mismatch, the function returns the substring up to the previous index. 
# If all characters match, the function returns the minimum length string itself.

