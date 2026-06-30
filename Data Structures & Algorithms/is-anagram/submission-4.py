class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = {}

        if len(s) != len(t):
            return False

        for ch in s:
            seen[ch] = seen.get(ch,0) + 1

        for ch in t:
            seen[ch] = seen.get(ch,0) - 1
            if seen[ch] < 0:
                return False
            
        print(seen)
        return True