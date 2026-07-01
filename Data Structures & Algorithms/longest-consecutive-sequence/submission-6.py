# https://claude.ai/chat/9cfac8b4-4df9-4bbd-95eb-1f74866d1439


#  better solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)      # 1. deduplicate + O(1) lookups
        best = 0
        for x in nums:        # 2. iterate unique values only
            if x-1 not in nums:   # 3. only start at sequence beginnings
                y = x + 1        # 4. probe ABOVE x (x is already confirmed in set)
                while y in nums:  # 5. walk up until gap
                    y += 1
                best = max(best, y - x)  # 6. length = high watermark - start
        return best

