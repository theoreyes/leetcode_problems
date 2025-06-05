# Theodore Reyes
#
# Explanation: Checks if the string is a palindrome by sending
# two pointers down the string from both ends, and skipping
# over any non-alphanum characters. If any non-matching
# characters are found, returns False. If the main loop completes,
# we know the string is a valid palindrome and thus return True.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length - 1
        while (i <= j):
            while (i < length - 1 and not s[i].isalnum()):
                i += 1
            while (j >= 0 and not s[j].isalnum()):
                j -= 1
            if (s[i] != s[j]):
                if (s[i].lower() != s[j].lower()): return False
            i += 1
            j -= 1
        return True
