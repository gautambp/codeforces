(a,b,c) = [int(i) for i in input().strip().split(' ')]
if a+b > c and a+c > b and b+c > a:
    print('0')
else:
    ab_diff = abs(c - (a+b))
    ac_diff = abs(b - (a+c))
    bc_diff = abs(a - (b+c))
    min_diff = ab_diff
    if ac_diff < min_diff: min_diff = ac_diff
    if bc_diff < min_diff: min_diff = bc_diff
    print(min_diff+1)
