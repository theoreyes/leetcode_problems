# Author: Theodore Reyes
# Problem: 3Sum
# Explanation: The solution I used for this problem is conceptually split two
#              parts. The first is an outer loop that fixes the value of one
#              of the elements in the triplet, incrementing forward in the list
#              after each outer loop. The second is an inner loop that
#              effectively reduces to 2Sum, where we have two pointers at
#              each end progressively making their way toward each other, while
#              recording any valid triplets seen along the way, and avoiding dupes.
#
#              Sorting the array beforehand is necessary to achieve O(n^2) time
#              with the two loops. Otherwise, 3 O(n) loops would be needed (naive method)
#
# Time:        Sorting is assumed to be O(n log(n)). Two nested loops both having
#              time complexity of O(n) results in complexity of O(n^2) altogether
#              for the nested loop. End result is O(n^2).
# Space:       O(1) for algorithm internals, O(n) for output list.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        i = 0

        while (i < (len(nums) - 2)):

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                if (nums[left] + nums[right] == target):
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    right -= 1
                    while (right > left and nums[right] == nums[right + 1]):
                        right -= 1
                elif (nums[left] + nums[right] < target):
                    left += 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                else:
                    right -= 1
                    while (right > left and nums[right] == nums[right + 1]):
                        right -= 1

            i += 1
            while (i < len(nums) - 2 and nums[i] == nums[i - 1]):
                i += 1

        return output
