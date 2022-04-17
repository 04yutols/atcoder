#!/usr/bin/env python3
i,j = map(str,input().split())
n = len(i)
z = len(j)
while True:
    if n == 0 or z == 0:
        print("Easy")
        break
    if len(str(int(i[n-1:n])+int(j[z-1:z]))) == 2:
        print("Hard")
        break
    else:
        n -= 1
        z -= 1