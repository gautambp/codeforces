n = int(input())
f1 = 1
f2 = 1
f = f1+f2
s = 'O'
idx = 2
while idx <= n:
    if idx == f:
        s += 'O'
        f1 = f2
        f2 = f
        f = f1+f2
    else:
        s += 'o'
    idx += 1

print(s)