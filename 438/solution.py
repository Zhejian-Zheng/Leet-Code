class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        ans = []

        p_counter = Counter(p)

        for i in range(s_len - p_len + 1):
            
            sub_s = s[i : i + p_len]
            
            if Counter(sub_s) == p_counter:
                ans.append(i)

        return ans

                