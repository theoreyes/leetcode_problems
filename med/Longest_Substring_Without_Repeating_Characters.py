# Inefficient implementation of this problem, will update with a O(n)
# solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        record = 0
        seen = set()
        for i in range(len(s)):
            substr = s[i:]
            for ch in substr:
                if ch in seen:
                    seen.clear()
                    length = 0
                    break
                seen.add(ch)
                length += 1
                if length > record : record = length
        return record
