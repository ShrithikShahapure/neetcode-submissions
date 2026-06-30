class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        best = 0

        while left < right:
        # current height is limited by the shorter line
            h = min(heights[left], heights[right])
        # width is the distance between pointers
            w = right - left
        # area = height × width
            best = max(best, h * w)

        # move the pointer at the shorter line inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best     
        