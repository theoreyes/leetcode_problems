# Theodore Reyes
#
# Explanation: Follows the algorithm outlined in problem to convert
# a string to an integer. Uses a dictionary to both check if a char
# is a digit as well as to grab said corresponding digit. Any valid
# string integer portion in the input string is converted directly
# into the correct output integer. This resulting integer is then
# signed accordingly and rounded up or down depending on its size,
# then returned as output.

class Solution:
    def myAtoi(self, s: str) -> int:
        nums = {
            '1' : 1, 
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        sign = None
        length = len(s)
        i = 0

        # Skip any leading whitespace
        while i < length and s[i] == ' ':
            i += 1

        # Gets sign of the number
        if (i < length and s[i] == '+'):
            sign = 1
            i += 1
        elif (i < length and s[i] == '-'):
            sign = -1
            i += 1
        else:
            sign = 1
        while i < length and s[i] == '0':
            i += 1

        # Converts the rest of the string to an integer
        result = 0
        while i < length and s[i] in nums:
            result += nums[s[i]]
            result *= 10
            i += 1
        result //= 10
        result *= sign
        
        # Returns value, rounding up or down if necessary
        if result < MIN_INT : result = MIN_INT
        if result > MAX_INT : result = MAX_INT
        return result
