n, a, b = list(map(int, input().split()))
l = [0]*n
for i in input().split():
    l[int(i)-1] = '1'
for i in input().split():
    l[int(i)-1] = '2'
print(' '.join(l))