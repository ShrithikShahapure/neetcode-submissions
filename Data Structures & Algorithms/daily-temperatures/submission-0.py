class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n
        stack = []  # will store indices

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res
        

# Key Ideas

# Result array → start with all zeros (because if no warmer day exists, answer is 0).
# Example: [0,0,0,0,0,0,0,0].

# Stack → stores indices of days we are still "waiting" on (haven’t yet found a warmer day for them).

# Why indices and not temperatures? → Because we need to calculate how many days later (i - prev_index).

# While loop → Each time we find a warmer day (temperatures[i] > temperatures[stack[-1]]), we:

# Pop that earlier index from the stack.

# Calculate how many days it took → i - prev_index.

# Store it in res[prev_index].

# Walkthrough Example

# Input:

# temperatures = [73,74,75,71,69,72,76,73]

# Iteration Process

# Day 0 (73)
# Stack empty → push 0
# Stack = [0]

# Day 1 (74)
# 74 > 73 → pop 0
# res[0] = 1 - 0 = 1
# Push 1
# Stack = [1]
# Result = [1,0,0,0,0,0,0,0]

# Day 2 (75)
# 75 > 74 → pop 1
# res[1] = 2 - 1 = 1
# Push 2
# Stack = [2]
# Result = [1,1,0,0,0,0,0,0]

# Day 3 (71)
# 71 < 75 → push 3
# Stack = [2,3]

# Day 4 (69)
# 69 < 71 → push 4
# Stack = [2,3,4]

# Day 5 (72)
# 72 > 69 → pop 4 → res[4] = 5 - 4 = 1
# 72 > 71 → pop 3 → res[3] = 5 - 3 = 2
# Push 5
# Stack = [2,5]
# Result = [1,1,0,2,1,0,0,0]

# Day 6 (76)
# 76 > 72 → pop 5 → res[5] = 6 - 5 = 1
# 76 > 75 → pop 2 → res[2] = 6 - 2 = 4
# Push 6
# Stack = [6]
# Result = [1,1,4,2,1,1,0,0]

# Day 7 (73)
# 73 < 76 → push 7
# Stack = [6,7]

# End of loop → indices left in stack have no warmer day, so they stay 0.

# Final Answer
# [1,1,4,2,1,1,0,0]