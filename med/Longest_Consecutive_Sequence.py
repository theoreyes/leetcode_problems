class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Num set from input
        numSet = set(nums)
        longest = 0

        # Build candidate array
        for num in numSet:
            if num - 1 not in numSet:
                # CANDIDATE FOUND
                run = 1
                current = num
                while current + 1 in numSet:
                    run += 1
                    current += 1
                if run > longest:
                    longest = run
        
        return longest
