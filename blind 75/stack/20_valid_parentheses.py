class Solution:
    def isValid(self, s):
        stack = ['#']
        for c in s:
            if c == '(': stack.append(')')
            elif c == '{': stack.append('}')
            elif c == '[': stack.append(']')
            elif c != stack.pop(): return False
        return stack == ['#']