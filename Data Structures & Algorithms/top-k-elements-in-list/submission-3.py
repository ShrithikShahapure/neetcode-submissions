class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        freq_map = Counter(nums)  # O(n)
        
        # Counter is basically the hashmap that we implemented in the previous thing

        # freq_map = {}

        # for i, num in enumerate(nums):
        #     if num in freq_map:
        #         freq_map[num] += 1
        #     else:
        #         freq_map[num] = 1
    
    # Less Space

    # freq_map = {}
            # for num in nums:
            # if num in freq_map:
            #     freq_map[num] += 1
            # else:
            #     freq_map[num] = 1


    # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)  # O(n)
    
    # Step 3: Gather results from high freq to low
        res = []
        for freq in range(len(buckets) - 1, 0, -1):  # O(n)
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res



# # from collections import Counter
# # from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # ------------------------------------------------------------------
#         # Step 1 – Count the frequency of every number
#         # ------------------------------------------------------------------
#         freq_map = Counter(nums)          # O(n) time, O(n) extra space
#         #   freq_map[x] == how many times `x` appears in `nums`

#         # ------------------------------------------------------------------
#         # Step 2 – Put numbers into “buckets” indexed by their frequency
#         # ------------------------------------------------------------------
#         # The largest possible frequency is `len(nums)` (all elements are equal)
#         buckets = [[] for _ in range(len(nums) + 1)]   # +1 because freq can be 0..n
#         for num, freq in freq_map.items():            # O(n) time
#             buckets[freq].append(num)                 # put `num` in bucket `freq`

#         # ------------------------------------------------------------------
#         # Step 3 – Collect the top k numbers, starting from the largest bucket
#         # ------------------------------------------------------------------
#         res = []
#         # Iterate frequencies from high → low
#         for freq in range(len(buckets) - 1, 0, -1):     # O(n) time
#             for num in buckets[freq]:                  # O(n) time over all buckets
#                 res.append(num)
#                 if len(res) == k:                     # stop once we have k
#                     return res
