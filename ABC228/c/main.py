#!/usr/bin/env python3
from itertools import count
from operator import itemgetter
from textwrap import indent
import copy
N,K = map(int,input().split())
P = [list(map(int, input().split())) for _ in range(N)]
oP = copy.copy(P)
ans = []
count = 0
while True:
    ans.append("No")
    count += 1
    if count > N-1:
        count = 0
        break
P.sort(reverse=True,key=lambda x:x[0]+x[1]+x[2])
border = sum(P[K])-300
while True:
    if count > N-1:
        count = 0
        break
    if sum(P[count])>=border:
        ans[oP.index(P[count])] = "Yes"
        count += 1
    else:
        count =0
        break
    
while True:
    if count > N-1:
        break
    print(ans[count])
    count += 1
    