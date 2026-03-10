# Author: Theodore Reyes
#
# Explanation: Parenthesis is checked for validity
# by matching all left parentheses with one of their
# right counterpart.
#
# Time: O(n)      <- traversing n-length input
# Space: O(n)     <- since we may store up to n/2 chars in list


class Solution:

    def isValid(self, s: str) -> bool:

        stack = list() 
        
        for ch in s:

            # If left parentheses, just push to stack
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:

                # If right parentheses, match it with its
                # appropriate left parentheses
                if len(stack) > 0: 
                    topChar = stack.pop()
                else:
                    return False # Returns False if unmatched right parentheses

                # If unmatched parentheses, returns False
                if topChar == '(' and ch != ')': return False
                if topChar == '{' and ch != '}': return False
                if topChar == '[' and ch != ']': return False

        if (len(stack) == 0):
            return True
        else:
            return False

