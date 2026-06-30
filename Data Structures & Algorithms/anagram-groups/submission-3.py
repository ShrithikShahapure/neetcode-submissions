# This solution is slow (n * k log k) because of sorting

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])
                
        return ans


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         mp = defaultdict(list)

#         for s in strs:

#             count = [0] * 26

#             for ch in s:
#                 count[ord(ch) - ord('a')] += 1

#             mp[tuple(count)].append(s)

#         return list(mp.values())


# https://chatgpt.com/c/689a1ced-afd4-8333-8763-d30537420fe4
