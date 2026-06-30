# My Solution

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         left, right = 0, len(numbers) - 1

#         while left < right:

#             if numbers[left] + numbers[right] == target:
#                 return [left + 1, right + 1]

#             while numbers[left] + numbers[right] < target:
#                 left += 1

#             while numbers[left] + numbers[right] > target:
#                 right -= 1

#         return [none]



# Chat gpt solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
            # Return 1‑based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:  # current_sum > target
                right -= 1

        # Problem guarantees a solution, so we never reach here
        raise ValueError("No two sum solution")

        

# expllaination

# Why the submission didn’t pass

# Problem in your code	What it actually does	Why it fails
# Returned the values, not the indices	return [numbers[left], numbers[right]]	LeetCode expects 1‑based indices. You should return [left + 1, right + 1].
# Using while instead of if to move the pointers	The inner while loops keep moving left or right as long as the condition holds.	If numbers[left] + numbers[right] < target is true once, the loop keeps incrementing left until the sum is ≥ target. That’s fine, but the second loop (for > target) is executed only once in the outer loop, so you can get stuck or skip the correct pair. The two inner loops are not mutually exclusive and can both fire in the same outer iteration, leading to a wrong result or infinite loop.
# Missing return [None]	return [none] (lower‑case none)	none is not defined; you probably meant None. Also the problem guarantees a solution, so this line should never be executed.
# No type hints or import for List	Not shown, but in LeetCode the import is usually handled.	Usually fine, but make sure you have from typing import List if you test locally.
# No early exit after moving pointers	You continue the outer while loop even after moving left/right in the inner loops.	You may skip over the correct pair if you overshoot. The standard pattern is: compute sum, then if sum < target: left += 1, elif sum > target: right -= 1, else return.