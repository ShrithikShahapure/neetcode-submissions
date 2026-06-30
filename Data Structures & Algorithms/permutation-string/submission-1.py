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

# Approach (Sliding Window + Frequency Count)

# A permutation of s1 has the same character frequencies as s1.
# (e.g., "ab" → {"a":1, "b":1}).

# We need to check every substring of s2 with length len(s1) to see if it has the same frequency counts.

# Instead of recomputing frequencies for every substring (which is slow), we use a sliding window:

# Build a frequency counter for s1.

# Build a window frequency counter for the first len(s1) characters of s2.

# Slide one character at a time:

# Remove the leftmost char from the window.

# Add the new char from the right.

# Compare frequency maps at each step.