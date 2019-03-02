k, n, w = list(map(int, input().split()))
c = k * w * (w+1) // 2
b = c - n
if b < 0: b = 0
print(b)