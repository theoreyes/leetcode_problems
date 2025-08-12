# Theodore Reyes
#
# Explanation: An input array is passed over once and a general
# "array product" is created by multiplying all positive
# elements with one another. The edge cases where 1 or more
# zeros are present in the input creates two sub-cases: if only
# one zero is present, all elements except the location of the single
# zero are zeroed out. In the case where more than one zero is present,
# every element will naturally be a zero, so an array representing this
# is returned.
#
# In the general case that all elements are non-zero, the output array
# is constructed by filling each location with the array product divided
# by the original corresponding element at that location.
#
# Note: I am still figuring out how to accomplish this without using division.
# When I do, I will create a separate file for that solution.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrProd = 1
        output = [None] * len(nums)
        zeros = 0
        zIndex = 0
        for i, n in enumerate(nums):
            if (n != 0): 
                arrProd *= n
            else:
                zeros += 1
                zIndex = i
                if (zeros > 1): 
                    return [0 for item in range(len(nums))]
        if (zeros == 1):
            output = [0 for item in range(len(nums))]
            output[zIndex] = arrProd
        else:
            for i in range(len(nums)):
                output[i] = arrProd // nums[i]
        return output
