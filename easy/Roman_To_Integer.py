# Theodore Reyes
#
# Explanation: Converts a string representation of a Roman numeral
# to integer by summing each numeral based on its roman-to-int value.
# In the case that the next character represents a larger value than
# the current one, we subtract the current one instead of adding it.

class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        length = len(s)
        i = 0
        while i < length:
            if i != (length - 1) and rom[s[i + 1]] > rom[s[i]]:
                result -= rom[s[i]]
            else:
                result += rom[s[i]]
            i += 1
        return result
