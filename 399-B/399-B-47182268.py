n = int(input())
s = input().strip()
op_cnt = 0
for i in range(n):
    if s[i] == 'B':
        op_cnt += 2 ** i
print(op_cnt)