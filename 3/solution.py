class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        s = list(s)
        for i in range(len(s)):
            uni_ele = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] in uni_ele:
                    break
                else:
                    uni_ele.append(s[j])
            if len(uni_ele) > max_len:
                max_len = len(uni_ele)

        
        return max_len