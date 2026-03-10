# Author: Theodore Reyes
#
# Explanation: Provides a very basic list-backed implementation of a stack.
# An auxiliary stack is maintained which contains the current minimum
# value of the main stack.
#
# Time: O(1) for each function, constant work per call
# Space: O(n) since we store 2n elements between the two stacks

class MinStack:

    def __init__(self):
        self.__stack = list()
        self.__minstack = list()

    def push(self, val: int) -> None:
        self.__stack.append(val)

        # If empty, first val is the min
        if (len(self.__stack) == 1):
            self.__minstack.append(val)
        # If new min, appends
        elif (val < self.__minstack[-1]):
            self.__minstack.append(val)
        # If no new min, re-appends previous min
        else:
            self.__minstack.append(self.__minstack[-1])

    def pop(self) -> None:
        self.__minstack.pop()       # Removes current min from minstack
        return self.__stack.pop()   # Returns pop'd val to user

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__minstack[-1]


