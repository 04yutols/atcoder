#!/usr/bin/env python3
from itertools import count


i = input().split()
z = input().split()
n = int(i[0])
a = int(i[1])
b = int(i[2])
p = int(z[0])
q = int(z[1])
r = int(z[2])
s = int(z[3])
lines = q - p + 1
rows = s - r + 1
max_a = max(1-a,1-b)
min_a = min(n-a,n-b)
max_b = max(1-a,b-n)
min_b = min(n-a,b-1) 
ans = "."*rows
list_a = []
counter = 1
while True:
    if counter > lines:
        counter = 0
        break
    list_a.append(ans)
    counter += 1
count_line = 1
count_row = 1
a_plus_k = a+max_a
b_plus_k = b+max_a
a_plus_k_2 = a + max_b
b_minus_k = b - max_b
space = 0
while True:
    if a_plus_k < 0 or b_plus_k < 0:
        a_plus_k += 1
        b_plus_k +=1
    if a_plus_k_2 < 0 or b_minus_k < 0:
        a_plus_k_2 += 1
        b_minus_k -= 1
    if max_a > min_a and max_b > min_b:
        break
    list_a[a_plus_k-1] = list_a[a_plus_k-1][:b_plus_k-1:]+"#"+list_a[a_plus_k-1][b_plus_k:]
    list_a[a_plus_k_2-1] = list_a[a_plus_k_2-1][:b_minus_k-1]+"#"+list_a[a_plus_k_2-1][b_plus_k:]
    a_plus_k += 1
    b_plus_k +=1
    a_plus_k_2 += 1
    b_minus_k -= 1
    max_a += 1
    max_b += 1

    
while True:
    if counter > lines:
        break
    print(list_a[counter])
    counter += 1