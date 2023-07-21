class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = [n] * 26

        for i in range(n):
            j = ord(s[i]) - ord('a')
            if count[j] == n:
                count[j] = i
            else:
                count[j] = -1

        res = n
        for i in range(26):
            if count[i] != n and count[i] != -1:
                res = min(res, count[i])

        return -1 if res == n else res

        
        