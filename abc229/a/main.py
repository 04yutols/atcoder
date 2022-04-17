#!/usr/bin/env python3
i = input()
j = input()
A = i[:1]
B = i[1:]
C = j[:1]
D = j[1:]
if A == B or A == C or B == D:
    print("Yes")
else:
    print("No")