ss = input().split()
n = int(ss[0])
s = int(ss[1])
a = list(map(int, input().split()))
a_max = max(a)
a_sum = sum(a)
if a_sum-a_max > s:
    print('NO')
else:
    print('YES')