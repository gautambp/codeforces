n = int(input())
s = input().split()
max_cnt = cur_cnt = last_val = 0
for i in range(n+1):
    val = (int(s[i]) if i < n else 0)
    if val > last_val:
        cur_cnt += 1
    else:
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
        cur_cnt = 1
    last_val = val
print(max_cnt)
