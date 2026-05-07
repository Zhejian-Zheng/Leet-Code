class Solution:
    CHAR_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        l = len(s)

        for i in range(l):
            value = self.CHAR_VALUES[s[i]]
            if i < l - 1 and value < self.CHAR_VALUES[s[i + 1]]:
                res -= value
            else:
                res += value
        return res