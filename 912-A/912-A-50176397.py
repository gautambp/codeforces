s = input().split()
yc, bc = int(s[0]), int(s[1])
s = input().split()
y, g, b = int(s[0]), int(s[1]), int(s[2])
tyc = y*2+g
tbc = b*3+g
t = (tyc-yc if tyc > yc else 0) + (tbc-bc if tbc > bc else 0)
print(t)