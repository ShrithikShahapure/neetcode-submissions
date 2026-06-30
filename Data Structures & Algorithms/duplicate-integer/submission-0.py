class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap[num] = i
            
        return False
        