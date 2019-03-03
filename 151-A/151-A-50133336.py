n, k, l, c, d, p, nl, np = list(map(int, input().split()))
pt = (l*k)//nl
lt = c*d
st = p//np
print(min(pt, lt, st)//n)
