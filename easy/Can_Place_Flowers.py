# Theodore Reyes
#
# Explanation: Uses sliding-window approach to see if new pot can be
# placed at ith location in the flowerbed. If at any point during
# execution num becomes equal to n, this means we have found n available
# locations for pots to be planted and thus return True without further
# iterating.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        i = 0
        num = 0
        while i < l:
            if flowerbed[i] == 0:
                if i + 1 < l:
                    if flowerbed[i + 1] == 0: 
                        num += 1
                        if num == n : return True
                    else:
                        i += 1
                else:
                    num += 1
                    if num == n  : return True
            i += 2
        return num >= n
