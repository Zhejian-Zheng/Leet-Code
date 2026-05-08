# huge time complexity
class Solution:
    def climbStairs(self, n: int) -> int:
        def dpClimb(n):
            if n <= 2:
                return n

            return dpClimb(n - 1) + dpClimb(n - 2)        

        return dpClimb(n)