class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # frequency counts for s1 and first window in s2
        s1_count = Counter(s1)
        window = Counter(s2[:n])

        # check the first window
        if s1_count == window:
            return True

        # slide the window
        for i in range(n, m):
            # add new char
            window[s2[i]] += 1
            # remove leftmost char
            window[s2[i - n]] -= 1

            # clean up zero counts (important for equality check)
            if window[s2[i - n]] == 0:
                del window[s2[i - n]]

            if s1_count == window:
                return True

        return False