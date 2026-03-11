# Author: Theodore Reyes
# 
# Explanation: Evaluates postfix notation of inputs using a stack.
# Input is assumed to be valid, which makes this a lot easier.
# As each token is iterated over, we apply the requested mathematical
# operations and store their results back into the stack. What is left
# at the end of a valid postfix sequence is the result of the computation.
#
# Time: O(n)   <-- Processing n items, each iteration is O(1) processing time
# Space: O(n)  <-- Storing O(n) data items in stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        op1 = 0
        op2 = 0

        # Main loop iterates over each token in input
        # and decides what to do based on postfix rules
        for s in tokens:
            if (s == "+"):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)
            elif (s == "-"):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif (s == "*"):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 * op2)
            elif (s == "/"):
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 / op1;
                # Division must truncate 'toward' zero 
                # according to restrictions of this problem
                if (result < 0): 
                    result = math.ceil(result)
                else:
                    result = math.floor(result)
                stack.append(result)
            else:
                stack.append(int(s))

        return stack.pop()

