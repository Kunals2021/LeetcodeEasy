#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
#and removing all non-alphanumeric characters, it reads the same forward and backward. 
#Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]

#First, we use a generator expression with join() to create a new string containing only 
# alphanumeric characters (letters and numbers). We do this by calling the isalnum() method on 
# each character of the original string s.
#We then convert the resulting string to lowercase using the lower() method.
#Finally, we check if the resulting string is equal to its reverse (i.e., if it's a palindrome) by 
# comparing it to s[::-1], which is s reversed.
#This code should work correctly for most cases. However, note that it may not handle all edge 
# cases perfectly (e.g., strings containing non-Latin characters)
#The first line of the function converts the string to lowercase and removes all non-alphanumeric 
# characters using regular expressions.
#The second line of the function creates a reversed string using slicing notation.
#The third line of the function checks if the original string and the reversed string are equal, 
# and returns True if they are, False otherwise.
#Overall, this is a simple and efficient solution to the problem of determining if a given string 
# is a palindrome.
