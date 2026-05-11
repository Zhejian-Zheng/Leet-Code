class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = str(num)
            for c in num:
                res.append(int(c))

        return res