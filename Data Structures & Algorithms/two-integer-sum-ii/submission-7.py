# https://claude.ai/chat/2eeb3e16-3884-4519-8923-b5cc512f7285

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

