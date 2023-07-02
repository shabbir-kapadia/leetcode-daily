class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        cur = ""
        for c in s:
            if c == "[":
                stack.append((cur, k))
                k = 0
                cur = ""
            elif c == "]":
                last_elm, last_k = stack.pop(-1)
                cur = last_elm + cur * last_k
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                cur += c
        return cur
    
