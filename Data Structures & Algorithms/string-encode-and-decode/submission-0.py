class Solution:



    def encode(self, strs: List[str]) -> str:

        parts = []
        for s in strs:
            # length first, then separator, then the string itself
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)          # O(total_len)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        n = len(s)

        while i < n:
            # 1. read the length (could be >1 digit)
            j = i
            while j < n and s[j] != '#':
                j += 1
            if j == n:
                raise ValueError("Malformed input: missing separator")

            length = int(s[i:j])   # length of the next string
            j += 1                 # skip '#'

            # 2. read the string itself
            str_part = s[j:j+length]
            if len(str_part) != length:
                raise ValueError("Malformed input: string too short")

            res.append(str_part)
            j += length
            i = j                   # move to next block

        return res
