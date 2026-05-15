class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        t = list(pattern)

        dir_s = {}
        dir_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dir_s.keys():
                dir_s[s[i]] = t[i]
            elif dir_s[s[i]] != t[i]:
                return False
            else:
                continue

        for i in range(len(s)):
            if t[i] not in dir_t.keys():
                dir_t[t[i]] = s[i]
            elif dir_t[t[i]] != s[i]:
                return False
            else:
                continue
    
        return True