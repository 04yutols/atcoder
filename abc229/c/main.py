#!/usr/bin/env python3
N,W = map(int,input().split())
A = []
B = []
z = 0
k = 0
for i in range(N):
    z , k = map(int,input().split())
    A.append(z)
    B.append(k)
sA = sorted(A,reverse=True)
count = 0
idx = 0
deli = 0
while True:
    if W == 0 or count == N:
        break
    idx = A.index(sA[count])
    if B[idx] <= W:
        deli += sA[count]*B[idx]
        W -= B[idx]
        count += 1
    else:
        deli += sA[count]*W
        break
print(deli)