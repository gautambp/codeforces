import math

s = input().split()
n = int(s[0])
r = int(s[1])

sx = math.sin(math.radians(180/n))
print('{:0.7f}'.format(round((r * sx / (1 - sx)), 7)))
