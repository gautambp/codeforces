import math

(n, k) = (15, 6)
(n, k) = [int(i) for i in input().split(' ')]
r = 2
g = 5
b = 8
num_sheet = math.ceil((r * n) / k)
num_sheet += math.ceil((g * n) / k)
num_sheet += math.ceil((b * n) / k)
print(num_sheet)
