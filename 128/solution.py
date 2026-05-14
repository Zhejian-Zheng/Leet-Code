class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        max_len = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
                
            # If it's exactly 1 greater than the previous, extend the sequence
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                # Sequence broke, reset current length
                max_len = max(max_len, curr)
                curr = 1
                
        # One final check in case the longest sequence ends at the last element
        return max(max_len, curr)