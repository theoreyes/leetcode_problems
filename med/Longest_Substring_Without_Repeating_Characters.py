# Theodore Reyes
#
# Explanation: Uses a single pass through the string, where
# the last-seen position of each character is kept track
# of in a hash table. When repeats are found, the start of the 
# current substring is moved 1 past the repeat's last-seen index,
# and the length updated accordingly. The greatest length value
# reached is returned as output.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        record = 0
        start = 0
        seen = {}
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                lastpos = seen[ch]
                start = lastpos + 1
                seen[ch] = i
                length = i - lastpos - 1
            length += 1
            if length > record : record = length
            seen[ch] = i
        return record
