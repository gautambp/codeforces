n = int(input())
l = list(map(int, input().split()))
cnt = 0
p_cnt = 0
for i in l:
    if i == -1:
        if p_cnt > 0:
            p_cnt -= 1
        else:
            cnt += 1
    else:
        p_cnt += i
print(cnt)
