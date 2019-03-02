s = input().split()
l, r, a = int(s[0]), int(s[1]), int(s[2])
while a > 0:
    if l <= r: 
        l += 1
    else:
        r += 1
    a -= 1
print(2*min(l, r))