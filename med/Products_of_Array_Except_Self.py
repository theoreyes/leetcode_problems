# Theodore Reyes
#
# Explanation: Solves product of array except self by computing both the
# forward and reverse rolling-product of the input array. Then, the output
# array is constructed by multiplying the pre-computed "left" and "right"
# sides against each other for each position in the array. Uses the
# product array itself to first store the forward "prefixes," then
# iterates backwards to get the reverse "suffixes," building
# the final output array on this reverse pass.

class Solution(object):
    def productExceptSelf(self, nums):

        length = len(nums)
        output = [None] * length

        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            output[i] = prefix
            
        suffix = 1
        for i in range(length - 1, -1, -1):
            if (i != 0):
                output[i] = output[i-1] * suffix
                suffix *= nums[i]
            else:
                output[i] = suffix

        return output
