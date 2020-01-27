# https://leetcode.com/problems/min-stack/

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = None

    def push(self, x: int) -> None:
        self.data.append(x)
        
        if self.mins == None or self.mins > x:
            self.mins = x
        
    def pop(self) -> None:
        val = self.data.pop()
        
        if len(self.data) > 0:
            self.mins = min(self.data)
        else:
            self.mins = None
            
    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return self.mins

# Runtime: 76 ms, faster than 34.32% of Python3 online submissions for Min Stack.
# Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Min Stack.