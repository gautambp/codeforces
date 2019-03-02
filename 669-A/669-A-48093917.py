import math

s = int(input())
if s == 1 or s == 2:
    print(1)
else:
    if s%3 == 0:
        print(2 * (s//3))
    else:
        print(1 + (2 * (s//3)))