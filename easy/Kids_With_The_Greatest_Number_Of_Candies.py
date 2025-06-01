# Theodore Reyes
#
# Explanation: Checks whether the ith kid has the greatest candies
# if they were to be given all of the extra candies. Does so by first
# grabbing the max number of candies that any ith kid has, then
# adding extraCandies to each element in the list. Each value is then
# checked to see if it would be the greatest candies in the original
# list (often several exist)
# 
# Comments: Starting to learn more "Pythonic" ways of doing things.
# I am still surprised at the level of abstraction available, and hope
# to continue to learn these abstractions as a useful addition to my
# programming skills and toolkit.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        g = max(candies)
        candies = [x + extraCandies for x in candies]
        return [x >= g for x in candies]
