# Question: https://leetcode.com/problems/longest-consecutive-sequence/

# approach:
'''
- Dump array into a HashSet (O(1) lookups + duplicates gone)
- Loop through each number
- if `n - 1` is NOT in the set, the `n` is a sequence start. 
'''

# Solution:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # dump array into a HashSet (O(1) lookups + duplicates gone)
        longest = 0 # track longest

        for num in nums: # loop through each number
            if num - 1 not in nums_set: # if `n - 1` is NOT in the set, the `n` is a sequence start.
                length = 1 # track length
                while num + length in nums_set:
                    length += 1 # increment length
                longest = max(longest, length) # update longest
        return longest