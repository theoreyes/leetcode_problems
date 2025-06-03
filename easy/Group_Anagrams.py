# Theodore Reyes
#
# Explanation: Uses lists that are encoded with character frequency
# to act as hashes to lists of words that are grouped by said frequency.
# This groups strings that are anagrams of one another, which is returned
# as a list of lists of these groups of strings.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aStrs = {}
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            anagramStr = tuple(freq)
            if anagramStr not in aStrs:
                aStrs[anagramStr] = list()
            aStrs[anagramStr].append(s)
        return list(aStrs.values())
