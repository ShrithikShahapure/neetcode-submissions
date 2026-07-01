# https://claude.ai/chat/9cfac8b4-4df9-4bbd-95eb-1f74866d1439


#  better solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for x in nums:
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y-x)

        return best

