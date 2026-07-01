# https://claude.ai/chat/0c2d6d2b-e872-492b-9bbe-e2e94deb2878

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right = 0, len(s) - 1   

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1


        return True        