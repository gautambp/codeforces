n = int(input())
s = input().strip()
last_s = s[0]
s_cnt = 0
cnt = 0
for i in range(1, n):
    if last_s != s[i]:
        cnt += s_cnt
        s_cnt = 0
    else:
        s_cnt += 1
    last_s = s[i]

print(cnt+s_cnt)