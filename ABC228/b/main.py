#!/usr/bin/env python3
N,X = map(int,input().split())
A = list(map(int,input().split()))
flag = []
for i in range(N):
    flag.append(False)
flag[X-1]=True
st = A[X-1]
while True:
    if flag[st-1] == True:
        break
    else:
        flag[st-1] = True
        st = A[st-1]
print(flag.count(True))
