class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 10 is made from 2 * 5, so we just need to count how many 2* 5 in the factorial
        num_z = 0
        while n > 0:
            n //= 5
            num_z += n
        
        return num_z