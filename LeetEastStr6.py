#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#The algorithm for myAtoi(string s) is as follows:
#Read in and ignore any leading whitespace.
#Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
#Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
#Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
#If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
#Return the integer as the final result.
#Note:\
#Only the space character ' ' is considered a whitespace character.
#Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.lstrip()
        
        # Check if string is empty
        if not s:
            return 0
        
        # Check for sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Read digits
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)
        
        # Apply sign and check bounds
        num *= sign
        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num

#explanation of the code for the myAtoi function:
#Initialize the result variable to 0, which will be used to store the final 
# integer value that we want to return.
#Remove any leading whitespace characters using the lstrip() method.
#Check if the next character (if not already at the end of the string) is '-' or '+'. 
# If it is either, set the negative variable accordingly. 
# This determines if the final result is negative or positive respectively. 
# If neither is present, assume the result is positive.
#Iterate through the remaining characters in the string using a for loop. 
# If a non-digit character is encountered, break out of the loop. 
# If a digit character is encountered, multiply the current value of result by 10 and add the integer 
# value of the digit (which is obtained using the built-in ord() and int() functions).
#After the loop, adjust the sign of the result variable based on the value of negative.
#If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
# then clamp the integer so that it remains in the range. 
# Specifically, integers less than -231 should be clamped to -231, and 
# integers greater than 231 - 1 should be clamped to 231 - 1.
#Return the result variable as the final result.
