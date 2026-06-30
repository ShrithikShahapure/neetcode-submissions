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

        