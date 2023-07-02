class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            toReach = target - nums[i] 
            if toReach in dic:
                return [dic[toReach], i]
            dic[nums[i]] = i
            