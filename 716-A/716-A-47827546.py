n, c = list(map(int, input().split()))
t = list(map(int, input().split()))
w_cnt = 1
for i in range(1, n):
    if t[i] - t[i-1] > c:
        w_cnt = 1
    else:
        w_cnt += 1
    #print('{} {}'.format(t[i], w_cnt))
print(w_cnt)