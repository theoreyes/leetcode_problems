# Theodore Reyes
#
# Explanation: Reverses the input integer using divs and mods, and compares
# with the original to determine if it is a palindrome. Negative inputs are
# immediately given a return value of False. This implementation does
# not check for overflow in the reverse integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0): return False    # negative nums are not palindromes
        tmpNum = x
        revNum = 0
        while (tmpNum > 9):
            revNum += tmpNum % 10
            revNum *= 10
            tmpNum //= 10
        revNum += tmpNum
        return (revNum == x)
