class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    # Return an array where each element is the product of all other elements.
    # No division is used. O(n) time, O(1) extra space (output excluded).
    
        n = len(nums)
    # Output array; start with all 1's (multiplicative identity)
        answer = [1] * n

    # First pass: compute prefix products
        left_prod = 1
        for i in range(n):
            answer[i] = left_prod
            left_prod *= nums[i]

    # Second pass: compute suffix products and multiply
        right_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_prod
            right_prod *= nums[i]

        return answer