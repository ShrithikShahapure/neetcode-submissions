class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Search range: [1, max(piles)]
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:  
                # Koko can eat all bananas at this speed
                right = mid  # try smaller k
            else:
                left = mid + 1  # need a bigger k

        return left