# Theodore Reyes
#
# Explanation: Simple check for if an array contains any duplicate
# values, using a hash table to keep track of elements we have
# already seen and short circuiting if we encounter an already-
# seen element during iteration through the input list.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x not in seen:
                seen.add(x)
            else: return True
        return False
