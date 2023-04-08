# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary to store the corresponding open and close brackets
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        # Create a stack to keep track of open brackets
        stack = []
        # Iterate through each character in the input string
        for char in s:
            # If the current character is an open bracket, add it to the stack
            if char in bracket_map:
                stack.append(char)
            # If the current character is a close bracket
            elif char in bracket_map.values():
                # Check if the stack is empty or if the top of the stack does not correspond to the current close bracket
                if not stack or bracket_map[stack.pop()] != char:
                    # If either of the above conditions is true, return False
                    return False
        # Check if there are any open brackets left in the stack
        return len(stack) == 0

# The basic idea of the solution is to use a stack to keep track of open brackets.
# When we encounter an open bracket, we add it to the stack. When we encounter a 
# close bracket, we check if it corresponds to the top of the stack. If it does, we pop the 
# top of the stack and continue. If it doesn't, we know that the input string is invalid and 
# we return False. After iterating through the input string, we check if there are any 
# open brackets left in the stack. If there are, we know that the input string is invalid
# and we return False. Otherwise, we return True.