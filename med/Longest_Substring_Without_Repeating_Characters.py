# Theodore Reyes
#
# Explanation: Performs a pass-through of parameter string s and
# maintains a set containing chars that have been seen so far. With each
# char iterated over, a len count is incremented. When a repeat
# char is encountered the char set is emptied and the len is set to 0 after
# updating the record len, if necessary.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len = 0
        record = 0
        seen = set()
        for ch in s:
            if ch in seen:
                if len > record:   # Updates record of longest substring
                    record = len
                len = 0
                seen.clear()       # wipes 'memory' of chars seen so far
            seen.add(ch)
            len += 1
        return record
