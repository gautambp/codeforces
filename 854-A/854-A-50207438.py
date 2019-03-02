import math
n = int(input())
for i in range(n//2, 0, -1):
    if math.gcd(i, n-i) == 1:
        print('{} {}'.format(i, n-i))
        break