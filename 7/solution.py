class Solution:
    def reverse(self, x: int) -> int:
        reversed_str = str(abs(x))[::-1]
        ans = int(reversed_str)
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        
        return ans if x > 0 else -ans