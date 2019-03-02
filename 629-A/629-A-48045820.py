n = int(input())
g = [None]*n
cnt = 0
for i in range(n):
    g[i] = input()

for i in range(n):
    c_cnt = 0
    r_cnt = 0
    for j in range(n):
        if g[i][j] == 'C':
            r_cnt += 1
        if g[j][i] == 'C':
            c_cnt += 1
    cnt += (r_cnt * (r_cnt-1) // 2 if r_cnt > 1 else 0)
    cnt += (c_cnt * (c_cnt-1) // 2 if c_cnt > 1 else 0)

print(cnt)