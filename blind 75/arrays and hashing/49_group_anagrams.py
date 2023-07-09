class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord('a') - ord(s)] += 1
            output[tuple(count)].append(str)    
        return output.values()      