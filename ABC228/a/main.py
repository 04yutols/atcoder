#!/usr/bin/env python3
A,B,C = map(int,input().split())
if A > B:
    B = B+24
    if A > C:
        C += 24
if A <= C and B > C:
    print("Yes")
else:
    print("No")