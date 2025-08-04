# Theodore Reyes
# 
# Explanation: I had to take a peak at some hints to get this problem solved,
# particularly the approach that uses bucket sort.
# The idea behind this approach is to build a hash table of numbers and the
# frequency with which they appear in the input array. Then, a form of bucket
# sort is used to build a secondary array of size n in which each element is 
# either None or a non-empty list of items, where items are inserted into 
# these lists according to their frequency in the input array. That is, the 
# element at a given index i will contain a list with all the numbers that 
# appear i times in the input array. From there, we simply iterate backwards
# over the array and add numbers until the output array reaches size k, and
# we return the output array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # Key, Frequency table
        freqArray = [None] * (len(nums) + 1) # Frequency count array
        output = [] # Output array
        for number in nums:
            if number in counts:
                counts[number] = counts[number] + 1
            else:
                counts[number] = 1
        
        for key in counts:
            if freqArray[counts[key]] == None:
                freqArray[counts[key]] = [key]
            else:
                freqArray[counts[key]].append(key)


        for lists in reversed(freqArray):
            if lists != None:
                for item in lists:
                    output.append(item)
                    if len(output) == k: break
            if len(output) == k: break

        return output
