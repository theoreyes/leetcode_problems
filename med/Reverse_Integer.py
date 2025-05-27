# Theodore Reyes
#
# Explanation: Snips the end of the input integer and appends it
# to result integer, shifting the input down a factor of 10 and
# the result number up a factor of 10 after each iteration.
#
# Note: Going to try and optimize this to avoid the sign check,
# just wanted to get the first shot uploaded for now

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0
        inpNum = x
        tmp = 0
        sign = 0
        if (inpNum < 0):
            sign = 1
            inpNum *= -1
        while inpNum > 0:
            tmp = inpNum % 10
            inpNum //= 10
            result += tmp
            result *= 10
        result //= 10
        if (sign == 1): result *= -1
        if result > INT_MAX or result < INT_MIN:
            return 0
        else:
            return result
