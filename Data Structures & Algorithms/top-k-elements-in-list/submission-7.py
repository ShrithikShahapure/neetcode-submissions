# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Step 1: Count frequency
#         freq_map = Counter(nums)  # O(n)
        
#         # Counter is basically the hashmap that we implemented in the previous thing

#         # freq_map = {}

#         # for i, num in enumerate(nums):
#         #     if num in freq_map:
#         #         freq_map[num] += 1
#         #     else:
#         #         freq_map[num] = 1
    
#     # Less Space

#         freq_map = {}
#         for num in nums:
#             if num in freq_map:
#                 freq_map[num] += 1
#             else:
#                 freq_map[num] = 1


#     # Try this to makle it a little more efficient

#     # d = {}
#     # for x in iterable:
#     #     d[x] = d.get(x, 0) + 1



#     # Step 2: Create buckets
#         buckets = [[] for _ in range(len(nums) + 1)]
#         for num, freq in freq_map.items():
#             buckets[freq].append(num)  # O(n)
    
#     # Step 3: Gather results from high freq to low
#         res = []
#         for freq in range(len(buckets) - 1, 0, -1):  # O(n)
#             for num in buckets[freq]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res

# from collections import Counter
# import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)



# Bucket-sort version runs in O(n) instead of O(n log k):  # Solution too slow

        # count = Counter(nums)
        # buckets = [[] for _ in range(len(nums)+1)]
        # for num, freq in count.items(): buckets[freq].append(num)
        # result = []
        # for freq in range(len(buckets)-1, 0, -1):
        #     for num in buckets[freq]:
        #         result.append(num)
        #         if len(result) == k: return result

