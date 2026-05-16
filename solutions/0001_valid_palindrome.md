# Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**Date:** 2026-05-16

## Intuition
two pointers on each end 

## Approach
two pointers on each end coming towards middle checking each index, if same all the way then it is palindrome.

## Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        left , right = 0, len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
```

## Notes
_No notes yet._
