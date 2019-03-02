n = int(input())
s = input().strip()
l = []
b_cnt = 0
for idx in range(n):
    if s[idx] == 'W':
        if b_cnt > 0:
            l.append(b_cnt)
        b_cnt = 0
    elif s[idx] == 'B':
        b_cnt += 1
if b_cnt > 0: l.append(b_cnt)
print(len(l))
for i in l: print(i, end=' ')
print('')