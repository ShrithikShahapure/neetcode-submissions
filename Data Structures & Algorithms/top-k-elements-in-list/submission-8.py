class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap approach — O(n log k) time, O(n + k) space
        # Standard "top k" pattern: maintain a heap of size k instead of
        # sorting all n elements.
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Bucket sort approach — O(n) time, O(n) space
#         # Key insight: frequency can never exceed len(nums), so we can use
#         # frequency itself as a bucket index instead of comparison-sorting.
#         count = Counter(nums)
#         buckets = [[] for _ in range(len(nums) + 1)]
#         for num, freq in count.items():
#             buckets[freq].append(num)

#         result = []
#         for freq in range(len(buckets) - 1, 0, -1):
#             for num in buckets[freq]:
#                 result.append(num)
#                 if len(result) == k:
#                     return result