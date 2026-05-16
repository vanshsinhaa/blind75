# Longest Consecutive string

**Difficulty:** Medium
**Pattern:** Other
**Date:** 2026-05-16

## Intuition
_Not yet written._

## Approach
- Dump array into a HashSet (O(1) lookups + duplicates gone)
- Loop through each number
- if `n - 1` is NOT in the set, the `n` is a sequence start.


## Code
```python
numSet = set(nums)
longest = 0

for n in numSet:
	if n - 1 not in numSet:
		length = 1

		while (n + length) in numSet:
			length += 1
		longest = max(longest, length)

return longest
```

## Notes
test
