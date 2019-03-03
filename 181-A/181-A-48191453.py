n, m = list(map(int, input().split()))
s = [None]*n
loc = []
for i in range(n):
    s[i] = input()
    for j in range(m):
        if s[i][j] == '*':
            loc.append((i, j))
r = c = 0
if loc[0][0] == loc[1][0]:
    r = loc[2][0]
elif loc[0][0] == loc[2][0]:
    r = loc[1][0]
else:
    r = loc[0][0]
if loc[0][1] == loc[1][1]:
    c = loc[2][1]
elif loc[0][1] == loc[2][1]:
    c = loc[1][1]
else:
    c = loc[0][1]
print('{} {}'.format(r+1, c+1))
