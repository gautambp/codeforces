n = int(input())
increment = 2
d_cnt = 1
for i in range(1, n+1):
    s_cnt = (n-d_cnt)//2
    print('*'*s_cnt, end='')
    print('D'*d_cnt, end='')
    print('*'*s_cnt)
    d_cnt += increment
    if d_cnt == n:
        increment *= -1
