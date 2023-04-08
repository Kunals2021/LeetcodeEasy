# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:
    def __init__(self):
        # Initialize two stacks, one for elements and another for the minimum values
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the new element to the main stack
        self.stack.append(val)
        
        # Check if the new element is smaller or equal to the current minimum value
        # If it is, push the new element to the minimum value stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Check if the element to be popped is the current minimum value
        # If it is, pop it from the minimum value stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        # Pop the element from the main stack
        self.stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the minimum value stack
        return self.min_stack[-1]

# The __init__ method initializes two stacks, one for elements and another for the minimum values. 
# The push method pushes a new element to the main stack and checks if it is smaller or equal to the 
# current minimum value. If it is, it pushes the new element to the minimum value stack as well. 
# The pop method checks if the element to be popped is the current minimum value. If it is, it pops it 
# from the minimum value stack as well. Then, it pops the element from the main stack. 
# The top method returns the top element of the main stack. The getMin method returns the 
# top element of the minimum value stack. All these methods have a time complexity of O(1).