n = int(input())
idx = 0
s = ''
while len(s) <= 1001:
    s += str(idx)
    idx += 1
print(s[n])