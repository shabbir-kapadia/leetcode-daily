class Solution:
    def minMoves(self, nums):
        if len(nums) == 0:
            return 0

        min_val = nums[0]
        for n in nums:
            min_val = min(min_val, n)

        res = 0
        for n in nums:
            res += n - min_val

        return res
