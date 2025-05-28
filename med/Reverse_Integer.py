# Theodore Reyes
#
# Explanation: Snips the end of the input integer and appends it
# to result integer, shifting the input down a factor of 10 and
# the result number up a factor of 10 after each iteration.
#
# Note: Re-wrote partially for clarity as well as to comply with
# the 32-bit constraint of operands. My overflow check consists
# of the semantic question "Can we handle doing the following
# operation given current value of result and tmp?"
# In practice, this looks like calculating the largest value
# of result that we can fit in 32-bits and then checking if
# the actual value is greater than this. This is simply to
# avoid overflowing during the multiply and add step found
# on the last line of the while loop :)

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        result = 0
        tmp = 0
        sign = x < 0
        if sign: x *= -1
        while x > 0:
            tmp = x % 10
            x //= 10
            if result > ((INT_MAX) - tmp) // 10: # avoids overflowing 32-bits
                return 0
            result = result * 10 + tmp
        if (sign == 1): result *= -1
        return result
