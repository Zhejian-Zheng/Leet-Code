class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minlen = min(map(len, strs))
        for i in range(minlen):
            std = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != std:
                    return strs[0][:i]
                    
        return strs[0][:minlen]