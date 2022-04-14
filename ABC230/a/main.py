#!/usr/bin/env python3
i = int(input())
if i >= 42:
    i +=1
a = str(i)
while True:
    if len(a) !=3 :
        a = "0"+a
    else:
        break
print("AGC"+a)