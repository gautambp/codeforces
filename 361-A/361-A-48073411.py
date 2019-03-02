import math
import collections

n,k = list(map(int, input().split()))
if k%n == 0:
    i = str(k // n) + ' '
    for _ in range(n):
        print(i*n)
else:
    i2 = str(math.ceil(k/n))
    i1 = str(math.ceil(k/n)-1)
    i2_len = k % n
    i1_len = n - i2_len
    l = collections.deque([i1]*i1_len + [i2]*i2_len)
    for i in range(n):
        print(' '.join(l))
        l.rotate(1)