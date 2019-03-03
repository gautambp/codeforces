x, y, z, t1, t2, t3 = list(map(int, input().split()))
w_time = abs(x-y)*t1
e_time = abs(z-x)*t2 + abs(x-y)*t2 + 3*t3
print('YES' if e_time <= w_time else 'NO')
