# Theodore Reyes
#
# Explanation: We traverse the input array and add previously
# visited numbers and their indices to a hashmap. When visiting
# some ith number, we check if its difference with the target
# is a key in the hashmap. If this key exists, it means we
# have found two values whose sum is the target, and so we return
# their indices as output. Otherwise, we add this number and its 
# index to the hashmap and continue to the next value.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for i, num in enumerate(nums):
            diff = target - num             
            if diff in prevNums:            # Returns indices if found
                return [i, prevNums[diff]]
            else:                           # Else, adds to hashmap
                prevNums[num] = i
