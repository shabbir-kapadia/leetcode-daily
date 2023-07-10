class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        freq = [[] for x in range(len(nums) + 1)]

        for key, values in count.items():
            freq[values].append(key)
        result = []
        for i in range(len(freq) -1,-1,-1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result

