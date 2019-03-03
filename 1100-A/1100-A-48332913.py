s = input().split()
n = int(s[0])
k = int(s[1])
l = list(map(int, input().split()))

max_val = -1000
for b in range(n):
    e = 0
    s = 0
    for j in range(n):
        if j%k != b%k:
            e += (1 if l[j] == 1 else 0)
            s += (1 if l[j] == -1 else 0)
    if abs(e-s) > max_val:
        max_val= abs(e-s)
print(max_val)
