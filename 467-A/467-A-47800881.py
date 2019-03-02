r_cnt = 0
for _ in range(int(input())):
    s = input().split()
    if abs(int(s[0]) - int(s[1])) >= 2:
        r_cnt += 1
print(r_cnt)