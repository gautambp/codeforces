n = int(input())
s = [int(i) for i in input().strip().split(' ')]
l = []
for i in range(1, n):
    if s[i] == 1:
        l.append(s[i-1])
l.append(s[n-1])
print(len(l))
for i in l: print(i, end=' ')
print('')
