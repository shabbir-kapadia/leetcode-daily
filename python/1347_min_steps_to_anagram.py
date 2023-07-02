import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count= collections.Counter(s)
        steps = 0
        
        for i in t:
            if count[i] > 0:
                count[i] -=1
            else:
                steps+=1
        return steps
    
        