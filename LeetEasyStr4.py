#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#typically using all the original letters exactly once.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of s and t are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create a dictionary to keep track of the frequency of each character in s
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        # Check if each character in t is in the dictionary and has the same frequency as in s
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            else:
                freq[char] -= 1
        
        # If all characters in t are in the dictionary and have the same frequency as in s, t is an anagram of s
        return True
