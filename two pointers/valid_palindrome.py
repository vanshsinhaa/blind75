# Question: https://leetcode.com/problems/valid-palindrome/

# approach:
'''
- Two pointers: left and right
- If the characters at the left and right pointers are not the same, return False
- If the characters at the left and right pointers are the same, move the pointers inward
- If the left pointer is greater than the right pointer, return True
'''

# Solution:

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

# Test case:
print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # True
print(Solution().isPalindrome("race a car")) # False