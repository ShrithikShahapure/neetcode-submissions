class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = defaultdict(int)
        left = 0
        max_freq = 0
        result = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])  # keep as a running max

            # shrink until valid
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # now the window is valid
            result = max(result, right - left + 1)

        return result
            


        