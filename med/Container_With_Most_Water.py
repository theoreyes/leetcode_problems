# Author: Theodore Reyes
# Explanation: Walks two pointers from each end of a heights
#              array, probing each for the amount of water 
#              they could carry (min height of the two, mult.
#              by their distance from each other), and moving
#              the ptr of the smaller height inward per
#              iteration.
#
# Time: O(n)   Constant work performed O(n) times, corresponding
#              to the length of the input array
#
# Space: O(1)  Only space used is a few variables, namely max_capacity
#              which is only ever updated and not grown in size

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0
        i = 0
        j = len(heights) - 1
        while i != j:
            distance = j - i
            capacity = min(heights[i], heights[j]) * distance
            if capacity > max_capacity:
                max_capacity = capacity
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_capacity
