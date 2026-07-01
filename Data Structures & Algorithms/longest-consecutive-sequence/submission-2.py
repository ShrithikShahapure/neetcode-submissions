# https://claude.ai/chat/9cfac8b4-4df9-4bbd-95eb-1f74866d1439

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)        # build hash set
        best = 0
        for num in nums:
            if (num-1) not in nums_set:  # is start?
                cur = num; length = 0
                while cur in nums_set:    # count up
                    cur += 1; length += 1
                best = max(best, length)

        return best