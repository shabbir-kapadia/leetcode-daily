#!/bin/python3

import math
import os
import random
import re
import sys


def getSubstringCount(s):
    ans = 0
    prev = 0
    curr = 1
    output = []
    if len(s) == 0:
        return 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans = min(prev, curr)
            output.append()
            prev = curr
            print(output)
            curr = 1        
        else:
            curr += 1
    ans += min(prev,curr)
    return ans

    def createSubstring(s, prev, curr):
        counts = []
        Cnt = 1
        for i in range(1,len(s)):
            if (s[i]!=s[i-1]):
                counts.append(cnt)
                Cnt = 1
            else:
                Cnt +=1

        Curr_index = 0
        Temp = 0
        Ans = []
        for i in range(1,len(output)):
            X = min(output[i],output[i-1])
            if s[Curr_index]==’0’:
                ans.append(‘0’*x+’1’*x)
            else:
                ans.append(‘1’*x+’0’*x)
            Curr_index += (x*2)
        return ans

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSubstringCount(s)

    fptr.write(str(result) + '\n')

    fptr.close()
