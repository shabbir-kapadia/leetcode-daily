class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        checkS = {}
        checkT = {}
        for i in range(len(s)):
            checkS[s[i]] = 1 + checkS.get(s[i], 0)
            checkT[t[i]] = 1 + checkT.get(t[i], 0)
        return checkS == checkT