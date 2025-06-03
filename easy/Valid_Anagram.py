# Theodore Reyes
#
# Explanation: Checks if two strings are anagrams of one another
# by building dictionaries/a hash table of the characters within
# each string and their frequency of occurence. These tables are
# then compared with one another to determine if both strings
# have the same characters and frequency of occurence as one
# another, indicating that they are anagrams of each other

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initializes dictionaries for each string, containing characters
        # and their frequency of occurence in the string
        sLetters = {}
        tLetters = {}
        for ch in s:
            sLetters[ch] = sLetters.get(ch, 0) + 1
        for ch in t:
            tLetters[ch] = tLetters.get(ch, 0) + 1

        # Quickly returns False if one string has letters that do not
        # appear in the other
        if len(sLetters) != len(tLetters): return False

        # Checks if character sets and their frequencies match
        for key in sLetters:
            if key not in tLetters or sLetters[key] != tLetters[key]:
                return False
        return True
