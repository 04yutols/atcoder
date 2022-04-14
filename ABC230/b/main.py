#!/usr/bin/env python3
s = input()
t = "oxx"*10**5
a = t.find(s)
if a == -1:
    print("No")
else:
    print("Yes")