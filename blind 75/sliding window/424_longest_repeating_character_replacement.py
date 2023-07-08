import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        dic = collections.defaultdict(int)
        start=0
        maxcount = 0
        maxlength=0
        end =0
        while end<length:
            dic[s[end]]+=1
            maxcount = max(maxcount,dic[s[end]])
            while end-start+1-maxcount>k:
                dic[s[start]]-=1
                start+=1
            maxlength = max(maxlength,end-start+1)
            end+=1
        return maxlength
            