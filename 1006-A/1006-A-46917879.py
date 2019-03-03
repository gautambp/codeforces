n = int(input())
a = [int(i) for i in input().strip().split(' ')]
for i in range(n):
    if a[i] > 0 and a[i] <= 1000000000:
        if a[i]%2 == 1:
            a[i] += 1
        if a[i]%2 == 0:
            a[i] -= 1
for i in a: print(i, end=' ')
print('')
