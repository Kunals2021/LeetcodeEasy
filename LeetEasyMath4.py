# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
    def romanToInt(self, s: str) -> int:
        # create a dictionary to map each roman numeral to its corresponding integer value
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # initialize the result variable to 0
        result = 0
        
        # iterate through the string of roman numerals from right to left
        for i in range(len(s) - 1, -1, -1):
            # get the integer value of the current roman numeral
            value = roman_values[s[i]]
            
            # if the value of the current numeral is less than the value of the next numeral to its right, 
            # subtract it from the result
            if i < len(s) - 1 and roman_values[s[i+1]] > value:
                result -= value
            # otherwise, add it to the result
            else:
                result += value
        
        # return the final result
        return result

# The function romanToInt takes a string s as input and converts it to an integer according to the 
# rules of Roman numerals. Here's how it works:
# First, a dictionary roman_values is created to map each Roman numeral to its corresponding 
# integer value.
# A variable result is initialized to 0.
# The function iterates through the string of Roman numerals from right to left using a for loop.
# For each numeral, the integer value is retrieved from the roman_values dictionary.
# If the value of the current numeral is less than the value of the next numeral to its right,
# it means that the current numeral represents a subtraction. In this case, the value of the 
# current numeral is subtracted from the result.
# Otherwise, the value of the current numeral is added to the result.
# After all the numerals have been processed, the final result is returned.