class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            
            # Check if we found the target
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in left side
                else:
                    left = mid + 1   # Target in right side
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target in right side
                else:
                    right = mid - 1  # Target in left side
        
        return -1  # Target not found