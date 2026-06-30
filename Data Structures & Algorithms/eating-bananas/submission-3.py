class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Koko's eating speed can be between 1 banana/hour and the size of the biggest pile
        left, right = 1, max(piles)

        # Binary search for the smallest valid speed
        while left < right:
            mid = (left + right) // 2   # Candidate eating speed

            # Calculate total hours needed at this speed
            # (p + mid - 1) // mid is the same as math.ceil(p / mid)
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                # If Koko can finish within h hours, try a smaller speed
                right = mid
            else:
                # Otherwise, she needs to eat faster
                left = mid + 1

        # When left == right, we found the minimum speed
        return left



# ⚡ Example 1:

# piles = [3, 6, 7, 11], h = 8

# Step 1: Setup

# left = 1, right = 11

# Step 2: Binary search

# mid = (1+11)//2 = 6

# Hours = (3+5)//6 + (6+5)//6 + (7+5)//6 + (11+5)//6

# = 1 + 1 + 2 + 2 = 6

# ✅ 6 <= 8 → possible, but maybe slower works → right = 6

# Now left=1, right=6, mid = 3

# Hours = (3+2)//3 + (6+2)//3 + (7+2)//3 + (11+2)//3

# = 1 + 2 + 3 + 4 = 10

# ❌ 10 > 8 → too slow → left = 4

# Now left=4, right=6, mid = 5

# Hours = (3+4)//5 + (6+4)//5 + (7+4)//5 + (11+4)//5

# = 1 + 2 + 2 + 3 = 8

# ✅ 8 <= 8 → works → right = 5

# Now left=4, right=5, mid = 4

# Hours = (3+3)//4 + (6+3)//4 + (7+3)//4 + (11+3)//4

# = 1 + 2 + 2 + 3 = 8

# ✅ 8 <= 8 → works → right = 4

# Now left=4, right=4 → done.
# Answer = 4 bananas/hour