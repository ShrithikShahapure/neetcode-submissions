class Solution:
    def findMin(self, nums: List[int]) -> int:



        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2
            
            # If middle is greater than right, min must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, min is in the left half (including mid)
                right = mid
        
        # Left will point to the minimum
        return nums[left]
        