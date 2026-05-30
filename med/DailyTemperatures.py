# Author: Theodore Reyes
# 
# Uses a stack to store (value, index) pairs that are monotonically
# decreasing. The catch is, as we traverse through the input array
# in a forward manner, we check the current element against the
# top element's value in the stack, and if the current element is
# bigger, we have found a critical value which we can derive 1 or
# more solutions for within the results array (specifically, all values
# in the temperatures array whose "answer" is the current element!)
#
# Time: O(n) - We traverse each element only once, and per value stored
#              in the results array we do a single comparison. All other
#              work is constant time.
#
# Space: O(n) - The size of the stack is proportional to the size of the
#               input array of size n. On average, it will be less than
#               the full length of the array but is only upper-bounded by
#               the size of the array itself, which the stack could grow
#               equal to if the array were purely monotonically decreasing.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = list()
        result = list(range(0, len(temperatures)))

        for i, temp in enumerate(temperatures):
            
            while (len(stack) != 0 and temp > stack[-1][0]):
                # Updates result for each monotonically decreasing value on stack
                result[stack[-1][1]] = i - stack[-1][1]
                # Remove element from the stack
                stack.pop()

            # Add current (value, index) to stack
            stack.append((temp, i))

        while (len(stack) != 0):
            # Fill-in 0's for any leftover elements at the end of the stack
            result[stack[-1][1]] = 0
            stack.pop()

        return result
