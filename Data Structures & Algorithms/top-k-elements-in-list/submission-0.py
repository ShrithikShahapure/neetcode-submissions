class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        freq_map = Counter(nums)  # O(n)
    
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