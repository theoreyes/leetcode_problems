# Author: Theodore Reyes
# 
# Explanation: We "walk" two pointers down both ends of the sorted array,
# where if we overshoot the target sum, we walk the "large number" pointer down by 1,
# and if we undershoot the target sum, we walk the "small number" pointer up by 1,
# until we arrive at the correct combination of indices.
#
# Time: O(n)   <-- n/2 iterations of loop to find index1 and index2 in worst case
# Space: O(1)  <-- Stores constant amount (indices, loop var) regardless of input size

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index1 = 0
        index2 = len(numbers) - 1

        for i in range(len(numbers)):
            if (numbers[index1] + numbers[index2]) > target:
                index2 -= 1
            elif (numbers[index1] + numbers[index2]) < target: 
                index1 += 1
            else:
                break

        return [index1 + 1, index2 + 1]

