# Binary Search

**Difficulty:** Easy
**Pattern:** Binary Search
**Date:** 2026-05-18

## Intuition
binary search typical method. 
just watch for a mid value and if the target is less than the mid then we know its in left side, since array is sorted, if larger than mid, then right so we gotta mvoe the left pointer for teh new window. 

## Approach
_Not yet written._

## Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        left, right = 0, len(nums) - 1

        # [-1, 0, 2, 4, 6, 8] 
        # mid = 0 + 5 = 5 // 2 = [2]
        # 2 < target so we know target will be on right side
        # left = mid + 1 
        # repeat 
        # mid = 0 + 3 // 2 = 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1

        
```

## Notes
O(log N)
