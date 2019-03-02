import math

n = int(input())
print(math.ceil(n*n/2))
odd_s = ''
even_s = ''
for i in range(1, n+1):
    odd_s += ('C' if i%2 == 1 else '.')
    even_s += ('C' if i%2 == 0 else '.')
for i in range(1, n+1):
    if i%2 == 1:
        print(odd_s)
    else:
        print(even_s)