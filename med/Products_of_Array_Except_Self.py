# Theodore Reyes
#
# Explanation: Solves product of array except self by computing both the
# forward and reverse rolling-product of the input array. Then, the output
# array is constructed by multiplying the pre-computed "left" and "right"
# sides against each other for each position in the array.

class Solution(object):
    def productExceptSelf(self, nums):
        fwdNums = [None] * len(nums) # Forward direction of pre-computed multiplications
        revNums = [None] * len(nums) # Reverse direction of pre-computed multiplications
        output = [None] * len(nums)
        fwdProduct = 1
        revProduct = 1
        for i, n in enumerate(nums):
            fwdProduct *= nums[i]
            fwdNums[i] = fwdProduct
        for i, n in reversed(list(enumerate(nums))):
            revProduct *= nums[i]
            revNums[i] = revProduct
        for i, n in enumerate(output):
            if (i == 0):
                output[i] = revNums[i+1]
            elif (i == len(output)-1):
                output[i] = fwdNums[i-1]
            else:
                output[i] = fwdNums[i-1] * revNums[i+1]
        return output
