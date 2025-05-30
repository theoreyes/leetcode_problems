# Theodore Reyes
#
# Explanation: Iterates through both strings using a while loop,
# and if does not cause out of bounds error, adds the next char
# from each string to the output list. Returns the joined
# list as output

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []
        len1 = len(word1)
        len2 = len(word2)
        longStrLen = len1 if len1 >= len2 else len2
        i = 0
        while i < longStrLen:
            if i < len1 : out.append(word1[i])
            if i < len2 : out.append(word2[i])
            i += 1
        return ''.join(out)
