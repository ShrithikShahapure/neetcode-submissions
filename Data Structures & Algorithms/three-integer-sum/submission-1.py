class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()     #Sort the array
        res = []

        for i in range (len(nums)):     # sets i as first value that is nioto a duplicate 

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # 2 pointer starts from here

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:    # avoids any duplicate entries in array
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res

